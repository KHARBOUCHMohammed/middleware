var express = require('express');
var app = express();
var path = require('path');
var mediaserver= require('mediaserver');
var fs = require('fs');
const fileUpload = require('express-fileupload');
var formidable = require('formidable');

app.get('/',function(req,res){

res.sendFile(__dirname+'/index.html');

});

app.get('/getMusic/:name',function (req,res) {
  var son =path.join(__dirname,'Musiques',req.params.name);
  var files = fs.readdirSync('Musiques/');
  mediaserver.pipe(req,res,son);
});

app.get('/getAllMusic/',function (req,res) {
  var files = fs.readdirSync('Musiques/');
  res.json(files);
});


app.listen(3000, function() {
    console.log("Lestning in 3000");

});



app.post('/sendText', function(req, res) {
    var form = new formidable.IncomingForm();
    form.parse(req, function(err, fields, files) {
        if (err) {
            console.error(err);
            return res.sendStatus(500);
        }

        var text = fields.text;
        console.log('Text received:', text);

        var words = text.split(' '); // Sépare le texte en mots en utilisant l'espace comme séparateur
        var firstWord = words[0]; // Récupère le premier mot
        var restOfText = words.slice(1).join(' '); // Récupère le reste du texte en le recomposant à partir des autres mots

        console.log('\'Action\':', firstWord);
        console.log('\'Objet\':', restOfText);

        // Enregistre les textes "Action" et "Objet" dans un fichier texte
        var data = 'Action: ' + firstWord + '\n' + ' Objet: ' + restOfText + '\n';
        fs.writeFile('output.txt', data, function(err) {
            if (err) {
                console.error(err);
                return res.sendStatus(500);
            }

            console.log('Text saved to output.txt');
            res.sendStatus(200);
        });
    });
});