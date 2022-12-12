# -*- coding: utf-8 -*-

{
    'name': 'Odoo Space Mission',
    'summary': """Taking Odoo to the moon.""",
    'description': """
    Moon spaceboi
    """,
    'author': 'Logan',
    'website': 'https://richardsonapparatus.com',
    'category': 'Task Management',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/spacemission_security.xml',
        'security/ir.model.access.csv',
        'views/spacemission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml'
    ],
    'demo': [
        'demo/spaceship_demo.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False
}
