# Sources:
# https://pythonprogramming.net/change-show-new-frame-tkinter/
# https://stackoverflow.com/questions/37068708/how-to-change-font-size-in-ttk-button
# https://pythonprogramming.net/tkinter-popup-message-window/

from tkinter import *
from tkinter import ttk
import OOGym

myFont = ("Helvetica", 12)
gym = OOGym.OOGym()

class gymGUI(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Some window details
        self.title("OO CLimbing Gym")
        self.geometry("400x450+300+50")
        self.resizable(False, False)

        # Contains everything in GUI
        mainContain = Frame(self)
        # Container is all encompassing
        mainContain.pack(side="top", fill="both", expand="True")

        # Configure with min size and priority
        mainContain.grid_rowconfigure(0, weight=1)
        mainContain.grid_columnconfigure(0, weight=1)

        # This dict will hold all our window pages
        self.pages = {}

        # ******Must add new page here for it to be connected to others*********
        for P in (MainPage, CheckInPage, RoutePage, NewMemPage, GearPage):
            page = P(mainContain, self)
            self.pages[P] = page
            # The page will "stick" to entire size of the container
            page.grid(row=0, column=0, sticky="nsew")

        self.showPage(MainPage)

    def showPage(self, controller):
        # Find the page we want in the pages dictionary
        page = self.pages[controller]
        # Raise that page to the front
        page.tkraise()


def fc(say="Basic boy"):
    print(say)


class MainPage(Frame):
    def __init__(self, parent, controller):
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
                                 command=lambda: controller.showPage(CheckInPage))
        checkInButt.pack(pady=(30, 10), padx=10)

        newMemButt = ttk.Button(self, text="New Member?", style='my.TButton',
                                command=lambda: controller.showPage(NewMemPage))
        newMemButt.pack(pady=10, padx=10)

        routeButt = ttk.Button(self, text="Check Out Our Routes!", style='my.TButton',
                               command=lambda: controller.showPage(RoutePage))
        routeButt.pack(pady=10, padx=10)


class CheckInPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Making a label object
        label = Label(self, text="Enter Your Information", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="W", padx=(0, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")

        # This is for the entry boxes
        loginLabel = Label(self, text="Phone Number:", font=myFont)
        loginEntry = Entry(self)

        loginLabel.grid(row=2, column=0, sticky="E", pady=(40, 5))
        loginEntry.grid(row=2, column=1, sticky="W", pady=(40, 5))

        enterButt = ttk.Button(self, text="Enter", style='my.TButton', command=lambda: checkInValues(controller, loginEntry.get()))
        enterButt.grid(row=3, column=1, pady=(40, 10))

        signUpButt = ttk.Button(self, text="New? Sign Up Here", style='my.TButton',
                                command=lambda: controller.showPage(NewMemPage))
        signUpButt.grid(row=4, column=1, pady=10)


def checkInValues(controller, phoneLogin):
    if len(phoneLogin) == 0:
        popupFillValue()
    else:
        print(phoneLogin)
        gym.checkIn(phoneLogin)
        print(gym.dbMem)
        controller.showPage(GearPage)




class RoutePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        tFrame = Frame(self)
        label = Label(self, text="Here's some gnar gnar", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(55, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")


class GearPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # Home button
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")

        label = Label(self, text="Gear Shop", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(55, 0), pady=(50, 30))

        # Checkbox Group 1
        gS = IntVar()
        shoes = Checkbutton(self, text="Shoes", variable=gS)
        shoes.grid(row=5, column=0, sticky="E")

        gH = IntVar()
        harness = Checkbutton(self, text="Harness", variable=gH)
        harness.grid(row=5, column=1)

        gR = IntVar()
        rope = Checkbutton(self, text="Rope", variable=gR)
        rope.grid(row=5, column=2, sticky="W")

        contButt = ttk.Button(self, text="Enter", style='my.TButton',
                              command=lambda: getGearValues(controller, gS.get(), gH.get(), gR.get()))
        contButt.grid(row=9, column=1, pady = (40,0))


def getGearValues(controller, shoeVal, harnVal, ropeVal):
    print(shoeVal, harnVal, ropeVal)
    return


class NewMemPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Making a label object
        tFrame = Frame(self)
        label = Label(self, text="Make your account here", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(55, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(MainPage))
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
    # name = nameEntry.get()
    print(len(memType), climbType)
    if checkState == 0:
        popupWaiver()
    elif (len(name) or len(phone)) == 0 or (len(memType) or len(climbType)) == 0:
        popupFillValue()
    else:
        gym.adduser(name, phone, memType, climbType)
        controller.showPage(GearPage)


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
