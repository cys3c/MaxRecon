#! /usr/bin/env python
'''
Author: Santiago de Diego
Python: python 3.5
'''

from imports import *

def main():
    option=0
    while option!='9':
        show_options()
        option=input()
        if option=='1':
            dns_query()
        elif option=='2':
            whois_query()
        elif option=='3':
            geolocate()
        elif option=='4':
            googlehacking()
        elif option=='5':
            metadata()
        elif option=='6':
            scan()
        elif option=='7':
            cam()
        elif option=='8':
            shodanhacking()

main()
