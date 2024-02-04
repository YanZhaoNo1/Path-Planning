#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import math

def main():
    while(True):
        a = float(input("Please input angle:"))
        result = (a-math.floor(a))*100/60+math.floor(a)
        print("%.2f"%result)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
