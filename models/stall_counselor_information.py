# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StallCounselorInformation(models.Model):
    _name = 'stall.counselor.information'
    _description = 'Stall Counselor Information'

    event_id = fields.Many2one('event', string="Event")
    event_stalls_information_id = fields.Many2one('event.stalls.information', string="Stall")
    name = fields.Char(string="Name")
    login = fields.Char(string="Login")
    password = fields.Char(string="Password")
    user_type = fields.Char(string="User Type")
    phone = fields.Char(string="Phone")
    counselor_code = fields.Char(string="Counselor Code")
    groups = fields.Char(string="Groups")
    time_zone = fields.Char(string="Time Zone")


