var express = require('express');
var router = express.Router();

/* POST messages */
router.post('/', function(req, res, next) {
  console.log("message recived", req.body.color);
  res.end();
});

module.exports = router;