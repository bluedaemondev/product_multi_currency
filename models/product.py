##############################################################################
#
#    Copyright (C) 2019 Eynes - Ingenieria del software (www.eynes.com.ar)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, models, tools, api
import logging

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    currency_id = fields.Many2one('res.currency', readonly=False, related='product_tmpl_id.currency_id', required=True)

    @api.depends('currency_id')
    def _compute_pricelist_id(self):
        #ars_currency = self.env['res.currency'].search([('name','=','ARS')])
        for prod in self:
            prod.pricelist_id = prod.env['product.pricelist'].search([('currency_id','=',prod.currency_id.id)], limit=1)
            _logger.info('computed pricelist = %s for %s ',prod.pricelist_id.name,prod.name)
            
    pricelist_id = fields.Many2one('product.pricelist',compute='_compute_pricelist_id', store=True)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _default_ars_currency(self):
        return self.env['res.currency'].search([('name','=','ARS')], limit=1)

    currency_id = fields.Many2one('res.currency', readonly=False, default=_default_ars_currency, store=True)

