# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class softonic(models.Model):
#     _name = 'softonic.softonic'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Language(models.Model):
    _name = 'softonic.language'
    name  = fields.Char(string='Name', required=True, help='Name of the language...')
    type  = fields.Char(string='Type', required=False, help='Additional info')
    # Un lenguaje de programación se usa en varios proyectos
    # proyects_ids = fields.Many2many('softonic.proyect', string="Proyects")
    # Un lenguaje es conocido por varios programadores
    # coders_ids = fields.Many2many('softonic.coder', string="Associated Pr0s")