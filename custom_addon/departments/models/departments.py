# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Departments(models.Model):
    _name = "departments"
    _description = "Departments"
    _inherit = ['mail.thread']
    _order = "name"

    name = fields.Char('Department Name', required=True)
    active = fields.Boolean('Active', default=True)
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)


