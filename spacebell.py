import argparse
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(args.topic)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


parser = argparse.ArgumentParser(description='The Chaosdorf doorbell service')

parser.add_argument('--server', type=str,
                    help='The mqtt server to connect to',
                    default='mqttserver.chaosdorf.space')
parser.add_argument('--topic', type=str,
                    help='The mqtt topic to subscribe to',
                    default='sensors/space/bell')
parser.add_argument('--sample', type=str,
                    help='The PulseAudio sample to play',
                    default='dong')
args=parser.parse_args()

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect("mqttserver.chaosdorf.space", 1883, 60)

client.loop_forever()
