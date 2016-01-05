Announcing Photon-HDF5
======================

:date: 2016-01-02
:modified: 2016-01-02
:tags: photon-hdf5, HDF5, smFRET, single-molecule, data format
:category: Scientific Computing
:slug: photon-hdf5
:authors: Antonino Ingargiola
:summary: Announcing Photon-HDF5: a file format for single-molecule fluorescence.
:status: draft


In this post I introduce `Photon-HDF5 <http://www.photon-hdf5.org>`__,
a format I contributed to develop in the past year.
For a more complete overview you can read the recently published paper
(get the `preprint <http://dx.doi.org/10.1101/026484>`__ or
the version `just published <http://dx.doi.org/10.1016/j.bpj.2015.11.013>`__ by *Biophysical Journal*).

.. image:: https://imgs.xkcd.com/comics/standards.png
    :alt: xkcd comic: standards

Briefly, Photon-HDF5 is a file format for storing single-molecule
fluorescence data based on photon timestamps and other per-photon data.
It is, in essence, a conventional structure to save this class of data
in `HDF5 <https://www.hdfgroup.org/HDF5/>`__ files, therefore facilitating
data sharing and long-term archival.

The format was initially designed to store freely-diffusing single-molecule
FRET data, but it has evolved to store any measurement
which consists of streams of "photon-data" (e.g. timestamps, detectors,
TCSPC nanotimes, etc.).

Design and Features
-------------------

Since Photon-HDF5 is based on HDF5 files, it inherits all its advantages.
In particular it is open standard, multi-platform and multi-language.
It is also an efficient binary format supporting compression
transparently.

In designing Photon-HDF5, we followed a set of generic principles
that may be useful also for other scientific formats:

- **self-describing**: each data field embeds a description explaining
  the purpose of the field;
- **self-contained**: it contains all the information necessary to analyze the data;
- suitable for **long-term archival**: rich metadata records experimental details,
  provenance, author and software version;
- supports arbitrary **user data**;
- all support software is **open source** (under MIT license).

Finally, the following features make Photon-HDF5 suitable for a wide range
of single-molecule fluorescence data:

- supports any number of spectral, polarization or `beam-split <http://photon-hdf5.readthedocs.org/en/latest/phdata.html#beam-split-ch>`__ channels.
- supports single- and multi-spot data.
- extensible: the bulk "photon-data" (present in all types of measurements)
  is logically separated from data specific of a single measurement type.

Thanks to this extensible structure, new measurement-types can be defined
in backward-compatible manner. In fact, we encourage users to propose
new measurement types (use the
`Photon-HDF5 mailing list <https://groups.google.com/forum/#!forum/photon-hdf5>`__).

Open Development
----------------

All Photon-HDF5 development (both specification documents and software)
takes place publicly `on GitHub <https://github.com/Photon-HDF5>`__.
We encourage users to join the effort, providing feedback and/or submitting Issues or
`Pull Requests <https://help.github.com/articles/creating-a-pull-request/>`__.
By providing feedback and ideas, you can shape the future development
of Photon-HDF5. Plus we acknowledge all `contributions <http://photon-hdf5.readthedocs.org/en/latest/contributing.html#contributions-acknowledgement>`__.


Supporting Software
-------------------

Photon-HDF5 files can be opened in `HDFView <https://www.hdfgroup.org/products/java/hdfview/>`__
and read exactly in the same way you read other HDF5 files. To help newcomers,
we posted
`reading examples <http://photon-hdf5.github.io/photon_hdf5_reading_examples/>`__
in Python, MATLAB and LabVIEW.

To write valid Photon-HDF5 files from scratch, we provide
a small open source python library called `phconvert <http://photon-hdf5.github.io/phconvert/>`__.
Phconvert
includes, additionally, `Jupyter <http://jupyter.org>`__ notebooks to convert common file formats to Photon-HDF5.
For all the other languages, the easiest and most robust way of writing
Photon-HD5 files is using an ad-hoc script called `phforge <http://photon-hdf5.github.io/phforge/>`__.

Try it Online!
--------------

To get a the taste of it, you can use the
`online conversion service <http://photon-hdf5.github.io/Photon-HDF5-Converter/>`__
to convert an existing data file (Becker Hickl SPC or PicoQuant HT3)
to Photon-HDF5. This service uses `MyBinder.org <http://mybinder.org/>`__ to provide access to
the Jupyter Notebooks implementing the file conversion.

Enjoy!
