import random
print(" __________________________________________________________")
print("\n|Welcome to Mike's Indecisive Ass Activity Selection Picker|\n")
print(" __________________________________________________________")
print("\n\n")

activities = ["Borderlands 3", "Gears of War 5", "Path of Exile", "Watch Youtube or Twitch", "BF 4", "GTA V", "League of Legends", "Max Payne", 
	"Do A Shot", "Skyrim", "Quake", "Coding Practice", "Wolfienstein", "Max Payne", "League of Legends", "Start New Game", "Sea of Thieves", 
	"Counter Strike", "Witcher 2"]


for x in range(len(activities)):
	print("\n" + activities[x])

print ("\n")


while True:
    answer = input("\n do you want to remove an option from the list? ")
    answer = answer.strip()
    #print(answer)
    if(answer == "yes" or answer == "y" or answer == "Y" or answer == "Yes" or answer == "YES"):
        try:
            itemToRemove = input("\nplease type the item to remove as listed above: ")
            itemToRemove = itemToRemove.strip()
            activities.remove(itemToRemove)
        except ValueError:
            print("\n" + itemToRemove + " is not currently in the list of activities")
        print("\ncurrent list is as follows:")
        for x in range(len(activities)-1):
            print("\n" + activities[x])
    elif(answer == "no" or answer == "n" or answer == "N" or answer == "No" or answer == "NO"):
        print("\n\nSelecting your activity..\n\n")
        print("\nthe coding gods have selected: \"" + activities[random.randint(0,len(activities))] + "\" to be your activity")
        break

    else:
        print("\nplease enter either yes or no")