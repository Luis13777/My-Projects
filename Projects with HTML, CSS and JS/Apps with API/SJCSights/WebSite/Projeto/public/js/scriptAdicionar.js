// Obtém o elemento do input de telefone
var telefoneInput = document.getElementById('Telefone');

// Adiciona um event listener para capturar as alterações no valor do input
telefoneInput.addEventListener('input', function (e) {
    var telefone = e.target.value;

    // Remove todos os caracteres que não são dígitos
    telefone = telefone.replace(/\D+/g, '');

    // Adiciona os parênteses, espaço e hífen conforme necessário
    telefone = telefone.replace(/^(\d{2})(\d)/g, '($1) $2');
    telefone = telefone.replace(/(\d{5})(\d{4})$/, '$1-$2');

    // Define o valor formatado de volta para o input
    e.target.value = telefone;
});
