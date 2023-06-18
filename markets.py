import requests,json

BASE_URL = 'http://api.marketstack.com/v1/'
API_KEY='a1fda0800a787f4df466e64c1c101f81'

def stockPrice(stock_symbol):
    params={
        'access_key':API_KEY
    }
    end_point = "".join([BASE_URL,"tickers/",stock_symbol,"/intraday/latest"])
    api_result=requests.get(end_point,params)
    json_result = json.loads(api_result.text)
    return {
        "last_price":json_result["last"]
    }