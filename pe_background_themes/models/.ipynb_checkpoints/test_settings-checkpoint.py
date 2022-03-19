from odoo import models, fields, api

class BackgroundThemesSettings(models.TransientModel):
     _inherit = 'res.config.settings'
     nav_font_color = fields.Char(string="NavBar Text")
     nav_background_color = fields.Char(string="Navbar Background")
     background_color = fields.Char(string="Menu Background")
     company = fields.Many2one('res.company', string='Société')