from branca.element import MacroElement
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


            var {{ this.get_name() }} = protomapsL.leafletLayer(
                {
                    "url":  '{{ this.url }}',
                    {% if this.style %}
                        ...protomapsL.json_style({{ this.style|tojson}}), 
                    {% endif %}
                    ...{{ this.options if this.options is string else this.options|tojson }}
                }
            )
            {{ this.get_name() }}.addTo({{ this._parent.get_name() }})
            {%- endmacro %}
            """
    )

    default_js = [
        (
            "protomapsL",
            "https://unpkg.com/protomaps-leaflet@1.24.0/dist/protomaps-leaflet.min.js",
        )
    ]

    def __init__(self, url, layer_name=None, style=None, options=None, **kwargs):
        self.layer_name = layer_name if layer_name else "PMTilesVector"

        super().__init__(name=self.layer_name, **kwargs)

        self.url = url
        self._name = "PMTilesVector"
        if style is not None:
            self.style = style

        if options is not None:
            self.options = options
        else:
            self.options = {}


class PMTilesMapLibreLayer(JSCSSMixin, Layer):
    """Based of
    https://github.com/python-visualization/folium/blob/56d3665fdc9e7280eae1df1262450e53ec4f5a60/folium/plugins/vectorgrid_protobuf.py
    """

    _template = Template(
        """
            {% macro script(this, kwargs) -%}
            let protocol = new pmtiles.Protocol();
            maplibregl.addProtocol("pmtiles", protocol.tile);

           {{ this._parent.get_name() }}.createPane('overlay');
           {{ this._parent.get_name() }}.getPane('overlay').style.zIndex = 650;
           {{ this._parent.get_name() }}.getPane('overlay').style.pointerEvents = 'none';

            var {{ this.get_name() }} = L.maplibreGL({
            pane: 'overlay',
            style: {{ this.style|tojson}},
            interactive: true,
            }).addTo({{ this._parent.get_name() }});

            {%- endmacro %}
            """
    )
    default_css = [
        ("maplibre_css", "https://unpkg.com/maplibre-gl@2.2.1/dist/maplibre-gl.css")
    ]

    default_js = [
        ("pmtiles", "https://unpkg.com/pmtiles@2.5.0/dist/index.js"),
        ("maplibre-lib", "https://unpkg.com/maplibre-gl@2.2.1/dist/maplibre-gl.js"),
        (
            "maplibre-leaflet",
            "https://unpkg.com/@maplibre/maplibre-gl-leaflet@0.0.17/leaflet-maplibre-gl.js",
        ),
    ]

    def __init__(self, url, layer_name=None, style=None, tooltip=None, **kwargs):
        self.layer_name = layer_name if layer_name else "PMTilesVector"

        super().__init__(name=self.layer_name, **kwargs)

        self.url = url
        self._name = "PMTilesVector"
        if tooltip is not None:
            self.add_child(tooltip)
        if style is not None:
            self.style = style
        else:
            self.style = {}


class PMTilesMapLibreTooltip(JSCSSMixin, MacroElement):
    _template = Template(
        """
            {% macro header(this, kwargs) %}
            <style>
            .maplibregl-popup {
                font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
                z-index: 651;
            }
            .feature-row{
                margin-bottom: 0.5em;
                &:not(:last-of-type) {
                    border-bottom: 1px solid black;
                }
            }
            </style>
            {% endmacro %}

            {% macro script(this, kwargs) -%}
                var {{ this.get_name() }} = {{ this._parent.get_name() }}.getMaplibreMap();
                const popup = new maplibregl.Popup({
                    closeButton: false,
                    closeOnClick: false
                });
                {{ this.get_name() }}.on('load', () => {
                    {{ this.get_name() }}.on('mousemove', (e) => { 
                        {{ this.get_name() }}.getCanvas().style.cursor = 'pointer';
                        const { x, y } = e.point;
                        const r = 2; // radius around the point
                        const features = {{ this.get_name() }}.queryRenderedFeatures([
                            [x - r, y - r],
                            [x + r, y + r],
                        ]);

                        const {lng, lat}  = e.lngLat;
                        const coordinates = [lng, lat]
                        const html = features.map(f=>`
                        <div class="feature-row">
                            <span>
                                <strong>${f.layer['source-layer']}</strong>
                                <span style="fontSize: 0.8em" }> (${f.geometry.type})</span>
                            </span>
                            <table>
                                ${Object.entries(f.properties).map(([key, value]) =>`<tr><td>${key}</td><td style="text-align: right">${value}</td></tr>`).join("")}
                            </table>
                        </div>
                        `).join("")
                        if(features.length){
                            popup.setLngLat(e.lngLat).setHTML(html).addTo({{ this.get_name() }});
                        } else {
                            popup.remove();
                        }
                    });
                    {{ this.get_name() }}.on('mouseleave', () => {popup.remove();});
                });
            {%- endmacro %}
            """
    )

    def __init__(self, name=None, **kwargs):
        super().__init__(**kwargs)
        self._name = name if name else "PMTilesTooltip"
