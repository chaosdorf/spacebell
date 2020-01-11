import argparse
import paho.mqtt.client as mqtt
import pulsectl


def on_connect(mqtt_server, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqtt_server.subscribe(args.topic)


def on_message(mqtt_server, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    print(args.sample)
    pulse_server.play_sample(args.sample, pulse_sinks[0])


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
args = parser.parse_args()

pulse_server = pulsectl.Pulse('spacebell')
pulse_sinks = pulse_server.sink_list()

mqtt_server = mqtt.Client()
mqtt_server.on_connect = on_connect
mqtt_server.on_message = on_message

mqtt_server.connect(args.server, 1883, 60)

mqtt_server.loop_forever()
