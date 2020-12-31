letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
#name = input("Enter Your Name\n")
#date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", 'ashish')
letter = letter.replace("<|DATE|>", '15')
print(letter)