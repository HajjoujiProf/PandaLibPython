# -*- coding: utf-8 -*-
"""AlgoPandaCourse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GZjDVCZusdw1IQSsyCDHjmD7Lm7YFxMM
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.__version__



import pandas as pd
num = pd.Series([8,53,9,42,15])

num

import pandas as pd
name = pd.Series(['United States','Saudi Arabia','Russia','China','Canada'],['1','2','3','4','5'])

name

name.loc['3']

import pandas as pd
df = pd.DataFrame({'Country':['китай','Марокко','США','Россия'],'Code':['86','212','1','7'],'Population':['1,330,044,000','31,627,428','310,232,863','140,702,000']})

df

import pandas as pd
df = pd.DataFrame({'Country':['китай','Марокко','США','Россия'],'Code':['86','212','1','7'],'Population':['1,330,044,000','31,627,428','310,232,863','140,702,000']},index=['1','2','3','4'])

df.Population

df.loc['4']