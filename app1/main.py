print("Derail Vally Run Log Workbook")

category_list = []

while True:
    user_action = input("Type add, show, exit: ")

    match user_action:

        case "add":

            category_input = input("Enter the Category here: ")
            category_list.append(category_input)

            category_code = input("Enter Category code: ")
            category_list.append(category_code)

            item_delivering = input("Enter the item to be deliver: ")
            category_list.append(item_delivering)

            source_company = input("Enter the source company: ")
            category_list.append(category_code)

            receiving_company = input("Enter the receiving company: ")
            category_list.append(category_code)

            time_bonus_input = input("Enter time bonus: ")
            category_list.append(time_bonus_input)

            train_value_input = input("Enter train value: ")
            category_list.append(train_value_input)

            train_mass_input = input("Enter train mass: ")
            category_list.append(train_mass_input)

            train_length_input = input("Enter train length: ")
            category_list.append(train_length_input)

            license_requirements = input("Enter licenses require: ")
            category_list.append(license_requirements)

        case "show":
            print(category_list)

        case "exit":
            break

print("Goodbye")