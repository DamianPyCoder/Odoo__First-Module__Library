# -*- coding: utf-8 -*-

from odoo import models, fields
class Book(models.Model):
    _name = "library.book" 		
    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    editorial = fields.Char(string="Editorial")
    isbn = fields.Integer(string="ISBN")
    year = fields.Integer(string="Year")
    category = fields.Selection(
        [('classics','Classics'),('crime','Crime'),('fantasy','Fantasy')]
    )
    pages= fields.Integer(string="Pages")
    # bestseller = fields.Boolean(default=False)


