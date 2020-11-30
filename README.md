# ds4led
#### Note: This is Linux only. You're welcome to fork this and adapt the bash script to Windows.
DualShock 4 LED color and battery utility  
Uses code from (upower-python)[https://github.com/wogscpar/upower-python]  
Based off of (ds4led)[https://gist.github.com/jacobmischka/7f96f3fddf93dbe21db2] by (jacobmischka)[https://github.com/jacobmischka]

## Installation
Copy both scripts to /usr/local/bin, and then run `sudo ds4led` at least once in terminal with the controller connected to set file permissions correctly.  
You can map `ds4led bat` to a hotkey using another tool or your Desktop Environment

## Usage
Set a color using rgb values - `ds4led <red> <green> <blue>`  
Set a preset color - `ds4led [orange/pink/green/red/white/off]`  
Flash battery status - `ds4led bat`

## Battery values
Here are all the rgb values for each battery level:

* 10% - 50, 0, 0
* 20% - 100, 30, 0
* 30% - 80, 70, 0
* 40% - 60, 100, 0
* 50-80% - 0, 100, 0
* 90-100% - 80, 100, 110