def get_ints_from_string(str):
		int_list = []
		for c in str:
			c_int = int(c)
			int_list.append(c_int)
		return int_list

def scam_book(isbn):
    list = get_ints_from_string(isbn)
    sum = 0
    for i in range (0,len(list)) :
        if i % 2 == 0:
            sum += list[i]*1
        elif i%2 == 1:
            sum += list[i]*3
        else :
            print("????? what did u input what")

    if sum%10 == 0:
        return True
    else:
        return False

isbn_list = ["9781535607629", "9780224599051", "9787805752891", "9780508922424", "9780217323017", "9787089244371", "9787001254364", "9785237891875", "9784766597677", "9785272747259", "9781713085522", "9785567719022", "9785567719022", "9982173479036", "9782399105092"]
scam= 0
for i in range(0, len(isbn_list)):
    if scam_book(isbn_list[i]) == False:
        scam += 1
    if scam_book(isbn_list[i]) == True:
        pass
print("There are ", scam, " scam calls.")
