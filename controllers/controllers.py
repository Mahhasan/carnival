# -*- coding: utf-8 -*-


from odoo import http
from odoo.http import request, Response
from json import dumps
from odoo.tools import date_utils


class Carnival(http.Controller):

    @http.route('/carnival/get/event_list', auth='public', type='http', csrf=False, methods=['GET'], cors='*')
    def event_list(self, **kwarg):
        result=[]
        events = request.env['event'].sudo().search([])
        for line_event in events:
            data = {
                "name":line_event.name,
                "organizers":line_event.organizers,
            }
            result.append(data)
        json_event_data = dumps(result, default=date_utils.json_default)
        return Response(json_event_data, headers={'content_type': 'application/json'}, status=200)

    @http.route('/carnival/get/stalls_list', auth='public', type='http', csrf=False, methods=['GET'], cors='*')
    def stalls_list(self, **kwarg):
        result = []
        stalls = request.env['event.stalls.information'].sudo().search([])
        for line_event_stalls_information in stalls:
            data = {
                "name": line_event_stalls_information.name,
                "exhibitor": line_event_stalls_information.exhibitor,
            }
            result.append(data)
        json_event_stalls_information_data = dumps(result, default=date_utils.json_default)
        return Response(json_event_stalls_information_data, headers={'content_type': 'application/json'}, status=200)

    @http.route('/carnival/get/halls_list', auth='public', type='http', csrf=False, methods=['GET'], cors='*')
    def halls_list(self, **kwarg):
        result = []
        halls = request.env['event.halls.information'].sudo().search([])
        for line_event_halls_information in halls:
            data = {
                "name": line_event_halls_information.name,
                "code": line_event_halls_information.code,
            }
            result.append(data)
        json_event_halls_information_data = dumps(result, default=date_utils.json_default)
        return Response(json_event_halls_information_data, headers={'content_type': 'application/json'}, status=200)

    @http.route('/carnival/get/halls_list', auth='public', type='http', csrf=False, methods=['GET'], cors='*')
    def halls_list(self, **kwarg):
        result = []
        halls  = request.env['event.halls.information'].sudo().search([])
        for line_event_halls_information in halls:
            data = {
                "name": line_event_halls_information.name,
                "code": line_event_halls_information.code,
            }
            result.append(data)
        json_event_halls_information_data = dumps(result, default=date_utils.json_default)
        return Response(json_event_halls_information_data, headers={'content_type': 'application/json'}, status=200)




