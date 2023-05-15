def max_two_times(given_list):
    result=[]
    for i in given_list:
        if(result.count(i)<2):
            result.append(i)
    print("Removed",len(given_list)-len(result))
    return result

print(max_two_times([10, 10, 15, 15, 20]))
