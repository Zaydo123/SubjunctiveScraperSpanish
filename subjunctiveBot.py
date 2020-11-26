import requests 
from colorama import Fore
from bs4 import BeautifulSoup


tenseoptions = '1 = yo\n2 = tu\n3 = el/ella/Ud.\n4 = nosotros\n5 = ellos/ellas/Uds.'
print(Fore.GREEN + tenseoptions)

print("Give us subject and verb")
print("Ex: tu intentar")



def lookforSubject(subject):
    if int(subject) == 1:
        yo = soup.find('div',{'class': '_2xfncFkp'})[34].text
        print(yo)
    elif int(subject) == 2:
        yo = soup.find('div',{'class': '_2xfncFkp'})[38].text
        print(yo)
    elif int(subject) == 3:
        pass
    elif int(subject) == 4:
        pass
    elif int(subject) == 5:
        pass






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

