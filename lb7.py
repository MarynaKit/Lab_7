import requests
import json

# валютний код криптовалюти
currency_code = input("Enter the cryptocurrency currency code: ")
# використовуючи валютний код формую посилання на API
api_url = f"https://api.coinpaprika.com/v1/coins/{currency_code}"
# виконуємо HTTP-запит та зберігаємо відповідь в форматі JSON
response = requests.get(api_url)
response_json = json.loads(response.text)
# отримуємо необхідну інформацію з JSON-об'єкту
currency_name = response_json['name']
currency_symbol = response_json['symbol']
currency_description = response_json['description']
# результат пошуку виводимо консоль
print(f"Name: {currency_name}")
print(f"Sybol: {currency_symbol}")
print(f"Description: {currency_description}")