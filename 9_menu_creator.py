print "Welcome to the easy menu creating program!"

menu_dict = {}

while True:
    dish = raw_input("Please enter a dish: ")
    price = int(raw_input("Please enter the price for " + dish + ": "))
    print "Your dish is " + dish + " and it costs " + str(price) + " Euro"

    new = raw_input("Would you like to enter a new dish? (yes/no) ")

    if new == "no":
        break

menu_file = open("menu.txt", "w+")  # open the TXT file (or create a new one)

print "Menu: "
menu_file.write("Menu:\n")  # write into the TXT file
print dish + " - "
menu_file.write(dish + " - ")  # add task into the TXT file

menu_file.write("\t")

print str(price) + " Euro"
menu_file.write(str(price) + " Euro" + "\n")  # add task into the TXT file

menu_file.close()  # close the TXT file

print "END"