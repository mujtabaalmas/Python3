import re

text = "Contact us at Siarra@example.com, test1@domain.org or test.2@site.co.uk"
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
print("All Emails: ",emails)

#checking is the number is valid or not 
number = "+92-333-33333"
match = re.fullmatch(r"\+92-\d{3}-\d{7}", number)
print("Valid" if match else "Invalid")

#extracting all capital words
text = "Ali and Sarah went to Islamabad to meet Mr. Raza."
cap_words = re.findall(r"\b[A-Z][a-z]*\b", text)
print("All capital words: ",cap_words)

#spliting names from string
sentence = "Ali, Sara; John     Alex"
parts = re.split(r"[,\s;]+", sentence)
print(parts)

#clearing unsual spaces in the string
messy = "This   is     a   line     with  extra  spaces."
cleaned = re.sub(r"\s+", " ", messy)
print("After Clearing spaces: ",cleaned)

#checking if the variable name is valid or not 
identifier = "_myVar123"
is_valid = re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier)
print("Valid Identifier" if is_valid else "Invalid Identifier")


post = "Loving the vibes! #Summer #Travel #PythonRocks"
hashtags = re.findall(r"#\w+", post)
print("All hashtags in the string: ",hashtags)

#checking is input password is strong match or weak match 
password = "MyP@ssw0rd123"
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$"
print("Strong" if re.fullmatch(pattern, password) else "Weak")

#extracting all dates from the text or string 
text = "My birthdate is 15/12/2001 and graduation was on 15/10/2024."
dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
print("All dates in string: ",dates)

#removing html tags from the strings 
html = "<h1>Hello</h1><p>This is a <b>test</b></p>"
clean_text = re.sub(r"<.*?>", "", html)
print("After Removing tags: ",clean_text)
