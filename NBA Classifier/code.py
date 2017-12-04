import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graphviz

from IPython.display import display
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import export_graphviz

#read from the csv file and return a Pandas DataFrame.
nba = pd.read_csv('NBAstats.csv')


# "Position (pos)" is the class attribute we are predicting.
class_column = 'Pos'

#The dataset contains attributes which we do not include as features. The reduced  dataset is shown below.
feature_columns = ['MP', 'FG%', '3P', '3PA', \
    '3P%', '2P%', 'eFG%', 'FT%', 'ORB', 'DRB', \
    'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PS/G']

#Pandas DataFrame allows you to select columns.
#We use column selection to split the data into features and class.
nba_feature = nba[feature_columns]
nba_class = nba[class_column]

#splitting into training and test dataset
train_feature, test_feature, train_class, test_class = \
    train_test_split(nba_feature, nba_class, stratify=nba_class, \
    train_size=0.75, test_size=0.25)
training_accuracy = []
test_accuracy = []

#prediction with KNN-classifier
knn = KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm='auto', metric='manhattan')
knn.fit(train_feature, train_class)
prediction = knn.predict(test_feature)

#accuracy of model
print("Test set accuracy: {:.2f}".format(knn.score(test_feature, test_class)))

#printing the 6x6 confusion matrix
print("Confusion matrix:")
print(pd.crosstab(test_class, prediction, rownames=['True'], colnames=['Predicted'], margins=True))

#10-fold cross-validation
scores = cross_val_score(knn, nba_feature, nba_class, cv=10)
print("Cross-validation scores: {}".format(scores))
print("Average cross-validation score: {:.2f}".format(scores.mean()))



