aasta = int("sisesta aasta: ")

if(aasta % 4 == 0 and aasta % 100!= 0) or (aasta % 400 == 0):
    print(f"{aasta} on liigaasta")
else: print(f"{aasta} ei ole liigaasta")