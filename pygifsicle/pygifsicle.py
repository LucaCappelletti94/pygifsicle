from typing import List, Union
import subprocess
import os

__all__ = ["gifsicle", "optimize"]


def gifsicle(sources: Union[List[str], str], destination: str = None, optimize: bool = False, colors: int = 256, options: List[str] = None):
    """Apply gifsickle with given options to image at given paths.

    Parameters
    -----------------
    sources:Union[List[str], str],
        Path or paths to gif(s) image(s) to optimize.
    destination:str=None
        Path where to save updated gif. By default the old image is overwrited.
    optimize:bool=False,
        Boolean flag to add the option to optimize image.
    colors:int=256,
        Integer value representing the number of colors to use. Must be a power of 2.
    options:List[str]=None
        List of options.

    Raises
    ------------------
    ValueError:
        If given source path does not exist.
    ValueError:
        If given source path is not a gif image.
    ValueError:
        If given destination path is not a gif image.

    References
    ------------------
    You can learn more about gifsicle at the project home page:
    https://www.lcdf.org/gifsicle/
    """
    if isinstance(sources, str):
        sources = [sources]
    if any([not os.path.exists(source) for source in sources]):
        raise ValueError("Given source path does not exists.")
    if any([not source.endswith(".gif") for source in sources]):
        raise ValueError("Given source path is not a gif image.")
    if destination is None:
        destination = sources[0]
    if not destination.endswith(".gif"):
        raise ValueError("Given destination path is not a gif image.")
    if options is None:
        options = []
    if optimize and "--optimize" not in options:
        options.append("--optimize")
    subprocess.call(["gifsicle", *options, *sources, "--colors",
                     str(colors), "--output", destination])


def optimize(source: str, *args, **kwargs):
    """Optimize given gif.

    Parameters
    -----------------
    source:str,
        Path to gif image to optimize.
    """
    gifsicle(source, *args, **kwargs, optimize=True)
