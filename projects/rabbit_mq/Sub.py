try :
    from InitServer import RabbitMqInitServer

except Exception as e :
    print(f'Some modules are missing: {e}')

class RabbitMqSubscriber(RabbitMqInitServer) :

    def __init__ (self, serverConfig) :
        RabbitMqInitServer.__init__(self, serverConfig)
          
    def callback(ch, method, properties, body) :
        print("Message received: ", body)

    def subscriber() :
        self._channel.basic_consume(
            queue='q_short_url', 
            on_message_callback = callback,
            auto_ack=False
        )      
        print('Waiting for message')
        self._channel.start_consuming()