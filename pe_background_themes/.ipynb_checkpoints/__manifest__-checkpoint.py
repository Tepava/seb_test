# -*- coding: utf-8 -*-
{
    'name': "Séléction de themes",

    'summary': """
        Personalisation du theme de Odoo""",

    'description': """
        Pour personalisez l'interface Odoo que ce soit la couleur du background, la police du menu de navigation
    """,

    'author': "Pacific-ERP",
    'website': "https://www.pacific-erp.com/",
    'images' : ['static/description/icon.png'],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/settings.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
