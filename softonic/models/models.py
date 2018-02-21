# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Language(models.Model):
    _name = 'softonic.language'
    name  = fields.Char(string='Name', required=True, help='Name of the language...')
    type  = fields.Char(string='Type', required=False, help='Additional info')
    # Un lenguaje de programación se usa en varios proyectos
    # proyects_ids = fields.Many2many('softonic.proyect', string="Proyects")
    # Un lenguaje es conocido por varios programadores
    # coders_ids = fields.Many2many('softonic.coder', string="Associated Pr0s")

class Client(models.Model):
    _name = 'softonic.client'
    name  = fields.Char(string='Name', required=True, help='Name of the client...')
    # Un cliente contiene una lista de sus proyectos
    #relatedProyects_ids = fields.one2Many(
    #   'softonic.proyect', 'client_id', string="Associated proyects"
    #)    

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