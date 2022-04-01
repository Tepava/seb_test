# -*- coding: utf-8 -*-

from odoo import models, fields, tools, api

class ResCompany(models.Model):
    _inherit = 'res.company'
    
    nav_font_color = fields.Char(string="NavBar Text Color", default="#FFFFFF")
    nav_background_color = fields.Char(string="Navbar Color", default="#FFFFFF")
    button_hover_color = fields.Char(string="Hover color", default="#FFFFFF")
    background_color = fields.Char(string="Backgroun color", default="#FFFFFF")
    pe_background_image = fields.Binary(string="Background Image(PE)", default=False, attachment=True)
    
