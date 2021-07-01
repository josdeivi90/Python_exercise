'''año = int(input('Introduce un año: '))
leap = True
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False
'''#1900, 2000, 2016, 1987
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
# coloca tu código aquí
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")