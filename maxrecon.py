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
        for case in switch(option):
            if case('1'):
                dns_query()
                break
            if case('2'):
                whois_query()
                break
            if case('3'):
                geolocate()
                break
            if case('4'):
                googlehacking()
                break
            if case('5'):
                metadata()
                break
            if case('6'):
                scan()
                break
            if case('7'):
                cam()
                break
            if case('8'):
                pass
                break
            if case('9'):
                pass
                break
            if case(): # default
                option=0

main()
