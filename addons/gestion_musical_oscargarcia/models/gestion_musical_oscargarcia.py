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

    date = fields.Date(String="Fecha")
    author = fields.Many2one("author", "Author")
    discs = fields.Many2many("disc", "Disc")
    top_songs = fields.Many2many("song", "Top_songd")
    cities = fields.Char(String="Cities")
