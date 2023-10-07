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
    full_name = fields.Char(string='Full Name', required=True, tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    sex = fields.Selection([('m', 'Male'),('f', 'Female')], string ="Sex",required=True)
    image = fields.Binary(string="Image")
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    department = fields.Char(string='Department')
    id_number = fields.Char(string='ID Number')
    institution = fields.Char(string='Institution')
    address = fields.Char(string='Add')
    # telephone = fields.Char(
    #     'TelePhone', tracking=50,
    #     compute='_compute_phone', inverse='_inverse_phone', readonly=False, store=True)
    # cellphone = fields.Integer(string='Cell Phone')
    # e_mail = fields.Char(string='E-Mail')
    # second_mail = fields.Char(string='Second-Mail')
    account_number = fields.Char(string='Account Number')
    openned_at = fields.Char(string='Oppenned At')
    bank = fields.Char(string='Bank Brank')


    @api.constrains('user_id')
    def _check_user_id(self):
        for record in self:
            # Define your domain logic here
            # For example, you can restrict records to only those with the same user_id as the current user
            if record.user_id != self.env.user:
                raise ValidationError(_("You can only create records for yourself."))