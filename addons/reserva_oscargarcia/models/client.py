# -*- coding: utf-8 -*-
from openerp import models, fields


class Client(models.Model):
    _name = 'client'

    name = fields.Char('Name', required=True)
    dni = fields.Char('DNI', required=True)
    age = fields.Integer('Age')
    birth_date = fields.Date("Birth date")
    rooms = fields.Many2many(comodel_name='room',
                             relation='clients_rooms',
                             column1='client_id',
                             column2='room_id',
                             string='Rooms')
