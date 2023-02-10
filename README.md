# 🗺️ Folium Plugin to support PMTiles

## Basic usage

### Vector

```python
import folium

from folium_pmtiles.vector import PMTilesVector

m = folium.Map(location=[43.7798, 11.24148], zoom_start=12, tiles=None)
pmtiles_layer = PMTilesVector(
    "https://protomaps.github.io/PMTiles/protomaps(vector)ODbL_firenze.pmtiles",
    "folium_layer_name",
    options={
        "attribution": """<a href="https://protomaps.com">Protomaps</a> © <a href="https://openstreetmap.org/copyright">OpenStreetMap</a>'"""
    },
)
m.add_child(pmtiles_layer)
```

See https://github.com/protomaps/protomaps.js/blob/eb9ca41a7469d30beada65f53cd51d94ea77c305/src/frontends/leaflet.ts#L42-L63
for valid options

### Raster

```python
import folium

from folium_pmtiles.raster import PMTilesRaster

m = folium.Map(location=[43.7798, 11.24148], zoom_start=2, tiles=None)
pmtiles_layer = PMTilesRaster(
    "https://protomaps.github.io/PMTiles/stamen_toner(raster)CC-BY+ODbL_z3.pmtiles",
    "folium_layer_name",
    options={
        "attribution": """Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>."""
    },
)
m.add_child(pmtiles_layer)
```

see https://leafletjs.com/reference.html#gridlayer-option for valid options

## Dev Setup

```
poetry install --with dev
poetry run pre-commit install
```
