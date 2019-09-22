import os

def gifsicle(source:str, destination:str=None):
    """Apply gifsickle with given options to image at given path.

    Parameters
    -----------------
    source:str,
        Path to gif image to optmize.
    destination:str=None
        Path where to save updated gif. By default the old image is overwrited.

    Raises
    ------------------
    ValueError:
        If given source path does not exist.
    ValueError:
        If given source path is not a gif image.

    References
    ------------------
    You can learn more about gifsicle at the project home page:
    https://www.lcdf.org/gifsicle/
    """
    if not os.path.exists(source):
        raise ValueError("Given source path does not exists.")
    if not source.endswith(".gif"):
        raise ValueError("Given source path is not a gif image.")
    