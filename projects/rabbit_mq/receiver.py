
try :
    from Config import RabbitMqServerConfigure
    from Sub import RabbitMqSubscriber

except Exception as e :
    print(f'Some modules are missing: {e}')


if __name__ == "__main__" :

    serverConfig = RabbitMqServerConfigure(
            host = 'localhost',
            queue = 'hello',
            exchange = 'amq.direct',
            routingKey = 'hello'
        )

    serverSubscriber = RabbitMqSubscriber(serverConfig)

    serverSubscriber.subscriber()
