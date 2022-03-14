# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventJudgeInformation(models.Model):
    _name = 'event.judge.information'
    _description = 'Event Judge Information'

    event_id = fields.Many2one('event', string="Event")
    name = fields.Char(string="Name")
    login = fields.Char(string="Login")
    password = fields.Char(string="Password")
    phone = fields.Char(string="Phone")
    user_type = fields.Char(string="User Type")
    groups = fields.Char(string="Groups")
    time_zone = fields.Char(string="Time Zone")
