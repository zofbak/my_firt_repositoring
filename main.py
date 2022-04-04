import time

def aa():
    a = input("Wpisz swoje imie: ")
    print(f"Git! {a}")

def godzina():
    t = time.location()
    current_time = time.strftime("%H:%M:%s", t)
    print("jest godzina ", current_time)

aa()
godzina()
