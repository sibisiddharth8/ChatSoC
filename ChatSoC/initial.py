# Initailize
import myLibs as mL
# Call main file
import main

# Load Dataset
# Login creditionals
path = "C:\\Users\sibis\Desktop\Chat SoC\Login Creditionals.csv"
logCred = mL.pd.read_csv(path)
usrData = logCred.set_index("Username",drop=False)

# creditionals Checking
def logCred(usrName,pswd):
    if (usrName in usrData['Username']):
        if str(usrData.loc[usrName,"Password"])==str(password):
            return True
        else:
            return False
    else:
        return False
     
#user login system    
while True:
    try:
        userName  = input(main.print_color("Enter User Name : ","blue"))
        password = input(main.print_color("Enter Password : ","blue"))
        if logCred(userName,password):
            print(main.print_color("Verified","green"))
            break
        elif (userName in usrData["Username"]) and ((usrData.loc[userName,"Version"]=="owned" or (usrData.loc[userName,"Version"]=="subscribed"))):
            choice=input(main.print_color("have SoC id to scan? (y/n):","blue"))
            if choice=="y":
                print(main.print_color("scan your SoC id to login","green"))
                bar_password=main.barcode_scan()
                if (usrData.loc[userName,"qrpass"]==bar_password):
                    print(main.print_color("Verified","green"))
                    break

        print(main.print_color("inavlid unername/password","red"))  
    except:
        print(main.print_color("oops something went wrong!","red"))
print()
print(main.print_color("Welcome to Chat SoC \n","yellow"))
print()


print()

# --------------------------- #
# Commands
txtToImg = '/text to image'
txtToAud = '/say this'
imgFrUrl = '/download image'
ytVidDownload = '/youtube video download'
quitChat = '/quit'

# --------------------------- #
chat_history=[]   # history for accurate resopnse
max_chat=10
a="one chat streach of chat can hold max upto "+str(max_chat)+" chats!"
print(main.print_color(a,"yellow"))
# --------------------------- #
chat=1
while True:
    try:
        query = input(main.print_color("Chat"+str(chat)+" : ","blue"))#read input query
        if query=="":#filter empty texts as query
            print(main.print_color("Sorry, Enter Something !","red"))
            continue
    except:
        print(main.print_color("oops! something went wrong","red")) 
        continue   

    try:
        # Generate AI Image
        if query.lower().__contains__(txtToImg):
            
            text = input(main.print_color("----> Enter your Idea to create AI Image : ","blue"))
            print()
            print(main.print_color("On Process...","green"))
            url = main.GenAiImg(text)
            # Show Generated Image
            mL.wb.open(url)

        # text to Audio
        elif query.lower().__contains__(txtToAud):
            text = input(main.print_color("----> Enter Text to Read : ","blue"))
            main.txtToAud(text)
            print(main.print_color("Command Executed","green"))

        # Download image from URL
        elif query.lower().__contains__(imgFrUrl):
            text = input(main.print_color("Enter Image URL : ","blue"))
            main.imgFrUrl(text)
            print(main.print_color("Downloaded Successfully ! , Folder : Downloads","green"))

        # Youtube video download
        elif query.lower().__contains__(ytVidDownload):
            videoUrl = input(main.print_color("Enter Video URL : ","blue"))
            main.ytVidDownload(videoUrl)
        
        elif query.lower().__contains__(quitChat):
            print(main.print_color("Thank you for using Chat SoC","yellow"))
            main.txtToAud("Thank you for using Chat SoC")
            break

        # Chat SoC
        else:
            chat_history.append(query)
            prompt_history = "\n".join(chat_history + [query])
            print(main.print_color("generating...","green"))
            generate=main.aiChat(prompt_history)
            print(generate)
            chat_history.append(generate)
            print()
        chat+=1
        if chat>max_chat:
            chat_history=[]
            print(main.print_color("max chat limit reached.chat history deleted! ","red"))
            print()
            print(main.print_color("-----------xxx----------xxx-----------","red"))
            chat=1    
    except:
        main.print_color("oops! something went wrong","red")        