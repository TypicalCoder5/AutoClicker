import pyautogui
import appJar
 
def buttonPress(button):
    if(button == "Click!"):
        amount = int(app.getEntry("amount"))
        button = app.radioButton("click")
        if(button == "Right click"):
            button = "right"
        else:
            button = "left"
        for _ in range(amount):
            pyautogui.click(button=button)
 
app = appJar.gui("autoclicker")
app.setSize("300x200")
app.setSticky("new")
app.addLabel("Amount", row=0)
app.addEntry("amount", row=1)
app.addButton("Click!", buttonPress, row=3)
app.setSticky("e")
app.radioButton("click", "Right click", row=2)
app.setSticky("w")
app.radioButton("click", "Left click", row=2)
 
app.go()