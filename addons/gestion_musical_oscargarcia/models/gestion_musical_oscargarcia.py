# -*- coding: utf-8 -*-
from openerp import models, fields


class AuthorExtension(models.Model):
    _inherit = 'author'

    lugar_nacimiento = fields.Char("Lugar de nacimiento")


class DiscExtension(models.Model):
    _inherit = 'disc'

    def _get_selection(self):
        return [
            ("rock", "Rock"),
            ("pop", "Pop"),
            ("pop_rock", "Pop-rock"),
            ("heavy", "Heavy")
        ]

    genero = fields.Selection(_get_selection, String="Genero")


class Gira(models.Model):
    _name = "gira"

    date = fields.Date(string="Fecha")
    author = fields.Many2one("author", string="Author")
    discs = fields.Many2many(comodel_name='disc',
                             relation='gira_discs',
                             column1='gira_id',
                             column2='disc_id',
                             string="Discos")

    top_songs = fields.Many2many(comodel_name='song',
                                 relation='top_songs',
                                 column1='gira_id',
                                 column2='song_id',
                                 string='Top Songs')

    cities = fields.Char(string="Ciudades")
