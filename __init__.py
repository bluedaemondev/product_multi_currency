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
import psycopg2
from . import models  # noqa

def pre_init_hook(cr):
    """Restore backup of hr_retention_personal_deduction table."""
    try:
        cr.execute(
            """
            ALTER TABLE product_product
            ADD pricelist_id INTEGER REFERENCES product_pricelist(id),
            ADD currency_id INTEGER REFERENCES res_currency(id);
            ALTER TABLE product_template
            ADD currency_id INTEGER REFERENCES res_currency(id);
            """
        )
    except psycopg2.ProgrammingError:
        cr.rollback()

    try:
        cr.execute(
            """
            UPDATE product_product
            SET pricelist_id = pricelist.id,
                currency_id = pricelist.currency_id
            FROM product_template AS ptemplate
            JOIN product_pricelist AS pricelist ON ptemplate.currency_id = pricelist.currency_id
            WHERE product_product.product_tmpl_id = ptemplate.id
            """
        )
    except psycopg2.ProgrammingError:
        cr.rollback()

    return True

