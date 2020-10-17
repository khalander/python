
try :
    from Config import RabbitMqServerConfigure
    from Sub import RabbitMqSubscriber
    from settings import HOST, QUEUE, EXCHANGE, ROUTE_KEY

except Exception as e :
    print(f'Some modules are missing: {e}')


if __name__ == "__main__" :

    serverConfig = RabbitMqServerConfigure(
            host = HOST,
            queue = QUEUE,
            exchange = EXCHANGE,
            routingKey = ROUTE_KEY
        )

    serverSubscriber = RabbitMqSubscriber(serverConfig)

    serverSubscriber.subscriber()

