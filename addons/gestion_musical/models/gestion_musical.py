# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

# DEFINIMOS LOS OBJETOS "DISCO", "AUTORES", "CANCIONES"

class Author(models.Model):
    _name = 'author'

    name = fields.Char(string="Nombre", required=True)
    birthday = fields.Date(string="Fecha nacimiento")
    age = fields.Integer(string="Edad")


class Disc(models.Model):
    _name = 'disc'

    name = fields.Char(string="Título", required=True)
    published_date = fields.Date(string="Fecha publicación")
    author_id = fields.Many2one(comodel_name="author", string="Autor del disco")
    song_ids = fields.Many2many(comodel_name='song',
					relation='disc_song_rel',
					column1='disc_id',
					column2='song_id')

class Song(models.Model):
    _name = 'song'

    name = fields.Char(string="Nombre de la cancion", required=True)
    duracion = fields.Integer(string="duración de la canción")
    author_id = fields.Many2one(comodel_name="author", string="Autor de la cancion")
    disc_ids = fields.Many2many(comodel_name='disc',
                                        relation='disc_song_rel',
                                        column1='song_id',
                                        column2='disc_id')
