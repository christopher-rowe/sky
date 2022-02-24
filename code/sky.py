import time
import adj
import gc
try:
    import urandom as random
except ImportError:
    import random

# dawn & dusk
def dawndusk(pixels, vbounds, path, c1, c2, delay, steps, dawn):

    # calcualte c1-c2 step sizes
    c1_c2_steps = [0, 0, 0]
    for i in range(0, 3):
        c1_c2_steps[i] = (c2[i] - c1[i])/(steps-1)

    # calculate max neighbor paths
    max_neighbor_paths = max(path, abs((len(vbounds) - 1) - path))

    # calcualte dsky-sun step sizes
    if dawn:
        sun = [225, 225, 0]
        sun_color = c2
        dsky_sun_steps = [0, 0, 0]
        multiplier = (max_neighbor_paths+9) - round((max_neighbor_paths+9)/3)
        for i in range(0, 3):
            dsky_sun_steps[i] = (sun[i] - c2[i])/(steps*multiplier-1)

    # define path range and variable to define prior pixel
    if vbounds[path][0] < vbounds[path][1]:
        path_range = list(range(vbounds[path][0], vbounds[path][1] + 1))
    else:
        path_range = list(reversed(range(vbounds[path][1], vbounds[path][0]+1)))

    # define neighborhing path ranges
    neighbor_path_ranges_l = {}
    neighbor_path_ranges_r = {}
    for i in range(1, max_neighbor_paths + 1):
        if (path - i) >= 0:
            if vbounds[path - i][0] < vbounds[path - i][1]:
                neighbor_path_ranges_l[str(i)] = list(range(vbounds[path - i][0], vbounds[path - i][1] + 1))
            else:
                neighbor_path_ranges_l[str(i)] = list(reversed(range(vbounds[path - i][1], vbounds[path - i][0] + 1)))
        if (path + i) <= (len(vbounds) - 1):
            if vbounds[path + i][0] < vbounds[path + i][1]:
                neighbor_path_ranges_r[str(i)] = list(range(vbounds[path + i][0], vbounds[path + i][1] + 1))
            else:
                neighbor_path_ranges_r[str(i)] = list(reversed(range(vbounds[path + i][1], vbounds[path + i][0] + 1)))

    color = []
    for p in pixels:
        color.append(p)
    for i in range(0, max_neighbor_paths + 9):
        for j in range(0, steps):
            if i <= (len(path_range) - 1):
                color[path_range[i]] = [max(min(color[path_range[i]][0] + c1_c2_steps[0], 255), 0),
                                        max(min(color[path_range[i]][1] + c1_c2_steps[1], 255), 0),
                                        max(min(color[path_range[i]][2] + c1_c2_steps[2], 255), 0)]
                pixels[path_range[i]] = [round(color[path_range[i]][0]),
                                         round(color[path_range[i]][1]),
                                         round(color[path_range[i]][2])]

            for k in range(1, max_neighbor_paths + 1):
                if i >= k:
                    if len(neighbor_path_ranges_l) >= k:
                        if i - k < (len(neighbor_path_ranges_l[str(k)])):
                            color[neighbor_path_ranges_l[str(k)][i - k]] = [max(min(color[neighbor_path_ranges_l[str(k)][i - k]][0] + c1_c2_steps[0], 255), 0),
                                                                            max(min(color[neighbor_path_ranges_l[str(k)][i - k]][1] + c1_c2_steps[1], 255), 0),
                                                                            max(min(color[neighbor_path_ranges_l[str(k)][i - k]][2] + c1_c2_steps[2], 255), 0)]
                            pixels[neighbor_path_ranges_l[str(k)][i - k]] = [round(color[neighbor_path_ranges_l[str(k)][i - k]][0]),
                                                                             round(color[neighbor_path_ranges_l[str(k)][i - k]][1]),
                                                                             round(color[neighbor_path_ranges_l[str(k)][i - k]][2])]
                    if len(neighbor_path_ranges_r) >= k:
                        if i - k < (len(neighbor_path_ranges_r[str(k)])):
                            color[neighbor_path_ranges_r[str(k)][i - k]] = [max(min(color[neighbor_path_ranges_r[str(k)][i - k]][0] + c1_c2_steps[0], 255), 0),
                                                                            max(min(color[neighbor_path_ranges_r[str(k)][i - k]][1] + c1_c2_steps[1], 255), 0),
                                                                            max(min(color[neighbor_path_ranges_r[str(k)][i - k]][2] + c1_c2_steps[2], 255), 0)]
                            pixels[neighbor_path_ranges_r[str(k)][i - k]] = [round(color[neighbor_path_ranges_r[str(k)][i - k]][0]),
                                                                             round(color[neighbor_path_ranges_r[str(k)][i - k]][1]),
                                                                             round(color[neighbor_path_ranges_r[str(k)][i - k]][2])]
            if dawn and i/(max_neighbor_paths+9) > 0.33:
                sun_color = [sun_color[0] + dsky_sun_steps[0],
                             sun_color[1] + dsky_sun_steps[1],
                             sun_color[2] + dsky_sun_steps[2]]
                pixels[vbounds[path][0]] = [round(max(min(sun_color[0], 255), 0)),
                                            round(max(min(sun_color[1], 255), 0)),
                                            round(max(min(sun_color[2], 255), 0))]

            pixels.write()
            time.sleep(delay)


# sun's journey
def sunpath(pixels, vbounds, path, sun, dsky, delay, steps):

    # calcualte dsky-sun step sizes
    dsky_sun_steps = [0, 0, 0]
    sun_dsky_steps = [0, 0, 0]
    for i in range(0, 3):
        dsky_sun_steps[i] = (sun[i] - dsky[i])/(steps-1)
        sun_dsky_steps[i] = (dsky[i] - sun[i])/(steps-1)

    # define path range and variable to define prior pixel
    if vbounds[path][0] < vbounds[path][1]:
        path_range = range(vbounds[path][0]+1, vbounds[path][1]+1)
        prior = -1
    else:
        path_range = reversed(range(vbounds[path][1], vbounds[path][0]))
        prior = 1

    for i in path_range:
        color1 = dsky
        color2 = sun
        for c in range(0, steps):
            color1 = [color1[0] + dsky_sun_steps[0],
                      color1[1] + dsky_sun_steps[1],
                      color1[2] + dsky_sun_steps[2]]
            pixels[i] = [round(max(min(color1[0], 255), 0)),
                         round(max(min(color1[1], 255), 0)),
                         round(max(min(color1[2], 255), 0))]
            pixels.write()

            color2 = [color2[0] + sun_dsky_steps[0],
                      color2[1] + sun_dsky_steps[1],
                      color2[2] + sun_dsky_steps[2]]
            pixels[i + prior] = [round(max(min(color2[0], 255), 0)),
                                 round(max(min(color2[1], 255), 0)),
                                 round(max(min(color2[2], 255), 0))]
            pixels.write()
            time.sleep(delay)

    color = sun
    for c in range(0, steps):
        color = [color[0] + sun_dsky_steps[0],
                 color[1] + sun_dsky_steps[1],
                 color[2] + sun_dsky_steps[2]]
        pixels[vbounds[path][1]] = [round(max(min(color[0], 255), 0)),
                                    round(max(min(color[1], 255), 0)),
                                    round(max(min(color[2], 255), 0))]
        pixels.write()
        time.sleep(delay)

def sunset(pixels, vbounds, path, delay, steps):

    initial_color = pixels[vbounds[path][0]]

    c1 = [0,0,10]
    origin = vbounds[path][1]
    mega_blob = []
    while len(mega_blob) / (max(max(vbounds)) - min(min(vbounds))) < 0.6:
        orange = random.randint(0,1)
        if orange == 1:
            r = random.randint(0, 100)
            g = round((random.randint(0,70)/100)*r)
            b = 0
            c2 = [r, g, b]
        else:
            r = random.randint(0, 100)
            g = 0
            b = r + round((random.randint(-100,100)/100)*r)
            c2 = [r, g, b]
        blob_size = random.randint(15, 50)
        blob_pixels = [origin]
        for i in range(0, blob_size):
            candidates = [x for x in adj.get_adj_p(blob_pixels[i]) if x not in blob_pixels]
            if len(candidates) == 0:
                break
            if len(candidates)==1:
                num_to_select = 1
            else:
                num_to_select = random.choice(range(1,len(candidates)))
            selection = []
            for j in range(0, num_to_select):
                candidates = [x for x in candidates if x not in selection]
                selection.extend([random.choice(candidates)])
            blob_pixels.extend(selection)
        del candidates
        del selection
        del num_to_select
        gc.collect()

        c1 = [pixels[i] for i in blob_pixels]
        color = c1
        for i in range(0, steps):
            for j in range(0, len(blob_pixels)):
                color[j] = [max(min(color[j][0] + (c2[0] - c1[j][0])/(steps-1), 255), 0),
                            max(min(color[j][1] + (c2[1] - c1[j][1])/(steps-1), 255), 0),
                            max(min(color[j][2] + (c2[2] - c1[j][2])/(steps-1), 255), 0)]
                pixels[blob_pixels[j]] = [round(color[j][0]),
                                          round(color[j][1]),
                                          round(color[j][2])]
            pixels.write()
            time.sleep(delay)

        origin = random.choice(blob_pixels)
        to_add = []
        for p in blob_pixels:
            if p not in mega_blob:
                to_add.extend([p])
        mega_blob.extend(to_add)

    del blob_pixels
    del to_add
    del color
    del c1
    del c2
    gc.collect()

    c2 = initial_color
    c1 = []
    for p in mega_blob:
        c1.append(pixels[p])
    color = []
    for p in c1:
        color.append(p)
    for i in range(0, steps):
        for j in range(0, len(mega_blob)):
            color[j] = [max(min(color[j][0] + (c2[0] - c1[j][0])/(steps-1), 255), 0),
                        max(min(color[j][1] + (c2[1] - c1[j][1])/(steps-1), 255), 0),
                        max(min(color[j][2] + (c2[2] - c1[j][2])/(steps-1), 255), 0)]
            pixels[mega_blob[j]] = [round(color[j][0]),
                                    round(color[j][1]),
                                    round(color[j][2])]
        pixels.write()
        time.sleep(delay)

    for i in range(6, 127):
        pixels[i] = [0, 0, 10]
    pixels.write()
