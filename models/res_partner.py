from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string='Is Instructor')
    teaching_skill = fields.Selection(
        [
            ('python', 'Python'),
            ('odoo', 'Odoo'),
            ('excel', 'Excel'),
            ('math', 'Math'),
        ],
        string='Teaching Skill'
    )
