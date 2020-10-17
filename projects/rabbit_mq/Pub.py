try :
    from InitServer import RabbitMqInitServer

except Exception as e :
    print(f'Some modules are missing: {e}')

class RabbitMqPublisher(RabbitMqInitServer) :

    def __init__ (self, serverConfig) :
        RabbitMqInitServer.__init__(self, serverConfig)

            
    def publish(self, payload = {}) :

        self._channel.basic_publish(
                exchange = self.exchange,
                routing_key = self.routingKey,
                body = str(payload)
        )
        print("Published message")
        self._connection.close()
