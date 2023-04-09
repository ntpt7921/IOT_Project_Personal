from Adafruit_IO import MQTTClient
import sys
import time
from datetime import datetime
import tomli

with open("../config.toml", "rb") as config_file:
    config = tomli.load(config_file)
aio_cfg = config['AIO']

AIO_USERNAME = aio_cfg['username']
AIO_KEY = aio_cfg['key']
TEST_FEED_ID = aio_cfg['feed']['sensor1']['feed_id']

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(TEST_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    client.publish(TEST_FEED_ID, str(datetime.now().time()))
    time.sleep(3)
