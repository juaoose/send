var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'Uniandes Cloud Week!',
    color:  '#000000'
  });
});

module.exports = router;
