# -*- coding: utf-8 -*-

"""
Created on July 2022

@author: Hosein Khanali
"""

import sys
import requests


BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = "\033[93m"
LINK = "\033[34m"
RESET = "\033[0;0m"

def check_page(url:str,page):
    try:
        res = requests.get(url + '/' + page).status_code
        return res
    except:
        print(RED + ' url is not available !')
        print(RED + ' example : http://target.com' + RESET)
        sys.exit()

def banner():
    print(BLUE + """
      ╔═╗┌┬┐┌┬┐┬┌┐┌  ╔═╗┌─┐┌─┐┌─┐  ╔═╗┬┌┐┌┌┬┐┌─┐┬─┐
      ╠═╣ │││││││││  ╠═╝├─┤│ ┬├┤   ╠╣ ││││ ││├┤ ├┬┘
      ╩ ╩─┴┘┴ ┴┴┘└┘  ╩  ┴ ┴└─┘└─┘  ╚  ┴┘└┘─┴┘└─┘┴└─""")
    print("" + RED,
          "#####################################################\n",
          "## " + BLUE + "SQL Injection Vulnerability on Traget           " + RED + "##\n",
          "##                                                 ##\n",
          "## " + GREEN + "Author :" + LINK + " Hosein Khanali                         " + RED + "##\n",
          "## " + GREEN + "Gmail  :" + LINK + " hosein.asf147@gmail.com                " + RED + "##\n",
          "## " + GREEN + "Github :" + LINK + " https://github.com/hosein-khanalizadeh " + RED + "##\n",
          "#####################################################\n" + RESET)

def main():
    banner()
    url = input(YELLOW + ' target >>> ' + RESET)
    print(' ' + 51*'-')
    print(BLUE + ' Start ...')
    print()
    pages = open('admin_login.txt', 'rb').readlines()
    for page in pages:
        page = page.decode('utf-8')
        res = check_page(url,page)
        if res == 200:
            print(' ' + GREEN + url + '/' + page + RESET)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()