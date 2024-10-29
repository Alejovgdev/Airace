# -*- coding: utf-8 -*-
# from odoo import http


# class Airace(http.Controller):
#     @http.route('/airace/airace', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/airace/airace/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('airace.listing', {
#             'root': '/airace/airace',
#             'objects': http.request.env['airace.airace'].search([]),
#         })

#     @http.route('/airace/airace/objects/<model("airace.airace"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('airace.object', {
#             'object': obj
#         })

