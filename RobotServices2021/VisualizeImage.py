#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""" Get an image. Display it and save it using PIL."""

import qi
import argparse
import sys
import time
from PIL import Image


def main(session):
    # Get the service ALVideoDevice.

    video_service = session.service("ALVideoDevice")
    resolution = 2    # VGA
    color_space = 11   # RGB

    video_client = video_service.subscribe("python_client", resolution, color_space, 5)

    # Timing to check transfer delta
    t0 = time.time()

    # Acquire image using ALVideoDevice
    # image[6] contains the image data passed as an array of ASCII chars.
    nao_image = video_service.getImageRemote(video_client)

    t1 = time.time()

    # Time the image transfer.
    print "acquisition delay ", t1 - t0

    video_service.unsubscribe(video_client)

    # Get the image size and pixel array.
    image_width = nao_image[0]
    image_height = nao_image[1]
    array = nao_image[6]
    image_string = str(bytearray(array))

    # Create a PIL Image from our pixel array.
    # im = Image.fromstring("RGB", (image_width, image_height), image_string)
    im = Image.frombytes("RGB", (image_width, image_height), image_string)

    # Save the image.
    im.save("camImage.png", "PNG")

    im.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.131",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n")
        sys.exit(1)
    main(session)