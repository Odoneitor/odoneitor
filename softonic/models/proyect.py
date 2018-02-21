# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Proyect(models.Model):
    _name = 'softonic.proyect'
    name  = fields.Char(string='Name', required=True, help='Name of the proyect...')
    # Un proyecto lleva una referencia a su cliente
    #client_id = fields.Many2one('softonic.client',
    #    ondelete='set null', string="Client", index=True)
    # Un proyecto involucra varios lenguajes de programación
    #langs_ids = fields.Many2many('softonic.language', string="Technologies used")
    # Relación con la tabla intermedia -> una lista de sus colaboraciones
    #relatedTeams_ids = fields.one2Many(
    #    'softonic.team', 'proyect_id', string="Collaborations"
    #)