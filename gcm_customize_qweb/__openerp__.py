# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2014-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################


{
    'name': 'GCM Customize QWEB Reports',
    'version': '1.0',
    'category': 'Report',
    'description' : """This Module help to print Customize QWEB Reports.""",
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    'depends': ['sale','stock','purchase','account'],
    'data': [
        'report_menu.xml',
        'report/gcm_proforma_layout.xml',
        'report/gcm_sale_layout.xml',
        'report/gcm_purchase_layout.xml',
        'report/gcm_deliver_layout.xml',
        'views/proforma_invoice.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'views/deliver_order.xml',
        ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
