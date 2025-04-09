const map = new maplibregl.Map({
    container: 'map',
    style:
        'https://api.maptiler.com/maps/streets/style.json?key=get_your_own_OpIi9ZULNHzrESv6T2vL',
    center: [-73.96919956110607,40.723901332022166],
    zoom: 12
});

map_pins.forEach((map_pin) => {
    if (map_pin['coordinates']) {
        new maplibregl.Marker()
        .setLngLat(map_pin['coordinates'].reverse())
        .addTo(map);
    }
  });

