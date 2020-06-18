{
    "name": "glo_backend_theme",
    "summary": "Glo Networks Backend Theme",
    "version": "12.0.0",
    "category": "Theme/Backend",
    "website": "https://www.glo.systems/",
    "description": """
    Glo Networks Backend theme for Odoo ommunity edition.
    Depends on OCA/web_responsive.
    """,
    "author": "Glo Networks",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',
    ],
    "data": [
        'views/assets.xml',
    ]
}
