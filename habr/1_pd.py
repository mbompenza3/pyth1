import pandas as pd
import numpy as np

df = pd.read_csv('telecom_churn.csv')
print(df.columns)

print(df.info())

df['Churn'] = df['Churn'].astype('int64')

df.describe()
df.describe(include=['object', 'bool'])

df['Churn'].value_counts(normalize=False,)
df['Area code'].value_counts(normalize=True)

df.sort_values(by='Total day charge',ascending=False).head()
df.sort_values(by=['Churn','Total day charge'],ascending=False).head()

df['Churn'].mean()
df[df['Churn'] == 1].mean()
df[(df['Churn'] == 0) & (df['International plan'] == 'No')]['Total intl minutes'].max()

df.loc[0:5, 'State':'Area code']
df[-1:]

df.apply(np.max)

d = {'No' : False, 'Yes' : True}
df['International plan'] = df['International plan'].map(d)
df.head()

df = df.replace({'Voice mail plan': d})
df.head()

columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
df.groupby(['Churn'])[columns_to_show].describe(percentiles=[])

columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']

df.groupby(['Churn'])[columns_to_show].agg([np.mean, np.std, np.min, np.max])

data = pd.read_csv('habr/adult.data.csv')
data.groupby(['race'])['age'].describe()
pd.crosstab(data['race'],data['salary'])

df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], ['Area code'], aggfunc='mean').head(10)
dtmax=data[data['hours-per-week']==max(data['hours-per-week'])]

data.pivot_table(['hours-per-week'],['native-country','salary'],aggfunc='mean')