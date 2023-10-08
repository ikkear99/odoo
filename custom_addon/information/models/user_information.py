# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class UserInformation(models.Model):
    _name = 'user.information'
    _description = 'User Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "full_name"

    user_id = fields.Many2one(
        'res.users',
        string='User',
        default=lambda self: self.env.context.get('user_id', self.env.user.id),
        index=True,
    )
    full_name = fields.Char(string='Full Name',required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex",required=True)
    image = fields.Binary(string="Image")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    department_id = fields.Many2one('departments',string='Departments')
    id_number = fields.Char(string='ID Number')
    institution = fields.Char(string='Institution')
    address = fields.Char(string='Add')
    account_number = fields.Char(string='Account Number')
    openned_at = fields.Char(string='Oppenned At')
    bank = fields.Char(string='Bank Brank')

    def user_information_action(self):
        user_id = self.env['user.information'].search([('user_id', '=', self._uid)])

        action = {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "user.information",
        }
        if user_id :
            action['res_id'] = user_id.id
            
        return  action  


