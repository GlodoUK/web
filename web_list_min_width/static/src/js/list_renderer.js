odoo.define("web_list_min_width.ListRenderer", function (require) {
    "use strict";

    const ListRenderer = require("web.ListRenderer");
    ListRenderer.include({
        _computeDefaultWidths: function () {
            this._super.apply(this, arguments);

            this.columns.forEach((column) => {
                if (!column.attrs["min-width"]) {
                    return;
                }

                const th = this._getColumnHeader(column);
                th.style.minWidth = column.attrs["min-width"];
            });
        },
    });
});
