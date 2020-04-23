import checkingIn
import DB

def main():
    test = checkingIn.checkingIn('7202195293')
    test = checkingIn.Shoes(test, '7202195293')
    test = checkingIn.Rope(test, '7202195293')
    test = checkingIn.Harness(test, '7202195293')

    #print(test.member)
    #print(test.getDescription() + " for a total: " + str(test.total()))
    test.checkout()


if __name__ == "__main__":
    main()
