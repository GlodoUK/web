odoo.define("web_list_min_width.ListRenderer", function (require) {
    "use strict";

    const ListRenderer = require("web.ListRenderer");
    ListRenderer.include({
        /**
         * @override
         * @private
         */
        _computeDefaultWidths: function () {
            this._super.apply(this, arguments);

            this.columns.forEach((column) => {
                if (!column.attrs["min-width"]) {
                    return;
                }

                const th = this._getColumnHeader(column);
                th.style.minWidth = column.attrs["min-width"];
                th.style.width = "";
            });
        },

        /**
         * @override
         * @private
         */
        _renderHeaderCell: function (node) {
            const $th = this._super.apply(this, arguments);
            if (node.attrs["min-width"]) {
                $th[0].style.minWidth = node.attrs["min-width"];
                $th[0].style.width = "";
            }
            return $th;
        },
    });
});
