Announcing Photon-HDF5
======================

:date: 2016-01-02
:modified: 2016-01-02
:tags: photon-hdf5, HDF5, smFRET, single-molecule, data format
:category: Scientific Computing
:slug: photon-hdf5
:authors: Antonino Ingargiola
:summary: Announcing Photon-HDF5: a file format for single-molecule fluorescence.
:status: published


A paper introducing the Photon-HDF5 format has just been published on a
selective peer-reviwed journal.

Photon-HDF5 is a file format to store data from single-molecule fluorescence
experiments (and simulations) based on photon timestamps and other per-photon
data. It is a conventional structure to save this kind of "photon-data"
in HDF5 files, facilitating data sharing and suitable for long-term archival.

The format design initiated from the need to store freely-diffusing
single-molecule FRET data files, but it has evolved to store any measurement
which records streams of "photon-data" (e.g. timestamp, detector,
TCSPC nanotimes, etc.).



Photon-HDF5 Features
--------------------

The main Photon-HDF5 features are:

- Open, multi-platform and multi-language: based on HDF5
- Efficient: it support compression out of the box and it is very fast to read.
- Self describing: each data field embeds a description string explaining
  the purpose of the field.
- Self-contained: contains all the information to analyze the data.
- Suitable for long-term archival: rich metadata records experimental details,
  author and software version.
- Supports any number of spectral, polarization or beam-split channels.
- Supports single- and multi-spot data.
- Modular design: measurement-type specific data logically separated from
  the bulk data. Support for new measurement-types can be easily added in
  backward compatible manner.
- Supports arbitrary user data.


Resources
---------

The main resources are:

- www.photon-hdf5.org - the Homepage
- Official documentation: specifications, reading and writing guides and more.
- Example data files
- Examples of reading Photon-HDF5 (in multiple languages)
- Writing Photon-HDF5 in python (using phconvert) or other languages
  (using phforge)
- Online service to convert data files (HT3 or SPC) to Photon-HDF5
  (using Jupyter notebooks and www.mybinder.org).

The online converter, in particular, allows trying the file conversion
without any installation.
As a side note, it was incredibly easy to setup thanks to the mybinder.org
service provided by @fremanlab which allows to turn any github repository
of Jupyter notebooks in runnable notebook, no login require.

Coming back to Photon-HDF5, this is only the beginning. We'd like to hear your
feedback: what works and what it doesn't work for you, suggestion and ideas
of future development.
