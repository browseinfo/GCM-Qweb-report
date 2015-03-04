# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today BrowseInfo (<http://www.browseinfo.in>).
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

import time
from openerp.osv import osv
from openerp.tools.translate import _
from openerp.report import report_sxw
from datetime import datetime
from openerp.modules.module import get_module_resource

class gcm_purchase_order(report_sxw.rml_parse):
    index = 0
    def __init__(self, cr, uid, name, context=None):
        super(gcm_purchase_order, self).__init__(cr, uid, name, context=context)
        self.init_bal_sum = 0.0
        self.localcontext.update({
            'time': time,
            'get_index': self._get_index,
            'get_total_qty': self._get_total_qty,
            'get_date': self._get_date,
            })
    
    def _get_index(self):
        self.index += 1;
        return self.index 
               
    def _get_total_qty(self,obj):
        total_qty = 0.0
        for line in obj.order_line:
            total_qty += line.product_qty
        return total_qty
        
    def _get_date(self, date_order):
        if date_order:
            d = datetime.strptime(date_order, '%Y-%m-%d %H:%M:%S')
            date1 = d.strftime('%d-%m-%Y')
            return date1
        
class purchase_order_qweb(osv.AbstractModel):
    _name = 'report.gcm_customize_qweb.purchase_order'
    _inherit = 'report.abstract_report'
    _template = 'gcm_customize_qweb.purchase_order'
    _wrapped_report_class = gcm_purchase_order

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
