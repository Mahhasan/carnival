# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HallGallery(models.Model):
    _name = 'hall.gallery'
    _description = 'Hall Gallery'

    event_halls_information_id = fields.Many2one('event.halls.information', string="Youtube Video")
    name = fields.Char(string="Name")
    image = fields.Binary(string="Image")


