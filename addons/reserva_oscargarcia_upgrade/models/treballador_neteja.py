# -*- coding: utf-8 -*-
from openerp import models, fields


class TreballadorNeteja(models.Model):
    _name = 'treballador.neteja'

    name = fields.Char('Name', required=True)
    dni = fields.Char('DNI', required=True)
    birth_date = fields.Date("Birth date")
    rooms = fields.Many2one(comodel_name="room", string="Rooms")
    clients = fields.Many2one(comodel_name="client", string="Clients")
