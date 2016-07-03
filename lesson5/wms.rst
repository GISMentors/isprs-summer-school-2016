OGC Web Mapping Service
-----------------------

http://opengeospatial.org/standards/wms

Publish map images from data stored on server to the client.

Parameters for the map:

* Image size
* Required layers
* Area extent
* Image format
* Coordinate reference system
* (Layer style)

.. note:: **How does the server and the client communicate**

    Client sends the request encoded in URL to some known server address.
    Example of WMS endpoint::

        http://my.maps-domain.org/wms

    The parameters for the request are stored at the end of the url behind
    starting `?` sign. Each parameter and it's value are separated with `&` sign
    ::

        http://my.maps-domain.org/wms?parameter1=value1&parameter2=value2&...

    The response from the server is either data itself (like PNG or JPEG image)
    or XML-encoded document


WMS Server should be able to handle 3 types of requests:

* GetCapabilities - retrieves server metadata (encoded as XML document)
* GetMap - retrieves PNG or JPEG image
* GetFeatureInfo - allows the client ask for attribute data identified by "mouse
  click" - single point

How to publish WMS data using QGIS
----------------------------------

Let's create some QGIS project with raster and vector data!

1. - otevřít qgis
2. - nastavit projekt
3. - nahrát ortofota
4. - nahrát vektorovou vrstvu
5. - nastylovat vrstvu
6. - publikovat wms
7. - nahrát projekt
8. - testování projektu, WMS

Parameter MAP, otherwise standard WMS request
http://localhost/cgi-bin/qgis_mapserv.fcgi?MAP=/home/jachym/Data/isprs/ISPRS%20Summer%20School%20workshop.qgs&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities

GetMap

Pro QGIS použít dlaždicování - nebo zvětšit max. velikost obrázku




