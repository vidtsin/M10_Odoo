# -*- coding: utf-8 -*-
from openerp import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    user_assigned = fields.Many2one('res.users', string="User Assigned", default=lambda s: s.env.user)

    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True
