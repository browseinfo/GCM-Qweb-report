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

class gcm_deliver_order(report_sxw.rml_parse):
    index = 0
    def __init__(self, cr, uid, name, context=None):
        super(gcm_deliver_order, self).__init__(cr, uid, name, context=context)
        self.init_bal_sum = 0.0
        self.localcontext.update({
            'time': time,
            'get_date': self._get_date,
            'get_index': self._get_index,
            'get_payment_term': self._get_payment_term,
            'get_salesman': self._get_salesman,
            })
 
    def _get_date(self, date):
        if date:
            d = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            date1 = d.strftime('%d-%m-%Y')
            return date1
               
    def _get_index(self):
        self.index += 1;
        return self.index
    
    def _get_payment_term(self,obj):
        origin = obj.origin
        so_obj = self.pool.get('sale.order')
        so_id = so_obj.search(self.cr,self.uid,[('name','=',origin)])
        if so_id:
            payment_term = so_obj.browse(self.cr,self.uid,so_id[0]).payment_term.name
            return payment_term

    def _get_salesman(self,obj):
        origin = obj.origin
        so_obj = self.pool.get('sale.order')
        so_id = so_obj.search(self.cr,self.uid,[('name','=',origin)])
        if so_id:
            salesman = so_obj.browse(self.cr,self.uid,so_id[0]).user_id.name
            return salesman
                               
class deliver_order_qweb(osv.AbstractModel):
    _name = 'report.gcm_customize_qweb.deliver_order'
    _inherit = 'report.abstract_report'
    _template = 'gcm_customize_qweb.deliver_order'
    _wrapped_report_class = gcm_deliver_order

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
