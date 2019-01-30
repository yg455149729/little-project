#coding=latin-1
import requests,json
import datetime
import time
from wxpy import *
def getdata():
    headers={'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Cookie':'abtest_userid=710f5f2f-0d3f-490a-8e11-3e4355a0055f; _bfa=1.1515668794144.i7lh1.1.1524730963362.1524734352030.3.9; _jzqco=%7C%7C%7C%7C1524730966572%7C1.782266857.1515668803273.1524731253782.1524734355294.1524731253782.1524734355294.undefined.0.0.8.8; __zpspc=9.5.1524734355.1524734355.1%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _ga=GA1.2.1381625996.1515668809; _RF1=27.115.82.179; _RSG=opKLsAtEHO6wK4xiy.mzp8; _RDG=2809518ea7429026d71c812358350b8b1d; _RGUID=66113b72-b655-4cf2-8cfd-c3ef2cec453a; Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; adscityen=Shanghai; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1524734355196%7D%5D; traceExt=campaign=CHNbaidu81&adid=index; MKT_Pagesource=PC; _bfi=p1%3D101027%26p2%3D101027%26v1%3D9%26v2%3D7; FD_SearchHistorty={"type":"S","data":"S%24%u4E0A%u6D77%28SHA%29%24SHA%242018-04-28%24%u5929%u6D25%28TSN%29%24TSN"}; _bfs=1.1',
    'Host': 'flights.ctrip.com',
    'Referer':"http://flights.ctrip.com/booking/SHA-TSN-day-1.html?DDate1= "+str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
    url='http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=SHA&ACity1=TSN&SearchType=S&DDate1='+str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day)+'&IsNearAirportRecommond=0&LogToken=0c27d8acb93649f9bcdf2add092fb985&rk=9.685994054213069171925&CK=A99305FD210A70D12408BB6D6F3F8AE1&r=0.2364733641351197613210'
    r=requests.get(url,headers=headers)
    content=r.json()
    dest=content['lps']
    list1=[]
    for key in dest:
        if(dest[key]<=250):
            list1.append( key+':'+dest[key])
    return list1
def main():
    bot = Bot()
    bot.file_helper.send('hello')
    while(1):
        list1=getdata()
        if list1!=[]:
            bot.file_helper.send(list1)
        time.sleep(43200)
main()