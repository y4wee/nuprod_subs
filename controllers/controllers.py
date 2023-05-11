# -*- coding: utf-8 -*-
# from odoo import http


# class NuprodSubs(http.Controller):
#     @http.route('/nuprod_subs/nuprod_subs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nuprod_subs/nuprod_subs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nuprod_subs.listing', {
#             'root': '/nuprod_subs/nuprod_subs',
#             'objects': http.request.env['nuprod_subs.nuprod_subs'].search([]),
#         })

#     @http.route('/nuprod_subs/nuprod_subs/objects/<model("nuprod_subs.nuprod_subs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nuprod_subs.object', {
#             'object': obj
#         })
