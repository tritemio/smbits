Batch Execution of Jupyter Notebooks
====================================

:date: 2015-12-23
:modified: 2015-12-23
:tags: jupyter, notebook, batch-processing, nbconvert, python
:category: Scientific Computing
:slug: execute-notebooks
:authors: Antonino Ingargiola
:summary: Batch execution of jupyter notebooks using nbconvert.
:status: published


Jupyter notebooks are increasingly used in scientific computing.
For example, computational projects often include several notebook to carry out
different parts of a bigger analysis. Or, libraries include
notebooks to provide documentation, examples or tests.

In all these cases, running notebook in batches, removes manual work
increasing robustness and reproducibility.

`nbconvert <http://nbconvert.readthedocs.org/>`__, the Jupyter component used
to convert notebooks, can be used to automatically execute and save one or more
notebooks.
This functionality is exposed through a python API and a similar
`command line interface <http://nbconvert.readthedocs.org/en/latest/usage.html>`__.

In this post we see how to use nbconvert (4.1+) python API interface
to programmatically execute notebooks.

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

Next, we configure the execution mode:

.. code-block:: python

    ep = ExecutePreprocessor(timeout=3600, kernel_name='python3')

We specified two (optional) arguments ``timeout`` and ``kernel_name``, which
define the execution timeout and the execution kernel to use respectively.

    The `kerne_name` keywords requires nbconvert 4.2 (unreleased,
    use master branch from github).

To actually run the notebook we call the method ``preprocess``:

.. code-block:: python

    out = ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})

Hopefully, we will not get any errors during the notebook execution
(see the last section for error handling). Note that ``path`` specifies
in which folder to execute the notebook.
Finally, to save the resulting notebook:

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
as command-line options. So we can pass the timeout from the command-line
like this::

    jupyter nbconvert --ExecutePreprocessor.timeout=3600 --to notebook --execute mynotebook.ipynb

Let's now discuss each traitlet in more detail.

The `timeout`` traitlet defines the maximum time (in seconds) the notebook is
allowed to run, if the execution takes longer an exception will be raised.
The default is only 30 s, so in many cases you may want to specify
an higher value.

The second traitlet, ``kernel_name``, allows to specify the name of the kernel
to be used for the execution. By default, the kernel name is retrieved from the
notebook metadata. ``kernel_name`` accepts a user-defined kernel name,
ignoring what is specified in the notebook. A common use case
is if that of a python 2/3 library which includes documentation/testing
notebooks. These notebooks will specify either python2 or python3 as kernel
(depending on the kernel used the last time the notebook was saved).
In reality, however, this notebook work on both 2 and 3 python versions.
For testing purposes, is important to execute these notebook on both
python 2 and 3. Here ``kernel_name`` traitlet comes to help, allowing
to specify "python2" and "python3" as kernel, overriding the value saved in the
notebook.

Error Handling
--------------

In the previous sections we saw how to save an executed notebook, assuming
there are no execution error. But, what if there are errors?

An error during the notebook execution, by default, will stop the execution
and raise a ``CellExecutionError``. Conveniently, the source cell causing
the error and the original error name and message are also printed.
If, after this error, we try to save the notebook as before:

.. code-block:: python

    nbformat.write(nb, open('executed_notebook.ipynb', mode='wt'))

we will obtain a notebook containing the output up until the failing cell,
including full stack-trace and error which can help debugging.
A pattern to execute a notebook even in case of errors can be the following:

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
``CellExecutionError`` is raised. The messages directs the user to
the saved notebook for further inspection.

As a last scenario, sometimes notebooks contains independent computations
in each code cell.
In this case it can be useful to run the notebook until the end,
in order to get a complete picture of all cells that are failing.
Luckily enough, the ``allow_errors`` traitlet (default False) allows to do that.
With ``allow_errors=True``,
the notebook is executed until the end, and a ``CellExecutionError`` is raised
if one or more cells threw an error. In this case, the output notebook
will contain the stack-traces and error messages for all the failing cells.

Conclusion
----------

Automating notebook execution can save time, facilitate testing and increase
robustness of computational pipelines base on notebooks.
``nbconvert`` serves the basic execution needs for most projects and has
the benefits of being a standard Jupyter component.

Another project worth mentioning is
`runipy <https://github.com/paulgb/runipy>`__, which a few years ago
was the only easy way to run notebooks in batches. With the recent features
gained by nbconvert, simple batch execution cases don't need runipy anymore.
runipy is still actively developed, however, as it is useful for backward
compatibility and to provide additional features not directly available in
nbconvert.

    I've not used runipy in a long time, so feel free leave a comment and
    correct me on the specific advantages of using runipy vs nbconvert.

Finally, I'm currently playing with the possibility of
`passing arguments to the notebook to be executed <https://github.com/tritemio/nbrun>`__,
but this will be the topic of a next post.
