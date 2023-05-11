# -*- coding: utf-8 -*-
{
    'name': "nuprod_subs",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose just to test subscription model
    """,

    'author': "NUprod",
    'website': "https://www.nuprod.fr/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
