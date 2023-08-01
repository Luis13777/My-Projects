function createLocal() {



    // var inputElement = document.getElementById("Imagens");
    // var files = inputElement.files;

    // var formData = new FormData();
    // for (var i = 0; i < files.length; i++) {
    //     formData.append("images", files[i]);
    // }

    // axios.post("/upload", formData)
    //     .then(function (response) {
    //         console.log(response.data);
    //         // Aqui você pode lidar com a resposta do servidor após o upload
    //     })
    //     .catch(function (error) {
    //         console.error(error);
    //         // Aqui você pode lidar com erros durante o upload
    //     });












    var title = document.getElementById("title")
    var descricaoBreve = document.getElementById("descricaoCurta")
    var descricaoLonga = document.getElementById("descricaoLonga")
    var idadeMinima = document.getElementById("idade1")
    var idadeMaxima = document.getElementById("idade2")
    var endereco = document.getElementById("Endereco")
    var telefone = document.getElementById("Telefone")
    var imagens = document.getElementById("Imagens")

    var Palavras = ["restaurante", "familia", "esporte", "turismo", "cinema", "parque", "compras", "hospedagem", "estacionamento", "festa"]

    var keyWords = []

    for (let i = 0; i < Palavras.length; i++) {
        if (document.getElementById(`${Palavras[i]}Switch`).checked) {
            keyWords.push(Palavras[i])
        }
    }

    var fotos = imagens.value.split(", ");
    fotos = fotos.map(foto => foto.replace(/ /g, ""));

    var local = {
        title: title.value,
        descricaoBreve: descricaoBreve.value,
        descricaoLonga: descricaoLonga.value,
        avaliacao: (Math.random() * 1.5 + 3.5).toFixed(1),
        imagens: fotos,
        keyWords: keyWords,
        idade: [idadeMinima.value, idadeMaxima.value],
        endereco: endereco.value,
        telefone: telefone.value
    }

    var Repetido = false
    axios.get("http://localhost:45678/locais").then(response => {
        var locais = response.data
        for (let i = 0; i < locais.length; i++) {
            if (locais[i].title == local.title)
                Repetido = true
        }
        if (Repetido) {
            axios.put("http://localhost:45678/local/" + local.title, local).then(response => {

                if (response.status == 200) {
                    alert("Local atualizado!")
                }
                location.reload();

            }).catch(err => {
                console.log(err)
            })
        }
        else {
            axios.post("http://localhost:45678/local", local).then(response => {

                if (response.status == 200) {
                    alert("Local cadastrado!")
                }
                location.reload();


            }).catch(err => {
                console.log(err)
            })
        }
    })
}



document.getElementById("submit").addEventListener("click", function () {
    createLocal()

});