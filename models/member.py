# -*- coding: utf-8 -*-

from odoo import models, fields
class Loan(models.Model):
    _name = "library.member" 		
    name = fields.Char(string="Name", required=True)
    loan_date = fields.Char(string="Email")
