##############################################################################
#
#    Copyright (C) 2018-TODAY Eynes (<http://www.e-mips.com.ar>)
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


def alter_product_pricelist_and_currency(cr):
    """Restore backup of hr_retention_personal_deduction table."""

    try:
        cr.execute(
            """
            ALTER TABLE product_product
            ADD pricelist_id INTEGER REFERENCES product_pricelist(id) SET DEFAULT 1,
            ADD currency_id INTEGER REFERENCES res_currency(id) SET DEFAULT 20;
            """
        )
    except psycopg2.ProgrammingError:
        cr.rollback()

    return True


def migrate(cr, installed_version):
    return alter_product_pricelist_and_currency(cr)
