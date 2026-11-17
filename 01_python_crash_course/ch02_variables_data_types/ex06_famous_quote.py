first_name = "dutch"
last_name = "goldberg"

# Method 1: Concatenation with + (Book's approach)
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# Method 2: f-strings (Modern Python standard)
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)