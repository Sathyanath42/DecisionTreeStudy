def info_gain(tbran, fbran, uct):

    p = float(len(tbran)) / (len(tbran) + len(fbran))
    ig = uct - p * gini(tbran) - (1 - p) * gini(fbran)
    return ig

# the info gain is given by the gini index of the starting node - the weighted gini index of the true branch
# - the weighted gini index of the false branch
# a = gini(tdata) gives the gini index of the starting dataset
# true_rows, false_rows = split(tdata, testingcondition(0, 50))
# we split the starting data set across the condition age>50
# b = info_gain(true_rows, false_rows, a)   this is a measure of how much uncertainity has been reduced by that split
# print(b)
# >>> 0.0341668057783549
