from openmtc_app.flask_runner import FlaskRunner
from openmtc_app import ContentSubscription, DA

##Este se encarga de imprimir todo lo que se guarde en el contenedor de alertas, al que solo se envian los datos cuando la temperatura es mayor a 70
class Alarm(DA):

    data = []
    container_name = "alarmContainer"
    def _on_register(self):

        alarm_subscription = ContentSubscription(
            None,
            self.container_name,
            content_handler=self._consumption_data
        )
        self.add_content_subscription(alarm_subscription)
        print "alarm_subscription to: Sensor  Container: " + self.container_name

    def _consumption_data(self, application, container, content):
        print "Got content"
        for i in content:
			##necesito un try catch para ver que tipo de alerta es.
            temp = i['temperature']
            house_id = i['house_id']
            self.data.append(temp)
            print "PROBLEMA:Temperatura:", temp

app_instance = Alarm()
gateway_ip= '192.168.169.135:4000'
runner = FlaskRunner(app_instance, port=5097, host='192.168.169.137')
runner.run(gateway_ip)