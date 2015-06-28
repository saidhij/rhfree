# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2015 rhfree for Odoo SA (<http://rhfree.com>).
#    Module coded by rhfree for odoo All Rights Reserved.
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
from openerp import models, fields, api


class hr_employee(models.Model):
    _inherit = 'hr.employee'
    _name = 'hr.employee'
	
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    complete_name = fields.Char(string="Full Name", compute='_complete_name')	
	
    @api.one
    @api.depends('first_name','last_name','name')
    def _complete_name(self):
	    if self.last_name :
		self.complete_name = self.first_name + " " + self.last_name
 
    @api.onchange('complete_name', 'name') # if these fields are changed, call method
    def check_change(self):     
        if self.name < self.complete_name:
		self.name = self.complete_name	
		

		
		
		
	