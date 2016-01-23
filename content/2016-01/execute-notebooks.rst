Batch Execution of Jupyter Notebooks
====================================

:date: 2016-01-02
:modified: 2016-01-23
:tags: jupyter, notebook, batch-processing, nbconvert, python
:category: Scientific Computing
:slug: execute-notebooks
:authors: Antonino Ingargiola
:summary: Batch execution of jupyter notebooks using nbconvert.
:status: published

In this post I show how to use `nbconvert <http://nbconvert.readthedocs.org/>`__'s (4.1+) Python API
to programmatically execute notebooks.

- **EDIT 2016-01-05**: *moved paragraph.*
- **EDIT 2016-01-15**: *apply corrections from Jupyter team*

    With the help of the Jupyter team, most of this post is now part of
    the official `nbconvert docs <http://nbconvert.readthedocs.org/en/latest/execute_api.html>`__!

Intro
-----

`Jupyter <http://jupyter.org/>`__ notebooks are increasingly used in scientific computing.
For example, computational projects often include several notebooks to carry out
different parts of a bigger analysis. Or, libraries include
notebooks to provide documentation, examples or tests.

In all these cases, running notebook in batches, removes manual work
increasing robustness and reproducibility.

`nbconvert <http://nbconvert.readthedocs.org/>`__, the Jupyter component used
to convert notebooks, can be used to automatically execute and save one or more
notebooks.
This functionality is exposed through a Python API (explored in this post)
and a similar
`command line interface <http://nbconvert.readthedocs.org/en/latest/usage.html>`__.


A Quick Example
---------------

Let's start with a complete quick example, leaving detailed explanations
to the following sections.

First we import nbconvert and the ``ExecutePreprocessor`` class:

.. code-block:: python

    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor

Assuming that ``notebook_filename`` is the path of a notebook,
we can load it with:

.. code-block:: python

    nb = nbformat.read(open(notebook_filename), as_version=4)

Next, we configure the notebook execution mode:

.. code-block:: python

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

We specified two (optional) arguments ``timeout`` and ``kernel_name``, which
define respectively the cell execution timeout and the execution kernel.

    The option to specify **kernel_name** is `new <https://github.com/jupyter/nbconvert/pull/177>`__
    in nbconvert 4.2+ (4.2 is at the moment still unreleased).
    When not specified or when using nbconvert <4.2,
    the default Python kernel is chosen.

To actually run the notebook we call the method ``preprocess``:

.. code-block:: python

    ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})

Hopefully, we will not get any errors during the notebook execution
(see the last section for error handling). Note that ``path`` specifies
in which folder to execute the notebook.
Finally, save the resulting notebook with:

.. code-block:: python

    nbformat.write(nb, open('executed_notebook.ipynb', mode='wt'))

That's all. Your executed notebook will be saved in the current folder
in the file *executed_notebook.ipynb*.

Execution Arguments
-------------------

The arguments passed to ``ExecutePreprocessor`` are configuration options
called `traitlets <http://traitlets.readthedocs.org/>`_.
There are many cool things about traitlets, for example
they enforce the type of the input and they can be accessed/modified as
class attributes. Moreover, each traitlet is automatically exposed
as command-line options. For example, we can pass the timeout from the
command-line like this::

    jupyter nbconvert --ExecutePreprocessor.timeout=600 --to notebook --execute mynotebook.ipynb

Let's now discuss in more detail the two traitlets we used.

The ``timeout`` traitlet defines the maximum time (in seconds) each notebook
cell is
allowed to run, if the execution takes longer an exception will be raised.
The default is 30 s, so in cases of long-running cells you may want to specify
an higher value.

The second traitlet, ``kernel_name``, allows specifying the name of the kernel
to be used for the execution. By default, the kernel name is obtained from the
notebook metadata. The traitlet ``kernel_name`` allows to specify a user-defined
kernel, overriding the value in the notebook metadata. A common use case
is that of a Python 2/3 library which includes documentation/testing
notebooks. These notebooks will specify either a python2 or python3 kernel
in their metadata
(depending on the kernel used the last time the notebook was saved).
In reality, these notebooks will work on both Python 2/3 and, for testing,
it is important to be able to execute them programmatically on both
versions. Here the traitlet ``kernel_name`` is helpful:
we can just run each notebook twice, specifying first "python2" and then
"python3" as kernel name.


Error Handling
--------------

In the previous sections we saw how to save an executed notebook, assuming
there are no execution errors. But, what if there are errors?

An error during the notebook execution, by default, will stop the execution
and raise a ``CellExecutionError``. Conveniently, the source cell causing
the error and the original error name and message are also printed.
After an error, we can still save the notebook as before:

.. code-block:: python

    nbformat.write(nb, open('executed_notebook.ipynb', mode='wt'))

The saved notebook contains the output up until the failing cell,
and includes a full stack-trace and error (which can help debugging).
A pattern I use to execute notebooks while handling errors is the following:

.. code-block:: python

    try:
        out = ep.preprocess(nb, {'metadata': {'path': run_path}})
    except CellExecutionError:
        msg = 'Error executing the notebook "%s".\n\n' % notebook_filename
        msg += 'See notebook "%s" for the traceback.' % notebook_filename_out
        print(msg)
        raise
    finally:
        nbformat.write(nb, open(notebook_filename_out, mode='wt'))

This will save the executed notebook regardless of execution errors.
In case of errors, however, an additional message is printed and the
``CellExecutionError`` is raised. The message directs the user to
the saved notebook for further inspection.

As a last scenario, it is sometimes useful to execute notebooks which
raise exceptions, for example to show an error condition.
In this case, instead of stopping the execution on the first error,
we can keep executing the notebook using the traitlet ``allow_errors``
(default False).
With ``allow_errors=True``,
the notebook is executed until the end, regardless of any error encountered
during the execution. The output notebook,
will contain the stack-traces and error messages for **all** the cells
raising exceptions.

Conclusions
-----------

Automating notebook execution can save time, facilitate testing and increase
robustness of computational pipelines base on notebooks.
``nbconvert`` serves the basic execution needs for most projects and has
the benefits of being a standard Jupyter component.

Another project worth mentioning is
`runipy <https://github.com/paulgb/runipy>`__, which a few years ago
was the only easy way to run notebooks in batches.

A natural extension to executing notebooks programmatically is passing
arguments, for example to select data files or analysis parameters.
You can find an experimental implementation of parameter passing in
`nbrun <https://github.com/tritemio/nbrun>`__.
