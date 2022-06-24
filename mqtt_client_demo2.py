import paho.mqtt.client as mqtt

# define static variable
# broker = "localhost" # for local connection
broker = "test.mosquitto.org"  # for online version
port = 1883
timeout = 60

username = ''
password = ''

topic = "mentor/pratama"
topic_greetings = "mentor/pratama/greetings"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic,qos=2)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload_decoded = msg.payload.decode('utf-8')

    print("Pesan diterima: " + payload_decoded)

    # publish message yang diterima dengan dimodifikasi seperti diatas dan publish ke topic_greetings
    # client1.publish(topic,payload=message,qos=1)
    # isi jawaban disini
    print("Pesan diteruskan")
    client.publish(topic_greetings, payload="Halo " + payload_decoded + ", selamat siang", qos=1)

          
        
# Create an MQTT client and attach our routines to it.
client = mqtt.Client("pratama19")
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)

client.loop_forever()

