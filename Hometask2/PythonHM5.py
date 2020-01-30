def main():
    password = "123"
    login = input("write login: ")
    ps = input("write password: ")
    while ps != password:
        if ps != password:
            print("Password for user:", login ,"is incorrect")
            print("Try again... ")
            ps = input("write password: ")
    print("Password for user: ", login ," is correct")

main()
