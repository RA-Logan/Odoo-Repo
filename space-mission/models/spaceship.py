# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    _name = 'spacemission.spaceship'
    _description = 'Spaceship'

    name = fields.Char(string='Ship ID', required=True)
    description = fields.Text(string='Mission')

    dry_weight = fields.Float(string='Dry Weight')
    fuel_capacity = fields.Float(string='Fuel Capacity')
    crew_capacity = fields.Integer(string='Crew Capacity')

    build_status = fields.Selection(string='Build Status',
                                    selection=[('slated', 'Slated'),
                                            ('allocated', 'Allocated'),
                                            ('underway', 'Underway'),
                                            ('complete', 'Complete')],
                                    copy=False)

    active = fields.Boolean(string='Active', default=True)
