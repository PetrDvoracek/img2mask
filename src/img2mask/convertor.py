import numpy as np
import colormap


def rgb2mask(mask_im, color2class):
    """
    mask_im: numpy image representing mask where each color
        represents class
    color2class: dictionary where each key specifiec hex color
        with '#' prefix and its value contains another dictionary with
        keys 'class_name' and 'idx', which represents class name and
        its index in N dim mask tensor. Example:
        color2class = {
            "#0000FF": {"class_name": "first class", "idx": 0},
            "#00FF00": {"class_name": "second class", "idx": 1},
            "#FF0000": {"class_name": "third class", "idx": 2},
        }
    """

    mask_h, mask_w, _ = mask_im.shape
    unique_classes = len(set(x["idx"] for x in color2class.values()))
    mask_ndim = np.zeros((mask_h, mask_w, unique_classes))

    for hex_color, class_info in color2class.items():
        class_mask = (mask_im == colormap.hex2rgb(hex_color)).all(-1)
        mask_ndim[..., class_info["idx"]] += class_mask

    return mask_ndim


def unique_classes(color2class):
    return len(set(x["idx"] for x in color2class.values()))
