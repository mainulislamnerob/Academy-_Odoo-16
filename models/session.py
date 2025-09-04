from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = "academy.session"
    _description = "Course Session"

    name = fields.Char(required=True)
    course_id = fields.Many2one("academy.course", required=True, ondelete="cascade")
    instructor_id = fields.Many2one(
        "res.partner", string="Instructor",
        domain="[('is_instructor','=',True), ('is_company','=',False)]"
    )
    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(help="Duration in days")
    seats = fields.Integer(default=10)
    attendee_ids = fields.Many2many("res.partner", string="Attendees")
    taken_seats = fields.Float(compute="_compute_taken_seats", store=True)
    active = fields.Boolean(default=True)

    @api.depends("seats", "attendee_ids")
    def _compute_taken_seats(self):
        for rec in self:
            rec.taken_seats = (100.0 * len(rec.attendee_ids) / rec.seats) if rec.seats else 0.0

    @api.constrains("seats", "attendee_ids")
    def _check_seats(self):
        for rec in self:
            if rec.seats < 0:
                raise ValidationError("Seats cannot be negative.")
            if rec.seats and len(rec.attendee_ids) > rec.seats:
                raise ValidationError("Too many attendees for the available seats.")

    @api.onchange("seats", "attendee_ids")
    def _onchange_seats(self):
        if self.seats is not None and self.seats < 0:
            return {'warning': {'title': 'Incorrect seats', 'message': 'Seats cannot be negative.'}}
        if self.seats and len(self.attendee_ids) > self.seats:
            return {'warning': {'title': 'Too many attendees', 'message': 'Reduce attendees or increase seats.'}}
