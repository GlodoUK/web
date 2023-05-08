{
    "name": "web_leaflet",
    "summary": "Defines an Odoo Enterprise-like Map view",
    "development_status": "Alpha",
    "category": "Hidden",
    "version": "16.0.1.0.0",
    "depends": ["web"],
    "data": [],
    "qweb": ["static/xml/templates.xml"],
    "auto_install": False,
    "author": "Glodo",
    "website": "https://www.glodo.uk/",
    "license": "LGPL-3",
    "assets": {
        "web.assets_backend": [
            "web_leaflet/static/lib/leaflet/*.css",
            "web_leaflet/static/src/scss/*.scss",
            "web_leaflet/static/src/js/*.js",
        ]
    },
}
