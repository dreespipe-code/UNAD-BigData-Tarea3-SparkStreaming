import json, time, random, datetime
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092",
                         value_serializer=lambda v: json.dumps(v).encode("utf-8"))

barrios = ["Laureles","El Poblado","Belen","Robledo","Buenos Aires"]
tipos = ["CHOQUE","ATROPELLO","VOLCAMIENTO"]

while True:
    msg = {
        "ts": datetime.datetime.now().isoformat(),
        "barrio": random.choice(barrios),
        "tipo_evento": random.choice(tipos),
        "lesionados": random.choice([0,0,1])
    }
    producer.send("accidentes_rt", msg)
    time.sleep(0.5)
