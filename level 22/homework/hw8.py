full_name = "YourFirstName YourLastName"
first_name = full_name[:full_name.index(" ")]
last_name = full_name[full_name.index(" ") + 1:]
print("First Name:", first_name)
print("Last Name:", last_name)