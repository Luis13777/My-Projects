
var balao = document.getElementsByClassName("ballon2")
var balaoComInfos = document.getElementsByClassName("ballon1")[0]

axios.get("http://localhost:45678/locais").then(response => {
    var locais = response.data
    locais.forEach (local => {
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
        local.keyWords.forEach (keyWord => {
            var icon = document.createElement("div")
            icon.classList.add(`icon`);
            icon.classList.add(`${keyWord}`);
            divKeyWords.appendChild(icon)
        })
        buttonExplore.id = `button${local.title}`
        buttonExplore.onclick = function (){
            openBallon ()
            carregarBalao1(local.title) 

        }

    })

})







