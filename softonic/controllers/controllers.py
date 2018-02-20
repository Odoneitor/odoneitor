# -*- coding: utf-8 -*-
from odoo import http

# class Softonic(http.Controller):
#     @http.route('/softonic/softonic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/softonic/softonic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('softonic.listing', {
#             'root': '/softonic/softonic',
#             'objects': http.request.env['softonic.softonic'].search([]),
#         })

#     @http.route('/softonic/softonic/objects/<model("softonic.softonic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('softonic.object', {
#             'object': obj
#         })