from pygifsicle import gifsicle
from touch import touch
import pytest

def test_gifsicle_exceptions():
    with pytest.raises(ValueError):
        gifsicle("non_existent_gif.gif")
    png = "existent_png.png"
    touch(png)
    with pytest.raises(ValueError):
        gifsicle(png)