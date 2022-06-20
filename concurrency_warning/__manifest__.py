# Copyright © 2021 Glo Systems (<https://www.glo.systems>)
# @author: Matt Lipski (<info@glo.systems>)
# License OPL-1 (https://www.odoo.com/documentation/15.0/legal/licenses.html).

{
    'name': 'Concurrency Warning',
    'version': '15.0.1.0.1',
    'category': 'Uncategorized',
    'author': 'Glo.systems',
    'website': 'https://www.glo.systems',
    'license': 'LGPL-3',
    'summary': "Issue a visual warning and reload the page content "
               "if a user has left a model open, and it been altered "
               "in the meantime.",
    'depends': [
        "base",
        "bus",
        "base_automation",
    ],
    'data': [
    ],
    'assets': {
        "web.assets_backend": [
            "/concurrency_warning/static/src/js/client_poke.esm.js"],
    },
    'demo': [
    ],
    'external_dependencies': {
    },
    'price': 0.0,
    'currency': 'EUR',
    'support': 'info@glo.systems',
    'application': False,
    'installable': True,
    'auto_install': False,
}
