# Academy (Odoo 16)

Small training app covering:
- Custom models: academy.course, academy.session
- Fields: Char, Text, Selection (level), Many2one, One2many, Many2many, Boolean, computed Float
- Model inherit: res.partner -> is_instructor
- Views: tree, form, calendar, graph
- Decorators: @api.depends, @api.onchange, @api.constrains
- ORM usage & PDF report

Paths:
- models: academy/models/{course.py,session.py,partner.py}
- views:  academy/views/{course_views.xml,session_views.xml,academy_menu.xml}
- report: academy/report/{report.xml,report_templates.xml}
- access: academy/security/ir.model.access.csv
- manifest: academy/__manifest__.py

How to test:
1) Contacts → mark a few as **Is Instructor**.
2) Academy → Courses → create courses (set **Level**).
3) Academy → Sessions → create sessions; set **Instructor**, add **Attendees**.
   - Negative seats → error
   - Instructor in attendees → error
   - Attendees > seats → warning
4) Sessions → Graph view works.
5) Session → **Print → Session Sheet**.
