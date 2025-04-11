const map = new maplibregl.Map({
    container: 'map',
    style:
        'https://www.overrice.nyc/map-styles/light.json',
    center: [-73.96919956110607,40.723901332022166],
    zoom: 12
});

// const popup = new maplibregl.Popup({offset: 25}).setText(
//     'Construction on the Washington Monument began in 1848.'
// );

const placeSideSheet = document.getElementById("place-side-sheet");

map.on('load', () => {
    mapPinsData.forEach((mapPinData) => {
        if (mapPinData['coordinates']) {
            var mapPin = new maplibregl.Marker()
            .setLngLat(mapPinData['coordinates'].reverse())
            // .setPopup(popup)
            .addTo(map)

            var mapPinElement = mapPin.getElement()
            mapPinElement.addEventListener("click", function() {
                placeSideSheet.innerText = mapPinData['name']
                replaceSideSheetContent(mapPinData['name']);
            });
        }
    });
});

function replaceSideSheetContent(placeName) {
    fetch('/place/' + placeName)
        .then(response => response.text())
        .then(data => { placeSideSheet.innerHTML = data });
}
