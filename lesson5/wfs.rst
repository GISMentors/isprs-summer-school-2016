OGC Web Feature Service
-----------------------

http://opengeospatial.org/standards/wfs

Publish geospatial vector data from data stored on server to the client.

Mandatory parameters for the data request:

* TYPENAME - list of feature types

Optional parameters:

* BBOX
* FILTER
* FEATUREID
* PROPERTYNAME
* ...

WFS Server should be able to handle 3 types of requests:

* GetCapabilities - retrieves server metadata (encoded as XML document)
* GetFeature - retrieves vector data
* DescribeFeatureType - retrieves schema of the database
* LockFeature - for editing
* GetFeatureWithLock - get fetaure and lock it

Testing OGC WFS directly
------------------------

Since we deployed our service as WFS too, we should be able to download `Roads`
data as GML. The `GetCapabilities` request should look like::

    http://147.32.26.113:91/cgi-bin/qgis_mapserv.fcgi?
    map=NAME/project.qgs&         <-- NOTE: this is not part of the WFS standard
    service=WFS&
    version=1.0.0&
    request=GetCapabilities

Concrete example in our case:

    http://147.32.26.113:91/cgi-bin/qgis_mapserv.fcgi?map=cepicky/ISPRS_summerschool_ospublication.qgs&service=WFS&request=GetCapabilities

Now we can download *layer* `Primary_road` as GML file:


    http://147.32.26.113:91/cgi-bin/qgis_mapserv.fcgi?map=cepicky/ISPRS_summerschool_ospublication.qgs&service=WFS&request=GetFeature&typename=Primary_road


Adding WFS layer to QGIS
------------------------

.. note:: It's worth to start a new empty QGIS project for this step
        to avoid confusion by all the layers you may have in the layer
        switcher.

#. Add new WFS server (:menuselection:`Layer --> Add WFS Layer --> New server`)

    .. figure:: images/20_wfs.png

        Add new WFS connection with URL 
        http://147.32.26.113:91/cgi-bin/qgis_mapserv.fcgi?map=cepicky/ISPRS_summerschool_ospublication.qgs

#. Select required layer

   .. figure:: images/18_wfs.png

        Select e.g. `Primary_road` layer (or more, if you want)

#. As result - you have new layer from the WFS server in your map

   .. figure:: images/19_wfs.png

#. If enabled, QGIS is even able to update the data and send them back to the
   server (using WFS-T standard)
