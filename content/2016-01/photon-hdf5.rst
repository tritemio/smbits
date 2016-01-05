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


In this post I informally introduce the `Photon-HDF5 format <www.photon-hdf5.org>`__,
of which I am one of the original authors.
For a more complete overview you can read the `Biophysical Journal paper <>`__,
or the `preprint from BiorXiv <http://dx.doi.org/10.1101/026484>`__.

Briefly, Photon-HDF5 is a file format for storing single-molecule
fluorescence data based on photon timestamps and other per-photon data.
It is, in essence, a conventional structure to save this class of data
in HDF5 files, therefore facilitating data sharing and long-term archival.

The format was initially designed to store freely-diffusing single-molecule
FRET data, but it has evolved to store any measurement
which consist of streams of "photon-data" (e.g. timestamps, detectors,
TCSPC nanotimes, etc.).

Since Photon-HDF5 is based on HDF5 files, it inherits all its advantages.
In particular:

- It is open, multi-platform and multi-language,
- It is efficient: it supports transparent compression and fast reading.

In designing Photon-HDF5, we followed a set of generic principles
that may be useful also to other scientific formats:

- Self describing: each data field embeds a description explaining
  the purpose of the field.
- Self-contained: contains all the information necessary to analyze the data.
- Suitable for long-term archival: rich metadata records experimental details,
  author and software version.
- Supports arbitrary user data.

Finally, these features are specific to the particular data
(single-molecule fluorescence experiments) stored in Photon-HDF5 files:

- Support of any number of spectral, polarization or `beam-split <http://photon-hdf5.readthedocs.org/en/latest/phdata.html#beam-split-ch>`__ channels.
- Support of single- and multi-spot data.
- Extensible: the bulk "photon-data" (present in all types of measurements)
  is logically separated from data specific of a single measurement type.
  Thanks to this separation, new measurement-types can be defined in
  backward-compatible manner.


Resources
---------

We resources are:

- www.photon-hdf5.org - the Homepage
- Official documentation: specifications, reading and writing guides and more.
- Example Photon-HDF5 data files
- Examples of reading Photon-HDF5 (in multiple languages)
- Writing Photon-HDF5 in python (phconvert) or other languages
  (phforge)
- Online service to convert data files (from HT3 or SPC) to Photon-HDF5
  (using Jupyter notebooks and www.mybinder.org).

The online converter, in particular, allows trying the file conversion
without any installation. So, if you are curious, give it a try!
