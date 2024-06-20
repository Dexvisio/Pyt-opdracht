#1             Audi, A4, A6 
#2             BMW, 3 serie, 5 serie 
#3             Mercedes, E Klasse,  S Klasse 
#4             Porsche, 718, 911 
#Wat wi and print an empty line
#Type 1 voor toevoegen van automerk aan de lijst  
#Type 2 voor verwijderen van een automerk  
#Type 3 voor toevoegen van een model bij een merk             
#Type 4 voor verwijderen van een model bij een merk 
#Type 0 voor afsluiten 

x = automexrk_lijst = {'Audi':['A4','A6'], 'BMW':['3 serie','5 serie'], 'Mercedes':['E klasse','S klasse'], 'Porsche':['718','911']}
#list in the list, feels like a pro 

# go while
while True:
    print('wat wil u met de bovenstaande lijst?')
    print('Type 1 voor toevoegen van automerk aan de lijst')
    print('Type 2 voor verwijderen van een automerk')
    print('Type 3 voor toevoegen van een model bij een merk')
    print('Type 4 voor verwijderen van een model bij een merk')
    print('Type 5 voor het printen van de tegenwoordig lijst')
    print('Type 0 voor afsuluiten')
    
    keuze = input('jouw keuze:')
    #asking to make a choice 
   
    
    while keuze == "1":
        automerk = input("Voer het automerk die u wilt toevoegen:")
        # asking to input the car that user wanna add
        if automerk in x:
            #if the carbrand is in the car list. 
            print(f"{automerk} is al in de lijst.")
            # print this car brand is already in our list.
            print("Nogweer invoeren op de menu.")
            # print asking again with menu.
            print(" ")
            # empty line, ready friendly in the terminal
            break
        else:
            #if the carbrand isnt in the car list.        
            x[automerk] = []
            #carbrand is the input, here is to assign a key for the brand.
            print(f"{automerk} is toegevoegd aan de lijst")
            #print the carbrand is added to the list.
            print(" ")
            # empty line, ready friendly in the terminal
            break
    
    while keuze == "2":
        automerk = input("Voer het automerk die u wilt verwijderen:")
        # asking to input the car that user wanna deletle
        if automerk in x:
            #if the carbrand is in the car list. 
            del x[automerk]
            #I tried to use 'remove', but it doesnt work. So i use del to delete the carbrand
            print(f"{automerk} invoeren op de menu.")
            # print asking again with menu.
            print(" ")
            # empty line, ready friendly in the terminal
            break
        else:
            print(f"{automerk} is niet in de lijst.")
            #print the carbrand is not in the list.
            print("Nogweer invoeren op de menu.")
            # print asking again with menu.
            print(" ")
            # empty line, ready friendly in the terminal
            break
    
    while keuze == "3":
        automerk = input("kies het automerk die u eem moedel wilt toevoegen:")
         # asking to input the carbrand which user wanna add the new model
        model = input("Voer het model naam die u " f"{automerk} wilt toevoegen:")
        # asking to add the car model to the brand that user choosed
        if automerk in x and model not in x[automerk]:
            #under the situation that carbrand is in the list, but the model isnt in any carbrand
            x[automerk].append(model)
            #it will add the model to the key, here refers to the carbrand.
            print(f"{model} is toegevoegd aan {automerk}")
            #print the carbrand is added to the list.
            print(" ")
            break
        if automerk not in x:
            #under the situation that carbrand isnt in the list 
            print(f"{automerk} is niet in de lijst.")
            #print the carbrand is not in the list.
            print("Nogweer invoeren op de menu.")
            # print asking again with menu.
            print(" ")
            # empty line, ready friendly in the terminal
            break
        else:
            print(f"{model} is al in {automerk}.")
            #print the carbrand is already in the list.
            print("Nogweer invoeren op de menu.")
            # print asking again with menu.
            print(" ")
            # empty line, ready friendly in the terminal
            break       

    while keuze == "4":
        automerk = input("kies het automerk die u eem moedel wilt verwijderen:")
        # asking to input the carbrand which user wanna delete the new model
        model = input("Voer het model naam die u " f"{automerk} wilt verwijderen:")
        # asking to delete the car model to the brand that user choosed
        if automerk in x and model in x[automerk]:
            #under the case if the model is already in the list.
            x[automerk].remove(model)
            #remove the model from the list   
            print(f"{model} is van {automerk} verwijderd.")
            #telling that the model is deleted from the carbrand list.
            print(" ")
            # empty line, ready friendly in the terminal
            break
        elif automerk in x and model not in x[automerk]:
            #if the carbrand isnt in the car list.
            print(f"{automerk} is in de lijst, maar {model} niet in {automerk} ")
            #print the carbrand is not in the list.
            print("Nogweer invoeren op de menu.")
            # print asking again with menu.
            print(" ")
            # empty line, ready friendly in the terminal
            break   
        elif automerk not in x:
            #if the carbrand isnt in the car list.
            print(f"{automerk} is niet in de lijst.")
            #print the carbrand is not in the list.
            print("Nogweer invoeren op de menu.")
            # print asking again with menu.
            print(" ")
            # empty line, ready friendly in the terminal
            break
        
    if keuze == "5":
        print(x)
        #print the list, include all the editing. 
        print(" ")
        # empty line, ready friendly in the terminal
    
  # if input is 0, then kill the script.
    if keuze == "0":
         print("Dit programa sluit af. Bedankt voor het gebruiken.")
         #tell the user this script is gonna close. 
         break
         
    if keuze not in ["0", "1", "2", "3", "4", "5"]:
         print("Niet herkenbaar keuze. Probeer nogmaals. Hier beidt de opties van 0 tot 5.")
         #tell the user that he can only type 1 to 5 and retry
         print(" ")
        # empty line, ready friendly in the terminal
