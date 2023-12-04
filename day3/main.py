totalSum = 0
def perimeterCheck(rindex, startingIndex, endingIndex):
    global totalSum
    for yRange in range(rindex-1, rindex+2):
        for xRange in range(startingIndex-1, endingIndex+2):
            if yRange==rindex and startingIndex <= xRange <= endingIndex:
                continue
            else:
                try:
                    if yRange==-1:
                        continue
                    else:
                        if grid[yRange][xRange]!=".":
                            totalSum+=int(wholeNumber)
                            return True
                except IndexError:
                    continue
                    # print(grid[yRange][xRange])
    return False
grid = []
with open('day3\input.txt','r') as input:
        for line in input:
            characters = list(line.strip())
            grid.append(characters)

for rindex, row in enumerate(grid):
    for eindex in range (140):
        try:
            if startingIndex < eindex <= endingIndex:
                continue
            else:
                # If the index is not between pairings then be sure to set values to None. 
                startingIndex = None
                endingIndex = None
        except Exception as e:
            if row[eindex].isdigit():
                # Digit Identified!
                wholeNumber = row[eindex]
                nextIndex = eindex+1
                # Before we find the next number, let's check we're not at the end of the array or if there's no following
                if nextIndex >= 140 or (row[nextIndex].isdigit() == False):
                    # If so we're going to declare the number we have and move on to the next line
                    if(perimeterCheck(rindex, eindex-1, eindex+1)):
                        print("whole digit:", wholeNumber)
                        '''print("y:",rindex) 
                        print("x range:",eindex-1,"-",eindex+1)
                        print()'''
                    continue

                # While the proceeding number is a digit...
                while row[nextIndex].isdigit():
                    # be sure to have the starting number be the eindex
                    startingIndex = eindex
                    # add the proceeding number to the whole number
                    wholeNumber += row[nextIndex]
                    # update the ending index with the current index
                    endingIndex = nextIndex
                    # increment index by one
                    nextIndex+=1
                    # If the next index would be outside of the array then break out of the while true
                    if nextIndex >= 140:
                        break
                if(perimeterCheck(rindex,startingIndex,endingIndex)):
                    print("y:",rindex) 
                    print("x range:",startingIndex,"-",endingIndex)   
                    print("whole digit:", wholeNumber)            
                print()

print(totalSum)