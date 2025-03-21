text = "ATG TGC CGC TTT"

list_ = text.split() # split the text into a list of strings

print(list_) # ['ATG', 'TGC', 'CGC', 'TTT']

text_1 = "ATG,TGC,CGC,TTT"

list_1 = text_1.split(",") # now using a comma as the separator
print(list_1) # ['ATG', 'TGC', 'CGC', 'TTT']

text_2 = "ATG-TGC-CGC-TTT"
list_2 = text_2.split("-", 2) # only split the first two occurrences by -
print(list_2) # ['ATG', 'TGC', 'CGC-TTT'] 

