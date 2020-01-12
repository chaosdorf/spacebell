# SpaceBell

## Description

This is a tiny service with the purpose to ring a bell when someone is at the door.

The bell button emits a message on mqtt, which is subscribed by the service. At every occurrence, the service plays a prepared audio sample on the PulseAudio server. This call is rate limited, to stop annoyance.

## Requirements/Usage

You need running mqtt and PulseAudio (PA) servers.

If the PA server runs on another machine, set an environment variable similar to this:

```
export PULSE_SERVER=pulseserver
```

SpaceBell uses Python 3 and some libraries. Install them like this:

```
pip3 install --user -r requirements.txt
```

Run the service with the following options:

```
usage: spacebell.py [-h] [--server SERVER] [--topic TOPIC] [--sample SAMPLE]

The Chaosdorf doorbell service

optional arguments:
  -h, --help       show this help message and exit
  --server SERVER  The mqtt server to connect to
  --topic TOPIC    The mqtt topic to subscribe to
  --sample SAMPLE  The PulseAudio sample to play
```

## Deployment

At the hackspace, we use [Docker Stacks](https://github.com/chaosdorf/docker-stacks) to deploy the service. When changing the code, make sure to update the Dockerfile as well, if needed!
