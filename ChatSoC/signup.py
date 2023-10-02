import myLibs as mL
import main


path = "Login Creditionals.csv"
logCred = mL.pd.read_csv(path)
usrData = logCred.set_index("Username",drop=False)
owned=["21AD037","21AD046","21AD050","21AD052"]

def sign_up():
    while True:
        version_choice="free"
        qrpass_default="-"
        try:
            username = input(main.print_color("Enter username: ","blue"))
            if len(username)>15 or len(username)<4:
                print(main.print_color("enter username as per criteria!(4 to 15 letters)","red"))
                continue
            with open('Login Creditionals.csv', mode='r') as file:
                reader = mL.csv.DictReader(file)
                for row in reader:
                    if row['Username'] == username:
                        print(main.print_color("Username already exists!","red"))
                        break
                else:
                    password = input(main.print_color("set password: ","blue"))
                    if len(password)<4 or len(password)>15:
                        print(main.print_color("enter password bases on criteria!(4 to 8 letters)","red"))
                        continue
                    version=input(main.print_color("want premium version?(y/n)","blue"))
                    if version=="y":
                        print(main.print_color("need SoC member aurthentication","yellow"))
                        scan=main.barcode_scan()

                        if scan in owned:
                            print(main.print_color("verified by SoC member","green"))
                            print(main.print_color("scan your id!","blue"))
                            usrscan=main.barcode_scan()
                            qrpass_default=usrscan
                            version_choice="subscribed"
                        else:
                            print(main.print_color("invalid SoC member","red"))
                            print(main.print_color("Access denied!","red"))
                            continue

                    with open('Login Creditionals.csv', mode='a', newline='') as file:
                        writer = mL.csv.writer(file)
                        writer.writerow([username, password, version_choice,qrpass_default])
                        print(main.print_color("yes! you are registered for chat SoC","green"))
                    break
        except KeyboardInterrupt:
            print(main.print_color("\nKeyboardInterrupt detected. Exiting program...","red"))
            break
        except Exception as e:
            print(main.print_color(f"An error occurred: {e}. Please try again.","red"))
            continue
sign_up()
