from difflib import SequenceMatcher
from colorama import Fore
def remove(var):
    return var.replace(" ", "")
def similar(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()*100
print(Fore.LIGHTGREEN_EX+"String Checker")
x = input(Fore.RED+"Enter First String : ")
y = input("Enter Second String : ")
text1 = x.strip()
text2 = y.strip()
if text1 == text2:
    print("The string is the same")
    print("Similarity :", end=" ")
    print(similar(text1,text2), "%")
else:
    print("The string is not the same")
    print("Similarity :", end=" ")
    print("%.2f" % similar(text1, text2) ,"%")