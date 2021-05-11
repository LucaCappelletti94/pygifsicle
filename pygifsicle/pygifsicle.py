from typing import List, Optional, Union
import subprocess
import os
from pathlib import Path

__all__ = ["gifsicle", "optimize"]


def gifsicle(
    sources: Union[List[str], str, List[Path], Path],
    destination: Optional[str] = None,
    optimize: bool = False,
    colors: int = 256,
    options: Optional[List[str]] = None
) -> None:
    """Apply gifsickle with given options to image at given paths.

    Parameters
    -----------------
    sources:Union[List[str], str, List[Path], Path],
        Path or paths to gif(s) image(s) to optimize.
    destination:Optional[str] = None
        Path where to save updated gif(s).
        By default the old image is overwrited.
        If multiple sources are specified, they will be merged.
    optimize: bool = False,
        Boolean flag to add the option to optimize image.
    colors:int = 256,
        Integer value representing the number of colors to use. Must be a power of 2.
    options:Optional[List[str]] = None
        List of options.

    Raises
    ------------------
    ValueError:
        If gifsicle is not installed.
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
    if isinstance(sources, (str, Path)):
        sources = [sources]
    for source in sources:
        if isinstance(source, Path):
            source = str(source)  # should work on all windows, mac, and linux
        if not os.path.exists(source):
            raise ValueError(
                "Given source path `{}` does not exist.".format(source)
            )
        if not source.endswith(".gif"):
            raise ValueError(
                "Given source path `{}` is not a gif image.".format(source)
            )
    if destination is None:
        destination = sources[0]
    if not str(destination).endswith(".gif"):
        raise ValueError("Given destination path is not a gif image.")
    if options is None:
        options = []
    if optimize and "--optimize" not in options:
        options.append("--optimize")
    try:
        subprocess.call(["gifsicle", *options, *sources, "--colors",
                        str(colors), "--output", destination])
    except FileNotFoundError:
        raise FileNotFoundError((
            "The gifsicle library was not found on your system.\n"
            "On MacOS it is automatically installed using brew when you "
            "use the pip install command.\n"
            "On other systems, like Linux systems and Windows, it prompts the "
            "instructions to be followed for completing the installation.\n"
            "You can learn more on how to install gifsicle on "
            "the gifsicle and pygifsicle documentation."
        ))

def optimize(source: Union[str, Path], *args, **kwargs) -> None:
    """Optimize given gif.

    Parameters
    -----------------
    source:Union[str, Path],
        Path to gif image to optimize.
    """
    gifsicle(source, *args, **kwargs, optimize=True)
