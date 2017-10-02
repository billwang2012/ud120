#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:len(features_train)/1]
labels_train = labels_train[:len(labels_train)/1] 

#########################################################
### your code goes here ###
#from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#clf = GaussianNB()
clf = SVC(kernel = 'rbf', C=10000)

#t0 = time()
clf.fit(features_train, labels_train)
#print ("training time:" + str(round(time()-t0, 3)) + "s")

predictions = clf.predict(features_test)

print("total no. of test set =" + str(predictions.shape[0]))
print("no. of predicted Chris class =" + str(np.sum(predictions)))

print("predictions[10] =" + str( predictions[10] ) )
print("predictions[26] =" + str( predictions[26] ) )
print("predictions[50] =" + str( predictions[50] ) )

print("accuracy =" + str(clf.score(features_test,labels_test)) )
#########################################################


