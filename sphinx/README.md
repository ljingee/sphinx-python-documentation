# Sphinx Python Documentation

## Overview

This document details the procedure to create documentation under folder ***\<project\>/sphinx*** using Sphinx. You can create the documentation in a different location using the similar procedure.

## Procedure

### Prepare doc strings in the source code

Make sure code has doc strings in stardard format.

### Create Python virtual environment and install packages

Follow [Project README](../README.md)

### Notes

* To set up sphinx from scratch, follow all steps described in ***Start Sphinx*** section.

* To re-create HTML or PDF files, follow step 8 ~ step 10 described in ***Start Sphinx*** section.

* To re-create HTML or PDF files after source code has been changed, follow step 6, step8 ~ step 10 described in ***Start Sphinx*** section.

### Start Sphinx

1. Open command prompt in the project folder.

2. Create a folder with name ***sphinx***.

3. Cd to the ***sphinx*** folder

4. Use commands below to start documentation process:

    In ***sphinx/***, run
    ```
    sphinx-quickstart
    ```
    * Separate source and build directories (y/n) [n]

    * Enter the proper values for ***Project name, Author name(s) and Project release*** and choose default options for other settings to continue the process.

      * Project name: Design Documentation
      * Author names(s): L. Z.
      * Project release [1]: 1.0

    * At the end of the process, it will create a number of files, But, we are only concerned with ***conf.py*** and ***index.rst***.

      ```bash
      Creating file C:<project>\sphinx\conf.py
      Creating file C:<project>\sphinx\index.rst
      Creating file C:<project>\sphinx\Makefile
      Creating file C:<project>\sphinx\make.bat
      ```

5. Edit ***conf.py***

   * Insert the code below to line 5

      ```bash
        # -- Path setup --------------------------------------------------------------

        # If extensions (or modules to document with autodoc) are in another directory,
        # add these directories to sys.path here. If the directory is relative to the
        # documentation root, use os.path.abspath to make it absolute, like shown here.
        #
        import os
        import sys
        sys.path.insert(0, os.path.abspath('../..'))
      ```

    * Add ***sphinx.ext.autodoc*** and ***rinoh.frontend.sphinx*** to the extensions list

    * Assign ***html_theme*** value ***sphinx_rtd_theme***

    * Insert the code below to the end of the file

      ```bash
        # -- Options for LaTeX output ------------------------------------------------

        latex_elements = {
            # The paper size ('letterpaper' or 'a4paper').
            'papersize': 'letterpaper',
            # The font size ('10pt', '11pt' or '12pt').

            'pointsize': '10pt',
            # Additional stuff for the LaTeX preamble.
            'preamble': '',
            # Latex figure (float) alignment
            'figure_align': 'htbp',
        }
      ```

6. Create Sphinx Source for Python Package

    Still in ***sphinx/***,

    On Windows, run
    ```
    update-src-doc.bat
    ```
    On MacOS or Linux, run
    ```
    ./update-src-doc.sh
    ```
   * This script runs `sphinx-apidoc -o ./_srcdoc ../..` to create sphinx source for python code.

      ```bash
      sphinx-apidoc [OPTIONS] -o <OUTPUT_PATH> <MODULE_PATH> [EXCLUDE_PATTERN …]
      ```
      * MODULE_PATH is the path to a Python package to document,
      * OUTPUT_PATH is the directory where the generated sources are placed.
      * Any EXCLUDE_PATTERNs given are [fnmatch-style](https://docs.python.org/3/library/fnmatch.html) file and/or directory patterns that will be excluded from generation.

   * In our case, OUTPUT_PATH is ***./_srcdoc***, and MODULE_PATH is ***\<project\>***

   * It will create a number of .rst files, for example:

      ```bash
      Creating file .\_srcdoc\main.rst.
      Creating file .\_srcdoc\commonlib.rst.
      Creating file .\_srcdoc\commonlib.atms.rst.
      Creating file .\_srcdoc\commonlib.devices.rst.
      Creating file .\_srcdoc\commonlib.ui.rst.
      Creating file .\_srcdoc\lib.rst.
      Creating file .\_srcdoc\modules.rst.
      ```

      If no python application code is available, only one file is generated:
      ```bash
      Creating file .\_srcdoc\modules.rst.
      ```

7. Edit ***index.rst***

   * Add ***modules*** inside the similar command as shown below

      ```bash
      Welcome to <Project Name>'s documentation!
      ========================================

       .. toctree::
          :maxdepth: 2
          :caption: Contents:

          _srcdoc/modules
      ```

8. Create the HTML and PDF documentation file

    Still in the ***sphinx/*** directory, run

    ```bash
    make clean
    make html
    sphinx-build -b rinoh . _build/rinoh
    ```

9. Open ***\<project\>/sphinx/_build/html/index.html*** to see output of html documentation

10. Open ***\<project\>/sphinx/_build/rinoh/*** to see output of pdf documentation (not completed)


## Publish HTML - Hosting the website on GitHub

*