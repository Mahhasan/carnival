# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventOrganizerInformation(models.Model):
    _name = 'event.organizer.information'
    _description = 'Event Organizer Information'

    event_id = fields.Many2one('event', string="Event")
    name = fields.Char(string="Name")
    login = fields.Char(string="Login")
    password = fields.Char(string="Password")
    phone = fields.Char(string="Phone")
    user_type = fields.Char(string="User Type")
    groups = fields.Char(string="Groups")
    time_zone = fields.Char(string="Time Zone")