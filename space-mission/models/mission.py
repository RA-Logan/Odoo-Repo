from odoo import models, fields, api

class Mission(models.Model):
    _name = 'spacemission.mission'
    _description = 'Mission'

    name = fields.Char(string='Mission Name', required=True)
    objective = fields.Text(string='Mission Brief')

    ship_id = fields.Many2one(comodel_name='spacemission.spaceship',
                                string='Spaceship',
                                ondelete='cascade',
                                required=True)

    launch_date = fields.Date(name='Launch Date')
    return_date = fields.Date(name='Return Date')

    ship_name = fields.Char(related="ship_id.name", string="Ship Name")
    ship_capacity = fields.Integer(related='ship_id.crew_capacity', string='Crew Capacity')
    ship_contractors = fields.Many2many(related='ship_id.contractor_ids', string='Ship Contractors')
    crew_ids = fields.Many2many(comodel_name='res.partner', string='Crew')

    fuel_required = fields.Float(string='Fuel Required')
    staff_size = fields.Integer(string='Staff Required')

    project_ids = fields.One2many(comodel_name='project.project', string='Related Projects')

    active = fields.Boolean(string='Active', default=True)
