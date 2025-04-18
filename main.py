from pet import Pet

def main():
    pet_name = input("Enter your pet name: ")
    my_pet = Pet(pet_name)
    
    print(f"\nYou've adopted a {my_pet.name} take good care of your new friend.\n")
    
    while True:
        print("\nWhat would you like to do with your pet?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Check status")
        print("5. Train a trick")
        print("6. Show tricks")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7):")
        
        if choice == '1':
            print(my_pet.eat())
        elif choice == '2':
            print(my_pet.sleep())
        elif choice == '3':
            print(my_pet.play())
        elif choice == '4':
            print(my_pet.get_status())
        elif choice == '5':
            trick = input("What trick would you like to teach?")
            print(my_pet.train(trick))
        elif choice == '6':
            print(my_pet.show_tricks())
        elif choice == '7':
            print(f"Goodbye take care of {pet_name}")
            break
        else:
            print("Invalid choice please try again")

if __name__ == "_main_":
   main()


