
import requests
# 获取实时汇率数据
def get_exchange_rates():
    api_key = '11b95e588508d54e2eaf7ea7'  # 替换成你的API密钥
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD' 
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['conversion_rates']
    else:
        print("Failed to fetch exchange rates.")
        return None

# 进行货币转换
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Invalid currencies.")
        return None

# 主函数
def con(data,from_currency,to_currency):
    exchange_rates = get_exchange_rates()
    if exchange_rates:
        amount = float(data)
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    else:
        print("无法获取汇率数据。")

    return converted_amount