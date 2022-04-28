# visiannot-example

This repository contains an example dataset in order to familiarize with **ViSiAnnoT** (see the documentation of [ViSiAnnoT](https://visiannot.readthedocs.io/en/latest/index.html) for details about the software and how to install it).

Once **ViSiAnnoT** is installed, open a console and go to the directory where you stored this repository. You may launch **ViSiAnnoT** with the following command line::

    $ python3 -m visiannot -c example_1.ini -n

The configuration file is ``example_1.ini``. The option ``-n`` disables the configuration GUI. You may remove this option in order to launch the configuration GUI before ViSiAnnoT GUI.

Another configuration file is provided and may be tested: ``example_2.ini``. Contrary to ``example_1.ini``, events annotation is disabled but image extraction is enabled. Moreover, there is intervals data.

The dataset is stored in the folder ``data``. The annotations are stored in the folder ``Annotations``.

The recording is made of 6 videos, each lasting one minute (except the last one, lasting 30 seconds). A set of CDs and vinyl are shown sequentially. The annotations give the periods when the disc belongs to one of the following musical genre:

- classical
- blues
- jazz
- rock
- reggae
- rap
- metal

Moreover, the disc format is also annotated in parallel with the following categories:

- cd
- vinyl

Some fake signals are also provided for illustrating the features of **ViSiAnnoT**.

It is possible to create a custom configuration file in order to familiarize with the features of **ViSiAnnoT**. Then, the value of the argument ``-c`` must be changed accordingly. See [documentation about editing a configuration file](https://visiannot.readthedocs.io/en/latest/userguide-configuration.html#editing-a-configuration-file).

A set of scripts is also provided, so that the user may explore the different features of **ViSiAnnoT** and how to use it in a script.