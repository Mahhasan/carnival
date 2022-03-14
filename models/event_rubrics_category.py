# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventRubricsCategory(models.Model):
    _name = 'event.rubrics.category'
    _description = 'Event Rubrics Category'

    event_id = fields.Many2one('event', string="Event")
    name = fields.Char(string="Name")
    marking_out_of = fields.Char(string="Marking Out of")
