# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016 rhfree  (<http://rhfree.com>).
#    Module coded by rhfree for Odoo. All Rights Reserved.
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
{
    'name': 'Employee name split into First and Last',
    'category': 'Human Resources',
    'author': 'Said Hijaoui (rhfree.com)',
    'website': 'http://rhfree.com',
    "license": "AGPL-3",
    'version': '1.1',
    'depends': ['hr'],
	'price': 9,
    'currency': 'EUR',
	
    'description': """This module allow you to have First Name and Last name fields and combine them automatically in employee name field.
    """,
    'data': [
        'view/hr_employee_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
