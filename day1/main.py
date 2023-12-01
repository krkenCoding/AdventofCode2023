from pathlib import Path
totalValue = 0
fakeNumbers = ["one", "two", "three","four","five","six","seven","eight","nine"]
p = Path(__file__).with_name('input.txt') 
with p.open('r') as f:
    for line in f:
        print("line:",line)
        for index, fakeNumber in enumerate(fakeNumbers):
            if fakeNumber in line:
                replacement = str(fakeNumber[0] + str(index+1) + str(fakeNumber[-1]))
                line=line.replace(fakeNumber, replacement)
        print("newLine:", line)
        currentDigit=''
        for character in line:
            if character.isdigit():
                currentDigit+=(character)
                break
        revLine = reversed(line)
        for character in revLine:
            if character.isdigit():
                currentDigit+=(character)
                break
        print(currentDigit)
        print()
        totalValue += int(currentDigit)
print(totalValue)