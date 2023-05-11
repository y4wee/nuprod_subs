# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nuprod_subs(models.Model):
    _inehrit = 'sale.subscription'

    _description = 'nuprod_subs.nuprod_subs'

    name = fields.Char()

    @api.onchange("date_start", "date", "recurring_next_date")
    def _onchange_date_start(self):
        print(self.date_start)
