try :
    from Config import RabbitMqServerConfigure
    from Pub import RabbitMqPublisher

except Exception as e :
    print(f'Some modules are missing: {e}')


if __name__ == "__main__" :

    serverConfig = RabbitMqServerConfigure(
            host = 'localhost',
            queue = 'hello',
            exchange = 'amq.direct',
            routingKey = 'hello'
        )

    serverPublish = RabbitMqPublisher(serverConfig)

    serverPublish.publish(payload = {
        "data" : 22
    })
