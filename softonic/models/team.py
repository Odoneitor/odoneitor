# -*- coding: utf-8 -*-

from odoo import models, fields, api  

class Team(models.Model):
    _name     = 'softonic.team'
    position  = fields.Char(string='Position', required=True, help='Programmer\'s position inside of the team...')
    hours     = fields.Float(digits=(6,2), required=False, help='Assigned hours...')
    # En el equipo debe haber una referencia al programador
    #coder_id = fields.Many2one('softonic.coder',
    #    ondelete='set null', string="Coder", index=True)
    # En el equipo debe haber una referencia al proyecto
    #proyect_id = fields.Many2one('softonic.proyect',
    #    ondelete='set null', string="Proyect", index=True)