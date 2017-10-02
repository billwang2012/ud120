#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

noperson = len(enron_data)
print("# of persons in the list =" + str(noperson) )

key0 = enron_data.keys()[0] # keys() will return all keys
key1 = enron_data.keys()[1]

print key0
print key1

print("# of features per person =" + str( len(enron_data[key0])))

nopoi = 0

for i in enron_data.iterkeys():
    if((enron_data[i]['poi'] == True)):
        nopoi = nopoi + 1
    else:
        nopoi = nopoi

print("# of poi's in the list =" + str(nopoi))

#What is the total value of the stock belonging to James Prentice
print("# of stock of James prentice =" + str( enron_data['PRENTICE JAMES']['total_stock_value']))

#How many email messages do we have from Wesley Colwell to persons of interest?
print("# of emails from Wesley Colwell to poi =" + str( enron_data['COLWELL WESLEY']['from_this_person_to_poi']))

#What’s the value of stock options exercised by Jeffrey K Skilling? 
print("values of stock options of Jeffrey K Skilling =" + str( enron_data['SKILLING JEFFREY K']['exercised_stock_options']))

print("total payment of Jeffrey K Skilling =" + str( enron_data['SKILLING JEFFREY K']['total_payments']))
print("total payment of Andrew Fastow =" + str( enron_data['FASTOW ANDREW S']['total_payments']))
print("total payment of Kenneth L Lay =" + str( enron_data['LAY KENNETH L']['total_payments']))

########################################
def countFeature(feature = '', value = ''):
    featureNotNaN = 0
    for i in enron_data.iterkeys():
        if(feature =='' or value == ''): 
            print("please provide feature/value input\n")
        else:
            if(value == 'NotNaN'):
                if((enron_data[i][feature] != 'NaN')):
                    featureNotNaN = featureNotNaN + 1
                else:
                    featureNotNaN = featureNotNaN
            elif(value == 'NaN'):
                if((enron_data[i][feature] == 'NaN')):
                    featureNotNaN = featureNotNaN + 1
                else:
                    featureNotNaN = featureNotNaN
    return featureNotNaN
    
#######################################
salaryNotNaN = countFeature('salary','NotNaN')
print("# of persons who have a qualified salary in the list =" )
print(salaryNotNaN)


emailNotNaN = countFeature('email_address','NotNaN')
print("# of persons who have a known email address in the list =" )
print(emailNotNaN)

#How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
#What percentage of people in the dataset as a whole is this?
paymentNaN =  countFeature('total_payments','NaN')
print("# of persons who's payment is NaN =" )
print(paymentNaN)
print("percentige of who's payment is NaN =" )
print(float(paymentNaN)/noperson)

paymentNaNwithPOI = 0

for i in enron_data.iterkeys():
    if((enron_data[i]['total_payments'] == 'NaN') and (enron_data[i]['poi'] ==  True)):
        paymentNaNwithPOI = paymentNaNwithPOI + 1
    else:
        paymentNaNwithPOI = paymentNaNwithPOI

#How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
#What percentage of people in the dataset as a whole is this?
print("# of poi who's payment is NaN =" + str(paymentNaNwithPOI))
print("percentige of poi who's payment is NaN =" + str(float(paymentNaNwithPOI)/nopoi))