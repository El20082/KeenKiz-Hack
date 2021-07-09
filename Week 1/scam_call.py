def get_ints_from_string(str):
		int_list = []
		for c in str:
			c_int = int(c)
			int_list.append(c_int)
		return int_list


list = get_ints_from_string(input())
sum = 0
for i in list :
    sum +=i

if sum == 20:
    print("SCAM CALL!")
else:
    print("not scam call :D")