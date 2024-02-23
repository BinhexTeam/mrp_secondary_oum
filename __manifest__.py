# -*- coding: utf-8 -*-
{
    'name': "Mrp Secondary Uom",

    'summary': """
        Show secondary unit on mrp.""",

    'description': """
        Show secondary unit on mrp.
    """,
    'author': "Binhex",
    'website': "https://binhex.cloud/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'summary': 'Manufacturing Orders & BOMs',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','product_secondary_unit','stock_secondary_unit','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_production_views.xml',
    ],
}
