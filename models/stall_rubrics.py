# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StallCounselorInformation(models.Model):
    _name = 'stall.counselor.information'
    _description = 'Stall Counselor Information'

    event_stalls_information_id = fields.Many2one('event.stalls.information', string="Stall")
    rubrics_category = fields.Char(string="Rubrics Category")
    marks = fields.Binary(string="Marks")


