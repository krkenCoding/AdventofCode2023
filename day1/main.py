from pathlib import Path
totalValue = 0
p = Path(__file__).with_name('input.txt') 
with p.open('r') as f:
    for line in f:
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
        totalValue += int(currentDigit)
print(totalValue)