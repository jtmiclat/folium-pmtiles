# 🗺️ Folium Plugin to support PMTiles

## Basic usage

### Installation

```
pip install folium folium-pmtiles
```

### Usage

The recommend way is to use `PMTilesVector`. This converts a simple mapbox style to a appropriate leaflet/protomaps styles.
If you need more complex styling, you can use `PMTilesMapLibreLayer`

A simple folium example is as follows:

```python
import folium

from folium_pmtiles.vector import PMTilesVector

m = folium.Map(location=[43.7798, 11.24148], zoom_start=12)
pmtiles_layer = PMTilesVector(
    "https://pmtiles.jtmiclat.me/protomaps(vector)ODbL_firenze.pmtiles",
    "folium_layer_name",
    style={
        "layers": [
            {
                "source-layer": "landuse",
                "type": "fill",
                "paint": {"fill-color": "steelblue"},
            },
            {
                "source-layer": "roads",
                "type": "line",
                "paint": {"line-color": "black"},
            },
        ],
    },
    options={
        "attribution": """<a href="https://protomaps.com">Protomaps</a> © <a href="https://openstreetmap.org/copyright">OpenStreetMap</a>'"""
    },
)
m.add_child(pmtiles_layer)
```

See [example/](example/) to see more examples and live demos via google collab or github.dev.

## Dev Setup

```
poetry install --with dev
poetry run pre-commit install
```
