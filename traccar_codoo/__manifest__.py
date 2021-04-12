# -*- coding: utf-8 -*-

{
    'name': "Traccar Codoo",

    'summary': """
        Odoo Fleet Tracking Using Traccar""",

    'description': """
        This module is used to Integrate Traccar with odoo through Traccar documentation
    """,

    'author': "Codoo",
    'license': 'LGPL-3',
    # for the full list
    'category': 'Stock',
    'version': '12.0',
    'support': 'codoo.dev@gmail.com',
    # any module necessary for this one to work correctly
    'depends': ['base','stock','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/report.xml',
        'views/configurations.xml',
        'data/data.xml',
    ],
    "images": ['static/description/icon.png'],

}
