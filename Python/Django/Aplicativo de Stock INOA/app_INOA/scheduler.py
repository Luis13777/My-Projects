from apscheduler.schedulers.background import BackgroundScheduler
import atexit

def ExecutarAPI():
    print("Função teste() executada")

def iniciar_agendador():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ExecutarAPI, 'interval', seconds=5)  # Agendar a função teste() a cada 1 minuto
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))