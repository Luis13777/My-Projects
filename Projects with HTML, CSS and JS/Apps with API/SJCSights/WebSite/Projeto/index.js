const express = require("express")
const app = express()

app.set("view engine", "ejs")
app.use(express.static(`public`))


app.get("/", (req,res)=>{
    res.render("index")
})

app.get('/explorar', (req,res)=>{
    res.render("explorar")
})

app.listen(8080, ()=>{
    console.log("App Rodando na porta 8080")
})