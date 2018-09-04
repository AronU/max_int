#Texti fyrir algrím
#Tekur inn input. 
#Ef inputtið er stærra en hæsta inputtið(max_int, byrjar í 0) þá er inputtið sett 
#inn í max_int. 

max_int = 0


while max_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int < 0:
        break
    elif num_int > max_int:
        max_int = num_int




print("The maximum is", max_int)    # Do not change this line
