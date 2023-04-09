import TeachableMachine as tm
import AIO as aio
from datetime import datetime as dt
import time

aio.client.connect()
aio.client.loop_background()

while True:
    aio.client.publish(aio.TEST_FEED_ID, str(dt.now().time()))
    time.sleep(3)
