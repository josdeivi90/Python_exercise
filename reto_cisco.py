def isYearLeap(year):
    leap = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

def daysInMonth(year, month):
#
    
    leap = isYearLeap(year)
    if(leap):
        meses = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        meses = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    return meses[month]


#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")