import socket

from markupsafe import escape

from odoo import api, models, tools
from odoo.tools import config

CONFIG = config.misc.get("web_environment_banner", {})


class EnvironmentBanner(models.AbstractModel):
    _name = "web.environment.banner"
    _description = "Web Env Systray"

    @api.model
    def _prepare_variables(self):
        return {
            "hostname": socket.gethostname(),
        }

    @api.model
    def _enabled(self):
        return tools.str2bool(CONFIG.get("enabled", "false")) and CONFIG.get("name")

    @api.model
    @tools.ormcache()
    def _get_data(self):
        if not self._enabled():
            return

        name_tmpl = CONFIG.get("name")

        try:
            name = (
                name_tmpl and name_tmpl.format(**self._prepare_variables()) or name_tmpl
            )
        except KeyError as e:
            name = "%s (unknown key '%s')" % (name_tmpl, str(e))

        return {
            "name": name,
            "bgcolour": CONFIG.get("bgcolour", "#FFDC00"),
            "fgcolour": CONFIG.get("fgcolour", "#000000"),
        }

    @api.model
    @tools.ormcache()
    def _render(self):
        data = self._get_data()
        if not data:
            return

        return """
        <div style="
             border: 10px solid {bgcolour};
             border-image: repeating-linear-gradient(
                -45deg,
                {fgcolour},
                {fgcolour} 20px,
                {bgcolour} 20px,
                {bgcolour} 40px
              ) 10;
            background-color: {bgcolour};
            font-white: bold;
            color: {fgcolour};
            text-transform: uppercase;
            font-family: monospace;
            font-size: 1.1em;
            box-sizing: border-box;
            padding: 0 1em; text-align: center
        ">
            {name}
        </div>
        """.format(
            bgcolour=escape(data.get("bgcolour")),
            fgcolour=escape(data.get("fgcolour")),
            name=escape(data.get("name")),
        )
