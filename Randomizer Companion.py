from tkinter import *
from tkinter import filedialog
STATUS = "Select Input File"
FILE_SELECTED = False
Main_Window = Tk()
import time
Checks_By_Location = [
    [
        "DMC Hammer Grotto",
        "DMC Deku Scrub Grotto Left",
        "DMC Deku Scrub Grotto Center",
        "DMC Deku Scrub Grotto Right"
    ],  #DMC Hammer Grotto
    [
        "DMC Upper Grotto",
        "DMC Upper Grotto Chest"
    ],  #DMC Upper Grotto
    [
        "DMT Storms Grotto",
        "DMT Storms Grotto Chest"
    ],  #DMT Storms Grotto
    [
        "DMT Cow Grotto",
        "DMT Cow Grotto Cow"
    ],  #DMT Cow Grotto
    [
        "Colossus Grotto",
        "Colossus Deku Scrub Grotto Rear",
        "Colossus Deku Scrub Grotto Front"
    ],  #Colossus Grotto
    [
        "GV Storms Grotto",
        "GV Deku Scrub Grotto Rear",
        "GV Deku Scrub Grotto Front"
    ],  #GV Storms Grotto
    [
        "GC Grotto",
        "GC Deku Scrub Grotto Left",
        "GC Deku Scrub Grotto Center",
        "GC Deku Scrub Grotto Right"
    ],  #GC Grotto
    [
        "Graveyard Composers Grave",
        "Song from Composers Grave",
        "Graveyard Composers Grave Chest"
    ],  #Graveyard Composers Grave
    [
        "Graveyard Heart Piece Grave"
        "Graveyard Heart Piece Grave Chest"
    ],  #Graveyard Heart Piece Grave
    [
        "Graveyard Dampes Grave",
        "Graveyard Dampe Race Freestanding PoH",
        "Graveyard Hookshot Chest"
    ],  #Graveyard Dampes Grave
    [
        "Graveyard Shield Grave",
        "Graveyard Shield Grave Chest"
    ],  #Graveyard Shield Grave
    [
        "HC Storms Grotto",
        "HC GS Storms Grotto"
    ],  #HC Storms Grotto
    [
        "HF Cow Grotto",
        "HF GS Cow Grotto",
        "HF Cow Grotto Cow"
    ],  #HF Cow Grotto
    [
        "HF Inside Fence Grotto",
        "HF Deku Scrub Grotto"
    ],  #HF Inside Fence Grotto
    [
        "HF Near Kak Grotto"
        "HF GS Near Kak Grotto"
    ],  #HF Near Kak Grotto
    [
        "HF Near Market Grotto"
        "HF Near Market Grotto Chest"
    ],  #HF Near Market Grotto
    [
        "HF Open Grotto",
        "HF Open Grotto Chest"
    ],  #HF Open Grotto
    [
        "HF Southeast Grotto",
        "HF Southeast Grotto Chest"
    ],  #HF Southeast Grotto
    [
        "HF Tektite Grotto",
        "HF Tektite Grotto Freestanding PoH"
    ],  #HF Tektite Grotto
    [
        "Kak Open Grotto",
        "Kak Open Grotto Chest"
    ],  #Kak Open Grotto
    [
        "Kak Redead Grotto",
        "Kak Redead Grotto Chest"
    ],  #Kak Redead Grotto
    [
        "KF Storms Grotto",
        "KF Storms Grotto Chest"
    ],  #KF Storms Grotto
    [
        "Deku Theater",
        "Deku Theater Skull Mask",
        "Deku Theater Mask Of Truth"
    ],  #Deku Theater
    [
        "LW Scrubs Grotto",
        "LW Deku Scrub Grotto Rear",
        "LW Deku Scrub Grotto Front"
    ],  #LW Scrubs Grotto
    [
        "LH Grotto",
        "LH Deku Scrub Grotto Left",
        "LH Deku Scrub Grotto Center",
        "LH Deku Scrub Grotto Right"
    ],  #LH Grotto
    [
        "LLR Grotto",
        "LLR Deku Scrub Grotto Left",
        "LLR Deku Scrub Grotto Center",
        "LLR Deku Scrub Grotto Right"
    ],  #LLR Grotto
    [
        "LW Near Shortcuts Grotto",
        "LW Near Shortcuts Grotto Chest"
    ],  #LW Near Shortcuts Grotto
    [
        "SFM Wolfos Grotto",
        "SFM Wolfos Grotto Chest"
     ],  #SFM Wolfos Grotto
    [
        "SFM Storms Grotto",
        "SFM Deku Scrub Grotto Rear",
        "SFM Deku Scrub Grotto Front"
    ],  #SFM Storms Grotto
    [
        "ZR Open Grotto",
        "ZR Open Grotto Chest"
    ],  #ZR Open Grotto
    [
        "ZR Storms Grotto",
        "ZR Deku Scrub Grotto Rear",
        "ZR Deku Scrub Grotto Front"
    ],  #ZR Storms Grotto
    [
        "DMT Great Fairy Fountain",
        "DMT Great Fairy Reward"
    ],  #DMT Great Fairy Fountain
    [
        "Colossus Great Fairy Fountain",
        "Colossus Great Fairy Reward"
    ],  #Colossus Great Fairy Fountain
    [
        "OGC Great Fairy Fountain",
        "OGC Great Fairy Reward"
    ],  #OGC Great Fairy Fountain
    [
        "GC Shop",
        "GC Shop Item 1",
        "GC Shop Item 2",
        "GC Shop Item 3",
        "GC Shop Item 4",
        "GC Shop Item 5",
        "GC Shop Item 6",
        "GC Shop Item 7",
        "GC Shop Item 8"
    ],  #GC Shop
    [
        "HC Great Fairy Fountain",
        "HC Great Fairy Reward"
    ],  #HC Great Fairy Fountain
    [
        "Kak Potion Shop Back",
        "Kak Potion Shop Item 1",
        "Kak Potion Shop Item 2",
        "Kak Potion Shop Item 3",
        "Kak Potion Shop Item 4",
        "Kak Potion Shop Item 5",
        "Kak Potion Shop Item 6",
        "Kak Potion Shop Item 7",
        "Kak Potion Shop Item 8"
    ],  #Kak Potion Shop Back
    [
        "Kak Impas House Back",
        "Kak Impas House Cow",
        "Kak Impas House Freestanding PoH"
    ],  #Kak Impas House Back
    [
        "Kak Bazaar",
        "Kak Bazaar Item 1",
        "Kak Bazaar Item 2",
        "Kak Bazaar Item 3",
        "Kak Bazaar Item 4",
        "Kak Bazaar Item 5",
        "Kak Bazaar Item 6",
        "Kak Bazaar Item 7",
        "Kak Bazaar Item 8"
    ],  #Kak Bazaar
    [
        "Kak House of Skulltula",
        "Kak 10 Gold Skulltula Reward",
        "Kak 20 Gold Skulltula Reward",
        "Kak 30 Gold Skulltula Reward",
        "Kak 40 Gold Skulltula Reward",
        "Kak 50 Gold Skulltula Reward"
    ],  #Kak House of Skulltula
    [
        "Kak Impas House",
        "Kak Impas House Cow"
    ],  #Kak Impas House
    [
        "Kak Potion Shop Front",
        "Kak Potion Shop Item 1",
        "Kak Potion Shop Item 2",
        "Kak Potion Shop Item 3",
        "Kak Potion Shop Item 4",
        "Kak Potion Shop Item 5",
        "Kak Potion Shop Item 6",
        "Kak Potion Shop Item 7",
        "Kak Potion Shop Item 8"
    ],  #Kak Potion Shop Front
    [
        "Kak Shooting Gallery",
        "Kak Shooting Gallery"
    ],  #Kak Shooting Gallery
    [
        "Kak Windmill",
        "Song from Windmill",
    ],  #Kak Windmill
    [
        "KF Kokiri Shop",
        "KF Shop Item 1",
        "KF Shop Item 2",
        "KF Shop Item 3",
        "KF Shop Item 4",
        "KF Shop Item 5",
        "KF Shop Item 6",
        "KF Shop Item 7",
        "KF Shop Item 8"
    ],  #KF Kokiri Shop
    [
        "KF Links House",
        "KF Links House Cow"
    ],  #KF Links House
    [
        "KF Midos House",
        "KF Midos Top Left Chest",
        "KF Midos Top Right Chest",
        "KF Midos Bottom Left Chest",
        "KF Midos Bottom Right Chest"
    ],  #KF Midos House
    [
        "LH Fishing Hole",
        "LH Adult Fishing",
        "LH Child Fishing"
    ],  #LH Fishing Hole
    [
        "LH Lab",
        "LH Lab Dive",
        "LH GS Lab Crate"
    ],  #LH Lab
    [
        "LLR Stables",
        "LLR Stables Left Cow",
        "LLR Stables Right Cow"
    ],  #LLR Stables
    [
        "LLR Talons House",
        "LLR Talons Chickens"
    ],  #LLR Talons House
    [
        "LLR Tower",
        "LLR Freestanding PoH",
        "LLR Tower Left Cow",
        "LLR Tower Right Cow"
    ],  #LLR Tower
    [
        "Market Bazaar",
        "Market Bazaar Item 1",
        "Market Bazaar Item 2",
        "Market Bazaar Item 3",
        "Market Bazaar Item 4",
        "Market Bazaar Item 5",
        "Market Bazaar Item 6",
        "Market Bazaar Item 7",
        "Market Bazaar Item 8"
    ],  #Market Bazaar
    [
        "Market Bombchu Bowling",
        "Market Bombchu Bowling First Prize",
        "Market Bombchu Bowling Second Prize"
    ],  #Market Bombchu Bowling
    [
        "Market Bombchu Shop",
        "Market Bombchu Shop Item 1",
        "Market Bombchu Shop Item 2",
        "Market Bombchu Shop Item 3",
        "Market Bombchu Shop Item 4",
        "Market Bombchu Shop Item 5",
        "Market Bombchu Shop Item 6",
        "Market Bombchu Shop Item 7",
        "Market Bombchu Shop Item 8"
    ],  #Market Bombchu Shop
    [
        "Market Potion Shop",
        "Market Potion Shop Item 1",
        "Market Potion Shop Item 2",
        "Market Potion Shop Item 3",
        "Market Potion Shop Item 4",
        "Market Potion Shop Item 5",
        "Market Potion Shop Item 6",
        "Market Potion Shop Item 7",
        "Market Potion Shop Item 8"
    ],  #Market Potion Shop
    [
        "Market Shooting Gallery",
        "Market Shooting Gallery",
    ],  #Market Shooting Gallery
    [
        "Market Treasure Chest Game",
        "Market Treasure Chest Game"
    ],  #Market Treasure Chest Game
    [
        "Market Guard House",
        "Market 10 Big Poes",
        "Market GS Guard House"
    ],  #Market Guard House
    [
        "Temple of Time",
        "Sheik at Temple",
        "ToT Light Arrows Cutscene"
    ],  #Temple of Time
    [
        "ZD Shop",
        "ZD Shop Item 1",
        "ZD Shop Item 2",
        "ZD Shop Item 3",
        "ZD Shop Item 4",
        "ZD Shop Item 5",
        "ZD Shop Item 6",
        "ZD Shop Item 7",
        "ZD Shop Item 8"
    ],  #ZD Shop
    [
        "ZF Great Fairy Fountain",
        "ZF Great Fairy Reward"
    ]  #ZF Great Fairy Fountain
]

Playthrough = []


LOCATION_CONVERT = {}
TEMP = []

# Establishes new file data to be created
FILE_DATA = ["FIXED LOCATIONS"]
ENTRANCE_POINTERS = []
ENTRANCES = []

# stores the data in the new file's data and closes the old file as its no longer needed
#FILE_VAR = open(filename, "r")
#for LINE_NUM in FILE_VAR.readlines():
#    FILE_DATA.append(LINE_NUM)
#FILE_VAR.close()


def Fix_Entrances():
    for i in range(len(FILE_DATA)):
        if '"entrances"' in FILE_DATA[i]:
            ENTRANCE_POINTERS.append(i + 1)
        elif '"locations"' in FILE_DATA[i]:
            ENTRANCE_POINTERS.append(i - 1)


def SAVE_FILE():
    global FILE_SELECTED
    if FILE_SELECTED:
        refreshstatus("Patching")
        Fix_Entrances()
        Main_Window.filename = filedialog.asksaveasfilename(initialdir="/", title="Save File",
                                                            filetypes=[("Json", '*.json'), ("All files", "*.*")])
        NEW_FILE = open(Main_Window.filename+".json", "w+")
        TEST = 0
        for i in range(len(FILE_DATA)):
            if int(len(FILE_DATA)) - i > 3:
                refreshstatus(FILE_DATA[TEST])
                Main_Window.update_idletasks()
            print(int(len(FILE_DATA))+1)
            if int(len(FILE_DATA)) - i < 5:
                print(int(len(FILE_DATA)) - i)
                time.sleep(1)
            if TEST == 0:
                refreshstatus(FILE_DATA[0])
                NEW_FILE.write(FILE_DATA[0] + "\n")
            else:
                NEW_FILE.write(FILE_DATA[TEST])
            TEST = TEST + 1
        NEW_FILE.close()
        #time.sleep(.1)
        refreshstatus("File Created at: "+Main_Window.filename)

def refreshstatus(STAT):
    status = Label(Main_Window, text=str(STAT), bd=1, width=30, relief=SUNKEN, anchor=W)
    status.grid(row=1, column=0, columnspan=3, sticky=W + E)


def SELECT_FILE():
    Main_Window.filename = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                                      filetypes=(("json files", "*.json"),("all files", "*.*")))
    FILE_VAR = open(Main_Window.filename, "r")
    FILE_VAR = open(Main_Window.filename, "r")
    for LINE_NUM in FILE_VAR.readlines():
        FILE_DATA.append(LINE_NUM)
        FILE_VAR.close()

    #print(Main_Window.filename)
    global FILE_SELECTED
    FILE_SELECTED = True
    refreshstatus(Main_Window.filename)



#Main_Window.resizable(width=False, height=False)
Main_Window.geometry("372x58")
Main_Window.resizable(height = False, width = False)
Main_Window.title("Randomizer Companion")
Button_Select_File = Button(Main_Window, text="Select File", width=24, command=SELECT_FILE)
Button_Select_File.grid(row=0,column=0, sticky=W, pady=(0, 10), padx=(5,2.5))
Button_Fix_Entrances = Button(Main_Window, text="Fix Entrances", width=24, command=SAVE_FILE)
Button_Fix_Entrances.grid(row=0,column=2, pady=(0, 10), padx=(2.5,5))
refreshstatus("Select Input File")
Main_Window.mainloop()
