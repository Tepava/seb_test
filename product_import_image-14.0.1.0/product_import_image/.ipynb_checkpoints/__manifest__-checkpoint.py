# -*- coding: utf-8 -*-
{
    "name": "Image import (PE)",
    "summary": "Add import zipped image option on product",
    "version": "0.1",
    "category": "Pacific-ERP",
    "author": "Mehdi Tepava",
    'website': "https://www.pacific-erp.com/",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["stock"],
    "data": [
        'security/ir.model.access.csv',
        'views/product_import_image_wizard_view.xml',
        ],
}