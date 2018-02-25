# -*- coding: utf-8 -*-

from odoo import models,fields    

class Team(models.Model):
    _name = 'softonic.team'
    name = fields.Char(string='name', required=True,
                           help='Name of the team')
    hours = fields.Float(digits=(6, 2), required=False,
                         help='Assigned hours...')
