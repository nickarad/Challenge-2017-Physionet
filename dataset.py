import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import labels as lb

def load_data():
    # dir = 'training2017CSV/'
    dir = 'test/'
    counter = 0
    # ==> Find all csv files and save them in records list:
    records = [f for f in listdir(dir) if isfile(join(dir, f)) if(f.find('.csv') != -1)]
    records.sort() 
    # print(records)
    print(len(records))
    #  =========================== Create Labels ======================================================================
    y, f = lb.get_labels()
    print(y)
    print(f)
    #  ================================================================================================================
    # x = np.array([])h
    # =========================== Create train test =====================================================================================
    x_train = np.array([])
    y_train = np.array([])
    file = np.array([])
    for r in records:
        # print(r)
        test = pd.read_csv(dir + r)
        test = test.values.tolist() # --> convert test dataframe to list
        # print(r)
        if len(test)==9000:
            for char in '.csv':  
                r = r.replace(char,'')  
            # print(r)
            x = np.array([])
            for t in test:
                # print(t[1])
                x = np.append(x,t[1])
            # print(x)
            x_train = np.append(x_train,x)
            # print(x_train,counter)
            # TODO : add switch mode eg: N --> 0 etc
            y_train = np.append(y_train,y[f.index(r)])
            file = np.append(file,r)
            counter = counter + 1


    x_train = x_train.reshape(counter, 9000)
    for i in range(0, counter):
        print(file[i],y_train[i])
    
    return x_train,y_train
# ************************** End of Functiom *****************************************************

# x_train,y_train = load_data() 

# print(x_train)
# print(len(x_train))

# print(x_train)
# print(file)
