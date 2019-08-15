#Write a Python program to remove and print every second number from a list of numbers until the
#list becomes empty
pos = 2-1
idx= 0
len_list = (len(int_list))
while  len_list > 0:
    idx = (pos + idx)% len_list

    #removes and prints the second number
    print (int_list.pop(idx))
    len_list -= 1

    nums = [40,20,300,140,1,3]
    remove_nums(nums)