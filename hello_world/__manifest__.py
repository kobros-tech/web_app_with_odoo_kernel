# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

{
    "name": "Hello World",
    "description": "Hello World Web App using Odoo",
    "author": "Mohamed Alkobrosli",
    "website": "https://www.kobros-tech.com",
    "license": "AGPL-3",
    "depends": [
        "basic",
    ],
    "data": [
        "views/layout.xml",
        "views/hello.xml",
        "views/home.xml",
    ],
    'assets': {
        'hello_world.assets_frontend': [
            ('include', 'basic.assets_frontend'),

            "hello_world/static/src/app/**/*",
        ],
    },
}
