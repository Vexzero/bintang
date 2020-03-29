import numpy as np
import cv2
import os
import sys
import subprocess
import getpass
import numpy as np
import color
try:
    if len(sys.argv) <2:
        os.system("cls||clear")
        sys.stdout.write(color.CYAN+"""
random tool
by:....

"""+color.END)
    else:
        sys.exit("Ussage : belajar.py")
        os.system("cls||clear")
    sys.stdout.write("""
1.Ascii changer
2.Email Sender
3.undescribable
4.binary converter
    """)
    try:
        print()
        halo = int(input(color.GREEN+" * tell me the number : "+color.YELLOW))
        if halo == 99:    
            ab = int(getpass.getpass(color.PURPLE+"pass: "+color.END))
            if ab == 2821:
                img = cv2.imread('290516.jpg')
                cv2.namedWindow('test',cv2.WINDOW_NORMAL)
                cv2.imshow('test',img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                os.system("cls||clear")
                os.system("python belajar.py")
            else:
                gmbr = cv2.imread('trap.jpg')
                cv2.imshow('U R not my owner',gmbr)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                os.system("cls||clear")
                
                os.system("cd Desktop")
                gmbr2 = cv2.imread('trap.jpg')
                cv2.imshow('U R not my owner',gmbr2)
                cv2.waitKey(0)
                da = cv2.destroyAllWindows()
                ab = 1
                while ab < 10:
                    os.system("start tree")
                    print(color.GREEN+"Lu buka owner gw "+color.END)
        elif halo == 1:
            str = input(color.YELLOW+"text : "+color.END)
            ascii = [ord(s) for s in str]
            print()
            print()
            print (ascii)
            os.system("python belajar.py")
        elif halo ==2:
            #some tool to send email to many people
            try:

                import smtplib
                smtp_server = 'smtp.gmail.com'
                port = 587
                email = input("Your email address: ")
                pswd = getpass.getpass("password : ")
                vmail = input("To : ")
                message = input("message : ")
            
                server = smtplib.SMTP(smtp_server,port)
                server.ehlo
                server.starttls()
                server.login(email,pswd)
                server.sendmail(email,vmail,message)
                print("success")
                server.quit()
            except smtplib.SMTPAuthenticationError:
                print("[X] check if yor username and password correct or nah")
                print("[?]check if the option of appication less security is enable")
            except KeyboardInterrupt:
                os.system("cls||clear")
                print("OK")
        elif halo == 3:
            img = cv2.imread('290516.jpg',0)
            cv2.namedWindow('image',cv2.WINDOW_NORMAL)
            cv2.imshow('image',img)
            a = cv2.waitKey(0)
            if a == 27:
                cv2.destroyAllWindows()
            elif a == ord('s'):
                cv2.imwrite('gggg.png',img)
                cv2.destroyAllWindow()
        elif halo == 4:
            bob = int(input("number : "))
            print(bin(bob)[2:])

        else:
            os.system("cls||clear")
            sys.stdout.write(color.RED+"""
=======================            
=                     =    
=    PROGRAM ENDED    =   
=                     =     
=======================            """+color.END)
    except KeyboardInterrupt:
        print("cancelled")
        os.system("cls||clear")
except KeyboardInterrupt:
    Print(color.RED+color.UNDERLINE+"[X]cancelled[X]"+color.END)
