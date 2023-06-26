window.addEventListener("DOMContentLoaded", function () {


  const bottom = document.getElementById("bottom")
  const alturaDispositivo = window.innerHeight


});

var titleInput = document.getElementById("title")
var descricaoCurtaInput = document.getElementById("descricaoCurta")
var descricaoLongaInput = document.getElementById("descricaoLonga")
var idade1Input = document.getElementById("idade1")
var idade2Input = document.getElementById("idade2")
var restauranteSwitchInput = document.getElementById("restauranteSwitch")
var familiaSwitchInput = document.getElementById("familiaSwitch")
var esporteSwitchInput = document.getElementById("esporteSwitch")
var turismoSwitchInput = document.getElementById("turismoSwitch")
var cinemaSwitchInput = document.getElementById("cinemaSwitch")
var parqueSwitchInput = document.getElementById("parqueSwitch")
var comprasSwitchInput = document.getElementById("comprasSwitch")
var hospedagemSwitchInput = document.getElementById("hospedagemSwitch")
var estacionamentoSwitchInput = document.getElementById("estacionamentoSwitch")
var festaSwitchInput = document.getElementById("festaSwitch")
var EnderecoInput = document.getElementById("Endereco")
var TelefoneInput = document.getElementById("Telefone")
var ImagensInput = document.getElementById("Imagens")



const barraLateral = document.getElementById("barra-lateral")

function openMenu() {
  barraLateral.classList.add('openMenu');


  barraLateral.addEventListener('animationend', function (event) {
    if (event.target === barraLateral) {
      barraLateral.classList.remove('openMenu');
      barraLateral.style.left = '0%'
    }

  })

}

function closeMenu() {
  barraLateral.classList.add('closeMenu');

  barraLateral.addEventListener('animationend', function (event) {
    if (event.target === barraLateral) {
      barraLateral.classList.remove('closeMenu');
      barraLateral.style.left = '-17%'
    }

  })
}






const ballon1 = document.getElementsByClassName("ballon1")[0]
const ballon2 = document.getElementsByClassName("ballon2")[0]
// const ballon1Pictures = document.getElementsByClassName("ballon2")[0]

var open = false

function openBallon() {

  if (open) {
    open = false
    ballon1.classList.add('closeBallon1');
    ballon2.classList.add('openBallon2');
    ballon1.addEventListener('animationend', eventCloseBallon)

  }
  else {
    open = true
    ballon1.classList.add('openBallon1');
    ballon2.classList.add('closeBallon2');
    ballon1.addEventListener('animationend', eventOpenBallon)
  }
}

function eventOpenBallon (event){
  if (event.target === ballon1) {
    ballon1.classList.remove('openBallon1');
    ballon2.classList.remove('closeBallon2');
    ballon1.style.width = '30%'
    ballon2.style.width = '67%'
    ballon1.removeEventListener('animationend', eventOpenBallon);
  }
}

function eventCloseBallon (event){
  if (event.target === ballon1) {
    ballon1.classList.remove('closeBallon1');
    ballon2.classList.remove('openBallon2');
    ballon1.style.width = '0%'
    ballon2.style.width = '97%'
    while (balaoComInfos.firstChild) {
      balaoComInfos.removeChild(balaoComInfos.firstChild);
    }
    ballon1.removeEventListener('animationend', eventCloseBallon);
  }
}














var botaoAdicionar = document.getElementsByClassName("adicionar")[0];
var all = document.getElementsByClassName("all")[0];
var balaoCentral = document.getElementsByClassName("balao")[0];
var tudo = document.getElementsByClassName("tudo")[0]




function eventAbrirAdiconar (event){
  if (event.target === balaoCentral) {
    balaoCentral.classList.remove('show')
    balaoCentral.style['height'] = '90vh'
    all.style["backdropFilter"] = 'blur(10px)';
    all.style["background-color"] = 'rgba(0, 0, 0, 0.8)'
    all.classList.remove('escondido');
    tudo.classList.remove('escondido');
    balaoCentral.removeEventListener('animationend', eventAbrirAdiconar);
  }

}


function abrirAdiconar() {

  all.classList.remove('escondido');
  all.classList.add('blur');
  balaoCentral.classList.add('show')

  balaoCentral.addEventListener('animationend', eventAbrirAdiconar)

}

const X = document.getElementsByClassName("X")[0]



function eventAbrirAdiconarFechar (event){
  if (event.target === balaoCentral) {
    balaoCentral.classList.remove('unshow')
    balaoCentral.style['height'] = '0vh'
    all.classList.remove('unblur');
    all.style["backdropFilter"] = 'blur(0px)';
    all.style["background-color"] = 'rgba(0, 0, 0, 0)'
    all.classList.add('escondido');
    titleInput.value = ''
    descricaoCurtaInput.value = ''
    descricaoLongaInput.value = '' 
    idade1Input.value = ''
    idade2Input.value = ''
    restauranteSwitchInput.checked = false
    familiaSwitchInput.checked = false
    esporteSwitchInput.checked = false
    turismoSwitchInput.checked = false
    cinemaSwitchInput.checked = false
    parqueSwitchInput.checked = false
    comprasSwitchInput.checked = false
    hospedagemSwitchInput.checked = false
    estacionamentoSwitchInput.checked = false
    festaSwitchInput.checked = false
    EnderecoInput.value = ''
    TelefoneInput.value = ''
    ImagensInput.value = ''
    balaoCentral.removeEventListener('animationend', eventAbrirAdiconarFechar);
  }
}

function closeAdicionar (){

  tudo.classList.add('escondido');

  all.classList.add('unblur');
  balaoCentral.classList.add('unshow');


  balaoCentral.addEventListener('animationend', eventAbrirAdiconarFechar)

}




