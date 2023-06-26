function deleteFunction (titulo){

    axios.delete("http://localhost:45678/local/" + titulo).then(response => {
        alert("Local deletado!")
        location.reload();
    }).catch(err => {
        console.log(err)
    })

}