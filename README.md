# 🗺️ Folium Plugin to support PMTiles

## Basic usage

### Vector

```python
import folium
from folium_pmtiles import PMTilesVector

m = folium.Map(location=[43.7798, 11.24148])
pmtiles_layer = PMTilesVector(
    "https://protomaps.github.io/PMTiles/protomaps(vector)ODbL_firenze.pmtiles",
    "folium_layer_name",
)
m.add_child(pmtiles_layer)
```

### Raster

```python
import folium
from folium_pmtiles import PMTilesRaster

m = folium.Map(location=[43.7798, 11.24148])
pmtiles_layer = PMTilesRaster(
    "https://protomaps.github.io/PMTiles/stamen_toner(raster)CC-BY+ODbL_z3.pmtiles",
    "folium_layer_name",
)
m.add_child(pmtiles_layer)
```

## Dev Setup

```
poetry install --with dev
poetry run pre-commit install
```

## TODO:

- [ ] Add styling support
- [ ] Add Raster support
