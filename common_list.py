def common(list1,list2):
    common_list=[]

    for item in list1:
        if item in list2:
            common_list.append(item)
    return common_list

a=[1,2,4,5,6,"kirtan","jay"]
b=[2,"kirtan","jay"]
print(common(a,b))
