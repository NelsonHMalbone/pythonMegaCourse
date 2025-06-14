print("Derail Vally Run Log Workbook")

all_categories = [] # list to hold each round of the category data

while True:
    user_action = input("Type add, show, edit ,calculator ,exit: ")
    user_action = user_action.strip() # strips uncessory white spaces
    match user_action:

        case "add":
            category_list = [] # Dictionary for one round of the input
            category_data = {} # optional if still wanting the list


            category_input = input("Enter the Category here: ")
            category_list.append(category_input)
            category_data['Category: '] = category_input

            category_code = input("Enter Category code: ")
            category_list.append(category_code.capitalize())
            category_data['Category Code: '] = category_code

            item_delivering = input("Enter the item to be deliver: ")
            category_list.append(item_delivering)
            category_data['Item to be Deliver: '] = item_delivering

            source_company = input("Enter the source company: ")
            category_list.append(source_company.title())
            category_data['Source Company: '] = source_company

            receiving_company = input("Enter the receiving company: ")
            category_list.append(receiving_company.title())
            category_data['Receiving Company: '] = receiving_company

            time_bonus_input = input("Enter time bonus: ")
            category_list.append(time_bonus_input)
            category_data["Time Bonus: "] = time_bonus_input

            train_value_input = input("Enter train value: ")
            category_list.append(train_value_input)
            category_data["Train Value: "] = train_value_input

            train_mass_input = input("Enter train mass: ")
            category_list.append(train_mass_input)
            category_data["Train Mass: "] = train_mass_input

            train_length_input = input("Enter train length: ")
            category_list.append(train_length_input)
            category_data["Train Length: "] = train_length_input

            license_requirements = input("Enter licenses require: ")
            category_list.append(license_requirements)
            category_data["Licenses Required: "] = license_requirements

            base_amount_total = input("Enter the dollar amount to be received: ")
            category_list.append(base_amount_total)
            category_data["Base Amount: "] = base_amount_total

            all_categories.append(category_data) # add this to round's data to the master list

        case "show": # | "display"
            print("\n---All Entries Categories ---")
            for idx, entry in enumerate(all_categories,1):
                print(f"\nEntry #{idx}")
                for key, value in entry.items():
                    print(f"{key}: {value}")

        case "edit": # allows user to edit contracts
            number = input("Number of the contract to edit: ")
            existing_category_list = all_categories[number]
            print(existing_category_list)


        case "exit":
            break

print("Goodbye")