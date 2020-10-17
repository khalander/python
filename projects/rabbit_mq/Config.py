class RabbitMqServerConfigure() :

    def __init__(self, host, queue, exchange, routingKey) :
        self.host = host
        self.queue = queue
        self.exchange = exchange
        self.routingKey = routingKey