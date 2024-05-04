var map = L.map('map').setView([-0.487605005885925, 117.17065147526995], 12.5);
        
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var greenIcon = L.icon({
    iconUrl: 'leaf-green.png',
    shadowUrl: 'leaf-shadow.png',

    iconSize:     [38, 95], // size of the icon
    shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

let koor = [[-0.48441190596084355, 117.12887316928524],[-0.4910381557300359, 117.14903350059049],[-0.494695119875663, 117.12445189128229]];

for(let i = 0; i < koor.length; i++){
    L.marker(koor[i]).addTo(map);
}