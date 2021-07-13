def get_ints_from_string(str):
		int_list = []
		for c in str:
			c_int = int(c)
			int_list.append(c_int)
		return int_list

list = get_ints_from_string(input("yes "))
sum = 0
for i in range (0,len(list)) :
    if i % 2 == 0:
        sum += list[i]*1
    elif i%2 == 1:
        sum += list[i]*3
    else :
        print("????? what did u input what")

if sum%10 == 0:
    print("wow valid book!")
else:
    print("imagine printing fake book")
