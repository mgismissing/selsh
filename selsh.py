selcell = 0
mincell = 0
maxcell = 8
cells = []
debug = 1

def init(min, max, sel, src):
    global selcell
    global mincell
    global maxcell
    global cells
    
    selcell = sel
    mincell = min
    maxcell = max
    cells = []

    for i in range(min, max):
        cells.append(src)

init(0, 4, 0, 0)
print("> Move by 1")
print("< Move by -1")
print("! Not gate")
print("= Set to [IN   ]")
print("? [OUT  ]")
print("0 Set to 0")
print("1 Set to 1")
code = input("[CODE ] = ")

print("[START]")
try:
    for i in range(len(code)):
        char = code[i]
        sel = cells[selcell]
        if char == ">":
            if not selcell >= maxcell - 1: selcell += 1
        if char == "<":
            if not selcell <= mincell: selcell -= 1
        if char == "!":
            if sel == 0: cells[selcell] = 1
            else: cells[selcell] = 0
        if char == "=":
            user = input("[GET ?] = ")
            cells[selcell] = 0 if user == "0" else 1
        if char == "?":
            print(f"[GET {sel}]")
    if code == "":
        print("[EMPTY]")
    print("[END  ]")
except KeyboardInterrupt:
    print("[KSTOP]")
    print("[EXIT ]")
except:
    print("[ERR  ]")