#! /usr/bin/env python3

import sys, shodan
from getpass import getpass

class shodan_search(object):

    def settingApi(self):
        try:
            print("Please, set your APIKey here:")
            shodanKeyString = getpass('API Key:' )
            self.shodanApi = shodan.Shodan(shodanKeyString)
        except:
            print("The specified APIKey is invalid, please insert another one.")
            exit()

    def run_full(self, search, filename):
        if filename is not None:
            file = open(filename, 'w')
            search_query = search.replace("-", ' ')
            try:
                results = self.shodanApi.search(search_query)
                file.write("Total results: %s" % (len(results['matches'])))
                file.write("\n")
                for result in results['matches']:
                    file.write("IP: %s \n" % (result['ip_str']))
                    file.write("PORT: %s \n" % (result['port']))
                    file.write("ISP: %s \n" % (result['isp']))
                    file.write("//////////ADDITIONAL DATA////////// \n")
                    file.write(result['data'])
                    file.write("\n=========================")
                    file.write('\n')
                    file.write('\n')

            except:
                print("Search parameters unavailable for your APIKey. More info in documentation.")
                exit()
        else:
            search_query = search.replace("-", ' ')
            try:
                results = self.shodanApi.search(search_query)
                print("Total results: %s" % (len(results['matches'])))
                print("\n")
                for result in results['matches']:
                    print("IP: %s \n PORT: %s \n ISP: %s \n " % (result['ip_str'], result['port'],
                                                                              result['isp']))
                    print("//////////ADDITIONAL DATA//////////")
                    print(result['data'])
                    print('\n')
            except:
               print("Search parameters unavailable for your APIKey. More info in documentation.")
               exit()

    def run_nofull(self, search, filename):
        if filename is not None:
            file = open(filename, 'w')
            search_query = search.replace("-", ' ')
            try:
                results = self.shodanApi.search(search_query)
                for result in results['matches']:
                    file.write(result['ip_str'])
                    file.write('\n')
            except:
                print("Search parameters unavailable for your APIKey. More info in documentation.")
                exit()
        else:
            search_query = search.replace("-", ' ')
            try:
                results = self.shodanApi.search(search_query)
                for result in results['matches']:
                    print(result['ip_str'])
            except:
                print("Search parameters unavailable for your APIKey. More info in documentation.")
                exit()

    def __init__(self, search, filename, full):
        self.settingApi()
        if full is True :
            self.run_full(search, filename)
        else:
            self.run_nofull(search, filename)
        exit()
