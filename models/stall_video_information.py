# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StallVideoInformation(models.Model):
    _name = 'stall.video.information'
    _description = 'Stall Video Information'

    event_id = fields.Many2one('event', string="Event")
    event_stalls_information_id = fields.Many2one('event.stalls.information', string="Stall")
    name = fields.Char(string="Name")
    file = fields.Binary(string="File")


