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

    hall_youtube_video_ids = fields.One2many('hall.youtube.video', 'event_halls_information_id', string="Youtube Video")
    hall_gallery_ids = fields.One2many('hall.gallery', 'event_halls_information_id', string="Gallery")
    hall_live_link_ids = fields.One2many('hall.live.link', 'event_halls_information_id', string="Live Link")