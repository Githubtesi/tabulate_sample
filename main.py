# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/02/09
from tabulate import tabulate

persons_table = [['Name', 'Age', 'Job'],
                 ['Mike', '22', 'Programmer'],
                 ['John', '24', 'Teacher'],
                 ['Jone', '23', 'Desinger'],
                 ['Jack', '28', 'Manager'],
                 ]

# 通常の出力
# for person in persons_table:
#     for person_data in person:
#         print(person_data, end='\t')
#     print()

# サードパーティ テーブルコンソール表示
print(tabulate(persons_table, headers='firstrow', tablefmt='grid'))

# html
with open(file="table.html", mode="w") as f:
    f.write(tabulate(persons_table, headers='firstrow', tablefmt='html'))
# tex
with open(file="table.tex", mode="w") as f:
    f.write(tabulate(persons_table, headers='firstrow', tablefmt='latex'))

# 別タイプのデータ
data = {
    'Name': ['Mike', 'John', 'Jone', 'Jack'],
    'Age' : ['22', '24', '23', '28'],
    'Job' : ['Programmer', 'Teacher', 'Desinger', 'Manager'],
}
print(tabulate(data, headers='keys', tablefmt='psql', showindex=True))

# numpy
import numpy as np

columns = ['COL1', 'COL2', 'COL3']
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(tabulate(arr, headers=columns, tablefmt='psql', showindex="always"))

# pandas
import pandas as pd

df = pd.DataFrame(data)
print(tabulate(df, headers='keys', tablefmt='psql', showindex="always"))
