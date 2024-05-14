#################################################################
#
# Code by P. Marti BFH 14.05.2024
# Ecercise OTA updater FS 2024
#
#################################################################

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
from machine import Pin
from time import sleep

#OTA Updater
firmware_url = "https://github.com/BTW2402-IoT/OTA-Updater"
ota_updater = OTAUpdater(IoT-BTW2403, IOTFOREVER, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

LED = Pin(13, Pin.OUT)
ShortBreak = 0.5
LongBreak = 2
Break = 5

#Can't you hear me, S.O.S.
# --- __ __ __ --- 

while(True):
    LED.on()            #1
    sleep(LongBreak)
    LED.off()
    sleep(LongBreak)
    LED.on()            #2
    sleep(LongBreak)
    LED.off()
    sleep(LongBreak)
    LED.on()            #3
    sleep(LongBreak)
    LED.off()
    sleep(LongBreak)
    LED.on()            #4
    sleep(ShortBreak)
    LED.off()
    sleep(ShortBreak)
    LED.on()            #5
    sleep(ShortBreak)
    LED.off()
    sleep(ShortBreak)
    LED.on()            #6
    sleep(ShortBreak)
    LED.off()
    sleep(ShortBreak)
    LED.on()            #7
    sleep(LongBreak)
    LED.off()
    sleep(LongBreak)
    LED.on()            #8
    sleep(LongBreak)
    LED.off()
    sleep(LongBreak)
    LED.on()            #9
    sleep(LongBreak)
    LED.off()
    sleep(Break)
