# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StallGalleryInformation(models.Model):
    _name = 'stall.gallery.information'
    _description = 'Stall Gallery Information'

    # event_id = fields.Many2one('event', string="Event")
    event_stalls_information_id = fields.Many2one('event.stalls.information', string="Stall")
    name = fields.Char(string="Name")
    file = fields.Binary(string="File")


