# -*- encoding: utf-8 -*-
##############################################################################
#
#    
#    Copyright (C) 2016 rhfree (<http://rhfree.com>).
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
{
    'name': 'Morocco-payroll',
    'category': 'human resources',
    'author': 'Said Hijaoui (rhfree.com)',
    'website': 'http://rhfree.com',
    "license": "AGPL-3",
    'version': '1.1Basic',
    'depends': ['hr_payroll'],
    
	
    'description': """Moroccan Payroll Rules Basic Version.
======================

     - Configuration of hr_payroll for Moroccan localization
    - Basic configuration for newly installed company'
    - Absence - Advances - CNSS - AMO
	- Pro version is complete and  handles all kinds of allowances and Bonuses plus 
	        - Seniority ( anciennété) and all other advantages:
        	- CIMR and private health insurance like  AXA 
			- Nice looking payslip
			- Legal reports ( etat 9421 ) ...
    - Important: you need to fill the wage amount for the employee in the contract and  choose moroccan payroll from the structure field.
    """,
    'active': False,
    'update_xml':['l10n_ma_payroll_view.xml'],
	 'data': [
        'l10n_ma_payroll_view.xml',
        'l10n_ma_payroll_data.xml',
		'views/payslip_report_view.xml',
        'l10n_ma_payroll_reports.xml',
        
       ],
    'auto_install': False,
    'installable': True,
    'application': False,
	
}
