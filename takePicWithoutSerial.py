# Picture capture script for the ERRNO cubesat
#
# Requires a serial connection to initiate the main loop. This is done by
#   an Arduino connected over GPIO.


# ===== Dependencies ===== #
import json, picamera
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
def takePicture(camera):
  camera.capture(str(time()).replace(".", "") + '.jpg')
  return
# ===== Function Definition ===== #


# ===== Main Section ===== #
if __name__ == "__main__":
  # Grab configuration
  config = load_json("{}/config.json".format(SCRIPT_DIR))

  # Change to the correct directory
  chdir("{}/{}".format(SCRIPT_DIR, config["picture_dir"]))

  # Get the camera connection
  camera = picamera.PiCamera()

  # Determine the wait time
  wait_ms = config["wait_time_minutes"] * 60;

  # Take picture then wait for configured interval
  while True:
    # Do the thing
    takePicture(camera)

    # Sleep for five minutes
    sleep(wait_ms)
# ===== Main Section ===== #
