from flask import Flask
from kafka import KafkaProducer

application = Flask(__name__)

@application.route("/producer")
def producer():
    return "Kafka producer test"

@application.route("/")
def hello():
    return "Ей, ты! А ну выпусти меня из этого контейнера!"

if __name__ == "__main__":
    application.run()
