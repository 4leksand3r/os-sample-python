from flask import Flask
from kafka import KafkaProducer

application = Flask(__name__)

@application.route("/producer")
def producer():
    
    prod = KafkaProducer(bootstrap_servers=['my-cluster-kafka-bootstrap:9091'], value_serializer=lambda x: dumps(x).encode('utf-8'))
    for e in range(1000):
        data = {'number' : e}
        prod.send('numtest', value=data)
    
    
    return "Kafka producer test"

@application.route("/consumer")
def consumer():
    return "Kafka consumer test"

@application.route("/")
def hello():
    return "Распакуй меня!"

if __name__ == "__main__":
    application.run()
