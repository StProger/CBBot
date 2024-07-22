import aiohttp

import xml.etree.ElementTree as ET

from bot.settings import settings


class HttpClient:

    def __init__(self):

        self._session = aiohttp.ClientSession()


class CentralBankClient(HttpClient):

    async def get_rates(self):

        async with self._session.get(url=settings.CB_URL) as response:

            if response.status == 200:

                cb_rates = await response.text()
                print(cb_rates)
                return cb_rates
            else:

                return None

    @staticmethod
    async def parse_rates(cb_rates):

        root = ET.fromstring(cb_rates)

        rates_list = []

        for rate in root:
            rate: ET.Element
            id_rate = rate.attrib
            value_rate = rate.find('Value').text
            name_rate = rate.find("Name").text

            rates_list.append(
                {
                    "id": id_rate,
                    "value": value_rate,
                    "name": name_rate
                }
            )

        return rates_list
