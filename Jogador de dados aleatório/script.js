const input = document.querySelector(".question input")
const botao = document.querySelector('.button')
const barra = document.querySelector(".barra")
const local = document.querySelector('.grafico')
const larguraDocumento = document.documentElement.clientWidth
const NumeroDeBarras = document.getElementById("N")





function plotar (){
    
    if (local.childElementCount != 0)
    {
        // Assuming your container has an id of "containerId"
        var container = local
        var divs = container.getElementsByTagName("div");

        // Convert HTMLCollection to an array to avoid live collection issues
        var divsArray = Array.from(divs);

        // Loop through the array and remove each div element
        divsArray.forEach(function(div) {
        div.remove();
        });
        // location.reload();
    }
    

    var N = +NumeroDeBarras.value

    const numero = +input.value
    var meuArray = new Array(N).fill(0);
    var i
    var posicao
    for (i=0;i<numero;i++)
    {
        var numero1 = Math.floor(Math.random()*(N+1))
        var numero2 = Math.floor(Math.random()*(N+1))
        var numero3 = Math.floor(Math.random()*(N+1))
        var numero4 = Math.floor(Math.random()*(N+1))
        var numero5 = Math.floor(Math.random()*(N+1))
        media = (numero1 + numero2 + numero3 + numero4 + numero5)/5

        // media = Math.floor(Math.random()*(N+1))

        meuArray[Math.floor(media)]++
    }

    var maior = 0

    for (i=0;i<N;i++)
    {
        if (meuArray[i]>maior)
            maior = meuArray[i]
    }
    for (i=0;i<N;i++)
    {
        meuArray[i] = 100.0*meuArray[i]/maior
    }

    largura = `${larguraDocumento/numero}px`
    for (i = 0; i<N; i++)
    {
        const novaBarra = document.createElement('div');
        novaBarra.className = 'barra'
        // novaBarra.id = `barra${i}`
        // novaBarra.style.height = `${Math.random()*100}%`
        novaBarra.style.height = `${meuArray[i]}%`
        novaBarra.style.width = `${larguraDocumento/N}px`
        novaBarra.style.left = `${larguraDocumento/N*i}px`
        local.appendChild(novaBarra)
    }
    console.log(meuArray)
}





botao.addEventListener('click', plotar);
