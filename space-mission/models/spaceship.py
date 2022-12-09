# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Spaceship(models.Model):
    _name = 'spacemission.spaceship'
    _description = 'Spaceship'

    name = fields.Char(string='Ship ID', required=True)
    description = fields.Text(string='Mission')

    dry_weight = fields.Float(string='Dry Weight')
    fuel_capacity = fields.Float(string='Fuel Capacity')
    crew_capacity = fields.Integer(string='Crew Capacity')
    height = fields.Float(string="Height", default=0.0)
    width = fields.Float(string="Width", default=0.0)
    depth = fields.Float(string="Depth", default=0.0)

    build_status = fields.Selection(string='Build Status',
                                    selection=[('slated', 'Slated'),
                                            ('allocated', 'Allocated'),
                                            ('underway', 'Underway'),
                                            ('complete', 'Complete')],
                                    copy=False)

    active = fields.Boolean(string='Active', default=True)

    @api.constrains("height", "width")
<<<<<<< Updated upstream
    def _check_ship_dimens(self):
        for record in self:
            if record.width > record.height:
                raise UserError('Width of ship cannot exceed height.')
=======
>>>>>>> Stashed changes
