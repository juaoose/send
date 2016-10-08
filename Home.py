from openmtc_app import DA
from openmtc_app.flask_runner import FlaskRunner
from random import randint
import time
import sys
import traceback

##Este se encarga de enviar los valores de los sensores, esto se envia al contenedor de una casa especifica.
class TempSensor(DA):



    def __init__(self, house_id=None):
        DA.__init__(self)
        self.house_id = house_id
        self.container_id = 'containerValoresSensores'

    def _on_register(self):
        print '_on_register'
        try:
            self.container = self.get_application('TempSensor1/containers/' + self.container_id)
            print "Container Found"
        except Exception:
            print "Container Not Found , Creating container"
            self.container = self.create_container(self.application, self.container_id)

        print "House " + str(self.house_id) + " launched"
        while True:
		##Valores random
			presion = randint(0, 100)
			glucosa = randint(0, 100)
			flow = randint(0, 100)
			oximetro = randint(0, 100)
            temperatura = randint(0,100)
            data = {
                "temperature": temperatura,
				"glucose": glucosa,
				"presion": presion,
				"flow": flow,
				"spo2": oximetro
                "house_id":self.house_id
            }
            self.push_content(self.container, data)
            print data
            time.sleep(5)

##identificador de cada sensor
house_id = 1
app_instance = TempSensor(house_id)
app_instance.app_id = 'TempSensor1'
app_instance.search_strings = ("TempHomes", )
gateway_add = '192.168.169.135:4000'
runner = FlaskRunner(app_instance,port=5001)
runner.run(gateway_add)







