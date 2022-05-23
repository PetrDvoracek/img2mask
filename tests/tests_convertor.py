import numpy as np
import colormap
import tabulate

import unittest

from src.img2mask import rgb2mask


class TestRGB2N(unittest.TestCase):
    def test_convertor_2_classes(self):
        color2class = {
            "#0000FF": {"class_name": "first class", "idx": 0},
            "#00FF00": {"class_name": "second class", "idx": 1},
        }
        w, h, channels = 2, 2, 3

        mask_im = np.zeros((w, h, channels))
        mask_im[0, 0] = colormap.hex2rgb(list(color2class.keys())[0])
        mask_im[1, 1] = colormap.hex2rgb(list(color2class.keys())[1])

        mask_expected = np.zeros((w, h, 2))
        mask_expected[0, 0, 0] = 1
        mask_expected[1, 1, 1] = 1

        mask_converted = rgb2mask(mask_im, color2class)

        mask_converted_print = tabulate.tabulate(mask_converted, tablefmt="fancy_grid")
        mask_im_print = tabulate.tabulate(mask_im, tablefmt="fancy_grid")
        print("input RGB mask:")
        print(mask_im_print)
        print("output N channel mask:")
        print(mask_converted_print)

        assert np.array_equal(mask_expected, mask_converted)


if __name__ == "__main__":
    unittest.main()
