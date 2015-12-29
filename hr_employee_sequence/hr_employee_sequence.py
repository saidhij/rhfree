
from datetime import timedelta
import openerp.addons.decimal_precision as dp
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from calendar import isleap
from openerp.tools.translate import _
from openerp.osv import fields, osv
from openerp.exceptions import UserError
from openerp import models, fields, api


	
class hr_contract(models.Model):
    _inherit = 'hr.contract'
	
	
    name = fields.Char('Contract Reference', required=False,readonly=True, copy=False, default='Autofill')

    @api.model
    def create(self, vals):
        if vals.get('number', 'Autofill') == 'Autofill':
            vals['name'] = self.env['ir.sequence'].next_by_code('contract.ref')
        return super(hr_contract, self).create(vals)
	
  

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    _name = 'hr.employee'
	
   
    code2 = fields.Char('Code', required=False,readonly=False, copy=False, default='autofill')
    
	
		
    @api.model
    def create(self, val):
        if val.get('number', 'autofill') == 'autofill':
            val['code2'] = self.env['ir.sequence'].next_by_code('employee.code2')
        return super(hr_employee, self).create(val)
		
		
    
		
		

		
		
		
	