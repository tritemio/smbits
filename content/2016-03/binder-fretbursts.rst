On-Line Analysis of smFRET Data
===============================

:date: 2016-03-22
:tags: smFRET, openscience, jupyter, reproducibility, mybinder
:category: Scientific Computing
:slug: binder-fretbursts
:authors: Antonino Ingargiola
:summary: Try FRETBursts online with the new demo service based on mybinder.org
:status: draft


In a `previous post <{filename}/2016-02/fretbursts.rst>`_, I introduced
`FRETBursts <http://tritemio.github.io/FRETBursts/>`__, an open source
burst analysis software for single-molecule FRET (smFRET) data with a strong
focus on reproducibility.
Today, I talk about a new service (based on `MyBinder.org <http://MyBinder.org>`__)
which allows running `FRETBursts on-line <https://github.com/tritemio/FRETBursts_notebooks#run-online>`__,
with zero installation.

With this new service you can try FRETBursts without the need
to install anything (i.e. python) on your computer.
All you need is clicking the following button, which will open a new instance
of the FRETBursts environment on the cloud:

.. image::
    http://mybinder.org/badge.svg
    :target: http://mybinder.org/repo/tritemio/FRETBursts_notebooks
    :alt: button launch binder

The previous button will open a new page in your browser
showing the `Jupyter Dashboard <http://jupyter-notebook-beginner-guide.readthedocs.org/en/latest/what_is_jupyter.html#notebook-dashboard>`__.
There, in the *notebooks* folder, you will find multiple FRETBursts notebooks
for different kind of analysis. All you have to do is pick one and run it.

.. note::
    If you are new to Jupyter Notebook start by clicking on the *First Steps* notebook.

In the future, publications using FRETBursts will hopefully also deposit
the data on a public repository (such as `Zenodo <https://zenodo.org/>`__
or `Figshare <https://figshare.com/>`__).
This will enable anybody to replicate
the computations in a paper simply using FRETBursts on the cloud.

Features and Limitations
------------------------

At the moment, the notebooks available in the on-line service are
the same ones included in FRETBursts source repository.
When ran unmodified, they will download a sample data file
and run the analysis on it.
You can also use your own data file which needs to be uploaded first
(see the *First Steps* notebook). You can even upload your own FRETBursts
notebook, if you happen to have one already.

A current technical limitation
(that `will be soon fixed <https://github.com/jupyter/notebook/issues/96>`__)
is that the **Upload** button on the dashboard works only form small files (<35MB).
For bigger files, you have to upload the data somewhere on the internet
and then download it to the server
(see explanation in the *First Steps* notebook).

As a final caveat, note that sessions on MyBinder are not permanent
(they are deleted after 1 hour of inactivity).
Therefore, if you modify a notebook and want store it for reference or future
use, please remember to download it on your own computer.

Feedback and questions are more than welcome.
Please open a
`GitHub Issue <https://github.com/tritemio/FRETBursts_notebooks/issues>`__
to discuss anything related to this service.

Behind the Scenes
-----------------

Even though MyBinder is an incredibly sophisticated service, setting it
up is incredibly easy. So easy that anybody (either using FRETBursts or not)
can setup a similar service to complement a publication, for example.

Starting from a repository containing a bunch of notebooks,
all I had to do was adding
a `text file <https://github.com/tritemio/FRETBursts_notebooks/blob/master/environment.yml>`__
with the list of (`conda <http://conda.pydata.org/docs/>`__) packages to be installed on the server
(and that file was mostly auto-generated). Then, MyBinder.org did the magic.

Here, I want to briefly highlight some pre-conditions that made possible
building such an incredible service.

First and foremost it's open source.
Like continuous integration (an automated testing infrastructure),
the service that allows to run FRETBursts on-line exists only because
all the FRETBursts software dependencies (python, jupyter,
numpy, scipy, lmfit, matplotlib, etc...) are free an open source.
If FRETBursts were written in MATLAB, for example, due to licensing cost,
running a continuous integration service or a service like MyBinder.org
to execute MATLAB code on the cloud would have been prohibitively expensive.
Moreover, since it would have been a closed platform, it would not have
received the sort or contributions (form individual and companied across the
world) that these software have. The technical (and ethical) superiority
of open source software for scientific computing cannot be understated
(see `this paper <http://dx.doi.org/10.1016/j.conb.2015.04.002>`__
for more detailed argumentations).

Second,
`early <https://github.com/tritemio/FRETBursts/commit/f4de178f834f1341f01a5c494ac659537c70298d>`__
in development of FRETBursts,
I choose to base the execution on Jupyter Notebooks
(at the time called IPython Notebook).
This allowed me to focus on developing FRETBursts as a library,
avoiding wasting time building GUIs or command line interfaces
that can easily become bloated or obsolete.
On the contrary, the notebook interface represents a semi-graphical
interface which is good enough even for non-programmers.
Notebooks are also quite good for storing full analysis workflows,
drastically simplifying the way we share analysis details and results.

Third, and most importantly, Jeremy Freeman and collaborators built MyBinder,
a service to execute on the could any Jupyter notebook contained
in a GitHub repository.
This was possible by recent developments in the Jupyter project
(e.g. JupyterHub), together
with a clever use of modern cloud technologies (docker + kubernetes).
For an introduction to MyBinder in scientific computing
see `this interesting post <http://ivory.idyll.org/blog/2016-mybinder.html>`__
from Titus Brown.

Synergies made possible by open source technologies **plus** skillful
individuals can make miracles.

In other words, with FRETBursts, we really stand on giant's shoulders!


----

*Thanks to Yazan Alhadid for commenting on an early draft of this post.*
