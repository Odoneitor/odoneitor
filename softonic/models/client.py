# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Client(models.Model):
    _name = 'softonic.client'
    name  = fields.Char(string='Name', required=True, help='Name of the client...')
    # Un cliente contiene una lista de sus proyectos
    #relatedProyects_ids = fields.one2Many(
    #   'softonic.proyect', 'client_id', string="Associated proyects"
    #)    
