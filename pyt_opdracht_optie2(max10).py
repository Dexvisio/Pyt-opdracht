#1             Audi, A4, A6 
#2             BMW, 3 serie, 5 serie 
#3             Mercedes, E Klasse,  S Klasse 
#4             Porsche, 718, 911 
#Wat wil je met de bovenstaande list?  
#Type 1 voor toevoegen van automerk aan de lijst  
#Type 2 voor verwijderen van een automerk  
#Type 3 voor toevoegen van een model bij een merk             
#Type 4 voor verwijderen van een model bij een merk 
#Type 0 voor afsluiten 

automerk_lijst = {
1 : {Audi:['A4','A6']}, 
2 : {BMW:['3 serie', '5 serie']},
3 : {Mercedes:['E klasse','S klasse']},
4 : {Porsche:['718','911']}
}
#list in the list, feels like a pro 

# go while
while True:
    print('wat wil je met de bovenstaande lijst?')
    print('Type 1 voor toevoegen van automerk aan de lijst')
    print('Type 2 voor verwijderen van een automerk')
    print('Type 3 voor toevoegen van een model bij een merk')
    print('Type 4 voor verwijderen van een model bij een merk')
    print('Type 0 voor afsuluiten')
    #asking the choice, ask to the input a number 
    keuze = input('jouw keuze:')
    #fill in the number if it is equal to 0,1,2,3,4

    if keuze == "1":
        automerk = input("Voer het automerk die je wilt toevoegen:")
        #asking to input the car that user wanna add
        uitgebreid_lijst = len(automerk_lijst) + 1
         #add the new brand to the list, old code is not logical, becoz it is list in the list. append might go first, but not sure.
        #need to learn 'len'.
        automerk_lijst[uitgebreid_lijst] =             
             
             
       

        
        print(f"{automerk} is toegevoed in de lijst")
        print(" ")
        #print the freedback, and print an empty line

 # if is 2, then add for the car brand
    elif keuze == "2":
        automerk = input("Voer het automerk die je wilt verwijderen:")
        #asking to input the car that user wanna delete
        if automerk in automerk_lijst:
        #got warning, i  need to add  a conditon  if the brand is already in the list. If not, print we dont have this car brand.
            automerk_lijst.remove(automerk)
        #remove the brand from the list
            print(f"{automerk} is verwijderd van de lijst.")
            print("")
            #print the feedback that it is deleted.
        else:
                print(f"{automerk} is niet in de lijst.")
                #print we dont have this car brand.
                print("Nogweer invoeren op de menu.")
                #print asking again with menu.
                print(" ")
  # if input is 0, then kill the script.
    elif keuze == "0":
         print("Dit programa sluit af. Bedankt voor het gebruiken.")
         #tell the user this script is gonna close. 
         break
         #shutdown the script 
         
# exit the scripts
    else:
         print("Niet herkenbaar keuze. Probeer nogmaals. Hier beidt de opties van 1, 2 en 0.")
         print(" ")

# if it is outside the option, ask again.

