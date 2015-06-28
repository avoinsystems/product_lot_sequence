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
# noinspection PyStatementEffect
{
    "name": "Lot Sequence for Product Categories",
    "version": "1.0",
    "category": "Stock",
    "description": """
Lot Sequence for Product Categories
===================================

This module adds the ability to define which sequence should be used to generate the next lot number for
manufactured or received products. Currently the sequence can only be set at product category level.
    """,
    "author": "Avoin.Systems",
    "website": "http://avoin.systems",
    "depends": [
        "stock",
        "product"
    ],
    "data": [
        "views/product.xml"
    ],
    "installable": True,
    "auto_install": False,
    "active": False
}
