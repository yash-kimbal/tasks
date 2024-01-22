# -*- coding: utf-8 -*--
{
    'name': "Real Estate Ads",
    'summary': """School Management Software""",

    'description': """
    Real Estate module to show available properties
    """,

    'author': "Yash Arora",
    'website': "http://www.your.com",
    'category': "Sales",
    'version': '1.0',
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/menu_items.xml',

        # Data Files
        # 'data/property_type.xml'
        'data/estate.property.type.csv'

    ],
    'demo':[
      'demo/property_tag.xml'
    ],
    'installable': True,
    'application': True,
    'licence':"LGPL-3"
}
