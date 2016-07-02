Lidar Analysis
==============

Raster binning and classification
---------------------------------

The input files are classified to the classes bellow:

#. ground (postfix ``_g``)
#. veggetation (postfix ``_v``)
#. building (postfix ``_b``)

First we import the input files (output resolution will be define by
:option:`resolution` regardless computation region settings):

.. code-block:: bash

   r.in.lidar -o input=pm_TANV37_b.laz output=pm_TANV37_b resolution=3 method=mean

   r.in.lidar -o input=pm_TANV37_g.laz output=pm_TANV37_g resolution=3 method=mean

   r.in.lidar -o input=pm_TANV37_v.laz output=pm_TANV37_v resolution=3 method=mean

.. tip:: Raster map resolution can be checked by :grasscmd:`r.info`
         command.

.. tip:: In the case that input data include classified
         points (can be check by ``lasinfo`` command) you can
         use :option:`class_filter`` and
         :option:`return_filter` of :grasscmd:`r.in.lidar`.
                  
The composite map can be created by :grasscmd:`r.mapcalc` (note that
we need to define computational region based on import maps before
running the command):

.. code-block:: bash

   g.region raster=pm_TANV37_b,pm_TANV37_g,pm_TANV37_v -p
   r.mapcalc "pm_TANV37_classes = if(!isnull(pm_TANV37_v), 2, if(!isnull(pm_TANV37_g), 1, if(!isnull(pm_TANV37_b),3, null())))"
                
We also apply custom color table using :grasscmd:`r.colors`
(:option:`rules` in Define tab):

::

   1 220:220:180
   2 0:180:0
   3 150:0:0

.. figure:: images/pm_TANV37_classes.png

   Raster classification.

..
   d.mon start=cairo output=pm_TANV37_classes.png
   d.rast pm_TANV37_classes
   d.legend -fs raster=pm_TANV37_classes at=55,95,95,98
   d.mon stop=cairo

High resolution DEM
-------------------

First we import data into vector point map by :grasscmd:`v.in.lidar`
(we skip creating attribute table):

.. code-block:: bash
                
   v.in.lidar -t -o input=pr_TANV37_5g.laz output=pr_TANV37_5g

We can also check the point overall point density using
:grasscmd:`v.outlier`:

.. code-block:: bash
             
   v.outlier -e input=pr_TANV37_5g

   Estimated point density: 0.6418
   Estimated mean distance between points: 1.248

We will interpolate (:grasscmd:`v.surf.rst` using regularized spline
with tension approximation) with resolution 0.5 meter, also create
slope and profile curvature map. Since the interpolation process can
be very slope we will perform the computation on smaller area.

.. code-block:: bash

   g.region vector=pr_TANV37_5g res=0.5 -pa
   v.surf.rst input=pr_TANV37_5g elevation=dem_37 slope=slope_37 pcurv=pcurv_37 npmin=80 tension=20 smooth=1

.. tip:: Set higher npmin to reduce artifacts from segmentation
         visible on slope and curvature maps (will be much slower!):

   .. code-block:: bash
                
      g.region n=5626866 s=5626530 w=532642 e=533062 res=0.5 -pa

.. tip:: It can be also useful to set mask on areas without measured
         data. Convex hull created by :grasscmd:`v.hull` can be used
         for this purpose. The mask can be specified by
         :grasscmd:`r.mask` command (note that the mask will be
         created only inside compuitational region), or simple define
         by :option:`mask` option of :grasscmd:`v.surf.rst`.

         .. code-block:: bash

            v.hull input=pr_TANV37_5g output=mask_37 -f
            r.mask vector=mask_37
                   

         
Visualize point density in 3D
-----------------------------

.. todo:: ?

   http://ncsu-osgeorel.github.io/uav-lidar-analytics-course/assignments/lidar.html
   
