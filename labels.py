import pandas as pd
import numpy as np

def get_labels():
    dir = 'training2017/'
    label = pd.read_csv(dir + 'REFERENCE.csv')
    label = label.values.tolist() # --> convert test dataframe to list
    # print(label)
    y = np.array([])
    file = []
    for t in label:
            # print(t[1])
            y = np.append(y,t[1])
            file.append(t[0])
        # print(x)
    return y,file


    
# ----------------------------------------------------------------------------------------------------------------------------
# dir = 'training2017/'
# label = pd.read_csv(dir + 'REFERENCE.csv')
# label = label.values.tolist() # --> convert test dataframe to list
# print(label)
# print(type(label))

# y = np.array([])
# file = []
# for t in label:
#         # print(t[1])
#         y = np.append(y,t[1])
#         file.append(t[0])
#     # print(x)

# y1, f1 = get_labels()
# print(y1)
# # print(type(y))
# print(f1)
# # print(type(file))

# # ==> Find an element in list
# print("Index for A00001 : ", f1.index('A00001'))

# print(f1[0])
# print(y1[f1.index('A00001')])