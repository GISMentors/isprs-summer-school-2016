var mymap = L.map('mapid').setView([49.1839233, 15.4544358], 13);

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
    maxZoom: 19
}).addTo(mymap);
