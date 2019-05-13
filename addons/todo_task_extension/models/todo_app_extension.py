# -*- coding: utf-8 -*-
from openerp import models, fields, api


class TodoTaskExtension(models.Model):
    _inherit = "todo.task"

    deadline = fields.Date("Deadline")
