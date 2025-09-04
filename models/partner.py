from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"
    is_instructor = fields.Boolean(string="Is Instructor", help="Can teach sessions")
