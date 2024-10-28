const botaoDeConfirmacao = document.getElementById("edit")
const input = document.getElementById("Local")


function FecharEditAposConfirmacao(){
    balaoCentralEdit.classList.remove('unshowEdit')
    balaoCentralEdit.style['height'] = '0vh'
    editContainer.classList.remove('unblur');
    editContainer.style["backdropFilter"] = 'blur(0px)';
    editContainer.style["background-color"] = 'rgba(0, 0, 0, 0)'
    editContainer.classList.add('escondido');
    balaoCentralEdit.removeEventListener('animationend', FecharEditAposConfirmacao);
}

function AnalisarInputEditar() {
    var localInput = input.value

    axios.get("http://localhost:45678/locais").then(response => {
        var locais = response.data
        var infos = null

        locais.forEach(local => {
            if (local.title === localInput) {
                infos = local
            }
        })

        if (infos === null) {
            alert('Local não encontrado!');
        }
        else {
            editInside.classList.add("escondido")
            botaoConfirmaEditar.classList.add("escondido")
            editContainer.classList.add('unblur');
            balaoCentralEdit.classList.add('unshowEdit');

            balaoCentralEdit.addEventListener('animationend', FecharEditAposConfirmacao)

            abrirAdiconar()
            
            titleInput.value = infos.title
            descricaoCurtaInput.value = infos.descricaoBreve
            descricaoLongaInput.value = infos.descricaoLonga
            idade1Input.value = infos.idade[0]
            idade2Input.value = infos.idade[1]
            EnderecoInput.value = infos.endereco
            TelefoneInput.value = infos.telefone
            ImagensInput.value = infos.imagens.join(", ")
            infos.keyWords.forEach(palavra => {
                document.getElementById(`${palavra}Switch`).checked = true
            })
        }

    }).catch(error => {
        console.log(error)
    })



}