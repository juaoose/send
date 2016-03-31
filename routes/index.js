var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'Uniandes Cloud Week!',
    color:  '#'+Math.floor(Math.random()*16777215).toString(16)
  });
});

module.exports = router;
