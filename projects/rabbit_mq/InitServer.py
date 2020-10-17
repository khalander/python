try :
    import pika
except Exception as e :
    print(f'Some modules are missing: {e}')
    
class RabbitMqInitServer() :

    def __init__ (self, serverConfig) :
       
        self._serverConfig = serverConfig
        self._params = pika.URLParameters(self._serverConfig.host)
        self._connection =  pika.BlockingConnection(self._params)
        self._channel = self._connection.channel()
        self._channel.queue_declare(self._serverConfig.queue, False, True)
        self.exchange = self._serverConfig.exchange
        self.routingKey = self._serverConfig.routingKey