Enters FRETBursts
=================

:date: 2016-02-19
:modified: 2016-02-19
:tags: smFRET, openscience, jupyter, preprints
:category: Scientific Computing
:slug: fretbursts
:authors: Antonino Ingargiola
:summary: Analyze smFRET data with FRETBursts: a new paper on bioRxiv.
:status: draft

.. image:: https://cloud.githubusercontent.com/assets/4156237/12906391/9866197a-ce94-11e5-932b-548a511e4840.png
    :alt: smFRET E-S histograms: ALEX jointplot produced by FRETBursts
    :align: left
    :width: 400

A few days ago I uploaded a `software paper <http://dx.doi.org/10.1101/039198>`__
to the bioRxiv introducing `FRETBursts <http://tritemio.github.io/FRETBursts/>`__,
an open source burst analysis python software for
single-molecule FRET data. In this post I highlight the aims of the manuscript
and a few strengths of FRETBursts.


The Manuscript
--------------

We wrote the `manuscript <http://dx.doi.org/10.1101/039198>`__ not only as an
introduction to the FRETBursts software but also as an accessible introduction
to burst analysis for smFRET data.
While writing the paper we had several target readers in mind.
Primary, it should help newbies to familiarize with the conceptual steps
of the analysis while at the same time learning how to perform them
in FRETBursts.
Additionally, users with previous experience in smFRET data analysis,
can find the detailed description helpful to clarify
exactly where FRETBursts implementation differs from
(or improves upon) commonly used algorithms. Finally, users with familiarity
with the python programming language can appreciate the software architecture
and data structures used to implement FRETBursts.

In order to don't scare away readers with no python experience we relegated
most of the language-specific details to special paragraphs marked as
"Python details".

FRETBursts execution model
--------------------------

FRETBursts is primary executed through the Jupyter notebook environment.
One advantage of Jupyter Notebook is that it binds together a narrative
description of the analysis, the code commands and the results in a single
interactive document that can be shared, modified and re-executed.
If you have never heard of Jupyter notebook you should definitely
`check it out <http://jupyter.org/>`__ (see also
`this paper <http://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261>`__
which provides a demo).

You can start using FRETBursts by simply executing pre-made notebooks
(we provide `several examples <http://nbviewer.jupyter.org/github/tritemio/FRETBursts_notebooks/blob/master/notebooks/FRETBursts%20-%20us-ALEX%20smFRET%20burst%20analysis.ipynb>`__).
But, as you gain more confidence, you can
customize the analysis by changing parameters, invoking different analysis
methods or making different plots. The Jupyter environment allows
a smooth transition from beginner to power-user.

Additionally, for users with deep experience in smFRET data analysis, FRETBursts
provides well-tested low-level methods for processing timestamps
and burst data.

As an example, SangYoon Chung (a Ph.D. candidate in our lab), recently
wrote a notebook implementing the `Burst Variance Analysis <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3059737/>`__
(BVA) using FRETBursts,
with no previous experience in programming (and only some elementary
notions of python).
This, of course, speaks volumes about SangYoon abilities to learn new
topics (his expertise is molecular biology and biophysics).
But it gave us a great example of how to use core FRETBursts routines
for manipulating timestamps and burst data for implementing a new
analysis.

SangYoon's `notebook <http://nbviewer.jupyter.org/github/tritemio/FRETBursts_notebooks/blob/master/notebooks/Example%20-%20Burst%20Variance%20Analysis.ipynb>`__
has been now added to FRETBursts. Moreover, we have
a section dedicated to the BVA implementation in the FRETBursts manuscript.


FRETBursts reliability
----------------------

All software have bugs. In biology or biophysics a software usually
gain "respect" when it is used in several publication and yields "reasonable"
results. While this type of "field" validation is very important,
`is not enough <http://ivory.idyll.org/blog/2016-containerization-disaster.html>`__
to demonstrate the correctness of a given software
implementation. In many cases we mis-place our trust in the correctness
of a software only because it is widely used.

Conversely, modern software engineering practices such as defensive programming
and unit testing, allow to minimize the presence of bugs, catch rare error
conditions and avoid regressions. In FRETBursts I use such common techniques.
All the core analysis functions, for example, have extensive unit tests that are
automatically executed at each commit though the `TravisCI <https://travis-ci.org/tritemio/FRETBursts>`__
service.
So, you don't have to trust my infallibility, but trust the "bug traps"
(i.e. tests) I put in place to protect you against my own errors.


Feedback
--------

In the spirit of open science we are eager to receive comments about the
software and/or the manuscript. We also are enthusiastically adopting and
supporting the immediate publications (i.e. `pre-prints
<http://www.nature.com/news/biologists-urged-to-hug-a-preprint-1.19384>`__)
for fast dissemination of scientific knowledge.
So, in `this spirit <http://asapbio.org/meeting-information/objectives>`__,
if you find something is not clear or you think
there is some glaring omission please let us know. We will soon send
the manuscript for formal peer-review, but in the meanwhile we are also
probing the ground with the "internet community".
