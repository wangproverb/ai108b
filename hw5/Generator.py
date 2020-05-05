'''
S = NP VP           -> 句子 = 名詞子句 + 動詞子句
NP = DET N          -> 名詞子句 = 定詞 + 名詞
VP = V NP           -> 動詞子句 = 動詞 + 名詞子句
'''

import random as r

name = ['佐藤','田中','鈴木','山本','高橋']
title = ['さん','君','ちゃん']
v = ['ある','います','いる','あります']
place = ['教室','部屋','店','家','会社','学校']
time = ['今','先','昨日は','今日は']



def S():
    return NP() + 'は' + VP()

def NP():
    return N() + Title()

def VP():
    return Time() + Place() + 'に'+ V()


def Title():
    return r.choice(title)

def Place():
    return r.choice(place)

def N():
    return r.choice(name)

def Time():
    return r.choice(time)

def V():
    return r.choice(v)

for i in range(10):
    print(S())