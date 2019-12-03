def cls_cnt(items):   # creates a dictionary where the keys are the unique terms in the
    cnt = dict()      # column and the values they relate to are the counts of that term
    for c in items:
        out = c[-1]
        cnt[out] = cnt.get(out, 0) + 1
    return cnt

# get(key,value to return if key doesnt exist) method returns the value of the item with the specified key
# {0: 1}
# {0: 2}
# {0: 3}
# ...
# {0: 190, 1: 1}
# {0: 190, 1: 2}
# {0: 190, 1: 3}
# ...
# final result :  {0: 190, 1: 136}


def gini(data):
    impurity = 1
    counts = cls_cnt(data)
    for t in counts:
        prob_val = counts[t] / float(len(data))
        impurity = impurity - prob_val**2
    return impurity

# probability of a value is given by its count in the column (accessed within the dictionary)
# divided by the len of the data set
# This value is subtracted from the impurity which was originally 1
# b = gini(tdata)
# >>> 0.48628100417780123 (the gini value for the original data set)
