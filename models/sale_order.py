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
import pdb

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'sale.order'

    @api.onchange('order_line')
    def _compute_new_total_on_company_currency(self):
        
        company_curr = self.company_id.currency_id

        for so in self:
            for soli in so.order_line:
                pdb.set_trace()
                if soli.product_id.currency_id.id != company_curr.id and\
                    soli.product_id.currency_id:
                    rate = soli.product_id.currency_id.rate
                    _logger.info('Ratio de = %s',rate)
                    list_price_rated = rate * soli.product_id.list_price
                    list_price_rated = company_curr.round(list_price_rated)
                    soli.price_unit = list_price_rated
                else:
                    _logger.info('order line %s has no currency, or price actualization has been already done.',soli.name)

