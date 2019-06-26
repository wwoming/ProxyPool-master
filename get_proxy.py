import random

import requests
import xlrd
import xlwt
import json


# 获取代理
def random_proxy():
    url = 'http://47.75.146.226:5555/random'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        return response.content.decode('utf-8')
    return None


def save_ip_to_excel():
    ip_pool = xlwt.Workbook()
    sheet = ip_pool.add_sheet('IPPOOL', cell_overwrite_ok=True)
    sheet.write(0, 0, '编号')
    sheet.write(0, 1, 'address')
    sheet.write(0, 2, 'port')
    for i in range(1, 150):
        address_port = random_proxy()
        address, port = address_port.split(':')
        print('写入excel')
        sheet.write(i, 0, i)
        sheet.write(i, 1, address)
        sheet.write(i, 2, port)

    ip_pool.save('../IPPOOL.xls')
    print('保存完成')


def get_ip_from_excel():
    ip_pool = xlrd.open_workbook('./IPPOOL.xls')
    sheet = ip_pool.sheet_by_name('IPPOOL')
    add_ports = []
    for i in range(1, 150):
        address = sheet.cell_value(i, 1)
        port = sheet.cell_value(i, 2)
        address_port = address+':'+port
        add_ports.append(address_port)

    return add_ports


def main():
    # save_ip_to_excel()
    add_ports = get_ip_from_excel()
    for i in range(10):
        print(add_ports[i])
    pass


if __name__ == '__main__':
    main()

