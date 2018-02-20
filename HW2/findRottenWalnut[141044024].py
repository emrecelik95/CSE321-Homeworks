def compareScales (leftScaleList, rightScaleList):
	result = sum(leftScaleList) - sum(rightScaleList)
	if result < 0:
		return 1
	elif result > 0:
		return -1
	else:
		return 0

def indexOfRottenWalnut(wList):
        size = len(wList)
        result = 0
        
        if(size == 1):
                return 0
        if(size == 2):
                return 0 if (compareScales(wList[0:size//2],wList[size//2:size]) == 1) else 1
        
        
        if(size % 2 == 0):
                result = compareScales(wList[0:size//2],wList[size//2:size])
        else:
                result = compareScales(wList[0:size//2],wList[size//2 + 1:size])


        if (result == 1):
                return indexOfRottenWalnut(wList[0:size//2])
        elif (result == -1):
                return size//2 + indexOfRottenWalnut(wList[size//2:])

        else:
                return size//2


         
print (indexOfRottenWalnut([1,1,0.5,1,1]))
