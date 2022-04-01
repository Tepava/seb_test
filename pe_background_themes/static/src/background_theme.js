/** @odoo-module */

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from 'web.utils';
var rpc = require('web.rpc');

patch(NavBar.prototype, 'pe_background_themes/static/src/background_theme.js', {
    
    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    /**
     * @override
     */
     setup() {
        this._super();
        this._search_def = $.Deferred();
        this.colors = this.get_values();
    },
    
    get_values: function() {
            var self = this;
            rpc.query({model: 'res.config.settings',method: 'get_value_from_company',args: [0],}).then(function(values){
                self.colors = values;
                console.log("values",values);
                
                if (values.nav_bg_color !== false){
                    document.documentElement.style.setProperty("--navbar-color",values.nav_bg_color);
                }
                if (values.nav_ft_color !== false){
                    document.documentElement.style.setProperty("--navbar-txt-color",values.nav_ft_color);
                }
                
                if (values.btn_hover_color !== false){
                    document.documentElement.style.setProperty("--btn-hover-color",values.btn_hover_color);
                }
                
                if (values.bg_color !== false){
                    document.documentElement.style.setProperty("--background-color",values.bg_color);
                }
                
                if (values.bg_image !== false){
                    document.documentElement.style.setProperty("--background-image",'url(data:image/png;base64,'+values.bg_image+')');
                }
            });
        },
});