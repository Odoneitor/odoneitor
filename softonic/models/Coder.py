class Coder(models.Model):
    _name    = 'softonic.coder'
    name     = fields.Char(string='Name', required=True, help='Name of the coder...')
    lastname = fields.Char(string='Last Name', required=True, help='Last Name of the proyect...')
    birthDate = fields.Date(string='Date of Birth', required=True)
    joinDate  = fields.Date(string='Hiring date', required=True)
    
    """
    # Un programador conoce varios lenguajes de programación
    langs_ids = fields.Many2many('softonic.language', string="Known Programming Languages")
    # Relación con la tabla intermedia -> una lista de sus colaboraciones
    relatedTeams_ids = fields.one2Many(
        'softonic.team', 'coder_id', string="Collaborations"
    )
    """