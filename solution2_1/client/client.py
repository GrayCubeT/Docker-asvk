#!/usr/bin/python3

import sys
from os import listdir, getcwd
from os.path import isfile, join
import requests

def main():
    # get all files in the current directory
    inputfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
    
    try:
        # iterate over files, send those with .txt in them as strings
        for i in inputfiles:
            if ('.txt' in i):
                print("Problem in " + i)
                with open(i, 'r') as file:
                    # read data
                    data = file.read().replace('\n', '')
                    if ('&' in data):
                        print("Error: '&' is a forbidden character")
                        return
                    # send a POST request
                    with requests.post('http://localhost:5000/calculate', data={'data':data}) as response:
                        print(response.text + '\n')
    except Exception as exc:
        print(exc)
        raise



if __name__ == "__main__":
    main()