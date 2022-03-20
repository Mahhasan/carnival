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

    @http.route('/carnival/get/stall_list', auth='public', type='http', csrf=False, methods=['GET'], cors='*')
    def stall_list(self, **kwarg):
        result = []
        stalls = request.env['event'].sudo().search([])
        for line_event_stalls_information in stalls:
            data = {
                "name": line_event_stalls_information.name,
                "organizers": line_event_stalls_information.position,
            }
            result.append(data)
        json_stall_data = dumps(result, default=date_utils.json_default)
        return Response(json_stall_data, headers={'content_type': 'application/json'}, status=200)



