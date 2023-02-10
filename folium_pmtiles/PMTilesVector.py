from folium.elements import JSCSSMixin
from folium.map import Layer
from jinja2 import Template


class PMTilesVector(JSCSSMixin, Layer):
    """Based of
    https://github.com/python-visualization/folium/blob/56d3665fdc9e7280eae1df1262450e53ec4f5a60/folium/plugins/vectorgrid_protobuf.py
    """

    _template = Template(
        """
            {% macro script(this, kwargs) -%}


            var {{ this.get_name() }} = protomaps.leafletLayer(
                {
                    "url":  '{{ this.url }}'
                })
            {{ this.get_name() }}.addTo({{ this._parent.get_name() }})
            {%- endmacro %}
            """
    )

    default_js = [
        (
            "pmtiles",
            "https://unpkg.com/protomaps@latest/dist/protomaps.min.js",
        )
    ]

    def __init__(self, url, layer_name=None, options=None):
        self.layer_name = layer_name if layer_name else "PMTilesVector"

        super().__init__(name=self.layer_name)

        self.url = url
        self._name = "PMTilesVector"

        if options is not None:
            self.options = options
