# -*- coding: utf-8 -*-
# from odoo import http


# class Carnival(http.Controller):
#     @http.route('/carnival/carnival', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/carnival/carnival/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('carnival.listing', {
#             'root': '/carnival/carnival',
#             'objects': http.request.env['carnival.carnival'].search([]),
#         })

#     @http.route('/carnival/carnival/objects/<model("carnival.carnival"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('carnival.object', {
#             'object': obj
#         })
