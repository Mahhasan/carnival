# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StallDocumentInformation(models.Model):
    _name = 'stall.document.information'
    _description = 'Stall Document Information'

    event_id = fields.Many2one('event', string="Event")
    event_stalls_information_id = fields.Many2one('event.stalls.information', string="Stall")
    name = fields.Char(string="Name")
    file = fields.Binary(string="File")


