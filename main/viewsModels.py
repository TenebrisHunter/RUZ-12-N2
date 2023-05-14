import requests
class TableViewModel():

    def __init__(self):
        pass

    def get_search(self, query: str) -> dict:
        """
        Get search from RUZ API
        Example of request: https://rasp.omgtu.ru/api/search?term=АТП
        Parameters:
        query (str): query string to search object name
        Returns:
        dict: json returned from api, example:
        [
            {
                "id": 1,
                "label": "АТП-191",
                "description": "Факультет информационных технологий и компьютерных систем | Дневная",
                "type": "group"
            },
            {
                "id": 141,
                "label": "ЗАТП-191",
                "description": "Институт заочного обучения | Заочная",
                "type": "group"
            }
        ]
        """
        search_params = {'term': str(query)}
        response = requests.get('https://rasp.omgtu.ru/api/search', params=search_params)
        return response.json()

    def get_schedule(self, type: str, id: int, start: str, end: str) -> dict:
        """
        Get schedule from RUZ API
        Example of request: https://rasp.omgtu.ru/api/schedule/group/1?start=2023.05.10&end=2023.05.10
        Parameters:
        type (str): type of object which schedule we need get
        id (int): id of object which schedule we need get
        start (str): date of schedule start in format yyyy.mm.dd
        end (str): date of schedule end in format yyyy.mm.dd
        Returns:
        dict: json returned from api, answer too big to give example
        """

        schedule_params = {
            "start": start,
            "finish": end,
            "lng": 1
        }
        response = requests.get('https://rasp.omgtu.ru/api/schedule/' + type + '/' + str(id),
                                params=schedule_params)
        return response.json()
