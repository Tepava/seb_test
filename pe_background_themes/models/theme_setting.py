# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Settings(models.Model):
     _name = 'theme.setting'
     _description = 'Configuration du themes'
     nav_font_color = fields.Char(string="Couleur navigation texte")
     nav_background_color = fields.Char(string="Couleur barre de navigation")
     background_color = fields.Char(string="Couleur du menu")
#     company = fields.Many2one(comodel_name='res.company',related='id')

