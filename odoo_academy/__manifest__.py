# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """An academy app to manage training""",
    'description': """
    Academy module to manage training
    ldin
    asdfoi
    """,
    'author': 'Logan',
    'website': 'https://richardsonapparatus.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml'
    ],
    'demo': [
        'demo/academy_demo.xml'
    ],
    'license': 'LGPL-3'
}
