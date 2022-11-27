from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='pt-BR', tz=360)



class GoogleTrends:
    def __init__(self, country='brazil'):
        self._words = []
        self._brazil_trends = pytrends.trending_searches(pn=country)

    def get_trends_brazil(self):

        obj = self._brazil_trends.to_dict()

        for value in obj:
            self._words = [value[1] for value in obj[value].items()]
            
            

