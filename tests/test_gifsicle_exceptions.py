from pygifsicle import gifsicle
from touch import touch
import os
import pytest

def test_gifsicle_exceptions():
    with pytest.raises(ValueError):
        gifsicle("non_existent_gif.gif")
    png = "existent_png.png"
    gif = "existent_gif.gif"
    touch(png)
    with pytest.raises(ValueError):
        gifsicle(png)
    with pytest.raises(ValueError):
        gifsicle(gif, png)
    os.remove(png)