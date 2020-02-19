"""
This programme take from the page cbr.ru/scripts/XML_daily.asp daily
currency exchange rates, parse them and print rate of Hong Kong dollar.

Copyright (C) 2020  Roman Shentsev (e-mail: 3184447@mail.ru)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl

# url = input("Please enter the url:")
# if len(url) < 1:
url = "http://www.cbr.ru/scripts/XML_daily.asp"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters.')
root = ET.fromstring(data)

for country in root.findall('Valute'):
    if country.find('Name').text == 'Гонконгских долларов':
        curName = country.find('Name').text
        nominal = int(country.find('Nominal').text)
        value = country.find('Value').text
    else:
        continue
    value = float(value.replace(',', '.'))
    print(nominal, curName, '=', value)
    print('1', curName, '=', value / nominal)
