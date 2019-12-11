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

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    company_id = fields.Many2one(
                                'res.company',
                                copy=True,
                                default=None,
                                store=True,
                                index=True,
                                readonly=False,
                                selectable=True,
                                ondelete='set null'
                                )

class ProductProduct(models.Model):
    _inherit = 'product.product'

    company_id = fields.Many2one(
                                'res.company',
                                copy=True,
                                related='product_tmpl_id.company_id',
                                default=None,
                                store=False,
                                readonly=False,
                                selectable=True,
                                ondelete='set null'
                                )