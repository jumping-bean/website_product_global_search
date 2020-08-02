# -*- coding: utf-8 -*-
{
    'name': "website_product_global_search",

    'summary': """
        Add an additional button to the default search box 
        for searching across all product categories.""",

    'description': """
        A simple module to add a global search button
        to the default product search box. This is only
        useful when the following web site customisations
        are set:
         * "eCommerce Categories" - enabled
         * "Categorized Shop Page" - disabled. 
        This allows searching across all categories without 
        first having to click on the "All products link" 
        from the "eCommerce Categories" menu.
    """,

    'author': "Jumping Bean",
    'website': "http://www.jumpingbean.co.za",
    'license': 'LGPL-3',
    'category': 'Website',
    'version': '0.1',

    'depends': ['base', 'website_sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',

    ]
}