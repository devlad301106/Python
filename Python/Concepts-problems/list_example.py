nums = [ 23,3,34,-234,-4,33,-44]

#for n in nums:
#   if n < 0 :
#        print(n)

#for n in nums :
#    if n > 0 :
#        print(n)

#mean = sum(nums) / len(nums)
#print(mean)

#greatest = max(nums)
#index = nums.index(greatest)
#print(greatest," ",index)

#nums = list(set(nums))
#nums.sort()
#print("Second greatest number is ", nums[-2])
nums.sort()
if nums == sorted(nums) :
    print(" list is sorted!")

else :
    print("list is not sorted!")