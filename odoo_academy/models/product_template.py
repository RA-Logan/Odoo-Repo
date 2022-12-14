from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_session_product = fields.Boolean(string='Use as Session Product', help='Check box if session product.', default=False)
