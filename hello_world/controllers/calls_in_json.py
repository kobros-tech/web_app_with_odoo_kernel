# -*- coding: utf-8 -*-
# Part of kobros-tech. See LICENSE file for full copyright and licensing details.

import json

import re
import werkzeug.exceptions
import werkzeug.urls
from odoo.http import request, route, Controller
from odoo import http, tools, _, SUPERUSER_ID, release

import requests


class JSONCalls(http.Controller):

    """
        Most critical methods that are POST methods and usually return critical data if they are accepting JSON connection, the returned data are stripped for security sake, this happens only when type=json.

        If type=http, then you can read the returned data in the JSON request.


        For GET methods, they are always read in type=http even if the requested data are in JSON, this is dominant outside odoo and inside odoo, for ultimate security sake!
    """

    @route(["/json_call", "/json_call/<index>"], type="http", methods=['POST', 'GET'], auth="public", cors="*", csrf=False)
    # @route(["/json_call", "/json_call/<index>"], type="json", methods=['POST'], auth="public", cors="*", csrf=False)
    def json_calls(self, index=None):

        data = {'key': 1, 'value': True}

        if request.httprequest.method == "POST":
            json_data = request.get_json_data()

            if json_data['params']['index']:
                data['key'] = json_data['params']['index']

                print("===================================")
                print(request.httprequest.method)
                print(json_data)
                print(index)
                print(json_data['params']['index'])
                print(data)
                print("===================================")
        
        data = json.dumps(data)
        response = request.make_response(data=data, headers=[('Content-Type', 'application/json')], status=200)
        
        print("response", response)
        
        return response


    @route("/json_call_get", type="http", methods=['GET', 'POST'], auth="public", cors="*", csrf=False)
    def json_calls_get(self):

        print("===================================")
        print("get method")
        print("===================================")

        data = {'key': 1, 'value': True}
        
        data = json.dumps(data)
        response = request.make_response(data=data, headers=[('Content-Type', 'application/json')], status=200)
        
        print("response", response)

        return response

    
    @route("/read_json", type="http", auth="public", website=True, csrf=False)
    def read_json(self):
        url = 'http://localhost:8070/json_call_get'
        payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {},
            'id': 1,
        }

        response = requests.post(
                url,
                json=payload,
                timeout=5,
                headers={'content-type': 'application/json'},
                ).json()
        
        print(response)
        
        response = requests.post(
                url,
                timeout=5,
                ).json()

        print(response)
