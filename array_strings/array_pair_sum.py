def pair_sum(arr,k):
    

    if len(arr)<2:
        return
    
    seen= set()

    output=set()

    for i in arr:
        target= k-i

        if target in seen:
            output.add((min(i,target),max(i,target)))
        else:
            seen.add(i)


    #making sets for seen
  
    return output


print('\n'.join(map(str,pair_sum([1,2,3,2,4],4))))


