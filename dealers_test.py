import logging
# import pyodbc
import pandas as pd
import urllib
import base64 as B
import csv
# import config as C
import os
import json
logging.basicConfig(
    filename='./Hack.log', level=logging.DEBUG)

output = pd.DataFrame()
output_main = pd.DataFrame()
output_list = pd.DataFrame()
output_final = pd.DataFrame()


'''
Code to read full file as json doc one-by-one
# https://jsoneditoronline.org/
'''
with open('QA_Country_Output.json', encoding='utf-8-sig') as f:
    doc = json.load(f)
    for single_doc in doc:
        # print("XXXXXXXXXX")
        # print(single_doc)
        output_main = pd.DataFrame()
        output_list = pd.DataFrame()
        output = pd.DataFrame()
        dict_main = {}
        dict_list = {}
        # single_doc would be the new d everytime
        for k, v in single_doc.items():
            if (isinstance(v, str) or isinstance(v, int)) and v != None:
                dict_main.update({k: v})
                print(dict_main)

            else:
                t = dict()
                if v != None:
                    for element in v:
                        if isinstance(element, dict):
                            for item, values in element.items():
                                new_key = k + "_" + item
                                t[new_key] = values
                            dict_list = {**dict_list, **t}
                            # print(dict_list)
                            output_list = output_list.append(
                                dict_list, ignore_index=True)
                        elif (type(v) is dict):
                            t = dict()
                            for item, values in v.items():
                                new_key = k + "_" + item
                                t[new_key] = v[item]
                            dict_main = {**dict_main, **t}
                            # print(dict_main)
        output_main = output_main.append(
            dict_main, ignore_index=True)

        if output_list.empty == True:
            output_final = output_final.append(
                output_main, ignore_index=True)
            # print(output_final)
        else:
            output_main['key'] = 1
            output_list['key'] = 1
            output = pd.merge(output_main, output_list,
                              on='key').drop("key", 1)
            output_final = output_final.append(
                output, ignore_index=True)
            # print(output_final)


output_final.to_csv(r'./TAR_Country.csv', mode='w',
                    index=False, encoding='utf-8-sig')
