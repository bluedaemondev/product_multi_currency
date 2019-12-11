##############################################################################
#
#    Copyright (C) 2014-TODAY Eynes (<http://www.e-mips.com.ar>)
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import psycopg2


def _update_new_currency_for_product_pricelist(cr):
    # update new columns from product_pricelist
    try:
        cr.execute(
            """
            UPDATE product_product
            SET pricelist_id = pricelist.id, currecy_id = pricelist.currency_id
            FROM product_template AS ptemplate
            JOIN product_pricelist AS pricelist ON ptemplate.currency_id = pricelist.currency_id
            WHERE product_product.product_tmpl_id = ptemplate.id
            """
        )
    except psycopg2.ProgrammingError:
        cr.rollback()

    return True


def migrate(cr, installed_version):
    return _update_new_currency_for_product_pricelist(cr)
