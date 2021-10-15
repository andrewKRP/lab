import platform
import threading
import time
from datetime import datetime


def system_time():
    while 1:
        print(datetime.now())
        time.sleep(5)


def system_arch():
    while 1:
        print(platform.architecture()[0])
        time.sleep(10)


threading.Thread(target=system_time).start()
threading.Thread(target=system_arch).start()

