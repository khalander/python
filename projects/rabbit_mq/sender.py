try :
    from Config import RabbitMqServerConfigure
    from Pub import RabbitMqPublisher
    import os
    from settings import HOST, QUEUE, EXCHANGE, ROUTE_KEY

except Exception as e :
    print(f'Some modules are missing: {e}')


if __name__ == "__main__" :
    print('sss',HOST, QUEUE)
    serverConfig = RabbitMqServerConfigure(
            host = HOST,
            queue = QUEUE,
            exchange = EXCHANGE,
            routingKey = ROUTE_KEY
        )

    serverPublish = RabbitMqPublisher(serverConfig)

    serverPublish.publish(payload = {
        "data" : 22
    })
