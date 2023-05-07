import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time
import json
import pushbullet




# تعیین اطلاعات API برای ارسال نوتیفیکیشن
API_KEY = 'o.zzKku8rNuusu1P1FBkLNCy7TXbH2pcnm'
url = 'https://api.pushbullet.com/v2/pushes'


# تعیین مقدار قیمت مورد نظر
threshold_price = 0.07

# آدرس صفحه‌ی دوج کوین در CoinMarketCap
url = 'https://coinmarketcap.com/currencies/dogecoin/'

# ایجاد یک شیء از کلاس ToastNotifier برای نمایش نوتیفیکیشن
toaster = ToastNotifier()

# حلقه‌ی بی‌نهایت برای چک کردن قیمت و ارسال نوتیفیکیشن
while True:
    # دریافت محتوای صفحه
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # یافتن المان قیمت
    price_element = soup.find('div', class_='priceValue')

    #print(price_element)

    # گرفتن قیمت به صورت متنی از المان
    price_text = price_element.text.strip()

    # تبدیل متن به عدد اعشاری
    price = float(price_text.replace(',', '').replace('$', ''))

    print(price)

    # ارسال نوتیفیکیشن اگر قیمت به مقدار مورد نظر رسید
    if price >= threshold_price:
            
        toaster.show_toast(
            "DOGE Coin Price Update",
            f"The price of DOGE Coin is now {price}.",
            duration=80  # مدت زمان نمایش نوتیفیکیشن
        )
        
        headers = {
            'Access-Token': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        data = {
            'type': 'note',
            'title': 'DOGE Coin Price Update',
            'body': f'The price of DOGE Coin is now {price}.'
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))

    

    # استراحت برای چک کردن قیمت مجدد
    time.sleep(60)



    