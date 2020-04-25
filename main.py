import checkingIn
import DB
import GymGUI
import ClimbArea as ca


def main():
    ''''
    # OSCAR WORK
    db = DB.DB()
    member = db.getMember("1234")
    test = checkingIn.checkingIn(member)
    test = checkingIn.Shoes(test, member)
    test = checkingIn.Rope(test, member)
    test = checkingIn.Harness(test, member)

    print(test.member)
    print(test.getDescription() + " for a total: " + str(test.total()))
    '''
    #THIS RUNS GUI

    app = GymGUI.gymGUI()
    app.mainloop()

    # # test.checkout()
    #

if __name__ == "__main__":
    main()
