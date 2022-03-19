# -*- coding: utf-8 -*-
# from odoo import http


# class BackgroundThemes(http.Controller):
#     @http.route('/background_themes/background_themes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/background_themes/background_themes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('background_themes.listing', {
#             'root': '/background_themes/background_themes',
#             'objects': http.request.env['background_themes.background_themes'].search([]),
#         })

#     @http.route('/background_themes/background_themes/objects/<model("background_themes.background_themes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('background_themes.object', {
#             'object': obj
#         })
