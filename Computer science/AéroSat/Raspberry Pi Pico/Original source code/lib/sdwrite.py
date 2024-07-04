import os
from machine import Pin, SPI
import sdcard

# Define SD card pins
SD_CS_PIN = 1
SD_SCK_PIN = 2
SD_MOSI_PIN = 3
SD_MISO_PIN = 4

# Initialize SPI
spi = SPI(0, baudrate=100000, sck=Pin(SD_SCK_PIN), mosi=Pin(SD_MOSI_PIN), miso=Pin(SD_MISO_PIN))

# Initialize SD card
sd = sdcard.SDCard(spi, Pin(SD_CS_PIN))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')

# Example write to file
with open('/sd/test.txt', 'w') as f:
    f.write("Hello, world!\n")

# Example read from file
with open('/sd/test.txt', 'r') as f:
    print(f.read())

# Unmount SD card
os.umount('/sd')
