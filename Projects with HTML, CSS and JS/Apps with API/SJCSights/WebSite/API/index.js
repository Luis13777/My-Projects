const express = require("express")
const app = express()
const bodyParser = require("body-parser")
const cors = require("cors")

app.use(cors())
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

const connectString = "mongodb+srv://luis:meucluster@clusterprojetomtp.jaqwgna.mongodb.net/BancoDeDadosSJC"


const mongoose = require("mongoose");
mongoose.connect(connectString, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((err) => {
    console.log("Error connecting to MongoDB:", err);
  });

// mongoose.connect("mongodb://localhost:27017/BancoDeDadosSJC", {
//   useNewUrlParser: true,
//   useUnifiedTopology: true,
// })
//   .then(() => {
//     console.log("Connected to MongoDB");
//   })
//   .catch((err) => {
//     console.log("Error connecting to MongoDB:", err);
//   });

const localSchema = new mongoose.Schema({
    title: String,
    descricaoBreve: String,
    descricaoLonga: String,
    avaliacao: Number,
    imagens: Array,
    keyWords: Array,
    idade: Array,
    endereco: String,
    telefone: String
});

Local = mongoose.model("locais", localSchema);

app.get("/locais", (req, res) => {
    Local.find()
      .then((locais) => {
        res.statusCode = 200;
        res.json(locais);
      })
      .catch((err) => {
        console.log(err);
        res.sendStatus(500);
      });
  });


  app.get("/local/:titulo", (req, res) => {
    const titulo = req.params.titulo;
  
    Local.findOne({ title: titulo })
      .then((local) => {
        if (local) {
          res.statusCode = 200;
          res.json(local);
        } else {
          res.statusCode = 404;
          res.json({ mensagem: "Local não encontrado" });
        }
      })
      .catch((err) => {
        console.log(err);
        res.sendStatus(500);
      });
  });
  



  
  app.post("/local", (req, res) => {
    const { title, descricaoBreve, descricaoLonga, avaliacao, imagens, keyWords, idade, endereco, telefone} = req.body;
  
    const newLocal = new Local({
      title: title,
      descricaoBreve: descricaoBreve,
      descricaoLonga: descricaoLonga,
      avaliacao: avaliacao,
      imagens: imagens,
      keyWords: keyWords,
      idade: idade,
      endereco: endereco,
      telefone: telefone
    });
  
    newLocal
      .save()
      .then(() => {
        res.sendStatus(200);
      })
      .catch((err) => {
        console.log(err);
        res.sendStatus(500);
      });
  });


  app.delete("/local/:titulo", (req, res) => {
    const localTitle = req.params.titulo;
  
    Local.findOneAndDelete({ title: localTitle })
      .then(() => {
        res.sendStatus(200);
      })
      .catch((err) => {
        console.log(err);
        res.sendStatus(500);
      });
  });
  
  app.put("/local/:titulo", (req, res) => {
    const localTitle = req.params.titulo;

    const { title, descricaoBreve, descricaoLonga, avaliacao, imagens, keyWords, idade, endereco, telefone} = req.body;
  
    Local.findOneAndUpdate({ title: localTitle }, { title, descricaoBreve, descricaoLonga, avaliacao, imagens, keyWords, idade, endereco, telefone}, { new: true })
      .then(() => {
        res.sendStatus(200);
      })
      .catch((err) => {
        console.log(err);
        res.sendStatus(500);
      });
  });
  

app.listen(45678,()=>{
    console.log("API rodando na porta 45678!")
})