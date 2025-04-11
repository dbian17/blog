const map = new maplibregl.Map({
    container: 'map',
    style:
        'https://www.overrice.nyc/map-styles/light.json',
    center: [-73.96919956110607,40.723901332022166],
    zoom: 12
});

const popup = new maplibregl.Popup({
    closeButton: false,
    closeOnClick: false
});

const placeSideSheet = document.getElementById("place-side-sheet");

map.on('load', () => {
    mapPinsData.forEach((mapPinData) => {
        if (mapPinData['coordinates']) {
            var mapPin = new maplibregl.Marker()
            .setLngLat(mapPinData['coordinates'].reverse())
            .addTo(map)

            var mapPinElement = mapPin.getElement()
            mapPinElement.addEventListener("click", function() {
                replaceSideSheetContent(mapPinData['name']);
            });

            mapPinElement.addEventListener("mousemove", function() {
                mapPinElement.style.cursor = 'pointer';
                popup.setLngLat(mapPinData['coordinates']).setHTML(mapPinData['rating'] + ' ' + mapPinData['name'].replaceAll("-", " ")).addTo(map);
            });

            mapPinElement.addEventListener("mouseleave", function() {
                popup.remove();
            });
        }
    });
});

function replaceSideSheetContent(placeName) {
    fetch('/place/' + placeName)
        .then(response => response.text())
        .then(data => { placeSideSheet.innerHTML = data });
}
