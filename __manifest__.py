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

{
    'name': "Multi currency for product_product",
    'version': '11.0.1.0.2',
    'category': 'Products',
    'description': "Product related customizations for Macro.",
    'author': 'Eynes - Ingenieria del software',
    'website': 'http://www.eynes.com.ar',
    'license': 'AGPL-3',
    "depends": [
        'purchase','product','point_of_sale','web'
    ],
    "data": [
        'views/product_views.xml',
        'views/templates.xml',
    ],
    "installable": True,
    "pre_init_hook": "pre_init_hook"
}
