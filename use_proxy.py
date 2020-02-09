#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3

import sys
from bs4 import BeautifulSoup
from urllib import request, error
import requests
import json
import time

def get_proxy():
    ################################################
    # please make sure you can retrieve proxy ip
    # successfully before proceeding
    ################################################
    req=request.Request('http://127.0.0.1:5010/get/')
    response=request.urlopen(req)
    proxy_bytes=response.read()
    proxy_string=proxy_bytes.decode('utf-8')
    proxy_json=json .loads(proxy_string)
    proxy=proxy_json['proxy']
    return proxy 

def import_sites(file_name):
    print('>> Retrieving site list...')
    with open(file_name,'r') as f:
        site_list=f.readlines()
    print('>> Totally {} sites to visit'.format(str(len(site_list))))
    return site_list

def visit_sites(site_list,headers,proxy):
    finished=0
    total=len(site_list)
    for site in site_list:
        response=requests.get(site.strip(),headers=headers,proxies={'http':'http://{}'.format(proxy)})
        ## site.strip() is necessary to remove the \n at the end of each line, 
        ## otherwise requests.get will fail
        if response.status_code == 200:
            finished+=1
            print('>> Progress - {}/{}'.format(str(finished),str(total)))
        else:
            print('>> [ERROR] Site {} can not be reached !!!'.format(site))
            continue
    return 


headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

if __name__ == '__main__':
    while True:
        input_number=input('Please input how many proxies you want to repeat for?\n')
        try:
            repeat_times=int(input_number)
        except Exception as e:
            print('Only integers are accepted')
            continue 
        break
    site_list=import_sites('sites.txt')
    time.sleep(1)
    for i in range(repeat_times):
        proxy=get_proxy()
        print('>> Start with no.{} proxy {}'.format(str(i+1),proxy))
        time.sleep(1)
        visit_sites(site_list,headers,proxy)
    print('>> Complete !!!')





