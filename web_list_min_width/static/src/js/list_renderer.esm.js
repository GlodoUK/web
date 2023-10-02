/** @odoo-module **/

import {ListRenderer} from "@web/views/list/list_renderer";
import {patch} from "@web/core/utils/patch";

patch(ListRenderer.prototype, "web_list_min_width", {
    calculateColumnWidth(column) {
        if (
            column.rawAttrs !== undefined &&
            column.rawAttrs["min-width"] !== undefined
        ) {
            return {
                type: "absolute",
                value: column.rawAttrs["min-width"],
            };
        }
        return this._super(column);
    },
});
