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

class gcm_report_invoice(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(gcm_report_invoice, self).__init__(cr, uid, name, context=context)
        self.record_len = 0.0
        self.localcontext.update({
            'time': time,
            'get_delivery_number': self._get_delivery_number,
            'get_date': self._get_date,
            'num2word': self._convert_num2word,
            })

    def _get_delivery_number(self, origin):
        if origin:
            do_id = self.pool.get('stock.picking').search(self.cr,self.uid,[('origin','=',origin)])
            if do_id:
                pick_obj = self.pool.get('stock.picking').browse(self.cr, self.uid, do_id[0])
                return pick_obj.name
        else:
            return ' '

    def _get_date(self, date_invoice):
        if date_invoice:
            d = datetime.strptime(date_invoice, '%Y-%m-%d')
            date1 = d.strftime('%m/%d/%Y')
            return date1

    def _convert_num2word(self, amount):
        amt_en = amount_to_text_en.amount_to_text(amount)
        return amt_en

class report_invoice_qweb(osv.AbstractModel):
    _name = 'report.gcm_report.report_account_invoice'
    _inherit = 'report.abstract_report'
    _template = 'gcm_report.report_account_invoice'
    _wrapped_report_class = gcm_report_invoice

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
