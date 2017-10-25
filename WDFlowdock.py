# -*- coding: utf-8 -*-
"""This module implements communication with Flowdock.

Copyright (C) 2017 Peter Pakos <peter.pakos@wandisco.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import requests
from requests.auth import HTTPBasicAuth


class WDFlowdock(object):
    def __init__(self, api_key):
        users = requests.get('https://api.flowdock.com/users/', auth=HTTPBasicAuth(api_key, '')).json()
        self._users = {}

        for user in users:
            self._users.update({
                user.get('email'): {
                    'id': user.get('id'),
                    'name': user.get('name'),
                    'nick': user.get('nick')
                }
            })

    def count_users(self):
        return len(self._users)

    def get_users(self):
        return self._users
