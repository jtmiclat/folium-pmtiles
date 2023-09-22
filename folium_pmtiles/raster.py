from folium.elements import JSCSSMixin
from folium.map import Layer
from jinja2 import Template


class PMTilesRaster(JSCSSMixin, Layer):
    """Based of
    https://github.com/python-visualization/folium/blob/56d3665fdc9e7280eae1df1262450e53ec4f5a60/folium/plugins/vectorgrid_protobuf.py
    """

    _template = Template(
        """
            {% macro script(this, kwargs) -%}


            var {{ this.get_name() }} = new pmtiles.PMTiles('{{ this.url }}')
            pmtiles.leafletRasterLayer(
                {{ this.get_name() }},
                {{ this.options if this.options is string else this.options|tojson }}
            ).addTo({{ this._parent.get_name() }})

            {%- endmacro %}
            """
    )

    default_js = [
        (
            "pmtiles",
            "https://unpkg.com/pmtiles@2.5.0/dist/index.js",
        )
    ]

    def __init__(self, url, layer_name=None, options=None, **kwargs):
        self.layer_name = layer_name if layer_name else "PMTilesRaster"

        super().__init__(name=self.layer_name, **kwargs)

        self.url = url
        self._name = "PMTilesRaster"

        if options is not None:
            self.options = options
        else:
            self.options = {}
