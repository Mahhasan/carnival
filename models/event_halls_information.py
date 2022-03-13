# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventHallsInformation(models.Model):
    _name = 'event.halls.information'
    _description = 'Event Halls Information'

    event_id = fields.Many2one('event', string="Event")
    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    live_link = fields.Char(string="Live Link")
    main_banner = fields.Binary(string="Main Banner", help="Select image here")
