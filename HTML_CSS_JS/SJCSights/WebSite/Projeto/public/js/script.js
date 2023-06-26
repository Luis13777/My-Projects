window.addEventListener("DOMContentLoaded", function() {

    const first = document.getElementById("first")
    const bottom = document.getElementById("bottom")
    const alturaDispositivo = window.innerHeight
    
    first.style.height = `${alturaDispositivo*0.92}px`
    bottom.style.height = `${alturaDispositivo*0.2}px`
    

  });



function goTo(local) {
  window.location.href = local
}

const barraLateral = document.getElementById("barra-lateral")


function openMenu(){
  barraLateral.classList.add('openMenu');

  barraLateral.addEventListener('animationend', function(event) {
    if (event.target === barraLateral) {
      barraLateral.classList.remove('openMenu');
      barraLateral.style.left = '0%'
    }

  });
}

function closeMenu(){
  barraLateral.classList.add('closeMenu');

  barraLateral.addEventListener('animationend', function(event) {
    if (event.target === barraLateral) {
      barraLateral.classList.remove('closeMenu');
      barraLateral.style.left = '-17%'
    }

  });
}