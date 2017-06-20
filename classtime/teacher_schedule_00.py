# -*- coding: utf-8 -*- 



# 列表推导只取有:的
data_classtime = [x for x in data if ":" in x]

dict_classtime = {x.split(":")[0]:x.split(":")[1] for x in data_classtime}
print (dict_classtime)

list_dict_classtime = [{'c_code': k, 'c_name': v} for k,v in dict_classtime.items()]
print (list_dict_classtime)
# ---------------------------------------------------


# 使用csv模块，将国家代码及简中国家名称数据输出至data\class.tsv备用

import csv
with open('cleaned_data.tsv', 'w', encoding='utf8') as csvfile:
    fieldnames = ['c_code ', 'c_name']
    writer = csv.DictWriter(csvfile, fieldnames=['c_code', 'c_name'])
    writer.writerow (list_dict_classtime)
