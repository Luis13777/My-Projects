var botaoEditar = document.getElementsByClassName("editar")[0];
var editContainer = document.getElementsByClassName("editAll")[0];
var balaoCentralEdit = document.getElementsByClassName("editBallon")[0];

var botaoConfirmaEditar= document.getElementById("edit")
var editInside = document.getElementsByClassName("editInside")[0]
var Xedit = document.getElementsByClassName("Xedit")[0]




function eventAbrirEditar (event){
  if (event.target === balaoCentralEdit) {
      editInside.classList.remove("escondido")
      balaoCentralEdit.classList.remove('showEdit')
        botaoConfirmaEditar.classList.remove("escondido")

      balaoCentralEdit.style['height'] = '15vh'
      editContainer.style["backdropFilter"] = 'blur(10px)';
      editContainer.style["background-color"] = 'rgba(0, 0, 0, 0.8)'
      balaoCentralEdit.removeEventListener('animationend', eventAbrirAdiconar);
  }

}
function abrirEditar() {
    editContainer.classList.remove('escondido');
    editContainer.classList.add('blur');
    balaoCentralEdit.classList.add('showEdit')
  
    balaoCentralEdit.addEventListener('animationend', eventAbrirEditar)
  
  }



function eventEditarFechar(event){
    if (event.target === balaoCentralEdit) {

        balaoCentralEdit.classList.remove('unshowEdit')
        balaoCentralEdit.style['height'] = '0vh'
        editContainer.classList.remove('unblur');
        editContainer.style["backdropFilter"] = 'blur(0px)';
        editContainer.style["background-color"] = 'rgba(0, 0, 0, 0)'
        editContainer.classList.add('escondido');
        editInside.classList.add("escondido")
        botaoConfirmaEditar.classList.add("escondido")
        balaoCentralEdit.removeEventListener('animationend', eventEditarFechar);
    }
  }

function closeEditar (){
    editInside.classList.add("escondido")
    botaoConfirmaEditar.classList.add("escondido")
    editContainer.classList.add('unblur');
    balaoCentralEdit.classList.add('unshowEdit');
    balaoCentralEdit.addEventListener('animationend', eventEditarFechar)
  
  }





