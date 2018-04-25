
from sklearn import datasets
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine


digits = datasets.load_digits()

features = digits.data

target = digits.target

#features(0)

# Generate feature matrix, target vector, and the true coefficients
features, target, coefficients = make_regression(n_samples = 100,
                                                 n_features = 3,
                                                 n_informative = 3,
                                                 n_targets = 1,
                                                 noise = 0.0,
                                                 coef = True,
                                                 random_state = 1)

# View feature matrix and target vector
#print('Feature Matrix\n', features[:3])
#print('Target Vector\n', target[:3])

#plt.scatter(features[:,0], features[:,1], c=target)
#plt.show()


# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.csv'

# Load dataset
dataframe = pd.read_csv(url)

# View first two rows
#print(dataframe.head(2))

# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx'

# Load data
dataframe = pd.read_excel(url, sheetname=0, header=1)

# View the first two rows
#print(dataframe.head(2))



# Create URL
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json'

# Load data
dataframe = pd.read_json(url, orient='columns')

# View the first two rows
#print(dataframe.head(2))

# Create a connection to the database
database_connection = create_engine('sqlite:///sample.db')

# Load data
dataframe = pd.read_sql_query('SELECT * FROM data', database_connection)

# View first two rows
print(dataframe.head(2))


