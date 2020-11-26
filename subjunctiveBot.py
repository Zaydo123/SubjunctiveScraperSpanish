import requests 
from colorama import Fore
from bs4 import BeautifulSoup

tenseoptions = '1 = yo\n2 = tu\n3 = el/ella/Ud.\n4 = nosotros\n5 = ellos/ellas/Uds.'
print(Fore.GREEN + tenseoptions)

print("Type number and verb, EX: '4 jugar'\n\n-----------------------------------\n")


def lookforSubject(subject):
    if int(subject) == 1:
        yo = soup.find_all('div',{'class': '_2xfncFkp'})[32].text
        print(yo)
    elif int(subject) == 2:
        yo = soup.find_all('div',{'class': '_2xfncFkp'})[36].text
        print(yo)
    elif int(subject) == 3:
        yo = soup.find_all('div',{'class': '_2xfncFkp'})[40].text
        print(yo)
    elif int(subject) == 4:
        yo = soup.find_all('div',{'class': '_2xfncFkp'})[44].text
        print(yo)
    elif int(subject) == 5:
        yo = soup.find_all('div',{'class': '_2xfncFkp'})[52].text
        print(yo)

while True:
    userinp = input("Enter: ")
    splitting = userinp.split(" ")
    if len(splitting) >= 3:
        print('Please only use one space in your input')
        break
    else:
        pass
    subject = splitting[0]
    verb = splitting[1]
    r = requests.get(f"https://spanishdict.com/conjugate/{verb}")
    soup = BeautifulSoup(r.text, 'html.parser')
    lookforSubject(subject)

