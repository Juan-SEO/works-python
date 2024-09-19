import random

nombres = ["juan" , "ana"]
lifes = 4

rndm_name = random.choice(nombres)
list_rndm_name = list(rndm_name)


solution = ["_" for x in range(len(list_rndm_name))]


while lifes >= 0:
    print(solution)
    input_letter = input("Tell me a letter: ")
    if input_letter in list_rndm_name:      
        print("This letter is OK")
        # Write letter on solution
        for i, letra in enumerate(list_rndm_name):
            if letra == input_letter:
                solution[i] = input_letter
        #Verify if solution its winner
        if solution == list_rndm_name:
            print("You are the winner!!!!!!!!!!")
            break


    elif input_letter not in list_rndm_name:
        print("This letter isnt in the word")
        lifes -= 1
        print(f"Yo lost a life, you have {lifes} lifes")
