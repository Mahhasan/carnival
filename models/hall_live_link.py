# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HallLiveLink(models.Model):
    _name = 'hall.live.link'
    _description = 'Hall Live Link'

    event_halls_information_id = fields.Many2one('event.halls.information', string="Live Link")
    name = fields.Char(string="Name")
    live_link = fields.Char(string="Live Link")


