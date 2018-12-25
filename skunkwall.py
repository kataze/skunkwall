from PIL import Image
from skunkwall_constants import WALL_HEIGHT, WALL_WIDTH

import asyncio
import aioping
import argparse

# Don't tell my mom
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (10000, -1))


def main():
    parser = argparse.ArgumentParser()
    help_string = f"The file to put on the wall! (Max res {WALL_WIDTH}x{WALL_HEIGHT})"
    parser.add_argument("image_file", help=help_string)
    args = parser.parse_args()

    with Image.open(args.image_file) as image:
        width, height = image.size
        if width > WALL_WIDTH or height > WALL_HEIGHT:
            raise RuntimeError(f"The image provided is too big to fit on the wall (Max res {WALL_WIDTH}x{WALL_HEIGHT})")
        
        image_pixels = image.load()
        # Targeting the lower right corner because it seems the least popular right now
        wall_x_offset = WALL_WIDTH - width
        wall_y_offset = WALL_HEIGHT - height
        
        
        
        for image_y in range(0,height):
            wall_y = image_y + wall_y_offset
            for image_x in range(0,width):
                red, green, blue, alpha = image_pixels[image_x,image_y]
                wall_x = image_x + wall_x_offset

                # IP ADDRESS FORMAT 2001:4c08:2028:X:Y:AA:BB:CC
                pixel_ip = f"2001:4c08:2028:{wall_x}:{wall_y}:{red:02x}:{green:02x}:{blue:02x}"
                print(pixel_ip)

                loop = asyncio.get_event_loop()
                loop.run_until_complete(aioping.verbose_ping(pixel_ip, timeout=0))


if __name__ == '__main__':
    main()
