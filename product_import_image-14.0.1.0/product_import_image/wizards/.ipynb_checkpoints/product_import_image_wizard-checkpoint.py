# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning, UserError
import odoo.addons.decimal_precision as dp
import base64, zipfile, os
import logging
from io import BytesIO
from odoo.tools.osutil import tempdir

MAX_FILE_SIZE = 100 * 1024 * 1024  # in megabytes

_logger = logging.getLogger(__name__)

class ProductImportImageWizard(models.TransientModel):
    _name = 'product.import.image.wizard'
    _description = u'Product Import Image'

    file = fields.Binary(u'Zip File', required=True)

    def button_import(self):
        self.ensure_one()
        zip_data = base64.decodestring(self.file)
        fp = BytesIO()
        fp.write(zip_data)

        if not fp:
            raise Exception(_("No file sent."))
        if not zipfile.is_zipfile(fp):
            raise UserError(_('Only zip files are supported.'))

        with zipfile.ZipFile(fp, "r") as z:
            for zf in z.filelist:
                if zf.file_size > MAX_FILE_SIZE:
                    raise UserError(_("File '%s' exceed maximum allowed file size") % zf.filename)
                    
                _logger.error(os.path.splitext(zf.filename))
                (name, extension) = os.path.splitext(zf.filename)
                _logger.error('name : %s & extension : %s' %(name,extension))
                product_ids = self.env['product.product'].search(['|','|',('default_code', '=', name), ('barcode', '=', name), ('id','=', name)])
                _logger.error(product_ids)
                if product_ids:
                    product_id = product_ids
                    _logger.error(product_id)
                    data = z.read(zf.filename)
                    product_id.image_1920 = base64.b64encode(data)
