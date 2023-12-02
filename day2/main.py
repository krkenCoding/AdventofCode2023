IDtotal=0
with open('day2\input.txt','r') as input:
        for index, line in enumerate(input):
            game = line.strip().split()[2:]
            print("game number:", index)
            configuration = {'red':12, 'green':13, 'blue':14}
            gameOver = False
            for element in game:
                print("element:", element)
                if element.isdigit(): digit=element
                else: 
                    for colour in configuration: 
                        if (colour in element):
                            configuration[colour]-=int(digit)
                            print("taking",digit,"away from",colour)
                            print("resulting config:", configuration)
                            if configuration[colour] < 0: 
                                gameOver = True
                                print("game over")

                    if (gameOver==True):
                        break

                    if ';' in element:
                        configuration = {'red':12, 'green':13, 'blue':14}
                        continue
                    elif "," in element:
                        continue
                    else:
                        IDtotal+= index+1
                        # You might be able to remove below
                        gameOver=False

print(IDtotal)
