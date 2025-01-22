import pandas as pd
import numpy as np

# Variable 
a = [15,12.5,'Lisa',22,'Konan']
score = [79,85,81,92,56]
name = ['Lisa','Jennie','Rose','Jisoo','Minnie']
name_dic = {'Lisa':79,'Jennie':85,'Rose':81,'Jisoo':92,'Minnie':75}
data = [
    [163,420,50],
    [175,380,40],
    [162,390,45],
    [168,290,48]
]
col = ['height','calories','duration']
name = ['Lisa','Jennie','Rose']

data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}

###################################################################

def basic_tuple(x):return pd.Series(x)

def basic_list():return pd.Series(([15,12.5,'Lisa',22,'Konan']))

def basic_numpy(x):return f"{np.array(x)}\n{pd.Series(np.array(x))}"

def column_name(x):print(pd.Series(np.array(x), name = 'Score'))

def serie_index(x,y):print(pd.Series(x, index=y, name='Grade' ))

def alt(): return pd.Series([79,85,81,92,56],index=['Lisa','Jennie','Rose','Jisoo','Minnie'],name='Grade')

def dictionary(x): return pd.Series(x, name='Grade')

def select_dictionary(x):return pd.Series(x, index=['Lisa','Minnie'])

def slice_dictionary(x):print(pd.Series(x)[3:])

# DataFrame

def dataframe(d):print(pd.DataFrame(d))

def dataframe_col(d, row):print(pd.DataFrame(d, columns=row))

def dataframe_list(data, col, name):print(pd.DataFrame(data, index=name, columns=col))

def dataframe_dictionary(x,y):print(pd.DataFrame(x,index=y))

def dataframe_loc(x):
    df = pd.DataFrame(x)
    df.set_index("name", inplace=True)
    print(df.loc['Rose'])
    
def dataframe_multiloc(x):
    print(pd.DataFrame(x).iloc[[2],[1]])

dataframe_multiloc(data)