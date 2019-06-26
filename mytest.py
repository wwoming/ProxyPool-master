import re
import threading

import requests
from get_proxy import *


def my_test_proxy():
    url = 'http://webapp.veryzhun.com/h5/flightsearch?arr=CTU&dep=PEK&date=2019-05-04&token=f1c9dae3737f47d45ceeb72cfa3c8094&limityzm=rpudsk'

    proxy = '98.172.141.125:8080'

    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }

    response = requests.get(url, proxies=proxies, verify=False)
    print(response.status_code)
    if response.status_code != 200:
        return my_test_proxy()
    print(response.text)


def crawl_89ip():
    for page in range(1, 11):
        start_url = 'http://www.89ip.cn/index_{}.html'.format(page)
        response = requests.get(start_url)
        if response.status_code == 200:
            html = response.text
            pattern = re.compile('<tr>.*?<td>\s*(.*?)\s*</td>.*?<td>\s*(.*?)\s*</td>.*?</tr>', re.S)
            result = re.findall(pattern, html)
            ip_ports = [':'.join(item) for item in result]
            for address_port in ip_ports:
                yield address_port


def get_page(page):
    headers = {
        'authority': 'www.toutiao.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'UM_distinctid=16a9a6555bc18a-0ff232f091842b-f353163-15f900-16a9a6555bd376; csrftoken=63623a2bed281546e68e1a5d30111843; tt_webid=6688846709977662989; _ga=GA1.2.1970246075.1557369652; uuid="w:22aae4c6f1f747f9b41094d05f8414bc"; s_v_web_id=0fa82aff0bcbf85d6469024600c548d1; CNZZDATA1259612802=1746419442-1557365329-https%253A%252F%252Flanding.toutiao.com%252F%7C1557457129; tt_webid=6688846709977662989; WEATHER_CITY=%E5%8C%97%E4%BA%AC',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }

    proxy = random_proxy()
    # proxy = '197.234.55.177:8083'

    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    s = requests.session()
    s.keep_alive = False
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E9%BB%91%E5%AE%A2&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1557485328666'.format(str(page))
    # url = 'http://httpbin.org/get'
    response = s.get(url, headers=headers)
    print('+++++++++++++++++++++当前第几页：', page)
    print(response.text)
    with open('./t/%s.json' % str(page), 'w', encoding='utf-8') as f:
        f.write(response.text)


def main():
    # threads = [threading.Thread(target=my_test_proxy) for _ in range(10)]
    # for thread in threads:
    #     thread.start()
    #     print('线程启动')
    # threads = [threading.Thread(target=get_page, args=(i, )) for i in range(10)]
    # for th in threads:
    #     th.start()
    # print('开始跑')
    for i in range(1):
        get_page(i)

    pass


if __name__ == '__main__':
    main()
