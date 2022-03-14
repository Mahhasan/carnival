# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventAdsInformation(models.Model):
    _name = 'event.ads.information'
    _description = 'Event Ads Information'

    event_id = fields.Many2one('event', string="Event")
    name = fields.Char(string="Name")
    main_banner = fields.Binary(string="Main Banner", help="Select image here")


