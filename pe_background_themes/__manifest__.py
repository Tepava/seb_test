# -*- coding: utf-8 -*-
{
    'name': "Séléction de themes",
    'summary': """Personalisation du theme de Odoo""",
    'description': """Pour personalisez l'interface Odoo que ce soit la couleur du background, la police du menu de navigation""",
    'author': "Mehdi TEPAVA",
    'website': "https://www.pacific-erp.com/",
    'images' : ['static/description/icon.png'],
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','web_studio','account','web'],
    'data': ['views/settings.xml'],
    'assets': {
        'web.assets_backend': [
            'pe_background_themes/static/src/background_theme.js',
            'pe_background_themes/static/src/custom_style.scss'
        ],
    },
    'license': 'LGPL-3',
}
