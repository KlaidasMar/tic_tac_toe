lentele = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
zaidejas = "X"
laimetojas = None
testi_zaidima = True

while testi_zaidima:
    def zaidimo_lentele(lentele):
        print("_____________")
        print("| " + lentele[0] + " | " + lentele[1] + " | " + lentele[2] + " |")
        print("-------------")
        print("| " + lentele[3] + " | " + lentele[4] + " | " + lentele[5] + " |")
        print("-------------")
        print("| " + lentele[6] + " | " + lentele[7] + " | " + lentele[8] + " |")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯")


    def veiksmas(lentele):
        veiks = int(input("Iveskite skaiciu tarp 1-9: "))
        if lentele[veiks - 1] == "-":
            lentele[veiks - 1] = zaidejas
        else:
            print("Pasirinkite kita vieta.")


    def tikrinti_eilutes(lentele):
        global laimetojas
        if lentele[0] == lentele[1] == lentele[2] and lentele[0] != "-":
            laimetojas = lentele[0]
            return True
        elif lentele[3] == lentele[4] == lentele[5] and lentele[3] != "-":
            laimetojas = lentele[3]
            return True
        elif lentele[6] == lentele[7] == lentele[8] and lentele[6] != "-":
            laimetojas = lentele[6]
            return True


    def tikrinti_kolonas(lentele):
        global laimetojas
        if lentele[0] == lentele[3] == lentele[6] and lentele[0] != "-":
            laimetojas = lentele[0]
            return True
        elif lentele[1] == lentele[4] == lentele[7] and lentele[1] != "-":
            laimetojas = lentele[1]
            return True
        elif lentele[2] == lentele[5] == lentele[8] and lentele[2] != "-":
            laimetojas = lentele[3]
            return True


    def tikrinti_istrizaines(lentele):
        global laimetojas
        if lentele[0] == lentele[4] == lentele[8] and lentele[0] != "-":
            laimetojas = lentele[0]
            return True
        elif lentele[2] == lentele[4] == lentele[6] and lentele[4] != "-":
            laimetojas = lentele[2]
            return True


    def lygiosios(lentele):
        global testi_zaidima
        if "-" not in lentele:
            zaidimo_lentele(lentele)
            print("Lygiosios!")
            result = input("Jei norite zaisti dar karta, iveskite zodi 'taip', jei norite iseiti, zodi 'ne'.")
            if result == "ne":
                testi_zaidima = False
                print("Iki pasimatymo.")


    def laimejimas(lentele):
        global testi_zaidima
        if tikrinti_eilutes(lentele):
            zaidimo_lentele(lentele)
            print(f"Zaidejas {laimetojas} laimi!!")
            result = input("Jei norite zaisti dar karta, iveskite zodi 'taip', jei norite iseiti, zodi 'ne'.")
            if result == "ne":
                testi_zaidima = False
                print("Iki pasimatymo.")

        elif tikrinti_kolonas(lentele):
            zaidimo_lentele(lentele)
            print(f"Zaidejas {laimetojas} laimi!")
            result = input("Jei norite zaisti dar karta, iveskite zodi 'taip', jei norite iseiti, zodi 'ne'.")
            if result == "ne":
                testi_zaidima = False
                print("Iki pasimatymo.")

        elif tikrinti_istrizaines(lentele):
            zaidimo_lentele(lentele)
            print(f"Zaidejas {laimetojas} laimi!")
            result = input("Jei norite zaisti dar karta, iveskite zodi 'taip', jei norite iseiti, zodi 'ne'.")
            if result == "ne":
                testi_zaidima = False
                print("Iki pasimatymo.")


    def zaideju_pasikeitimas():
        global zaidejas
        if zaidejas == "X":
            zaidejas = "O"

        else:
            zaidejas = "X"


    print("""

                 MM              MM              
    `YMM'   `MP' MM   .g8""8q.   MM `YMM'   `MP' 
      VMb.  ,P   MM .dP'    `YM. MM   VMb.  ,P   
       `MM.M'    MM dM'      `MM MM    `MM.M'    
         MMb     MM MM        MM MM      MMb     
       ,M'`Mb.   MM MM.      ,MP MM    ,M'`Mb.   
      ,P   `MM.  MM `Mb.    ,dP' MM   ,P   `MM.  
    .MM:.  .:MMa.MM   `"bmmd"'   MM .MM:.  .:MMa.
                 MM              MM              
                 MM              MM              
      .g8""8q.   MM `YMM'   `MP' MM   .g8""8q.   
    .dP'    `YM. MM   VMb.  ,P   MM .dP'    `YM. 
    dM'      `MM MM    `MM.M'    MM dM'      `MM 
    MM        MM MM      MMb     MM MM        MM 
    MM.      ,MP MM    ,M'`Mb.   MM MM.      ,MP 
    `Mb.    ,dP' MM   ,P   `MM.  MM `Mb.    ,dP' 
      `"bmmd"'   MM .MM:.  .:MMa.MM   `"bmmd"'   
                 MM              MM              
                 MM              MM              
    `YMM'   `MP' MM   .g8""8q.   MM `YMM'   `MP' 
      VMb.  ,P   MM .dP'    `YM. MM   VMb.  ,P   
       `MM.M'    MM dM'      `MM MM    `MM.M'    
         MMb     MM MM        MM MM      MMb     
       ,M'`Mb.   MM MM.      ,MP MM    ,M'`Mb.   
      ,P   `MM.  MM `Mb.    ,dP' MM   ,P   `MM.  
    .MM:.  .:MMa.MM   `"bmmd"'   MM .MM:.  .:MMa.
                 MM              MM              
                 MM              MM                                                                                                                                                                                                                                                                      
    """)

    print("*****************************************")
    print("Sveiki atvyke i kryziuku nuliuku zaidima!")
    print("*****************************************\n")

    print("Uzeiti ant lenteles galite nurodydimi bet kuri skaiciu tarp 1-9.")
    print("Stai kaip atrodo skaitmenys lenteleje.")
    print("↓    ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓")
    print("""
_____________
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
¯¯¯¯¯¯¯¯¯¯¯¯¯\n\n""")
    print("  Pradekite  ")
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓")
    while testi_zaidima:
        zaidimo_lentele(lentele)
        veiksmas(lentele)
        laimejimas(lentele)
        lygiosios(lentele)
        zaideju_pasikeitimas()
