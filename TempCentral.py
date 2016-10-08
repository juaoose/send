from openmtc_app.flask_runner import FlaskRunner
from openmtc_app import ContentSubscription, NA

##Servidor
class Central(NA):

    data = []
    alertContainers = []

    def _on_register(self):

        container = 'containerValoresSensores'

        temp_subscription = ContentSubscription(
            None,
            (container,),
            ("TempHomes",),
            content_handler=self._consumption_data,
            container_handler=self.cont_hand,
            application_handler=self.handle_app
        )

        self.add_content_subscription(temp_subscription)
        print "Content_subscription to: Sensor  Container: " + container

        #Creación o verificación del contenedor de valores criticos.
        alarm_container_name =  "alarmContainer"
        try:
            alarmcontainer = self.get_application('Central/containers/' + alarm_container_name)
            print "Container  Alarm Found"
            self.alertContainers.append(alarmcontainer)
        except Exception:
            print "Container Alarm Not Found , Creating container"
            alarmcontainer = self.create_container(self.application, alarm_container_name)
            self.alertContainers.append(alarmcontainer)

    def cont_hand(self, application, container):
        print "CONTAINER " + container.name + " " + application.name

    def handle_app(self, application):
        print "handle_app " + application.name

    def _consumption_data(self, application, container, content):
        for i in content:
            print i
            temp = i['temperature']
			presion = i['presion']
			spo2 = i['spo2']
			glucosa = i['glucose']
			flow = i['flow']
            house_id = i['house_id']
            self.data.append(temp)
			##Verificar Temperatura
            if temp > 37.5:
                print "PROBLEMA:Temperatura:", temp , "house_id: ", house_id, " Container: ", container.name
                data = {
                    "temperature": temp,
                    "house_id": house_id
                }
                self.push_content(self.alertContainers[house_id-1], data)
            else:
                print "OK:Temperatura:", temp, "house_id: ", house_id, " Container: ", container.name
				##Puedo pushear data a un contenedor general para valores que no son alerta.
			##Verificar Presion
			if presion > 37.5:
                print "PROBLEMA:Presion:", presion , "house_id: ", house_id, " Container: ", container.name
                data = {
                    "presion": presion,
                    "house_id": house_id
                }
                self.push_content(self.alertContainers[house_id-1], data)
            else:
                print "OK:Presion:", presion, "house_id: ", house_id, " Container: ", container.name
			##Verificar Glucosa
			if glucosa > 37.5:
                print "PROBLEMA:Glucosa:", glucosa , "house_id: ", house_id, " Container: ", container.name
                data = {
                    "glucosa": glucosa,
                    "house_id": house_id
                }
                self.push_content(self.alertContainers[house_id-1], data)
            else:
                print "OK:Glucosa:", glucosa, "house_id: ", house_id, " Container: ", container.name
			##Verificar Oximeter	
			if spo2 < 0.94:
                print "PROBLEMA:Oximeter:", spo2 , "house_id: ", house_id, " Container: ", container.name
                data = {
                    "spo2": spo2,
                    "house_id": house_id
                }
                self.push_content(self.alertContainers[house_id-1], data)
                ##print "Sent alert - temp:", temp, "house_id: ", house_id
            else:
                print "OK:Oximeter:", spo2, "house_id: ", house_id, " Container: ", container.name
			##Verificar respiracion
			if flow > 37.5:
                print "PROBLEMA:Respiracion:", flow , "house_id: ", house_id, " Container: ", container.name
                data = {
                    "flow": flow,
                    "house_id": house_id
                }
                self.push_content(self.alertContainers[house_id-1], data)
                ##print "Sent alert - temp:", temp, "house_id: ", house_id
            else:
                print "OK:Respiracion:", flow, "house_id: ", house_id, " Container: ", container.name


app_instance = Central()

core_ip = '192.168.169.135:4000'
runner = FlaskRunner(app_instance, port=5076, host='192.168.169.137')
runner.run(core_ip)
