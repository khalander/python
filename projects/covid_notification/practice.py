print('notification')
from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe (title, message) :
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10
    )

def getData(url) :
    r = requests.get(url)
    return r.text


# notifyMe('Covid test ', 'Notification example')

myHtml = getData('https://www.mohfw.gov.in/')
soup = BeautifulSoup(myHtml, 'html.parser')
# print(soup)
for tr in soup.find_all('table'):
    print(tr.get_text())
