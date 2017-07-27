# Picture capture script for the ERRNO cubesat
#
# Requires a serial connection to initiate the main loop. This is done by
#   an Arduino connected over GPIO.


# ===== Dependencies ===== #
import serial, picamera, json
from RPi import GPIO
from time import time, sleep
from os import chdir
# ===== Dependencies ===== #


# ===== Globals ===== #
SCRIPT_DIR = "/home/pi/ERRNO_Picture_Daemon"
# ===== Globals ===== #


# ===== Function Definition ===== #
# Load a JSON file into a python variable
def load_json(save_file):
  state = open(save_file, "r")
  contents = json.load(state)
  state.close()

  return contents

# Load a JSON file into a python variable
def save_json(save_file, contents):
  out = open(save_file, "w")
  json.dump(contents, out)
  out.close()

# Take a picture and store it in the current working directory
def takePicture():
  camera.capture(str(time()).replace(".", "") + '.jpg')
  return
# ===== Function Definition ===== #


# ===== Main Section ===== #
if __name__ == "__main__":
  # Grab configuration
  config = load_json("{}/config.json".format(SCRIPT_DIR))

  # Change to the correct directory
  chdir("{}/{}".format(SCRIPT_DIR, config["picture_dir"]))

  # Configure the serial connection
  ser = serial.Serial(config["serial_port"], config["baud_rate"])
  ser.baudrate = config["baud_rate"]

  # Get the camera connection
  camera = picamera.PiCamera()

  # Set the GPIO mode
  GPIO.setmode(GPIO.BOARD)

  # Block the thread for a while until we get a line
  read_ser = ser.readline()

  # Determine the wait time
  wait_ms = config["wait_time_minutes"] * 60 * 1000;

  # If the command recieved is the one to initiate the pictures, start capture
  if(read_ser == config["start_cmd"]):
    while True:
      # Do the thing
      takePicture()

      # Send reply back confirming picture was taken

      # Sleep for five minutes
      sleep()
# ===== Main Section ===== #
