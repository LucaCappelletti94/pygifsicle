from pygifsicle import optimize
import os

def test_optimize():
    optimize("tests/big.gif", "small.gif")
    optimize("small.gif")
    os.remove("small.gif")