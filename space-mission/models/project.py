from odoo import fields, models, api

class Project(models.Model):
    _inherit = 'project.project'

    mission_id = fields.Many2one(comodel_name='spacemission.mission', string='Related Mission', ondelete='cascade')
