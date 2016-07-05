.. |pythoneditor| image:: ../_static/icons/grass/python.png
   :width: 1.5em
.. |script| image:: ../_static/icons/grass/script-load.png
   :width: 1.5em               
                   
Python scripting for GRASS
==========================

Example: Flooding simulation
----------------------------

Instead of creating our first Python script for GRASS from scratch we
will use model created in :doc:`previous section <modeler>`. The
Graphic Modeler allows on-the-fly conversion to simple Python script
(tab *Python editor*).

.. figure:: images/modeler-python.png

   Model as Python script.

We save this script to a new file by clicking on *Save as* button. This script can
be launched from menu :menuselection:`File --> Launch script` or from
the toolbar |script|.

Afterwards we will open this file in GRASS Python editor or in your
favourite editor. GRASS Python editor can be launched from Layer
Manager (tab *Python*, button *Simple editor*) or from the main
toolbar |pythoneditor|.

.. figure:: images/lmgr-python-editor.png

   Launching GRASS Python editor from Layer Manager.

In this editor we open our Python script and will start modifying
it. Our goal will be a script capable to run flooding analysis multiple
times based on *start* and *end* water level and *step* value.

One of the advantages is that the result script behaves as normal GRASS
module. If user doesn't enter all required parameters GRASS generates
GUI dialog similarly to other GRASS commands.

.. figure:: images/lake-dialog.png

   Generated GUI dialog of our Python lake script.

Example of resultant script to download: `lake.py
<../_static/scripts/lake.py>`_

.. literalinclude:: ../_static/scripts/lake.py
   :language: python

Real stuff: DEM from Lidar data
----------------------------------------

Script to download: `isprs.py
<../_static/scripts/isprs.py>`_

.. literalinclude:: ../_static/scripts/isprs.py
   :language: python

