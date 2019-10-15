pygifsicle
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Python package wrapping the `gifsicle library <https://www.lcdf.org/gifsicle/>`_ for editing and optimizing gifs.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install pygifsicle

While running the installation, on **MacOS** the setup will automatically install **gifsicle** using `Brew <https://brew.sh/>`_.

On Linux you will need to install **gifsicle** using apt-get as follows:

.. code:: shell

    sudo apt-get install gifsicle
    
On Windows you will need to download and install the `correct port of the library <https://eternallybored.org/misc/gifsicle/>`_ for your OS.

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Usage examples
----------------------------------------------
The library is currently pretty plain: it offers a wrapper to gifsicle and a method to optimize gifs, wrapping the options for gifsicle.

Optimizing a gif
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To optimize a gif, use the following:

.. code:: python

    from pygifsicle import optimize
    optimize("path_to_my_gif.gif")


General wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To run gifsicle from Python use the following:

.. code:: python

    from pygifsicle import gifsicle
    gifsicle(
        sources=["list.gif", "of.gif", "gifs.gif"], # or a single_file.gif
        destination="destination.gif" # or just omit it and will use the first source provided.
        optimize=False, # Whetever to add the optimize flag of not
        colors=256, # Number of colors t use
        options=["--verbose"] # Options to use.
    )

Learn more about the general wrapper `by reading the function documentation. <https://github.com/LucaCappelletti94/pygifsicle/blob/0c7a1928eb0a5eb3dc99c46c227f970c7bd6b31b/pygifsicle/pygifsicle.py#L8>`_

Troubleshooting
---------------------------------------------------
One of the most common issues you can get, especially on windows, is that simply the **gifsicle** library is not available system wide. Do try to run `gifsicle` in your terminal to check if the library is properly installed.

Help and support
---------------------------------------------------
Wanna add another wrapper for easier usage? `Do a pull request! <https://github.com/LucaCappelletti94/pygifsicle/pulls>`_

Did you find an error or weird behavior? `Open an issue! <https://github.com/LucaCappelletti94/pygifsicle/issues>`_


.. |travis| image:: https://travis-ci.org/LucaCappelletti94/pygifsicle.png
   :target: https://travis-ci.org/LucaCappelletti94/pygifsicle
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_pygifsicle&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_pygifsicle
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_pygifsicle&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_pygifsicle
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_pygifsicle&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_pygifsicle
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/pygifsicle/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/pygifsicle?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/pygifsicle.svg
    :target: https://badge.fury.io/py/pygifsicle
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/pygifsicle
    :target: https://pepy.tech/badge/pygifsicle
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/a27dcd22ccdb4eb195073d42b5a97945
    :target: https://www.codacy.com/manual/LucaCappelletti94/pygifsicle?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/pygifsicle&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/6a4ca49a061d72eb040c/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/pygifsicle/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/6a4ca49a061d72eb040c/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/pygifsicle/test_coverage
    :alt: Code Climate Coverate
