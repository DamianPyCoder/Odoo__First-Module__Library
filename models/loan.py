# -*- coding: utf-8 -*-

from odoo import models, fields
class Loan(models.Model):
    _name = "library.loan" 		
    name = fields.Char(string="Name", required=True)
    loan_date = fields.Datetime(string='Loan Date', required=True)
    return_date = fields.Datetime(string='Return Date')
    book_id = fields.Char(string='Book ID', required=True)
    member_id = fields.Char(string='Member ID', required=True)