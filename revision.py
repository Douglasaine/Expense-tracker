while True:
    selected_option = input("Please enter 'A', 'B', or 'C', or enter 'Q' to quit: ")

    if selected_option == "A":
        print("You selected option 'A'!")
    elif selected_option == "B":
        print("You selected option 'B'!")
    elif selected_option == "C":
        print("You selected option 'C'!")
    elif selected_option == "Q":
        print("You selected option 'Q'! Quitting the menu!")
        break
    else:
        print("You selected an invalid option.")

