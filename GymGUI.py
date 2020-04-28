# Sources:
# https://pythonprogramming.net/change-show-new-frame-tkinter/
# https://stackoverflow.com/questions/37068708/how-to-change-font-size-in-ttk-button
# https://pythonprogramming.net/tkinter-popup-message-window/

from tkinter import *
from tkinter import ttk
import OOGym
import time
import sys

myFont = ("Helvetica", 12)



class gymGUI(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Some window details
        self.title("OO Climbing Gym")
        self.geometry("400x450+300+50")
        self.resizable(False, False)

        # Contains everything in GUI
        self.mainContain = Frame(self)
        # Container is all encompassing
        self.mainContain.pack(side="top", fill="both", expand="True")

        # Initializing gym, routes, and ticket pool
        self.__gym = OOGym.OOGym()
        self.__gym.establishRoutes()
        self._ticketPool = OOGym.ticketPool(2)


        # Configure with min size and priority
        self.mainContain.grid_rowconfigure(0, weight=1)
        self.mainContain.grid_columnconfigure(0, weight=1)

        # This dict will hold all our window pages
        self.pages = {}

        self.showPage(None, MainPage)

    def showPage(self, current ,controller):
        # Find the page we want in the pages dictionary
        page = controller(self.mainContain , self, self.__gym, self._ticketPool)
        #self.pages[controller]
        page.grid(row=0, column=0, sticky="nsew")
        # Raise that page to the front
        page.tkraise()
        del current


def fc(say="Basic boy"):
    print(say)


class MainPage(Frame):
    def __init__(self, parent, controller, gym, tickP):
        # Pass in parent class and init frame
        Frame.__init__(self, parent)
        otherFont = ("Helvetica", 15)
        # font = myFont
        # Making a label object
        label = Label(self, text="Welcome to the OO Climbing Gym!", font=otherFont)
        label.pack(pady=40, padx=10)

        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 12))

        # Lambda helps us get around parameter problems in
        checkInButt = ttk.Button(self, text="Check-In", style='my.TButton',
                                 command=lambda: controller.showPage(self,CheckInPage))
        checkInButt.pack(pady=(30, 10), padx=10)

        newMemButt = ttk.Button(self, text="New Member?", style='my.TButton',
                                command=lambda: controller.showPage(self,NewMemPage))
        newMemButt.pack(pady=10, padx=10)

        routeButt = ttk.Button(self, text="Check Out Our Routes!", style='my.TButton',
                               command=lambda: controller.showPage(self,RoutePage))
        routeButt.pack(pady=10, padx=10)

        employeeButt = Button(self, text="Employees Only", font = ("Helvetica", 8),
                               command=lambda: controller.showPage(self,EmployeePage))
        employeeButt.pack(pady=(80,0), padx=10, side = "right")

# Page for the Employees
class EmployeePage(Frame):
    def __init__(self, parent, controller, gym, tickP):
        Frame.__init__(self, parent)
        # Home button
        homeButt = ttk.Button(self, text="Home", style='my.TButton',
                              command=lambda: controller.showPage(self, MainPage))

        homeButt.pack(side=TOP, anchor=NW)

        openButt = ttk.Button(self, text="Open Gym", style='my.TButton',
                               command=lambda: openStore(controller))
        openButt.pack(pady=(110,10), padx=10)

        closeButt = ttk.Button(self, text="Close Gym", style='my.TButton',
                              command=lambda: closeQ())
        closeButt.pack(pady=10, padx=10)

        closeButt = ttk.Button(self, text="Set Next Climb Area", style='my.TButton',
                               command=lambda: changeArea(self, controller))
        closeButt.pack(pady=10, padx=10)

        # Changes the climb areas
        def changeArea(current, controller):
            popup = Tk()
            popup.wm_title("Setting Route")
            # Make it nice and center
            popup.geometry("525x175+250+200")

            nextArea = gym.ondra.getNextSet()
            oldRoutes = str(nextArea.getRoutes())

            #This changes route and returns the new routes as a string list
            newRoutes = gym.ondra.setNextRoute()
            controller.showPage(current, RoutePage)


            # Tell them what to do
            label = ttk.Label(popup, text= nextArea.name + " has been set!", font=myFont)
            label.pack(side="top", pady=10)
            oldLabel = ttk.Label(popup, text="Was: " + oldRoutes, font=("Helvetica", 8))
            oldLabel.pack(side="top", pady=10)
            newLabel = ttk.Label(popup, text="Now: " + str(newRoutes), font=("Helvetica", 8))
            newLabel.pack(side="top", pady=10)
            # Destroys pop-up when you hit ok, until next time..
            B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
            B1.pack(pady=10)
            popup.mainloop()

        # pop up to make sure they want to close the store
        def closeQ():
            popup = Tk()
            popup.wm_title("Closing")
            # Make it nice and center
            popup.geometry("250x100+350+200")
            # Tell them what to do
            label = ttk.Label(popup, text="Close Gym?", font=myFont)
            label.pack(side="top", pady=10)
            # Destroys pop-up when you hit ok, until next time..
            B1 = ttk.Button(popup, text="No", command=popup.destroy)
            B1.pack(pady=10, padx = 30, side = 'right')
            B2 = ttk.Button(popup, text="Yes", command= lambda: closing(popup))
            B2.pack(pady=10, padx = 30, side = 'left')
            popup.mainloop()


        # cals closing function
        def closing(popup):
            gym.closing()
            popup.destroy()
            sys.exit()

        # adds opening reciept to daily customer
        def openStore(controller):
            gym.openRec()
            controller.showPage(self, MainPage)

# page where they type phone number to get info from db
class CheckInPage(Frame):
    def __init__(self, parent, controller, gym,tickP):
        Frame.__init__(self, parent)
        # Making a label object
        label = Label(self, text="Enter Your Login ", font=14)
        label.grid(row=0, column=1, columnspan=3, sticky="W", padx=(10, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(self,MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")

        # This is for the entry boxes
        loginLabel = Label(self, text="Phone Number:", font=myFont)
        loginEntry = Entry(self)

        loginLabel.grid(row=2, column=0, sticky="E", padx=(25, 0), pady=(40, 5))
        loginEntry.grid(row=2, column=1, sticky="W", pady=(40, 5))

        enterButt = ttk.Button(self, text="Enter", style='my.TButton',
                               command=lambda: checkInValues(controller, loginEntry.get(), self))
        enterButt.grid(row=3, column=1, pady=(40, 10))

        signUpButt = ttk.Button(self, text="New? Sign Up Here", style='my.TButton',
                                command=lambda: controller.showPage(self,NewMemPage))
        signUpButt.grid(row=4, column=1, pady=10)

        # checks the value isn't empty
        def checkInValues(controller, phoneLogin, current):
            if len(phoneLogin) == 0:
                popupFillValue()
            else:
                tick = tickP.getTicket()
                if tick == None:
                    popupGymFull(False)
                    controller.showPage(current, MainPage)
                else:
                    gym.checkIn(phoneLogin)
                    controller.showPage(current ,GearPage)

# The page to check out where the routes are
class RoutePage(Frame):
    def __init__(self, parent, controller, gym, tickP):
        Frame.__init__(self, parent)
        tFrame = Frame(self)
        label = Label(self, text="Here's our current routes", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(5, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(None, MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")

        areaInfo = []
        areaCounter = 3
        for a in gym.ondra.areaList:
            txtN = Text(self, height=1, width=10, font=("Helvetica", 8))
            txtN.grid(row=areaCounter, column=0, padx=(10, 0), pady=(10, 0))
            txtN.insert(END, a.name + ":")
            txtN.config(state=DISABLED)
            areaCounter += 1
            txtR = Text(self, height=1, width=62, font=("Helvetica", 8))
            txtR.grid(row=areaCounter, column=0, padx=(10, 0), pady=(10, 0), sticky='E')
            txtR.insert(END, a.routes)
            txtR.config(state=DISABLED)
            areaCounter += 1
            # areaInfo.append((a.name, a.routes))
        # print("Son",str(areaInfo))

# Chekcing what gear they want page
class GearPage(Frame):
    def __init__(self, parent, controller, gym, tickP):
        Frame.__init__(self, parent)

        # Home button
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(self,MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")

        label = Label(self, text="Gear Shop", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(55, 0), pady=(50, 30))

        #This is for presenting the right gear based on your climber type
        gearOptions = [ACTIVE, DISABLED, DISABLED]

        if gym.dbMem['climbType'] == 'Top Rope':
            gearOptions[1] = ACTIVE
        elif gym.dbMem['climbType'] == 'Lead':
            gearOptions[1] = ACTIVE
            gearOptions[2] = ACTIVE

        # Checkbox Group 1
        gS = IntVar()
        shoes = Checkbutton(self, text="Shoes", variable=gS, state = gearOptions[0])
        shoes.grid(row=5, column=0, sticky="E")

        gH = IntVar()
        harness = Checkbutton(self, text="Harness", variable=gH, state=gearOptions[1])
        harness.grid(row=5, column=1)

        gR = IntVar()
        rope = Checkbutton(self, text="Rope", variable=gR, state = gearOptions[2])
        rope.grid(row=5, column=2, sticky="W")

        climbTypeLabel = Label(self, text = "Your climber type is:  " + gym.dbMem["climbType"])
        climbTypeLabel.grid(row=9, column=1, pady=(10, 0))
        changeButt = ttk.Button(self, text="Change Climber Type?", style='my.TButton', command=lambda: controller.showPage(self, ChangeGearPage))
        changeButt.grid(row=10, column=1, pady=(10, 0))

        contButt = ttk.Button(self, text="Enter", style='my.TButton',
                              command=lambda: getGearValues(controller, gS.get(), gH.get(), gR.get(), self))
        contButt.grid(row=11, column=1, pady=(70, 0))


        def getGearValues(controller, shoeVal, harnVal, ropeVal, current):
            gym.pickgear(shoeVal, ropeVal, harnVal)
            controller.showPage(current, CheckOutPage)

# page for them to change the climber type
class ChangeGearPage(Frame):
    def __init__(self, parent, controller, gym, tickP):
        Frame.__init__(self, parent)
        # Making a label object
        tFrame = Frame(self)
        label = Label(self, text="Pick your desired climber type", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(90, 0), pady=(100, 2))

        # Radio button Group 1
        cG = StringVar()
        bType = Radiobutton(self, text="Boulder", value="Boulder", variable=cG)
        bType.grid(padx = (50,0), row=5, column=0, sticky="E")
        tType = Radiobutton(self, text="Top Rope", value="Top Rope", variable=cG)
        tType.grid(row=5, column=1)
        lType = Radiobutton(self, text="Lead", value="Lead", variable=cG)
        lType.grid(row=5, column=2, sticky="W")

        contButt = ttk.Button(self, text="Back to Gear Shop", style='my.TButton',
                              command=lambda: backToGear(controller, self, cG.get()))
        contButt.grid(row=6, column=1, pady = (50,0))

        def backToGear(controller, current, climbChoice):
            #Makes sure you picked something
            if len(climbChoice) == 0:
                popupFillValue()
                controller.showPage(current, ChangeGearPage)
            else:
                # Calls function to update mongoDB
                gym.changeClimberType(gym.dbMem["phone"], climbChoice)
                # Pulls information from database
                gym.checkIn(gym.dbMem["phone"])
                #Goes back to gear page
                controller.showPage(current, GearPage)

# the checking out page
class CheckOutPage(Frame):
    def __init__(self, parent, controller, gym,tickP):
        Frame.__init__(self, parent)
        # Making a label object
        label = Label(self, text="Checking out for: " + gym.dbMem['name'], font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="W", padx=(0, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(self ,MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")
        txtN = Text(self, height=7, width=30, font=("Helvetica", 12))
        txtN.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))
        txtN.insert(END, gym.showReceipt())
        txtN.config(state=DISABLED)

        txtz = Text(self, height=1, width=30, font=("Helvetica", 12))
        txtz.grid(row=8, column=0, padx=(10, 0), pady=(10, 0))
        txtz.insert(END, "Total with " + gym.dbMem['memType'] + " membership: $" + str(gym.gMember.total()) )
        txtz.config(state=DISABLED)


        contButt = ttk.Button(self, text="Check Out", style='my.TButton',
                              command=lambda: checkOut(controller , self))
        contButt.grid(row=9, column=1, pady=(40, 0))

        def checkOut(controller, current):
            gym.checkOut();
            print("Receipt added")
            controller.showPage(current, MainPage)

# the new membership page
class NewMemPage(Frame):
    def __init__(self, parent, controller, gym, tickP):
        Frame.__init__(self, parent)
        # Making a label object
        tFrame = Frame(self)
        label = Label(self, text="Make your account here", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(45, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(self, MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")

        # This is for the entry boxes
        nameLabel = Label(self, text="Name:", font=myFont)
        phoneLabel = Label(self, text="Phone #:", font=myFont)
        nameEntry = Entry(self)
        phoneEntry = Entry(self)

        nameLabel.grid(row=2, column=0, sticky="E", pady=(20, 5))
        nameEntry.grid(row=2, column=1, sticky="W", pady=(20, 5))

        phoneLabel.grid(row=3, column=0, sticky="E", pady=10)
        phoneEntry.grid(row=3, column=1, sticky="W", pady=10)

        # Radio button Group 1
        vM = StringVar()
        memLabel = Label(self, text="Choose membership:", font=myFont)
        memLabel.grid(row=4, column=1, columnspan=2, sticky='W', pady=(15, 10))
        casMem = Radiobutton(self, text="Casual", value="Casual", variable=vM)
        casMem.grid(row=5, column=0, sticky="E")
        regMem = Radiobutton(self, text="Regular", value="Regular", variable=vM)
        regMem.grid(row=5, column=1)
        preMem = Radiobutton(self, text="Premium", value="Premium", variable=vM)
        preMem.grid(row=5, column=2, sticky="W")

        # Radio button Group 2
        vC = StringVar()
        memLabel = Label(self, text="Choose climber type:", font=myFont)
        memLabel.grid(row=6, column=1, columnspan=2, sticky='W', pady=(15, 10))
        casMem = Radiobutton(self, text="Boulder", value="Boulder", variable=vC)
        casMem.grid(row=7, column=0, sticky="E")
        regMem = Radiobutton(self, text="Top Rope", value="Top Rope", variable=vC)
        regMem.grid(row=7, column=1)
        preMem = Radiobutton(self, text="Lead", value="Lead", variable=vC)
        preMem.grid(row=7, column=2, sticky="W")

        # Sign yo waiver!
        cW = IntVar()
        waiver = Checkbutton(self, text="Sign Waiver", variable=cW)
        waiver.grid(row=8, column=0, columnspan=2, pady=(10, 5), padx=(40, 0), sticky='W')

        contButt = ttk.Button(self, text="Enter", style='my.TButton',
                              command=lambda: getNewMemValues(controller, nameEntry.get(), phoneEntry.get(), vM.get(),
                                                              vC.get(), cW.get()))
        contButt.grid(row=9, column=1)

        def getNewMemValues(controller, name, phone, memType, climbType, checkState):
            if checkState == 0:
                popupWaiver()
            elif (len(name) or len(phone)) == 0 or (len(memType) or len(climbType)) == 0:
                popupFillValue()
            else:
                gym.adduser(name, phone, memType, climbType)

                tick = tickP.getTicket()
                if tick == None:
                    popupGymFull(True)
                    controller.showPage(current, MainPage)
                else:
                    gym.checkIn(phone)
                    controller.showPage(self, GearPage)


# This pop-up will display if you have not filled out the waiver
def popupWaiver():
    popup = Tk()
    popup.wm_title("!!!")
    # Make it nice and center
    popup.geometry("250x100+350+200")
    # Tell them what to do
    label = ttk.Label(popup, text="You must sign the waiver fool", font=myFont)
    label.pack(side="top", pady=10)
    # Destroys pop-up when you hit ok, until next time..
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack(pady=10)
    popup.mainloop()


# This pop-up will display if you have not filled out all the values asked
def popupFillValue():
    popup = Tk()
    popup.wm_title("!!!")
    # Make it nice and center
    popup.geometry("250x100+350+200")
    # Tell them what to do
    label = ttk.Label(popup, text="Please enter all the information", font=myFont)
    label.pack(side="top", pady=10)
    # Destroys pop-up when you hit ok, until next time..
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack(pady=10)
    popup.mainloop()

# This pop-up will display if gym is full.
def popupGymFull(newMemBool):
    popup = Tk()
    popup.wm_title("We're Sorry")
    # Make it nice and center
    popup.geometry("300x120+350+200")
    # Says something different depending on what screen it is triggered
    if newMemBool == False:
        label = ttk.Label(popup, text="We are sorry but the gym is at capacity", font=myFont)
        label.pack(side="top", pady=10)
    else:
        label = ttk.Label(popup, text="Account Created Succesfully", font=myFont)
        label.pack(side="top", pady=2)
        label2 = ttk.Label(popup, text="However Gym is Currently Full", font=myFont)
        label2.pack(side="top", pady=(2,10))
    # Destroys pop-up when you hit ok, until next time..
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack(pady=10)
    popup.mainloop()
