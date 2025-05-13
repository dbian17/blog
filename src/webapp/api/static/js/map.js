const map = new maplibregl.Map({
    container: 'map',
    style:
        '/static/map-style.json',
    center: [-73.96919956110607,40.723901332022166],
    zoom: 12
});

const popup = new maplibregl.Popup({
    closeButton: false,
    closeOnClick: false
});
// popup.addClassName('map-pin-popup')

const PLACE_SIDE_SHEET_CONTENT = document.getElementById('place-side-sheet-content');
const PLACE_SIDE_SHEET = document.getElementById('place-side-sheet');
const PLACE_SIDE_SHEET_CLOSE_BUTTON = document.getElementById('place-side-sheet-close-button');

const PLACE_BOTTOM_SHEET_CONTENT = document.getElementById('place-bottom-sheet-content');
const PLACE_BOTTOM_SHEET = document.getElementById('place-bottom-sheet')
const PLACE_BOTTOM_SHEET_CLOSE_BUTTON = document.getElementById('place-bottom-sheet-close-button');

PLACE_SIDE_SHEET_CLOSE_BUTTON.addEventListener('click', (e) => {
    PLACE_SIDE_SHEET.style.width = "0px";
});

PLACE_BOTTOM_SHEET_CLOSE_BUTTON.addEventListener('click', (e) => {
    PLACE_BOTTOM_SHEET.style.maxHeight = "0px";
});

map.on('load', async () => {
    // const image = await map.loadImage('https://maplibre.org/maplibre-gl-js/docs/assets/custom_marker.png');
    // // Add an image to use as a custom marker
    // map.addImage('custom-marker', image.data);

    map.addSource('places', {
        'type': 'geojson',
        'data': {
            'type': 'FeatureCollection',
            'features': addPins()
        }
    });

    // Add a layer showing the places.
    map.addLayer({
        'id': 'places',
        'type': 'circle',
        'source': 'places',
        'layout': {
            'circle-sort-key':['to-number', ['get', 'rating']],

            // 'icon-image': 'custom-marker',
            // 'icon-allow-overlap': true,
            // 'symbol-sort-key': ['to-number', ['get', 'rating']],
            // 'symbol-z-order' : 'source'

        },
        'paint': {
            'circle-color':  [
                'interpolate-hcl',
                ['linear'],
                ['to-number', ['get', 'rating']],
                2,
                '#F50C5E',
                10,
                '#0CF589'
            ],
            'circle-radius': isDesktop ? 5 : 20
        }
    });
    
    addHoverEvent();
    addClickEvent();
    addSearchEvent();
});

function addPins() {
    const featuresList = []
    mapPinsData.forEach(function(mapPinData) {
        var feature = {
            'type': 'Feature',
            'properties': {
                'id': mapPinData['id'],
                'rating': mapPinData['rating'],
                'name': mapPinData['name'],
                'search': mapPinData['types'] + mapPinData['name'] + mapPinData['rating']
            },
            'geometry': {
                'type': 'Point',
                'coordinates': mapPinData['coordinates'].reverse()
            }
        }
        featuresList.push(feature);
    });
    return featuresList;
}

function addClickEvent() {
    map.on('click', 'places', (event) => {
        const placeId = event.features[0].properties['id'];

        if (isDesktop) {
            fetch('/place/' + placeId)
            .then(response => response.text())
            .then(data => { PLACE_SIDE_SHEET_CONTENT.innerHTML = data });
            
            PLACE_SIDE_SHEET.style.width = "30%";
        } else {
            fetch('/place/' + placeId)
            .then(response => response.text())
            .then(data => { PLACE_BOTTOM_SHEET_CONTENT.innerHTML = data });
            
            PLACE_BOTTOM_SHEET.style.maxHeight = "60%";
            PLACE_BOTTOM_SHEET.style.width = "100%";
            PLACE_BOTTOM_SHEET.style.display = "block";
            document.body.style.overflow = "hidden";
            PLACE_BOTTOM_SHEET.style.bottom = "0";
        }
    });
}

function addHoverEvent() {
    // Make sure to detect marker change for overlapping markers
    // and use mousemove instead of mouseenter event
    let currentFeatureCoordinates = undefined;
    map.on('mousemove', 'places', (event) => {
        const featureCoordinates = event.features[0].geometry.coordinates.toString();
        if (currentFeatureCoordinates !== featureCoordinates) {
            currentFeatureCoordinates = featureCoordinates;

            // Change the cursor style as a UI indicator.
            map.getCanvas().style.cursor = 'pointer';

            const description = getPopupHtml(event.features[0].properties);
            const coordinates = event.features[0].geometry.coordinates.slice();

            // Ensure that if the map is zoomed out such that multiple
            // copies of the feature are visible, the popup appears
            // over the copy being pointed to.
            while (Math.abs(event.lngLat.lng - coordinates[0]) > 180) {
                coordinates[0] += event.lngLat.lng > coordinates[0] ? 360 : -360;
            }

            // Populate the popup and set its coordinates
            // based on the feature found.
            popup.setLngLat(coordinates).setHTML(description).addTo(map);
        }
    });

    map.on('mouseleave', 'places', () => {
        currentFeatureCoordinates = undefined;
        map.getCanvas().style.cursor = '';
        popup.remove();
    });
}

function getPopupHtml(feature_properties) {
    return '<p>' +  feature_properties['rating'] + ' ' + feature_properties['name'] + '</p>';
}

function addSearchEvent() {
    const searchBar = document.getElementById('search-bar'); 
    searchBar.addEventListener('keyup', (e) => {
        var search_input = e.target.value.toLowerCase();
        map.setFilter('places', ['any', ['>', ['index-of', search_input, ['downcase', ['to-string', ['get', 'search']]]], -1]])
    });
}

// let isDragging = false;
// let startY, startBottom;

// dragHandle
//     .addEventListener("mousedown", startDragging);

// function startDragging(e) {
//     console.log("Dragging")
//     e.preventDefault();
//     isDragging = true;
//     startY = e.clientY;
//     startBottom =
//         parseInt(getComputedStyle(PLACE_BOTTOM_SHEET).bottom);

//     document.addEventListener("mousemove", drag);
//     document.addEventListener("mouseup", stopDragging);
// }

// function drag(e) {
//     if (!isDragging) return;
//     const deltaY =
//         e.clientY - startY;
//     PLACE_BOTTOM_SHEET.style.bottom =
//         Math.max(startBottom - deltaY, 0) + "px";
// }

// function stopDragging() {
//     isDragging = false;
//     document
//         .removeEventListener("mousemove", drag);
//     document
//         .removeEventListener("mouseup", stopDragging);
// }
