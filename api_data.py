from requests import get
from json import dumps
import pandas as pd
from pathlib import Path

class api_data:
    def __init__(self,ENDPOINT):
        self.ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"

    def request_data(self,ENDPOINT,params):
        AREA_TYPE = "nation"
        AREA_NAME = "england"
        filters = [
            f"areaType={AREA_TYPE}",
            f"areaName={AREA_NAME}"
        ]

        structure = {
            "date": "date",
            "name": "areaName",
            "code": "areaCode",
            "dailyCases": "newCasesByPublishDate",
            "cumulativeCases": "cumCasesByPublishDate",
            "dailyDeaths": "newDeaths28DaysByPublishDate",
            "cumulativeDeaths": "cumDeaths28DaysByPublishDate",
            "hospitalCases": "hospitalCases",
            "newReinfectionsBySpecimenDate": "newReinfectionsBySpecimenDate"
        }

        api_params = {
            "filters": str.join(";", filters),
            "structure": dumps(structure, separators=(",", ":"))
        }
        response = get(ENDPOINT, params=api_params, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: {response.text}')

        return response.json()

    def final_data(self):
        data_req = self.request_data(self.ENDPOINT, self.params)
        Data = data_req['data']
        df = pd.json_normalize(Data)
        filepath = Path('C:/Users/Srivalli Padala/Desktop/Gnana_Personal/ARC_Assignment/apidata.csv')
        df.to_csv(filepath)
        return df
