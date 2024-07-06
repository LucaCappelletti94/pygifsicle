# Pygifsicle

[![pip](https://badge.fury.io/py/pygifsicle.svg)](https://pypi.org/project/pygifsicle/)
[![License](https://img.shields.io/github/license/LucaCappelletti94/pygifsicle)](LICENSE)
[![downloads](https://pepy.tech/badge/pygifsicle)](https://pepy.tech/project/pygifsicle)
[![python versions](https://img.shields.io/pypi/pyversions/pygifsicle)](https://www.python.org/downloads/)
[![GitHub actions](https://github.com/LucaCappelletti94/pygifsicle/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/pygifsicle/actions/)

Python package wrapping the [gifsicle library](https://www.lcdf.org/gifsicle/) for editing and optimizing gifs.

## How do I install this package?

As usual, just download it using pip:

```shell
pip install pygifsicle
```

While running the installation, on **MacOS** the setup will automatically install **gifsicle** using [Brew](https://brew.sh/).

On Linux you will need to install **gifsicle** using apt-get as follows:

```shell
sudo apt-get install gifsicle
```

On Windows you will need to download and install the [correct port of the library](https://eternallybored.org/misc/gifsicle/) for your OS.

## Usage examples

The library is currently pretty plain: it offers a wrapper to gifsicle and a method to optimize gifs, wrapping the options for gifsicle.

### Optimizing a gif

To optimize a gif, use the following:

```python
from pygifsicle import optimize
optimize("path_to_my_gif.gif")
```

### General wrapper

To run gifsicle from Python use the following:

```python
from pygifsicle import gifsicle
gifsicle(
    sources=["list.gif", "of.gif", "gifs.gif"], # or a single_file.gif
    destination="destination.gif", # or just omit it and will use the first source provided.
    optimize=False, # Whether to add the optimize flag or not
    colors=256, # Number of colors to use
    options=["--verbose"] # Options to use.
)
```

Learn more about the general wrapper [by reading the function documentation](https://github.com/LucaCappelletti94/pygifsicle/blob/0c7a1928eb0a5eb3dc99c46c227f970c7bd6b31b/pygifsicle/pygifsicle.py#L8).

## Troubleshooting

One of the most common issues you can get, especially on Windows, is that simply the **gifsicle** library is not available system-wide. Do try to run `gifsicle` in your terminal to check if the library is properly installed.

## Help and support

Wanna add another wrapper for easier usage? [Do a pull request!](https://github.com/LucaCappelletti94/pygifsicle/pulls)

Did you find an error or weird behavior? [Open an issue!](https://github.com/LucaCappelletti94/pygifsicle/issues)