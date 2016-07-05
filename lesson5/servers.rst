Open source and free software web mapping server programs
=========================================================

MapServer - the fast one
------------------------

http://mapserver.org

    .. figure:: images/mapserver.png 

Pros:

* Fast as hell
* Support for all coordinate reference systems and in/out formats thanks to GDAL
  and Proj4
* MapScript - Python, PHP, ...

Cons:

* Text file configuration

GeoServer - with GUI
--------------------

http://geoserver.org

    .. figure:: images/geoserver.png

Pros:

* Web based graphical administration
* REST api

Cons:

* Java (slower, complicated to install)
* More difficult configuration

Mapnik - for OpenStreetMap and Cartography
------------------------------------------

http://mapnik.org

    .. figure:: images/mapnik.png

Pros:

* Cartography
* Great support for OSM data

Cons:

* Slow
* Custom not easy configuration
* Support for OGC OWS via custom Python wrapper

QGIS - The easy one
-------------------

http://qgis.org

    .. figure:: images/qgis.png
    
Pros:

* 100% compatibility with QGIS desktop
* What can you do in desktop, can you have in server

Cons:

* The slowest one
* Stability (getting better)
