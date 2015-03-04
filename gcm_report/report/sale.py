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
from openerp.tools import amount_to_text_en
from openerp.modules.module import get_module_resource

class gcm_sales_receipt(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(gcm_sales_receipt, self).__init__(cr, uid, name, context=context)
        self.sub_total=0.00
        self.localcontext.update({
            'time': time,
            'num2word': self._convert_num2word,
            'get_contact_person': self.get_contact_person,
            'get_subtotal': self.get_subtotal,
            })

    def _convert_num2word(self, amount):
        amt_en = amount_to_text_en.amount_to_text(amount)
        return amt_en 

    def get_contact_person(self,invoice_obj):
        if invoice_obj.partner_id.child_ids:
            return invoice_obj.partner_id.child_ids[0].name
        return ' '

    def get_subtotal(self):
        total= self.sub_total
        self.sub_total=0.00
        return total       
 
class report_sale_qweb(osv.AbstractModel):
    _name = 'report.gcm_report.report_sales_receipt'
    _inherit = 'report.abstract_report'
    _template = 'gcm_report.report_sales_receipt'
    _wrapped_report_class = gcm_sales_receipt

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
