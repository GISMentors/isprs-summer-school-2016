New QGIS project
================

Let's create a new project in QGIS Desktop:

#. copy example dataset from `/mnt/repository/isprs/publication_workshop` to
   `Projects` directory

#. DO NOT open existing project `ISPRS_summerschool_ospublication.qgs` - create
   new one

#. Open QGIS

    .. figure:: images/01_qgis.png

        Open a new QGIS project.

#. Set project properties: Name, CRS, relative data path


    .. figure:: images/02_projection.png

        Set name of the project, CRS (EPSG:32633 WGS84/UTM33), relative path.

Ortophoto images
----------------

#. Load Ortophoto images from `publication-data/orthophoto_0_25_utm/north_up`

    .. figure:: images/03_ortophotos.png

        Ortophoto images are stored in `publication-data/orthophoto_0_25_utm/north_up`.
        If asked, set EPSG:32633 WGS84/UTM33 the CRS value of input data.

#. Set transparency of raster data to value `0`

    .. figure:: images/04_transparency.png

        Layer properties - Transparency set `0`.

#. As result, have Ortophoto image of Telč

    .. figure:: images/05_transparency.png

        Do not forget to create `Ortophoto` layer group in the layer switcher.

Vector data
-----------

#. Add INSPIRE hydrology dataset

    .. figure:: images/06_hydrology.png

        Data are stored in `publication-data/publication-data/isprire_hy_gml_etrf89/HY.290399b.gml`.

#. Select *all layers*

    .. figure:: images/07_hydrology.png

        Click on `Select all` button.

#. Create `Hydrology group`

#. Add all vector files from `publication-data/zabaged_topography_shp_utm`

#. Create map composition, play with styles

    .. figure:: images/08_map_composition.png


    :Cesta:             Path 
    :ElektrickeVedeni:  Wire 
    :LesniPrusek:       Bridle way 
    :SilniceDalnice:    Primary road
    :Ulice:             Residential road
    :ZeleznicniTrat:    Railway

