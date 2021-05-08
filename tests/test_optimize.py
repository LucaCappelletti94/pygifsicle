from pygifsicle import optimize
import os
from pathlib import Path

def test_optimize():
    optimize("tests/big.gif", "small.gif")
    optimize("small.gif")
    os.remove("small.gif")
    
    
def test_optimize_pathlib():
    here = Path(__file__).parent.resolve()
    source = here / "big.gif"
    destination = here / "small.gif"
    optimize(source, destination)
    optimize(destination)
    os.remove(destination)
