# Sources:
# https://pythonprogramming.net/change-show-new-frame-tkinter/
# https://stackoverflow.com/questions/37068708/how-to-change-font-size-in-ttk-button

from tkinter import *
from tkinter import ttk

myFont = ("Helvetica", 12)


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

        # Must add new page here for it to be connected to other
        for P in (MainPage, CheckInPage, RoutePage, NewMemPage):
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


def fc(say="Basic bitch"):
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

        enterButt = ttk.Button(self, text="Enter", style='my.TButton', command=lambda: controller.showPage(MainPage))
        enterButt.grid(row=3, column=1, pady=(40, 10))

        signUpButt = ttk.Button(self, text="New? Sign Up Here", style='my.TButton',
                                command=lambda: controller.showPage(NewMemPage))
        signUpButt.grid(row=4, column=1, pady=10)


class RoutePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        tFrame = Frame(self)
        label = Label(self, text="Here's some gnar gnar", font=14)
        label.grid(row=0, column=0, columnspan=3, sticky="N", padx=(55, 0), pady=(50, 2))

        # Lambda helps us get around parameter problems in
        homeButt = ttk.Button(self, text="Home", style='my.TButton', command=lambda: controller.showPage(MainPage))
        homeButt.grid(row=0, column=0, sticky="nw")


class NewMemPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        myFont = ("Helvetica", 12)
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

        # Checkbox Group 1
        vM = StringVar()
        memLabel = Label(self, text="Choose membership:", font=myFont)
        memLabel.grid(row=4, column=1, columnspan=2, sticky='W', pady=(15, 10))
        casMem = Radiobutton(self, text="Casual", variable=vM, value=1)
        casMem.grid(row=5, column=0, sticky="E")
        regMem = Radiobutton(self, text="Regular", variable=vM, value=2)
        regMem.grid(row=5, column=1)
        preMem = Radiobutton(self, text="Premium", variable=vM, value=3)
        preMem.grid(row=5, column=2, sticky="W")

        # Checkbox Group 2
        vC = StringVar()
        memLabel = Label(self, text="Choose climber type:", font=myFont)
        memLabel.grid(row=6, column=1, columnspan=2, sticky='W', pady=(15, 10))
        casMem = Radiobutton(self, text="Boulder", variable=vC, value=1)
        casMem.grid(row=7, column=0, sticky="E")
        regMem = Radiobutton(self, text="Top Rope", variable=vC, value=2)
        regMem.grid(row=7, column=1)
        preMem = Radiobutton(self, text="Lead", variable=vC, value=3)
        preMem.grid(row=7, column=2, sticky="W")

        # Sign yo waiver!
        cW = IntVar()
        waiver = Checkbutton(self, text="Sign Waiver", variable=cW, command=lambda: fc("Im a little gay checkbox"))
        waiver.grid(row=8, column=0, columnspan=2, pady=(10, 5), padx=(40, 0), sticky='W')

        contButt = ttk.Button(self, text="Enter", style='my.TButton', command=lambda: controller.showPage(MainPage))
        contButt.grid(row=9, column=1)
