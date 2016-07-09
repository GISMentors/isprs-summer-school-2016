var mymap = L.map('mapid').setView([49.1839233, 15.4544358], 13);

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    maxZoom: 19
}).addTo(mymap);


var wmsLayer = L.tileLayer.wms(
    'http://gislab:91/cgi-bin/qgis_mapserv.fcgi?map=cepicky/ISPRS_summerschool_ospublication.qgs',
    {
      layers: 'Ortophoto',
      format: 'image/png',
      opacity: 0.9,
      transparent: true
    }).addTo(mymap);

var jsonLayer = new L.GeoJSON.AJAX('hydrology.json',
    {
      style: {
        color: 'navy',
        weight: 3,
        opacity: 0.9
      }
    });       
jsonLayer.addTo(mymap);
