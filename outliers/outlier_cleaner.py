#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    ### input (predictions, ages, net_worths)
    ### output (ages, net_worths, error)
    m = len(ages)
    for i in range(m):
        cleaned_data.append((ages[i], net_worths[i], predictions[i] - net_worths[i]))
        #print(i)
        
    cleaned_data.sort(key=lambda tup: tup[2])
    
    for i in range(int(m*0.1)):
       cleaned_data.pop()
       
    return cleaned_data

