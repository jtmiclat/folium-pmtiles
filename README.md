# 🗺️ Folium Plugin to support PMTiles

## Basic usage

### Installation

```
pip install folium folium-pmtiles
```

### Usage

The recommend way is to use `PMTilesMapLibreLayer`. This overlays a maplibre instance over leaflet which allows declarative styling using mapbox style specification.

A simple folium example is as follows:

```python
import folium

from folium_pmtiles.vector import PMTilesMapLibreLayer

m = folium.Map(location=[43.7798, 11.24148], zoom_start=13, tiles="cartodb positron")
pmtiles_url = "https://pmtiles.jtmiclat.me/protomaps(vector)ODbL_firenze.pmtiles"
pmtiles_layer = PMTilesMapLibreLayer(
    "folium_layer_name",
    style={
        "version": 8,
        "sources": {
            "example_source": {
                "type": "vector",
                "url": "pmtiles://" + pmtiles_url,
                "attribution": '<a href="https://protomaps.com">Protomaps</a> © <a href="https://openstreetmap.org/copyright">OpenStreetMap</a>',
            }
        },
        "layers": [
            {
                "id": "buildings",
                "source": "example_source",
                "source-layer": "landuse",
                "type": "fill",
                "paint": {"fill-color": "steelblue"},
            },
            {
                "id": "roads",
                "source": "example_source",
                "source-layer": "roads",
                "type": "line",
                "paint": {"line-color": "black"},
            },
        ],
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
