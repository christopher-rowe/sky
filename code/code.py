import board
import neopixel
import time
import sky

numpix = 133
pixels = neopixel.NeoPixel(board.D3, numpix, brightness=1, auto_write=False)

vector_bounds = [[6, 13], [23, 14], [24, 34], [46, 35],
                 [47, 59], [72, 60], [73, 85], [97, 86], [98, 108],
                 [118, 109], [119, 126]]

while True:

    for path in range(1, len(vector_bounds)-4):

        # set sky to night
        for i in range(0, numpix):
            pixels[i] = [0, 0, 0]
        pixels.write()

        # dawn
        sky.dawndusk(pixels, vector_bounds, path,
                    [0, 0, 0], [0, 0, 10], 0, 1000,
                    dawn = False)

        sky.dawndusk(pixels, vector_bounds, path,
                     [0, 0, 10], [0, 0, 40], 0, 1000,
                     dawn = True)

        # sun path
        sky.sunpath(pixels, vector_bounds, path,
                    [225, 225, 0], [0, 0, 40], 0, 1000)

        # dusk
        sky.dawndusk(pixels, vector_bounds,
                     len(vector_bounds) - 1 - path,
                     [0, 0, 40], [0, 0, 10], 0, 1000,
                     dawn = False)

        # sunset
        sky.sunset(pixels, vector_bounds,
                   path, 0, 1000)

        # nightfall
        sky.dawndusk(pixels, vector_bounds,
                     len(vector_bounds) - 1 - path,
                     [0, 0, 10], [0, 0, 0], 0, 1000,
                     dawn = False)
