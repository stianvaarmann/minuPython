from random import randint

print('\n ///////ALAEALISTE HASARTMANGUD/////// \n')
print('KUI TAHAD LOPETADA, PEAB STOP OLEMA KIRJUTATUD: \n --kas koik vaiksed tahed \n --VOI KOIK SUURED TAHED')
print('\n ///////ALAEALISTE HASARTMANGUD/////// \n')
while True:
    vastus = input('VAJUTA ENTER ET MANGIDA, SISESTA "STOP" ET LOPETADA: ')
    
    if vastus == "STOP" or vastus == "stop":
        break
    elif vastus != "":
        print('TRA KYLL PIDID ENTER VAJUTAMA')
        break
    else:
        arv1 = randint(1, 7)
        arv2 = randint(1, 7)
        arv3 = randint(1, 7)

        print(f'| {arv1} | {arv2} | {arv3} |')

        if arv1 == 7 and arv2 == 7 and arv3 == 7:
            print("SA SAID RIKKAKS NEEGER")
            break
        else:
            print("PERKELE RAHA ON LAINUD PROOVI UUESTI")