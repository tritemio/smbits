Run FRETBursts On-Line
======================

:date: 2016-03-22
:tags: smFRET, openscience, jupyter, reproducibility, mybinder
:category: Scientific Computing
:slug: fretbursts
:authors: Antonino Ingargiola
:summary: Try FRETBursts online with the new demo service based on mybinder.org
:status: published


In a `previous post <{filename}/2016-02/fretbursts.rst>`_, I introduced
`FRETBursts <http://tritemio.github.io/FRETBursts/>`__, which is an open source
burst analysis software for single-molecule FRET data with a strong
focus on reproducibility.
Today, I talk about a new service (based on `MyBinder.org <http://MyBinder.org>`__)
which allows running `FRETBursts online <https://github.com/tritemio/FRETBursts_notebooks#run-online>`__,
with zero installation.

With this new service you can try FRETBursts without the need
to install anything (i.e. python) on your computer.
All you need is clicking the following button:

.. image::
    http://mybinder.org/badge.svg
    :target: http://mybinder.org/repo/tritemio/FRETBursts_notebooks
    :alt: button launch binder

When you click on it, a new cloud instance of
the FRETBursts environment is created on fly and the Jupyter Dashboard
will appear in the web browser. From there, you only have to select
which FRETBursts notebook to open and run.

.. note::
    If you are new to Jupyter Notebook start by clicking on the *First Steps* notebook.

The notebooks on the on-line service are the same notebooks included
in FRETBursts source repository.
When ran unmodified, they will download a sample data file and run the analysis
on it.
You can also use your own data file which needs to be uploaded first
(see the *First Steps* notebook). You can even upload your own notebook,
if you happen to have one already. To upload small files (<35MB), either a
new notebook or a new data file, you can use the Upload button in
the dashboard.

As a final caveat, note that sessions on MyBinder are not permanent
(they are deleted after 1 hour of inactivity).
Therefore, if you modify a notebook and want store it for reference or future
use, please remember to download it on your own computer.

Behind the Scenes
-----------------

To be fair, setting up this service was not hard, indeed it was
quite trivial. And not because I'm a cloud computing expert (I'm not),
but because all the hard work was done by MyBinder.org.
All I had to do is adding to the FRETBursts notebooks repository
a `text file <https://github.com/tritemio/FRETBursts_notebooks/blob/master/environment.yml>`__
with the list of (conda) packages to be installed on the server
(and that file was mostly auto-generated). Then, MyBinder.org did the magic.

Here, I want to highlight some of the "conditions" that allowed building
such a service for running FRETBursts on the cloud.

First and foremost it's open source.
Like continuous integration (an automated testing infrastructure),
the service that allows to run FRETBursts on-line exists only because
all the FRETBursts software dependencies (python, jupyter,
numpy, scipy, lmfit, matplotlib, etc...) are free an open source.
Take MATLAB for example. Due to licensing cost, running a continuous
integration service or a service like MyBinder.org to execute MATLAB code
on the cloud would be prohibitively expensive. And since it would a closed
platform, it would not receive the sort or contributions that these
software have received from users and companies from around the world.

Second, early in the `development stage <https://github.com/tritemio/FRETBursts/commit/f4de178f834f1341f01a5c494ac659537c70298d>`__,
I choose to base FRETBursts execution on Jupyter Notebooks
(at the time called IPython Notebook).
This allowed me to focus on developing FRETBursts as a library,
avoiding wasting time building GUIs or command line interfaces
that can easily become bloated or obsolete.
On the contrary, the notebook interface represents a semi-graphical
interface which is good enough even for non-programmers.
Notebooks are also quite good at storing full analysis workflows,
drastically simplifying the way we share analysis details and results.

Third, Jeremy Freeman and collaborators built MyBinder, a service
to execute on the could any Jupyter notebook contained in a GitHub repository.
This has been made possible by
more recent development of the Jupyter project (e.g. JupyterHub) together
with a clever use of modern cloud technologies (docker + kubernetes).
For an introduction to MyBinder see `this post <http://ivory.idyll.org/blog/2016-mybinder.html>`__
from Titus Brown.
Again, synergies made possible by open source technologies **plus** skillful
individuals can make miracles.

In other words, with FRETBursts, we really stand on giant's shoulders!
