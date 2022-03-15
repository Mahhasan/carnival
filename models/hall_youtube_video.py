# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HallYoutubeVideo(models.Model):
    _name = 'hall.youtube.video'
    _description = 'Hall Youtube Video'

    event_halls_information_id = fields.Many2one('event.halls.information', string="Youtube Video")
    name = fields.Char(string="Name")
    youtube_link = fields.Char(string="Youtube Link")


