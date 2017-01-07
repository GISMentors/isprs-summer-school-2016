Building the web app
====================

Creating the web page
---------------------

`First simple example <http://147.32.26.113:91/barrel/cepicky/webapp/01_simplepage.html>`_ of our web app has
only heading and description text

.. literalinclude:: ../_static/webapp/01_simplepage.html
   :language: html
   :linenos:

Adding javascript code and map container
----------------------------------------

Add container `div` for the map and some javascript library as well as reference
to our code in `second simple example <http://147.32.26.113:91/barrel/cepicky/webapp/02_addjavascript.html>`_.

.. literalinclude:: ../_static/webapp/02_addjavascript.html
   :language: html
   :linenos:
   :emphasize-lines: 7-9,17-18

Writing simple Leaflet map
--------------------------

Let's now create file called `03_simple.js <http://147.32.26.113:91/barrel/cepicky/webapp/03_simple.js>`_,
which will contain the JavaScript code.

.. literalinclude:: ../_static/webapp/03_simple.js
   :language: javascript
   :linenos:

And let's embed this javascript code to our web page `03_simple.html <http://147.32.26.113:91/barrel/cepicky/webapp/03_simple.html>`_

.. literalinclude:: ../_static/webapp/03_simple.html
   :language: html
   :linenos:
   :emphasize-lines: 17-21


Add some WMS from our server
----------------------------

Let's add new WMS layer `04_wms.js <http://147.32.26.113:91/barrel/cepicky/webapp/04_wms.js>`_

.. literalinclude:: ../_static/webapp/04_wms.js
   :language: javascript
   :linenos:
   :emphasize-lines: 9-16

And have a look at our web page `04_wms.html <http://147.32.26.113:91/barrel/cepicky/webapp/04_wms.html>`_

Add some JSON data
------------------

.. note:: Mark parameters OutputFormat=GeoJSON and
          TypeName=HY_Watercourse_LineString

#. Get the data as JSON via WFS and save the to file `hydrology.json`

    http://147.32.26.113:91/cgi-bin/qgis_mapserv.fcgi?map=cepicky/ISPRS_summerschool_ospublication.qgs&service=WFS&request=GetFeature&typename=HY_Watercourse_LineString&outputformat=GeoJSON

#. Add new JSON layer to our script  `05_json.js <http://147.32.26.113:91/barrel/cepicky/webapp/05_json.js>`_

   Add Leaflet-Ajax plugin to the page

   .. literalinclude:: ../_static/webapp/05_json.html
       :language: html
       :linenos:
       :emphasize-lines: 10


   Add the vector layer to the web page and load the data in the background in
   asynchronous mode.

   .. literalinclude:: ../_static/webapp/05_json.js
       :lines: 1-17
       :language: javascript
       :linenos:
       :emphasize-lines: 18-17

   and see the result on `05_json.html <http://147.32.26.113:91/barrel/cepicky/webapp/05_json.html>`_
