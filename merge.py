def mergeList(lst1, lst2, lst3=[], idx1=0, idx2=0):
    '''

    Objective: to merge two sorted lists via recursion.

    Parameters:
         1) list_num: the first list of numbers.
         2) list_num2: the second list of numbers which needs to be merged with the first list.
         3) list_index: the list_index argument will be used to traverse through the elements of the first list.
         4) index: the index argument will be used to traverse through the elements of the second list.

    Return value: list_num, i.e. the merged list in sorted order.

    '''
    assert idx1<len(lst1)+1
    assert idx2<len(lst2)+1
    
    if(lst1[idx1]<lst2[idx2]):
        lst3.append(lst1[idx1])
        mergeList(lst1, lst2, lst3, idx1+1, idx2)
    elif(lst1[idx1]>lst2[idx2]):
        lst3.append(lst2[idx2])
        mergeList(lst1,lst2, lst3, idx1, idx2+1)
    print(lst3)
        
        
list_num = [1, 5, 16, 27, 35, 47, 61]
list_num2 = [2, 3, 4, 10, 14, 24, 32, 44, 65, 71]
lst3=[]
mergeList(list_num,list_num2,lst3)
