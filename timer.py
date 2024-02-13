"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down

import time
import random
from PIL import Image

# Function to play the 'Nerve of Steel' game
def nerve_of_steel_game(image_path):
    print("Players stand")

    # Sleep for a random time between 5 to 25 seconds
    sleep_time = random.randint(5, 25)
    time.sleep(sleep_time)

    # After the sleep time is over, it shows the image and prints the message
    im = Image.open(image_path)
    im.show()
    print("Time Up. Last to sit down wins.")

# The actual image path will need to be provided when calling this function.
nerve_of_steel_game("/Users/bass/Downloads/times-up.jpeg")



