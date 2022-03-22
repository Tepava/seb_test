# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
        
    nav_ft_color = fields.Char(string="NavBar Text Color", related="company_id.nav_font_color")
    nav_bg_color = fields.Char(string="Navbar Color", related="company_id.nav_background_color")
    btn_hover_color = fields.Char(string="Hover color", related="company_id.button_hover_color")
    bg_color = fields.Char(string="Menu Background color", related="company_id.background_color")
    bg_image = fields.Binary(string="Menu Background Image", related="company_id.background_image", attachment=True)
    
    def get_value_from_company(self):
        values ={}
        image = self.env.user.company_id.background_image
        values['nav_ft_color'] = self.env.user.company_id.nav_font_color
        values['nav_bg_color'] = self.env.user.company_id.nav_background_color
        values['btn_hover_color'] = self.env.user.company_id.button_hover_color
        values['bg_color'] = self.env.user.company_id.background_color
        if not image:
            values['bg_image'] = None
        else:
            values['bg_image'] = image
        return values
        
    
    @api.model
    def create(self, values):
        if 'bg_image' in values:
            resize_image = tools.image_process(values['bg_image'], (1024, 1024))
            values['bg_image'] = resize_image
            return super(ResConfigSettings, self).create(values)
    
    