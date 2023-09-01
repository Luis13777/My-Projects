from django.shortcuts import render, redirect
from .models import Ativo
from .models import Email
from django.http import HttpResponse

def home(request):
    return render(request,"main/home.html")

def ativos(request):
    ativos = Ativo.objects.all() 
    email = Email.objects.first() 
    context = {'Ativos': ativos, 'Email': email}
    return render(request,"main/ativos.html", context)

def adicionar_ativo(request):
    novo_ativo = Ativo()
    novo_ativo.nome = request.POST.get("nome_ativo")
    novo_ativo.save()
    return redirect("ativos")

def excluir_ativo(request, ativo_id):
    ativo = Ativo.objects.get(id_ativo=ativo_id)
    ativo.delete()
    return redirect("ativos")



def is_convertible_to_number(input_string):
    try:
        float(input_string)  # Tenta converter a string em um número de ponto flutuante
        return True
    except ValueError:
        return False
    
def is_convertible_to_inteiro(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def atualizar_ativo(request, ativo_id):
    if request.method == "POST":
        ativo = Ativo.objects.get(id_ativo=ativo_id)
        limite_inferior = request.POST.get("limite_inferior")
        limite_superior = request.POST.get("limite_superior")
        delay = request.POST.get("delay")

        if not is_convertible_to_number(limite_inferior) or not is_convertible_to_number(limite_superior) or not is_convertible_to_inteiro(delay):
            return redirect("ativos")

        ativo.delay = int(delay)
        ativo.limite_inferior = float(limite_inferior)
        ativo.limite_superior = float(limite_superior)
        ativo.save()
        return redirect("ativos")
        
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

schedulers = []

def ativar_rastreador (request):


    global schedulers
    ativos = Ativo.objects.all() 
    context = {'Ativos': ativos}
    for ativo in context["Ativos"]:
        scheduler = BackgroundScheduler()
        scheduler.add_job(CheckAPI, 'interval', seconds=ativo.delay*60, args=(ativo.id_ativo,))  
        scheduler.start()
        schedulers.append(scheduler)

    return redirect("ativos")


import requests


def get_stock (id):
    chave_api = "33EC98Q6UTM733QC"

    ativo = Ativo.objects.get(id_ativo=id)


    company = ativo.nome

    urlDefault = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE"

    url = f'{urlDefault}&symbol={company}&apikey={chave_api}'
    r = requests.get(url)
    data = r.json()

    return float(data['Global Quote']['05. price'][:-2:])





def CheckAPI (id):
    ativo = Ativo.objects.get(id_ativo=id)
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    if ativo.datas is None:
        ativo.datas = {}
    preco = get_stock(id)
    ativo.datas[now_str] = preco
    ativo.save()
    if preco > ativo.limite_superior:
        MandarEmail(ativo.nome, preco, now_str, True, ativo.limite_superior)
    elif preco < ativo.limite_inferior:
        MandarEmail(ativo.nome, preco, now_str, False, ativo.limite_inferior)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def MandarEmail (nome, valor, data, vender, limite):
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_username = 'ContaTesteINOA@outlook.com'  
    smtp_password = 'INOAteste'  

    email = Email.objects.get(id_email=1)

    # Configurações do e-mail
    de = 'ContaTesteINOA@outlook.com'
    para = email.email

    if vender:
        assunto = f'Ativo {nome} está em alta!'
        mensagem = f'O seu ativo {nome} atingiu o valor de {valor} e está acima de {limite} agora ({data}), bom momento para vender!'
    elif not vender:
        assunto = f'Ativo {nome} está em baixa!'
        mensagem = f'O seu ativo {nome} atingiu o valor de {valor} e está abaixo de {limite} agora ({data}), bom momento para comprar!'

    msg = MIMEMultipart()
    msg['From'] = de
    msg['To'] = para
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  
    server.login(smtp_username, smtp_password)
    server.sendmail(de, para, msg.as_string())
    server.quit()



def desativar_rastreador(request):
    global schedulers

    # Parar cada scheduler e limpar a lista
    for scheduler in schedulers:
        scheduler.shutdown()

    # Limpar a lista de schedulers
    schedulers = []

    return redirect("ativos")

def alterar_email(request):
    if request.method == "POST":
        input_email = request.POST.get("input_email")
        email = Email.objects.first()
        if email is None:
            email = Email()
        email.email = input_email
        email.save()
    return redirect("ativos")


import matplotlib.pyplot as plt
from datetime import datetime
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import base64

def imprimir_dados (request):
    ativo_imprimir = request.POST.get("imprimir_input")
    ativos = Ativo.objects.all()
    ativos_dict = {ativo.nome: [ativo.datas, ativo.limite_inferior, ativo.limite_superior] for ativo in ativos}

    if ativo_imprimir in ativos_dict:
        infos = ativos_dict[ativo_imprimir]

        data = infos[0]
        empresa = ativo_imprimir

        limite_inferior = infos[1]
        limite_superior = infos[2]


        # Separar os dados de tempo e preço
        timestamps = [datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') for timestamp in data.keys()]
        prices = list(data.values())

        plt.subplots(figsize=(20, 6))

        ax1 = plt.subplot()
        ax1.plot(timestamps, prices, marker='o')  # Criação do gráfico de linha
        ax1.set_ylabel('Preço')
        ax1.set_title(f'Gráfico de Preço ao Longo do Tempo do ativo {empresa}')
        ax1.tick_params(axis='x', rotation=45)  # Rotaciona as datas para melhor legibilidade

        # Eixo secundário para as datas formatadas
        ax2 = ax1.twiny()
        ax2.set_xlim(ax1.get_xlim())
        ax2.set_xticks(timestamps)
        date_format = "%d/%m/%Y %H:%M"
        date_labels = [timestamp.strftime(date_format) for timestamp in timestamps]
        ax2.set_xticklabels(date_labels, rotation=0)
        ax2.set_xlabel('Tempo')

        # Remover as marcações do eixo superior
        ax2.get_xaxis().set_ticks([])

        # Adicionar linhas horizontais
        ax1.axhline(y=limite_inferior, color='red', linestyle='--', label='Limite inferior')
        ax1.axhline(y=limite_superior, color='blue', linestyle='--', label='Limite superior')

        # Mostrar a legenda
        ax1.legend()
        plt.tight_layout()  # Ajusta a disposição dos elementos

        temp_file = io.BytesIO()
        plt.savefig(temp_file, format='png')
        temp_file.seek(0)
    
        encoded_image = base64.b64encode(temp_file.read()).decode('utf-8')

        return render(request, "main/home.html", {"imagem_grafico": encoded_image})
    return redirect("home")

