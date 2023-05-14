from pytrends.request import TrendReq

pytrends = TrendReq(hl='pt-BR', tz=360)

py = pytrends.trending_searches(pn='brazil')

print(py)