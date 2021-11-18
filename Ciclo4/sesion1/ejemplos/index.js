const math = require('./math');
const os = require('os');
const colors = require('colors');
const express = require('express');
const app = express();

app.get('/', function(req, res) {
    res.send('<h1> Hola Mundo desde node.js Express <h1>');
});

app.listen(3000, function() {
    console.log('server on port 3000'.blue);
});


/*
console.log(math.add(1, 2));
console.log(math.substract(1, 2));
console.log(math.multiply(1, 2));
console.log(math.division(1, 2));

console.log('el sistema operativo es: ', os.platform());
console.log('este mensaje es azul'.blue)
*/