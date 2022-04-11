# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from io import BytesIO
import logging
import base64, zipfile, os


MAX_IMAGE_SIZE = 100 * 1920 * 1024  # in megabytes

_logger = logging.getLogger(__name__)

class ProductImportImageWizard(models.TransientModel):
    _name = 'product.import.image.wizard'
    _description = 'Import of zip image file'

    zipped = fields.Binary(string='Zip File', required=True)

    def import_image(self):
        self.ensure_one()
        zip = base64.decodestring(self.zipped)
        # saving zip content into memory
        zip_content = BytesIO()
        zip_content.write(zip)

        if not zip_content:
            raise Exception(_('No file sent.'))
        if not zipfile.is_zipfile(zip_content):
            raise UserError(_('Only zip files are supported.'))

        with zipfile.ZipFile(zip_content, "r") as files:
            for file in files.filelist:
                if file.file_size > MAX_IMAGE_SIZE:
                    raise UserError(_("File '%s' exceed maximum allowed file size") % file.filename)
                    
                (name, extension) = os.path.splitext(file.filename)
                if not name.isdigit():
                    product_ids = self.env['product.product'].search(['|','|',('name', '=', name), ('barcode', '=', name), ('default_code','=', name)])
                    if product_ids:
                        product_id = product_ids
                        data = files.read(file.filename)
                        product_id.image_1920 = base64.b64encode(data)
                    else:
                        raise UserError(_('No product found with the name,barcode,id corresponding to %s' % file.filename))
                else:
                    product_ids = self.env['product.product'].search(['|','|',('id', '=', name), ('barcode', '=', name), ('default_code','=', name)])
                    if product_ids:
                        product_id = product_ids
                        data = files.read(file.filename)
                        product_id.image_1920 = base64.b64encode(data)
                    else:
                        raise UserError(_('No product found with the name,barcode,id corresponding to %s' % file.filename))
