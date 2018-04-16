import requests
def eskatu(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    print(r.json())
    return r.text

def bidali(url, balioa):
    r = requests.get(url+str (balioa))
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    return r.text

url='http://mendillorriapps.pythonanywhere.com/ledurdina/'
eskatu(url)

url='http://mendillorriapps.pythonanywhere.com/ledgorria/'
eskatu(url)

url='http://mendillorriapps.pythonanywhere.com/ledtxuria/'
eskatu(url)

url='http://mendillorriapps.pythonanywhere.com/ponpa/'
eskatu(url)

url='http://mendillorriapps.pythonanywhere.com/bozgoragailua/'
eskatu(url)

print("T=1")
url='http://mendillorriapps.pythonanywhere.com/tenperatura/'
bidali(url, 1)


url='http://mendillorriapps.pythonanywhere.com/ledgorria/'

eskatu(url)
print("T=30")
url='http://mendillorriapps.pythonanywhere.com/tenperatura/'
bidali(url, 30)
url='http://mendillorriapps.pythonanywhere.com/ledgorria/'
eskatu(url)