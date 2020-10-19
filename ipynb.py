#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터 전처리 -> ssps 재공 data에서 , 예시는 FH
Lotlist_raw = pd.read_csv("Lotlist.csv", sep=",") #파일명 입력

Lotlist_fh = Lotlist_raw[Lotlist_raw['PROCESS_ID'] == 'KHFH'] #KHFH만 불러옴
Lotlist_fh_arr = Lotlist_fh[(Lotlist_fh['QTY']>2) & (Lotlist_fh['QTY']<22)] # BATCH SIZE 만족이 안되는 LOT들만 불러옴
Lotlist_fh_arr_qty = Lotlist_fh_arr['QTY']
Lotlist_fh_arr_sort = Lotlist_fh_arr.sort_values(by='QTY')
Lotlist_fh_arr_sort
Lotlist_fh_arr_sort_pick = Lotlist_fh_arr_sort.loc[:,['PROCESS_ID','LOT_ID','QTY']] # 원하는 컬럼을 가져옴
Lotlist_fh_arr_sort_pick['max'] = 24 - Lotlist_fh_arr_sort_pick['QTY']
Lotlist_fh_arr_sort_pick['min'] = 22 - Lotlist_fh_arr_sort_pick['QTY']
Lotlist_fh_arr_sort_pick


# In[ ]:




