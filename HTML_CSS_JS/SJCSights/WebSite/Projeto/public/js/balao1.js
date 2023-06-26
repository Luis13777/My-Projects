function carregarBalao1(titulo) {

  if (open) {
    axios.get("http://localhost:45678/local/" + titulo).then(response => {
      var local = response.data

      var tituloImagemInfosContainer = document.createElement("div")
      var tituloImagemDescribing = document.createElement("div")
      var tituloImagemSlidesContainer = document.createElement("div")


      // imganes
      // -------------------------------------------------------------------


      var descricaoInfosContainer = document.createElement("div")
      var descricaoDescribing = document.createElement("div")
      var descricaoDetailsContainer = document.createElement("div")

      var telefoneInfosContainer = document.createElement("div")
      var telefoneIcon = document.createElement("div")
      var telefoneDescribing = document.createElement("div")
      var telefoneDetailsContainer = document.createElement("div")

      var enderecoInfosContainer = document.createElement("div")
      var enderecoIcon = document.createElement("div")
      var enderecoDescribing = document.createElement("div")
      var enderecoDetailsContainer = document.createElement("div")

      var idadeInfosContainer = document.createElement("div")
      var idadeDescribing = document.createElement("div")

      var iconsContent = document.createElement("div")

      var deleteContainer = document.createElement("div")
      var deleteButton = document.createElement("button")
      var spanButton = document.createElement("span")
      var imgButton = document.createElement("img")




      balaoComInfos.appendChild(tituloImagemInfosContainer)
      tituloImagemInfosContainer.classList.add("infosContainer")

      tituloImagemInfosContainer.appendChild(tituloImagemDescribing)
      tituloImagemDescribing.classList.add("describing")
      tituloImagemDescribing.innerHTML = local.title

      tituloImagemInfosContainer.appendChild(tituloImagemSlidesContainer)
      tituloImagemSlidesContainer.classList.add("slidesContainer")

      var slidershow = document.createElement("div")
      tituloImagemSlidesContainer.appendChild(slidershow)
      slidershow.classList.add("slidershow")

      var slides = document.createElement("div")
      slidershow.appendChild(slides)
      slides.classList.add("slides")

      var numeroDeImagens = local.imagens.length






      var allSlides = document.createElement("div")
      slides.appendChild(allSlides)
      allSlides.classList.add("allSlides")
      allSlides.style.width = `${100 * numeroDeImagens}%`;
      allSlides.style.left = `0`;


      var navigation = document.createElement("div")
      tituloImagemInfosContainer.appendChild(navigation)
      navigation.classList.add(`navigation`)


      for (let i = 1; i <= numeroDeImagens; i++) {
        // var input = document.createElement("input")
        // slides.appendChild(input)
        // input.type = "radio";
        // input.name = "r";
        // input.id = `r${i}`;
        // if (i === 1) {
        //     input.checked = true;
        // }

        // input.addEventListener("change", function () {
        //     allSlides.style.left = `${100 * (i-1)}%`;
        // });


        slides.classList.add("slides")

        var slide = document.createElement("div")
        allSlides.appendChild(slide)
        slide.style.width = `${100 / i}%`
        slide.style.aspectRatio = '16/9';

        var imagemDoSlide = document.createElement("div")
        slide.appendChild(imagemDoSlide)
        imagemDoSlide.classList.add("imgSlide")


        imagemDoSlide.style.backgroundImage = `url("/image/${local.imagens[i - 1]}")`

        var label = document.createElement("label")
        navigation.appendChild(label)
        label.classList.add(`bar`)
        label.for = `r${i}`

        label.addEventListener("click", function () {
          allSlides.style.left = `${-100 * (i - 1)}%`;
        });
      }




      // ------------------------------------------

      balaoComInfos.appendChild(descricaoInfosContainer)
      descricaoInfosContainer.classList.add("infosContainer")

      descricaoInfosContainer.appendChild(descricaoDescribing)
      descricaoDescribing.classList.add("describing")
      descricaoDescribing.innerHTML = "Descrição do Local"

      descricaoInfosContainer.appendChild(descricaoDetailsContainer)
      descricaoDetailsContainer.classList.add("detailsContainer")
      descricaoDetailsContainer.contentEditable = true;
      descricaoDetailsContainer.innerHTML = local.descricaoLonga.replace(/\n/g, "<br>");

      // ------------------------------------------

      balaoComInfos.appendChild(telefoneInfosContainer)
      telefoneInfosContainer.classList.add("infosContainer")

      telefoneInfosContainer.appendChild(telefoneDescribing)
      telefoneDescribing.classList.add("describing")
      telefoneDescribing.classList.add("recudeFont")
      telefoneDescribing.innerHTML = "Telefone"

      telefoneInfosContainer.appendChild(telefoneDetailsContainer)
      telefoneDetailsContainer.classList.add("detailsContainer")
      telefoneDetailsContainer.classList.add("telefoneInfos")
      telefoneDetailsContainer.innerHTML = local.telefone
      telefoneDescribing.appendChild(telefoneIcon)
      telefoneIcon.classList.add("telefoneIcon")


      // ------------------------------------------

      balaoComInfos.appendChild(enderecoInfosContainer)
      enderecoInfosContainer.classList.add("infosContainer")

      enderecoInfosContainer.appendChild(enderecoDescribing)
      enderecoDescribing.classList.add("describing")
      enderecoDescribing.classList.add("recudeFont")
      enderecoDescribing.innerHTML = "Endereço"

      enderecoInfosContainer.appendChild(enderecoDetailsContainer)
      enderecoDetailsContainer.classList.add("detailsContainer")
      enderecoDetailsContainer.classList.add("enderecoInfos")
      enderecoDetailsContainer.innerHTML = local.endereco
      enderecoDescribing.appendChild(enderecoIcon)
      enderecoIcon.classList.add("enderecoIcon")

      // ------------------------------------------

      balaoComInfos.appendChild(idadeInfosContainer)
      idadeInfosContainer.classList.add("infosContainer")

      idadeInfosContainer.appendChild(idadeDescribing)
      idadeDescribing.classList.add("describing")
      idadeDescribing.classList.add("recudeFont")
      idadeDescribing.innerHTML = `Idade Recomendada: ${local.idade[0]} - ${local.idade[1]}`


      // ------------------------------------------

      balaoComInfos.appendChild(iconsContent)
      iconsContent.classList.add("iconsContent")

      local.keyWords.forEach(palavra => {
        var icone = document.createElement("div")
        icone.classList.add("icon")
        icone.classList.add(`${palavra}`)
        icone.classList.add("marginIcon")
        iconsContent.appendChild(icone)
      })

      // ------------------------------------------

      balaoComInfos.appendChild(deleteContainer)
      deleteContainer.classList.add("deleteContainer")

      deleteContainer.appendChild(deleteButton)
      deleteButton.classList.add("delete")

      deleteButton.appendChild(spanButton)
      spanButton.classList.add("deleteSpan")
      spanButton.innerHTML = "CONFIRMAR"

      deleteButton.appendChild(imgButton)


      imgButton.classList.add("deleteSvg")
      imgButton.src = '/image/trash.png'


      deleteButton.onclick = function () {
        var imgStyle = window.getComputedStyle(imgButton);
        var opacityValue = imgStyle.getPropertyValue('opacity');
        if (opacityValue == 0){
          deleteFunction(local.title);
        }
      };

    })
  }
}







