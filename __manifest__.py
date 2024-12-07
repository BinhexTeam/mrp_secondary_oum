{
    "name": "Mrp Secondary Uom",
    "summary": """
        Show secondary unit on mrp.""",
    "description": """
        Show secondary unit on mrp.
    """,
    "author": "Binhex",
    "website": "https://binhex.cloud/",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    # any module necessary for this one to work correctly
    "depends": [
        "mrp",
        "product_secondary_unit",
        "stock_secondary_unit",
    ],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/mrp_production_views.xml",
    ],
}
