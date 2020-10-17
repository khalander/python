from decouple import config
HOST = config('HOST')
QUEUE = config('QUEUE')
EXCHANGE = config('EXCHANGE')
ROUTE_KEY = config('ROUTE_KEY')