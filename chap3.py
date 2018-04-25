import pandas as pd

#Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

#Load data as DataFrame
dataframe  = pd.read_csv(url)

#print(dataframe.head(5))

#Creating Empty Dataframe
dataframe = pd.DataFrame()

#Add columns
dataframe['Name'] = ['Amy Jackson','Steve Stevenson']
dataframe['Age'] = [38, 25]
dataframe['Driver'] = [True,False]

#show dataframe
#print(dataframe)

#create row
new_person = pd.Series(['Molly Mony',40, True], index=['Name','Age','Driver'])

#append_row
dataframe.append(new_person, ignore_index=True)

#print(dataframe)

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

#load data
dataframe1 = pd.read_csv(url)

#show 2 rows
#print(dataframe1.head(2))

#show dimension
#print(dataframe1.shape)

#show stattics
#print(dataframe1.describe())

#show first row
#print(dataframe1.iloc[0])

#show  3 rows
#print(dataframe1.iloc[1:4])

#show 5 rows
print(dataframe1.iloc[:6])

#set index
#dataframe1.set_index(dataframe1['Name'])


#show row
#print(dataframe1.loc['Allen, Miss Elisabeth Walton'])


url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

#select rows based on conditionals
print(dataframe[dataframe['Sex'] == 'female'].head(2))

print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] == 65)])

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

#Replacing values
print(dataframe['Sex'].replace("female","woman").head(2))

print(dataframe['Sex'].replace(["female", "male"], ["woman","men"]).head(5))

print(dataframe.replace(1, "One").head(2))


url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

#renaming column

print(dataframe.rename(columns={'PClass': 'Passenger Class'}).head(2))

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'

dataframe = pd.read_csv(url)

#finding max min
print('Maximum :', dataframe['Age'].max())
print('Minimum :', dataframe['Age'].min())
print('Mean :', dataframe['Age'].mean())
print('Sum :', dataframe['Age'].sum())
print('Count :', dataframe['Age'].count())
