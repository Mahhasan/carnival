# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventStallsInformation(models.Model):
    _name = 'event.stalls.information'
    _description = 'Event Stalls Information'

    event_id = fields.Many2one('event', string="Event")
    name = fields.Char(string="Name")
    exhibitor = fields.Char(string="Exhibitor")
    generate_code = fields.Char(string="Generate Code")
    stall_logo = fields.Binary(string="Stall Logo", help="Select image here")
    stall_view_live = fields.Char(string="Stall View Live")
    stall_category = fields.Char(string="Stall Category")
    company_website = fields.Char(string="Company Website")
    facebook = fields.Char(string="Facebook")
    youtube = fields.Char(string="Youtube")
    stall_type = fields.Char(string="Stall Type")
    stall_color = fields.Char(string="Stall Color")
    video_link = fields.Char(string="Video Link")
    chatbot_channel = fields.Char(string="ChatBot Channel")
    position = fields.Char(string="Position")
    number_of_counselor = fields.Char(string="Number of Counselor")
    main_banner = fields.Binary(string="Main Banner", help="Select image here")
    counselor_code = fields.Char(string="Counselor Code")
    exe_banner_1 = fields.Binary(string="Exe Banner 1", help="Select image here")
    exe_banner_2 = fields.Binary(string="Exe Banner 2", help="Select image here")
    left_banner = fields.Binary(string="Left Banner", help="Select image here")
    right_banner = fields.Binary(string="Right Banner", help="Select image here")

    stall_document_information_ids = fields.One2many('stall.document.information', 'event_stalls_information_id',
                                                     string="Document Information")
    stall_video_information_ids = fields.One2many('stall.video.information', 'event_stalls_information_id',
                                                  string="Video Information")
    stall_gallery_information_ids = fields.One2many('stall.gallery.information', 'event_stalls_information_id',
                                                    string="Gallery Information")
    stall_counselor_information_ids = fields.One2many('stall.counselor.information', 'event_stalls_information_id',
                                                      string="Counselor Information")
    stall_rubrics_ids = fields.One2many('stall.rubrics', 'event_stalls_information_id', string="Rubrics")