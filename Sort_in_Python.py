# min to max
unsorted_list=[5,7,8,4,1,6,9,2]
for i in range(len(unsorted_list)):
    min_i=i
    for j in range(i+1,len(unsorted_list)):
        if(unsorted_list[j]<unsorted_list[min_i]):
            min_i=j
    unsorted_list[i],unsorted_list[min_i]=unsorted_list[min_i],unsorted_list[i]
print(unsorted_list)
# max to min
unsorted_list=[5,7,8,4,1,6,9,2]
for i in range(len(unsorted_list)):
    min_i=i
    for j in range(i+1,len(unsorted_list)):
        if(unsorted_list[j]>unsorted_list[min_i]):
            min_i=j
    unsorted_list[i],unsorted_list[min_i]=unsorted_list[min_i],unsorted_list[i]
print(unsorted_list)
