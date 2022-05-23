import numpy as np
import colormap

import time

from src.img2mask import rgb2mask


def measure_duration(f):
    def wrapper(*args, **kwargs):
        before = time.time()
        _ = f(*args, **kwargs)
        duration = time.time() - before
        return duration

    return wrapper


rgb2mask_duration = measure_duration(rgb2mask)


def test_speed():
    color2class = {
        "#0000FF": {"class_name": "first class", "idx": 0},
        "#00FF00": {"class_name": "second class", "idx": 1},
        "#0300FF": {"class_name": "first class", "idx": 2},
        "#0A00FF": {"class_name": "first class", "idx": 3},
        "#0800FF": {"class_name": "first class", "idx": 4},
        "#1000FF": {"class_name": "first class", "idx": 5},
    }
    rgb_colors = [colormap.hex2rgb(x) for x in color2class.keys()]
    w, h, channels = 1600, 1600, 3
    mask_im = np.zeros((w, h, channels))
    mask_im[:32, 32] = rgb_colors[0]
    mask_im[32:70, 32:90] = rgb_colors[1]
    mask_im[70:162, 90:128] = rgb_colors[2]
    mask_im[162:180, 128:190] = rgb_colors[3]
    mask_im[180:1200, 190:500] = rgb_colors[4]
    mask_im[1200:1500, 500:1500] = rgb_colors[5]

    n_runs = 10
    for i in range(0, n_runs):
        duration = rgb2mask_duration(mask_im, color2class)
        print(f"run {i}/{n_runs} duration: {duration:0.2f} s")


if __name__ == "__main__":
    test_speed()
