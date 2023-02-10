# Folium Plugin to support PMTiles

## Basic usage

```python
import folium
from folium_pmtiles import PMTilesVector
m = folium.Map(location=[43.7798, 11.24148])
pmtiles_layer = PMTilesVector("https://protomaps.github.io/PMTiles/protomaps(vector)ODbL_firenze.pmtiles", "folium_layer_name")
m.add_child(pmtiles_layer)
```

## TODO:

- [ ] Add styling support
- [ ] Add Raster for pmtiles
