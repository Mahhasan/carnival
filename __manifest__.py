# -*- coding: utf-8 -*-
{
    'name': "carnival",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/hall_live_link_view.xml',
        'views/hall_gallery_view.xml',
        'views/hall_youtube_video_view.xml',
        'views/stall_rubrics_view.xml',
        'views/stall_gallery_information_view.xml',
        'views/stall_counselor_information_view.xml',
        'views/stall_video_information_view.xml',
        'views/stall_document_information_view.xml',
        'views/event_rubrics_category_view.xml',
        'views/event_judge_information_view.xml',
        'views/event_organizer_information_view.xml',
        'views/event_ads_information_view.xml',
        'views/event_halls_information_view.xml',
        'views/event_stalls_information_view.xml',
        'views/event_view.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
