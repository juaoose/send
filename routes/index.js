var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'Uniandes Cloud Week!',
    color:  '#b3ffb3'
  });
});

module.exports = router;
