import paho.mqtt.client as mqtt
import time

config_data={
    "temperature":"45",
    "humidity":"90",
    "location":{
        "latitude":"45.56565",
        "longitude":"88.418556"
    }
}

mqtt_pub_topic="mqtt/gdgsiliguri"
client=mqtt.Client()

def on_connect(client, userdata, flags, rc):
    client.connected_flag=True
    client.disconnect_flag=False
    print("Connected")
    print("rc: " + str(rc))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_disconnect(client, userdata, rc):
    print("disconnecting reason  "  +str(rc))
    client.connected_flag=False
    client.disconnect_flag=True
    client.loop_stop()

def on_message(client, userdata, message):
    message_received=json.loads(message.payload)
    print("message received  ",message_received)

def init_mqtt(client,mqtt_host,mqtt_port,mqtt_uid,mqtt_password):
    mqtt.Client.connected_flag=False
    #client.username_pw_set(username=mqtt_uid,password=mqtt_password)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect    
    client.on_publish = on_publish
    client.connect(mqtt_host, int(mqtt_port))
    #client.subscribe(mqtt_topic)
    client.loop_start()
    while not client.connected_flag: #wait in loop
        print("In wait loop")
        time.sleep(1)
    #return 0

def handler():
    mqtt_host="mqtt.eclipse.org"
    mqtt_port="1883"
    mqtt_uid=""
    mqtt_password=""
    #Connection initiated
    init_mqtt(client,mqtt_host,mqtt_port,mqtt_uid,mqtt_password)
    while client.connected_flag:
        client.publish(str(mqtt_pub_topic),str(config_data))
        print(config_data)
        time.sleep(1)

if __name__ == "__main__": 
    handler()
