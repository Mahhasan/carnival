# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
    _name = 'event'
    _description = 'Event Table'

    name = fields.Char(string="Name")
    main_banner = fields.Binary(string="Main Banner", help="Select image here")
    number_of_stall = fields.Char(string="Number of Stall")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    organizers = fields.Char(string="Organizers")
    version = fields.Char(string="Version")

    event_stalls_information_ids = fields.One2many('event.stalls.information', 'event_id', string="Stalls")
    event_halls_information_ids = fields.One2many('event.halls.information', 'event_id', string="Halls")