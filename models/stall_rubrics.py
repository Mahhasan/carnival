# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StallRubrics(models.Model):
    _name = 'stall.rubrics'
    _description = 'Stall Rubrics'

    event_id = fields.Many2one('event', string="Event")
    event_stalls_information_id = fields.Many2one('event.stalls.information', string="Stall")
    rubrics_category = fields.Char(string="Rubrics Category")
    marks = fields.Char(string="Marks")

