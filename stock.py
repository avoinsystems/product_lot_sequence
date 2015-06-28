# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Avoin Systems (http://avoin.systems).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
__author__ = 'miku'

# -*- coding: utf-8 -*-
from openerp import models, api


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    # noinspection PyAttributeOutsideInit
    @api.onchange('product_id')
    def get_next_lot(self):
        if not self.product_id:
            self.name = False

        sequence_obj = self.env['ir.sequence']
        if self.product_id.categ_id and self.product_id.categ_id.lot_sequence:
            # If the product category has a sequence, use it to get the next lot number
            self.name = sequence_obj.next_by_id(self.product_id.categ_id.lot_sequence.id)
        else:
            # If the product category doesn't have a sequence, use the default lot numbering scheme
            self.name = sequence_obj.next_by_id(self.env.ref('stock.sequence_production_lots').id)

    def default_get(self, cr, uid, fields_list, context=None):
        if 'name' in fields_list:
            # Don't set the default value for `name`. It will be set in the onchange method above.
            fields_list.remove('name')

        return super(StockProductionLot, self).default_get(cr, uid, fields_list, context)