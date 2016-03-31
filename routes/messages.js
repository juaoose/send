var express = require('express');
var router = express.Router();
var eventHubs = require("eventhubs-js")



/* POST messages */
router.post('/', function(req, res, next) {
    var color = req.body.color;
    var id = req.body.id;
    console.log("message recived", color);
  
    var hubnamespace = 'cloudweek';
    var hubname = 'uniandes';
    var keyname = 'send';
    var key = 'UQvsUaY2U6gvURspPgkN2MQ3XQUkd09Tllolv/Cvnbw=';

    eventHubs.init({
        hubNamespace: hubnamespace,
        hubName: hubname,
        keyName: keyname,
        key: key
    });
    
    try{
        eventHubs.sendMessage({
            message: {
                color: color
            },
            deviceId: id
        }).then(function () {
            console.info('message sended');
        }).catch(function (error) {
            console.error(error);
        });
    }  catch(e){
        console.error(e);
    }
    res.end();
});

module.exports = router;