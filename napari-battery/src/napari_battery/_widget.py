"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from magicgui import magic_factory
from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget

if TYPE_CHECKING:
    import napari


class ExampleQWidget(QWidget):
    # your QWidget.__init__ can optionally request the napari viewer instance
    # in one of two ways:
    # 1. use a parameter called `napari_viewer`, as done here
    # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        btn = QPushButton("Click me!")
        btn.clicked.connect(self._on_click)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(btn)

    def _on_click(self):
        print("napari has", len(self.viewer.layers), "layers")


@magic_factory
def example_magic_widget(img_layer: "napari.layers.Image"):
    print(f"you have selected {img_layer}")


# Uses the `autogenerate: true` flag in the plugin manifest
# to indicate it should be wrapped as a magicgui to autogenerate
# a widget.
def example_function_widget(img_layer: "napari.layers.Image"):
    print(f"you have selected {img_layer}")




# 위에까지는 예시. 여기부터는 새롭게 작성한 부분

# blurred image, 새로운 function - ex.detect_spots 를 위해 추가한 부분 
import numpy as np
from scipy import ndimage as ndi
from skimage.feature import blob_log

# blurred image를 위해 추가한 부분 
def gaussian_high_pass(image: np.ndarray, sigma: float=2):
    # image: filter될 이미지
    # sigma(float): 가우시안 필터의 sigma (width) - default는 2
    
    # highpassed_im : high pass filter가 적용된 image를 결과값으로 return
    low_pass = ndi.gaussian_filter(image, sigma)
    high_passed_im = image - low_pass 

    return high_passed_im

def detect_spots(
        image: "napari.types.ImageData",
        high_pass_sigma: float = 2, # default value
        spot_threshold: float = 0.01, # default value
        blob_sigma: float = 2
) -> "napari.types.LayerDataTuple":
    """Apply a gaussian high pass filter to an image.

    Parameters
    ----------
    image : napari.types.ImageData
        The image in which to detect the spots.
    high_pass_sigma : float
        The sigma (width) of the gaussian filter to be applied.
        The default value is 2.
    spot_threshold : float
        The threshold to be passed to the blob detector.
        The default value is 0.01.
    blob_sigma: float
        The expected sigma (width) of the spots. This parameter
        is passed to the "max_sigma" parameter of the blob
        detector.

    Returns
    -------
    layer_data : napari.types.LayerDataTuple
        The layer data tuple to create a points layer
        with the spot coordinates.

    """

    # filter the image
    filtered_spots = gaussian_high_pass(image, high_pass_sigma)

    # detect the spots
    blobs_log = blob_log(
        filtered_spots,
        max_sigma = blob_sigma,
        num_sigma = 1,
        threshold = spot_threshold
    )
    points_coords = blobs_log[:, 0:2]
    sizes = 3 * blobs_log[:,2]
    
    layer_data = (
        points_coords,
        {
            "face_color": "magenta",
            "size": sizes
        },
        "Points"
    )
    return layer_data

# 여기까지