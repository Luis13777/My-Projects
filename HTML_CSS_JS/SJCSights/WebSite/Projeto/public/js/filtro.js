var balaoFiltro = document.getElementsByClassName("balaoFiltro")[0]
var tudoFiltro = document.getElementsByClassName("tudoFiltro")[0]
var allFiltro = document.getElementsByClassName("allFiltro")[0]


// verificar se pelo menos um item de palavrasDoLocal esta em palavrasFiltradas
function checkArrayIgual (palavrasFiltradas, palavrasDoLocal){

    for (let i = 0; i < palavrasDoLocal.length; i++){
        if(palavrasFiltradas.includes(palavrasDoLocal[i]))
        {
            return true
        }
    }
    return false
}


function atualizar() {

    var Palavras = ["restaurante", "familia", "esporte", "turismo", "cinema", "parque", "compras", "hospedagem", "estacionamento", "festa"]

    let palavrasChaves = []


    while (balao[0].firstChild) {
        balao[0].removeChild(balao[0].firstChild);
    }
    
    for (let i = 0; i < Palavras.length; i++) {
        if (document.getElementById(`${Palavras[i]}SwitchFilter`).checked) {
            palavrasChaves.push(Palavras[i])
        }
    }




    axios.get("http://localhost:45678/locais").then(response => {

        var locais = response.data

        locais.forEach(local => {


            if (checkArrayIgual(palavrasChaves, local.keyWords)) {
                var divLocal = document.createElement("div")
                var divImagem = document.createElement("div")
                var divContent = document.createElement("div")
                var divTitulo = document.createElement("div")
                var divContentText = document.createElement("div")
                var divInfos = document.createElement("div")
                var divRating = document.createElement("div")
                var divEstrela = document.createElement("div")
                var divRatingValue = document.createElement("div")
                var divButtons = document.createElement("div")
                var buttonExplore = document.createElement("button")
                var divAge = document.createElement("div")
                var divAgeValue = document.createElement("div")
                var divKeyWords = document.createElement("div")

                balao[0].appendChild(divLocal)
                divLocal.appendChild(divImagem)
                divLocal.appendChild(divContent)
                divContent.appendChild(divTitulo)
                divContent.appendChild(divContentText)
                divContent.appendChild(divInfos)
                divInfos.appendChild(divRating)
                divRating.appendChild(divEstrela)
                divRating.appendChild(divRatingValue)
                divInfos.appendChild(divButtons)
                divButtons.appendChild(buttonExplore)
                divInfos.appendChild(divKeyWords)

                divLocal.classList.add("local");
                divImagem.classList.add("imagem");
                divContent.classList.add("content");
                divTitulo.classList.add("titulo");
                divContentText.classList.add("content-text");
                divInfos.classList.add("infos");
                divRating.classList.add("rating");
                divEstrela.classList.add("estrela");
                divRatingValue.classList.add("ratingValue");
                divButtons.classList.add("buttons");
                buttonExplore.classList.add("button-explore")
                divAge.classList.add("age")
                divAgeValue.classList.add("ageValue")
                divKeyWords.classList.add("keywords")

                var imageUrl = `/image/${local.imagens[0]}`;

                fetch(imageUrl, { method: 'HEAD' })
                    .then(response => {
                        if (response.ok) {
                            // A imagem existe
                            divImagem.style.backgroundImage = `url("${imageUrl}")`;
                        } else {
                            // A imagem não existe
                            console.log("A imagem não foi encontrada.");
                        }
                    })
                    .catch(error => {
                        console.error("Ocorreu um erro ao verificar a imagem:", error);
                    });

                divTitulo.innerHTML = local.title
                divContentText.contentEditable = true;
                divContentText.innerHTML = local.descricaoBreve.replace(/\n/g, "<br>");


                divRatingValue.innerHTML = local.avaliacao
                divAgeValue.innerHTML = `${local.idade[1]}+`
                buttonExplore.innerHTML = '<span>Explore</span>'
                local.keyWords.forEach(keyWord => {
                    var icon = document.createElement("div")
                    icon.classList.add(`icon`);
                    icon.classList.add(`${keyWord}`);
                    divKeyWords.appendChild(icon)
                })
                buttonExplore.id = `button${local.title}`
                buttonExplore.onclick = function () {
                    openBallon()
                    carregarBalao1(local.title)

                }

            }



        })

    })
}













function eventAbrirFiltro(event) {
    if (event.target === balaoFiltro) {
        balaoFiltro.classList.remove('showFilter')
        balaoFiltro.style['height'] = '45vh'
        allFiltro.style["backdropFilter"] = 'blur(10px)';
        allFiltro.style["background-color"] = 'rgba(0, 0, 0, 0.8)'
        allFiltro.classList.remove('escondido');
        tudoFiltro.classList.remove('escondido');
        balaoFiltro.removeEventListener('animationend', eventAbrirFiltro);
    }

}


function abrirFiltro() {
    allFiltro.classList.remove('escondido');
    allFiltro.classList.add('blur');
    balaoFiltro.classList.add('showFilter')
    balaoFiltro.addEventListener('animationend', eventAbrirFiltro)
}


function eventFecharFiltro(event) {
    if (event.target === balaoFiltro) {
        balaoFiltro.classList.remove('unShowFilter')
        allFiltro.classList.remove('unblur');

        balaoFiltro.style['height'] = '0vh'
        allFiltro.style["backdropFilter"] = 'blur(0px)';
        allFiltro.style["background-color"] = 'rgba(0, 0, 0, 0)'
        allFiltro.classList.add('escondido');
        balaoFiltro.removeEventListener('animationend', eventFecharFiltro);
    }

}

function closeFiltro() {
    atualizar()
    allFiltro.classList.add('unblur');
    balaoFiltro.classList.add('unShowFilter')
    tudoFiltro.classList.add('escondido');
    balaoFiltro.addEventListener('animationend', eventFecharFiltro)
}
