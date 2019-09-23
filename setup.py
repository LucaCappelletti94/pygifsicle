import os
import re
# To use a consistent encoding
from codecs import open as copen
import platform
from setuptools import find_packages, setup
import subprocess
import sys

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with copen(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def is_stdout_enabled() -> bool:
    """Return a boolean representing if script is in a terminal with stdout enabled."""
    return sys.stdout.isatty()


def read(*parts):
    with copen(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("pygifsicle", "__version__.py")

linux_distributions_help = {
    "default":"""The sources to compile can be found at: https://github.com/kohler/gifsicle""",
    "ubuntu":"sudo apt-get install gifsicle",
    "arch":"sudo pacman -S gifsicle",
    "":"sudo pacman -S gifsicle", # Some time on arch platform.linux_distribution() results in ("","","")
    "fedora":"wget -O gifsicle.rpm https://centos.pkgs.org/7/epel-x86_64/gifsicle-1.91-1.el7.x86_64.rpm.html\nrpm -i gifsicle.rpm",
    "centos":"wget -O gifsicle.rpm https://centos.pkgs.org/7/epel-x86_64/gifsicle-1.91-1.el7.x86_64.rpm.html\nrpm -i gifsicle.rpm"
}

if platform.system() == "Darwin":
    subprocess.call(["brew", "install", "gifsicle"])
elif platform.system() == "Linux":
    if is_stdout_enabled():
        print("Installing gifsicle on Linux requires sudo!")
        distro = platform.linux_distribution()[0].lower()
        print("The current system was detected to be {}".format(distro))
        print("Please run the following command in your terminal:")
        print(linux_distributions_help.get(distro, linux_distributions_help["default"]))
        input("Press any key to continue with the installation of the python package.")
elif platform.system() == "Windows":
    if is_stdout_enabled():
        print("Please install the current gifsickle version from the website:")
        print("https://eternallybored.org/misc/gifsicle/")
        input("Press any key to continue with the installation of the python package.")

test_deps = [
    "pytest",
    "pytest-cov",
    "coveralls",
    "validate_version_code",
    "codacy-coverage",
    "touch"
]

extras = {
    'test': test_deps,
}

setup(
    name='pygifsicle',
    version=__version__,
    description="Python package wrapping the gifsicle library for editing and optimizing gifs.",
    long_description=long_description,
    url="https://github.com/LucaCappelletti94/pygifsicle",
    author="Luca Cappelletti",
    author_email="cappelletti.luca94@gmail.com",
    # Choose your license
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    # Add here the package dependencies
    install_requires=[],
    extras_require=extras,
)
