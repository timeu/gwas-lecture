import matplotlib
import numpy as np
from numpy.testing import assert_array_equal, assert_allclose


def get_data(ax):
    lines = ax.get_lines()
    if len(lines) > 0:
        xydata = np.concatenate(
            [x.get_xydata() for x in lines], axis=0)

    else:
        collections = ax.collections
        if len(collections) > 0:
            xydata = np.concatenate(
                [x.get_offsets() for x in collections], axis=0)

        else:
            raise ValueError("no data found")

    return xydata


def get_label_text(ax):
    text = [x for x in ax.get_children()
            if isinstance(x, matplotlib.text.Text)]
    text = [x for x in text if x.get_text() != ax.get_title()]
    text = [x for x in text if x.get_text().strip() != '']
    return [x.get_text().strip() for x in text]


def get_label_pos(ax):
    text = [x for x in ax.get_children()
            if isinstance(x, matplotlib.text.Text)]
    text = [x for x in text if x.get_text() != ax.get_title()]
    text = [x for x in text if x.get_text().strip() != '']
    return np.vstack([x.get_position() for x in text])


def get_image(ax):
    images = ax.get_images()
    if len(images) == 0:
        raise ValueError("Expected one image, but there were none. Did you remember to call the plotting function (probably `matshow` or `imshow`)?")
    if len(images) > 1:
        raise ValueError("Expected one image, but there were {}. Did you call the plotting function (probably `matshow` or `imshow`) more than once?".format(len(images)))
    return images[0]


def get_imshow_data(ax):
    image = get_image(ax)
    return image._A

def get_image_colormap(ax):
    image = get_image(ax)
    return image.cmap.name

def assert_image_equal(ax, arr):
    data = get_imshow_data(ax)
    assert_array_equal(data, arr)


def assert_image_allclose(ax, arr):
    data = get_imshow_data(ax)
    assert_allclose(data, arr, atol=1e-6)
