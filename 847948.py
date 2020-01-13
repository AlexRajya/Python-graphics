#847948 - Python Coursework
from graphics import * 

def getinputs():
    chosencols = [] #new list for chosen colours
    while True: #Repeats until a valid input is given, then exits the loop
        size = input("Enter size(5,7,9): ")
        if size in ['5','7','9']:
            break
        else:
            print("Invalid input, try again.")

    for i in range(1,4):
        while True: #Checks if 3 unique colours from the list are inputted
            temp = (input("Enter colour "+str(i)+": ")).lower()
            if temp in ['red','green','blue','magenta','orange','pink']:
                if chosencols.count(temp) == 0:
                    chosencols.append(temp)
                    break
                else:
                    print('Colour already entered, try again.')
            else:
                print('Invalid input, try again')
    return int(size), chosencols#Returns colours and size
            
def drawpatch1(colour,x,y,win):
    border = Rectangle(Point(x,y),Point(x+100,y+100)) 
    border.draw(win) #Draws border around patch
    
    patch = [] #Creates a empty list for each item to be written into 
    
    startx = x 
    starty = y + 100
    starty2 = y
    for i in range(5): #Draws patch corresponding to last UP number
        startx = startx + 20
        starty = starty - 20
        starty2 = starty2 + 20 
       
        line = Line(Point(x,starty),Point(startx,y+100))
        line.setFill(colour),patch.append(line),line.draw(win)
       
        line2 = Line(Point(startx,y),Point(x+100,starty))
        line2.setFill(colour),patch.append(line2),line2.draw(win)
       
        line3 = Line(Point(startx,y),Point(x,starty2))
        line3.setFill(colour),patch.append(line3),line3.draw(win)
        
        line4 = Line(Point(startx,y+100),Point(x+100,starty2))
        line4.setFill(colour),patch.append(line4),line4.draw(win)
    return patch #Returns list of items to go into list of patches

def shapespatch2(colours,patch,xpos,ypos,win,x,y):
    if y == ypos+20 or y == ypos+60: #Checks which line is being drawn
        if x == xpos+20 or x == xpos+60: #Checks which shape is being drawn
            tri1 = Polygon(Point(x,y),Point(x,y+20),Point(x+10,y+10))
            tri1.setFill(colours), patch.append(tri1), tri1.draw(win)
            tri2 = Polygon(Point(x+10,y),Point(x+10,y+20),Point(x+20,y+10))
            tri2.setFill(colours), patch.append(tri2), tri2.draw(win)
        else:
            circle = Circle(Point(x+10,y+10),10)
            circle.setFill(colours),patch.append(circle),circle.draw(win)
    else:
        if x == xpos+20 or x == xpos+60:   
            circle = Circle(Point(x+10,y+10),10)
            circle.setFill(colours),patch.append(circle),circle.draw(win)
        else:
            tri1 = Polygon(Point(x,y),Point(x+10,y+10),Point(x+20,y))
            tri1.setFill(colours), patch.append(tri1), tri1.draw(win)
            tri2 = Polygon(Point(x,y+10),Point(x+10,y+20),Point(x+20,y+10))
            tri2.setFill(colours), patch.append(tri2), tri2.draw(win) 
                              
def drawpatch2(colours,xpos,ypos,win):
    border = Rectangle(Point(xpos,ypos),Point(xpos+100,ypos+100))
    border.draw(win) #Draws border
    
    patch = [] #Empty patch for each item in patch
    for y in range(ypos,ypos+100,20): #Draws patch corresponding to 5th UP number
        for x in range(xpos,xpos+100,20):
           shapespatch2(colours,patch,xpos,ypos,win,x,y) 
        x = xpos
        
    return patch #Returns list of items to go into list of patches
        
def replace(temp,patches,x,y,win,layout,yxlayout):#Switches patch design
    if patches[int(temp)] != 1:
        for item in patches[int(temp)]:#Removes old patch
            item.undraw()
    
    for i in range(len(layout)):
        if str(yxlayout) == layout[i]:
            colour = layout[i+1]
            
    if len(patches[int(temp)]) < 21: #Checks which patch is currently drawn 
        patches.pop(int(temp))#Removes old patch from list
        patches.insert(int(temp),drawpatch2(colour,int(x)*100,int(y)*100,win))
    else:
        patches.pop(int(temp))
        patches.insert(int(temp),drawpatch1(colour,int(x)*100,int(y)*100,win))
        
def changecol(temp,patches,x,y,colour,win,layout,yxlayout):#Draws patch in colour
    if patches[int(temp)] != 1:
        for item in patches[int(temp)]:#Removes old patch
            item.undraw()
            
    for i in range(len(layout)):
        if yxlayout == layout[i]:
            layout[i+1] = colour
        
    patches.pop(int(temp)) #Removes old patch from list
    patches.insert(int(temp),drawpatch1(colour,int(x)*100,int(y)*100,win))
    
def extrafeatures(size,colours,win,patches,layout):
    xy = win.getMouse() #Gets mouse click
    y = int(xy.getY()/100)
    x = int(xy.getX()/100)
    
    thickborder = Rectangle(Point(x*100,y*100),Point(x*100+100,y*100+100))
    thickborder.setWidth(3), thickborder.draw(win)
    
    patchespos = [] #Creates list to determine patch positions in main list
    pos = 0
    for i in range(size):
        for item in range(size):
            patchespos.append(str(i)+str(item))
            patchespos.append(pos)
            pos = pos + 1 
            
    yxlayout = str(y)+str(x) #Gets position of patch in list of patches
    for i in range(len(patchespos)):
        if yxlayout == patchespos[i]:
            temp = patchespos[i+1]
            break     
            
    cols = ['red','green','blue','magenta','orange','pink']
    key = win.getKey()
    while key != "Return": #Repeats until enter is pressed to deselect the patch
        if key in ['d','r','s','g','b','o','m','p']:
            if key == 'd': #Deletes patch
                if patches[int(temp)] != 1:
                    for item in patches[int(temp)]:
                        item.undraw()
                patches.pop(int(temp)),patches.insert(int(temp),1)
                #^Replaces patch with 1 in list to say its been deleted
            if patches[int(temp)] != 1:#checks if patch is deleted
                if key == 's': #Switches patch if not deleted already
                    replace(temp,patches,x,y,win,layout,yxlayout)
            if patches[int(temp)] == 1: #Draws if patch has been deleted
                for i in range(len(cols)):
                    if key == (cols[i])[0]:
                        changecol(temp,patches,x,y,cols[i],win,layout,yxlayout)
        key = win.checkKey()
    thickborder.undraw() #Undraws border
                
def main():
    size, colours = getinputs() #get user inputs for size and colour
    win = GraphWin("Coursework - 847948",(size*100),(size*100)) #Creates window 
    win.setBackground('white')
    patches = [] #List for all patches to be in
    layout = []#List for colour layout
    
    cpos = 0 #Close starting pos
    fpos = size-1 #Far starting pos
    for y in range(size):#Drawing Pattern with patches based on size
        for x in range(size):
            if (fpos < x < cpos) or (cpos < x < fpos):
                patches.append(drawpatch2(colours[1],x*100,y*100,win))
                layout.append(str(y)+str(x)), layout.append(colours[1])
            elif x == cpos or x == fpos:
                patches.append(drawpatch1(colours[0],x*100,y*100,win))
                layout.append(str(y)+str(x)), layout.append(colours[0])
            else:
                patches.append(drawpatch1(colours[2],x*100,y*100,win))
                layout.append(str(y)+str(x)), layout.append(colours[2])
        cpos = cpos + 1
        fpos = fpos - 1
    
    while True: #Calls challenge section forever as no exit button was stated
        extrafeatures(size,colours,win,patches,layout)
main() #Calls main function to begin program