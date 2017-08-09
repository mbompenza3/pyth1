from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
# отключим предупреждения Anaconda
import warnings
warnings.simplefilter('ignore')

# будем отображать графики прямо в jupyter'e


#увеличим дефолтный размер графиков
from pylab import rcParams
rcParams['figure.figsize'] = 8, 5
import pandas as pd
import seaborn as sns

df = pd.read_csv('C:\\Users\\MokhnachevskiyAN\\PycharmProjects\\pyth1\\habr\\video_games_sales.csv')
# df.info()
df=df.dropna()
# print(df.shape)
useful_cols = ['Name', 'Platform', 'Year_of_Release', 'Genre',
               'Global_Sales', 'Critic_Score', 'Critic_Count',
               'User_Score', 'User_Count', 'Rating'
              ]

# sales_df = df[[x for x in df.columns if 'Sales' in x] + ['Year_of_Release']]
# p=sales_df.groupby('Year_of_Release').sum().plot()

df['User_Score']=df['User_Score'].astype('float64')

# print(df.info())
# cols = ['Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
# sns_plot = sns.pairplot(df[cols])
# sns_plot.savefig('pairplot.png')

sns.distplot(df.Critic_Score)
sns.jointplot(df.Critic_Score,df.User_Score )
