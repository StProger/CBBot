import aiohttp

import xml.etree.ElementTree as ET

from bot.settings import settings


# class HttpClient:
#
#     def __init__(self):
#
#         self._session = ClientSession()


class CentralBankClient:

    async def get_rates(self):

        async with aiohttp.ClientSession() as session:
            response = await session.get(settings.CB_URL)
            if response.status == 200:

                cb_rates = await response.text()
                print(cb_rates)
                return cb_rates
            else:

                return None

    async def parse_rates(self, cb_rates):

        root = ET.fromstring(cb_rates)

        rates_list = []

        for rate in root:
            rate: ET.Element
            char_code = rate.find("CharCode").text
            value_rate = rate.find('VunitRate').text
            name_rate = rate.find("Name").text

            rates_list.append(
                {
                    "char_code": char_code,
                    "value": value_rate,
                    "name": name_rate
                }
            )

        return rates_list
