from lxml import html

from odoo.http import request

from odoo.addons.web.controllers.main import Database


class Database(Database):
    def _render_template(self, **d):
        data = super()._render_template(**d)

        enabled = request.env["web.environment.banner"]._enabled()
        if enabled:
            m = html.fromstring(data)
            first = m.xpath("//body")[0]
            first.insert(
                0, html.fromstring(request.env["web.environment.banner"]._render())
            )

            data = html.tostring(m)

        return data
