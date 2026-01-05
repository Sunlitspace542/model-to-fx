import os
import sys
import fileinput
import fnmatch

#-----------------------STEP 1: GETTING INFO ABOUT THE FILE---------------------

lines = []
with open('readytoconvert.txt') as f:
    lines = f.readlines()

IFFACE = 0
IFEDGE = 0

for line in lines:
    NORM = f"{line}"
    if NORM.replace("f ", "") == NORM[2:]:
        IFFACE = 1

for line in lines:
    NORM = f"{line}"
    if NORM.replace("l ", "") == NORM[2:]:
        IFEDGE = 1
print (IFEDGE)
print (IFFACE)

count = 0
VERTSL = []
print ("vert points")
for line in lines:
    count += 1
    NORM = f"{line}"
    #print(NORM)
    if NORM.replace("v ", "") == NORM[2:]:
        print(NORM)
        VERTSL.extend ([count])

print ("on lines",VERTSL)

count = 0

if IFFACE == 1:
    FACESL = []
    print ("faces")
    for line in lines:
        count += 1
        NORM = f"{line}"
        print(NORM)
        if NORM.replace("f ", "") == NORM[2:]:
            print(NORM)
            FACESL.extend ([count])

count = 0

if IFEDGE == 1:
    EDGESL = []
    for line in lines:
        count += 1
        NORM = f"{line}"
        print(NORM)
        if NORM.replace("l ", "") == NORM[2:]:
            print(NORM)
            EDGESL.extend ([count])

if IFFACE == 1:
    print (FACESL[0], "and", FACESL[-1])
if IFEDGE == 1:
    print (EDGESL[0], "and", EDGESL[-1])

#-----------------------STEP 2: MAKING THE FILE---------------------

os.system("if exist 3DG1.txt del 3DG1.txt")

videoscape = open("3DG1.txt", "w")

#Write 3DG1 magic
videoscape.write("3DG1\n")

vertamount = VERTSL[-1]-VERTSL[0]+1

#Number of points
videoscape.write(str(vertamount))
videoscape.write("\n")

#Write points
count = 0
for line in lines:
    count += 1
    NORM = f"{line}"
    if NORM.replace("v ", "") == NORM[2:]:
        NORM = NORM[2:]
        print(NORM)
        videoscape.write(NORM)

#Parse and write faces/lines
if IFFACE == 1:
    OVERALLRANGE=1000
    
    countA=int(0)
    count = 0
    rangestuff=int(FACESL[-1])
    
    for countA in range(OVERALLRANGE):
        countA +=1
        
        BAK = int(OVERALLRANGE-countA)
        #print(BAK)
        
        REP ="/" + str(BAK)
        REP2 ="//" + str(BAK)
        REP =str(REP)
        REP2 =str(REP2)
        #line=line.replace(REP, "")
        count = 0
        
        for count in range(rangestuff):
            #count += 1
            TEMP = lines[count]
            TEMP = TEMP.replace(REP2, "")
            TEMP = TEMP.replace(REP, "")
            
            lines[count] = TEMP
    print (lines)
    
    COLL = 0
    EDGECOLL = 0
    count = 0  
    count2 = 0
    START = FACESL[0]-2
    END = FACESL[-1]+1
    os.system("cls")
    
    print(START)
    print(END)
    
    #os.system("pause")

    dummy =str(1)

    print ("start of fun")
    
    for line in lines:
        count +=1
        #for count in range(START,END):
        if count in range(START,END):
            count2 += 1
            
            if count2 == 4:
                #this makes things work, i don't know why
                pass
            
            readytoprint = f"{line}"
            
            if readytoprint[0:2] == "un":
                print ("FOUND VN INSTEAD")
            
            elif readytoprint[0:1] == "s":
                print("FOUND s THING INSTEAD")
            
            elif readytoprint[0:1] == "g":
                print("FOUND g THING INSTEAD")
            
            elif readytoprint[0:9] == "usemtl FE":
                EDGECOLL = readytoprint.replace("usemtl FE","")
            
            elif readytoprint[0:9] == "usemtl FX":
                COLL = readytoprint.replace("usemtl FX","")
            
            elif readytoprint[0:6] == "usemtl":
                os.system("cls")
                print ("MATERIAL NAME USES INCORRECT FORMAT")
                print ("USE FX1 FX2 FX3 etc")
                os.system("pause")
            
            else:
            
                readytoprint = readytoprint[2:]
                FACEAM = readytoprint.count(' ')
                FACEAM = FACEAM+1
                readytoprint = readytoprint.replace("\n","")
                # decrease leading vertex indices by 1
                parts = readytoprint.split()
                new_parts = []
                for tok in parts:
                    sub = tok.split('/')
                    if len(sub) > 0:
                        try:
                            sub0 = int(sub[0]) - 1
                            sub[0] = str(sub0)
                        except Exception:
                            pass
                    new_parts.append('/'.join(sub))
                new_ready = ' '.join(new_parts)
                print(FACEAM, new_ready)
                videoscape.write(str(FACEAM) + " " + new_ready + " " + str(COLL))
            
            #videoscape.write("\n")

#os.system("cls")
print(IFEDGE)


if IFEDGE == 1:        
    count = 0
    #os.system("pause")
    for line in lines:
        count += 1
        NORM = f"{line}"
        print(NORM)
        #os.system("pause")
        
        if NORM.replace("l ", "") == NORM[2:]:
            # decrease leading vertex indices by 1
            content = NORM[2:].strip()
            toks = content.split()
            new_toks = []
            for t in toks:
                try:
                    new_toks.append(str(int(t) - 1))
                except Exception:
                    new_toks.append(t)
            NORM = "2 " + " ".join(new_toks) + " " + str(EDGECOLL)
            print(NORM)
            videoscape.write(NORM)

#write EOF marker
videoscape.write("\x1a")
videoscape.close()
#os.system("pause")
