first_name = "arthur"
last_name = "morgan"

# Method 1: Concatenation with + (Book's approach)
famous_person = first_name + " " + last_name
message = "I knew you were going to be here old fried, Mister " + famous_person.title() + "!"
print(message)

# Method 2: f-strings (Modern Python standard)
famous_person = f"{first_name} {last_name}"
message = f"It's been a long time brother, {famous_person.title()}!"
print(message)