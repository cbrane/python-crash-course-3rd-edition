## Strings - CHanging Case in a String with Methods

# Use title case to begin with uppercase at beginning of each word
name = "ada lovelace"
print(name.title())

# Use upper to make the whole thing uppercase
print(name.upper())

# Use lower to make the whole thing lowercase
print(name.lower())

# One way that you can use this is when storing data. You do not really want to trust the capitalization of your users, so you convert the strings to lowercase before storing them.

## Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
# F strings - the f stands for format
full_name = f"{first_name} {last_name}" # To insert a variable's value into a string, place the letter f immediately before it, and then put braces around the names of any variables you want to use in the string.
print(full_name) 

# Printing a complete message with f strings
print(f"Hello, {full_name.title()}!")

# You can also use f strings to compose a message and then assign the message to a variable
message = f"Hello, {full_name.title()}!"
print(message)

## Adding Whitespace to Strings with Tabs or Newlines

# Add a tab to your text
print("Python")
print("\tPython")

# Add a new line in a string
print("Languages:\nPython\nC\nJavaScript")

# You can also combine tabs and newlines in a single string
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace - lstrip for left side, rstrip for right side, strip for both sides
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip()) # you will see strip work here, but \/
print(favorite_language) # then, when you try to do it again, it will not stay, as it only temporarily removes the whitespace
# To permanently change , you have to associate stripped value with the variable name
favorite_language = favorite_language.lstrip()
# Right strip
favorite_language = favorite_language.rstrip()
# Strip
favorite_language = favorite_language.strip()

## Removing prefixes
# One example being a URL with a common prefix (https://)
nostarch_url =  'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)

# 2-3: Personal Message
message = "Hey man, how is your day going today?"
print(message)

# 2-4: Name Cases
someones_first_name = "Connor"
someones_last_name = "Raney"
someones_full_name = f"{someones_first_name} {someones_last_name}"
print(someones_full_name.title())
print(someones_full_name.upper())
print(someones_full_name.lower())

# 2-5: Famous Quote
famous_quote = "The best way to predict the future is to invent it."
authors_name = "Albert Einstein"
print(f'{authors_name} once said, "{famous_quote}"')

# 2-6: Famous Quote 2
message = f'{authors_name} once said, "{famous_quote}"'
print(message)

# 2-7: Stripping Names
unstripped_name = "\tConnor Raney\n"
print(unstripped_name.lstrip())
print(unstripped_name.rstrip())
print(unstripped_name.strip())

# 2-8: File Extensions
filename = "python_notes.txt"
filename = filename.removesuffix(".txt")
print(filename)




