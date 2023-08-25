'''
國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，
文字為"Hello welcome to Cathay 60th year anniversary"，
請寫一個程式計算每個字母(大小寫視為同個字母)出現次數

輸出：
0 1
6 1
A 4
C 2
E 5
H 3
....(繼續印下去)
'''
import collections
from collections import OrderedDict

def count_characters(input: str) -> int:
    if len(input) == 0:                         #沒輸入可計算之字句，退出程式
        print(f'Please input sentences or words to count.')
        return None
    
    counter = dict(collections.Counter(input))  #統計各字元出現次數
    result = {}                                 #用dictionary來紀錄每個字母出現次數
    for index in counter:
        if index == ' ':                        #空格不予計算
            continue
        if index.islower():                     #大小寫視為同個字母，計入大寫計算
            if index.upper() in result:
                result[index.upper()] += counter[index]
            else:
                result[index.upper()] = counter[index]
        elif index.isupper():                   #計算大寫字母出現次數
            if index in result:
                result[index] += counter[index]
            else:
                result[index] = counter[index]
        else:                                   #計算數字、標點符號出現次數
            result[index] = counter[index]
    
    if len(result) == 0:                        #沒輸入可計算之字句，退出程式
        print(f'Please input sentences or words to count.')
        return None

    result = sorted(result.items(), key=lambda x:x[0])  #排序，照字母順序輸出
    for i in result:
        print(f'{i[0]} {i[1]}')

assert count_characters("Hello welcome to Cathay 60th year anniversary") is None
assert count_characters("") is None
assert count_characters("                ") is None