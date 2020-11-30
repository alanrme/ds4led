import os
import dbus
import sys
from time import sleep

class UPowerManager():

    def __init__(self):
        self.UPOWER_NAME = "org.freedesktop.UPower"
        self.UPOWER_PATH = "/org/freedesktop/UPower"

        self.DBUS_PROPERTIES = "org.freedesktop.DBus.Properties"
        self.bus = dbus.SystemBus()

    def detect_devices(self):
        upower_proxy = self.bus.get_object(self.UPOWER_NAME, self.UPOWER_PATH) 
        upower_interface = dbus.Interface(upower_proxy, self.UPOWER_NAME)

        devices = upower_interface.EnumerateDevices()
        return devices

    def get_device_percentage(self, battery):
        battery_proxy = self.bus.get_object(self.UPOWER_NAME, battery)
        battery_proxy_interface = dbus.Interface(battery_proxy, self.DBUS_PROPERTIES)

        return battery_proxy_interface.Get(self.UPOWER_NAME + ".Device", "Percentage")



def interpolate(oldcolors, newcolors, interpolationrange):
    for i in range(interpolationrange+1): # interpolate between the colors and set the dualshock's color to interpolated value
        interpolated = []
        for j in range(len(oldcolors)):
            # find interpolated value, round it, convert to string and add to interpolated array
            interpolated.append(str(round(oldcolors[j] + (newcolors[j] - oldcolors[j]) * i / interpolationrange)))
        os.system(f"ds4led {' '.join(interpolated)}")



def setcolor():
    upwr = UPowerManager()
    devices = upwr.detect_devices()
    # look for an element that contains "sony_controller" in the devices array and replace unnecessary stuff with ""
    matching = [s for s in devices if "sony_controller" in s]
    percentage = upwr.get_device_percentage(matching[0]) # get percentage of first matching device
    print(f"Controller at {str(percentage)}%")

    # above each of these percentages the color next to it is shown
    colors = {
        0: [50,0,0],
        10: [100,30,0],
        20: [80,70,0],
        30: [60,100,0],
        40: [0,100,0],
        80: [80,100,110],
    }
    del sys.argv[0] # remove first arg which is the file to run
    oldcolors = [ int(x) for x in sys.argv ] # convert all elems to int

    for i in colors:
        if percentage > i:
            newcolors = colors[i]

    interpolate(oldcolors, newcolors, 20)
    sleep(1)
    interpolate(newcolors, oldcolors, 20)



setcolor()