class Language(models.Model):
    _name = 'softonic.language'
    name  = fields.Char(string='Name', required=True, help='Name of the language...')
    type  = fields.Char(string='Type', required=False, help='Additional info')
    # Un lenguaje de programación se usa en varios proyectos
    # proyects_ids = fields.Many2many('softonic.proyect', string="Proyects")
    # Un lenguaje es conocido por varios programadores
    # coders_ids = fields.Many2many('softonic.coder', string="Associated Pr0s")