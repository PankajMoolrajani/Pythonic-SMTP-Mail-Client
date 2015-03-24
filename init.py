from socket import *
import ssl
import base64
 
def main():
    mailserver = "smtp.gmail.com"
        port = 587
         
        sender = "sender@gmail.com"
        reciever = "reciever@gmail.com"
         
        subject = "SMPT Socket Programming
        username = sender
        password = "sender email passowrd"
         
        message = "HI, I have sent u an email from my smtp mail client."
     
    cs = socket(AF_INET, SOCK_STREAM)
    cs.connect((mailserver, port))
    recv1 = cs.recv(1024)
    print "recv1: ",
    print recv1
    if recv1[:3] != "220":
        print "220 - Reply NOT RECIEVED from server - "+mailserver
    #sslcs = ssl.wrap_socket(cs)
     
    #send hello before starttls
    cmd_ehlo = "EHLO smtp.gmail.com\r\n"
    cs.send(cmd_ehlo)
    recv2 = cs.recv(1024)
    print "recv2: ",
    print recv2
    if recv2[:3] != "250":
        print "250 - Reply NOT RECIEVED from server - "+mailserver
     
    #send starttls  
    cmd_strtls = "STARTTLS\r\n"
    cs.send(cmd_strtls)
    recv3 = cs.recv(1024)
    print "recv3: ",
    print recv3
    if recv3[:3] != "220":
        print "220 - Reply NOT RECIEVED from server - "+mailserver
     
     
    #make ssl scoket
    cs = ssl.wrap_socket(cs)
     
    #send helo after ssl tls
    cmd_ehlo = "EHLO [10.0.2.15]\r\n"
    cs.send(cmd_ehlo)
    recv4 = cs.recv(1024)
    print "recv4: ",
    print recv4
    if recv4[:3] != "250":
        print "250 - Reply NOT RECIEVED from server - "+mailserver
     
    #send auth login
    cmd_auth = "AUTH LOGIN\r\n"
    cs.send(cmd_auth)
    recv5 = cs.recv(1024)
    print "recv5: ",
    print recv5
    if recv5[:3] != "334":
        print "334 - Reply NOT RECIEVED from server - "+mailserver
 
    #send username
    cs.send(base64.b64encode(username)+'\r\n')
    recv6 = cs.recv(1024)
    print "recv6: ",
    print recv6
    if recv6[:3] != "334":
        print "334 - Reply NOT RECIEVED from server - "+mailserver
 
     
    #send password
    cs.send(base64.b64encode(password)+'\r\n')
    recv7 = cs.recv(1024)
    print "recv7: ",
    print recv7
    if recv7[:3] != "235":
        print "235 - Reply NOT RECIEVED from server - "+mailserver
 
     
    cmd_mailfrom = "MAIL FROM: <"+sender+">"+"\r\n"
    cmd_rcptto = "RCPT TO: <"+reciever+">"+"\r\n"
     
    #send mail from command
    cs.send(cmd_mailfrom)
    recv8 = cs.recv(1024)
    print "recv8: ",
    print recv8
    if recv8[:3] != "250":
        print "250 - Reply NOT RECIEVED from server - "+mailserver
     
    #send rcpt to
    cs.send(cmd_rcptto)
    recv9 = cs.recv(1024)
    print "recv9: ",
    print recv9
    if recv9[:3] != "250":
        print "250 - Reply NOT RECIEVED from server - "+mailserver
     
    #send data command
    cmd_data = "DATA\r\n"
    cs.send(cmd_data)
    recv10 = cs.recv(1024)
    print "recv10: ",
    print recv10
    if recv10[:3] != "354":
        print "354 - Reply NOT RECIEVED from server - "+mailserver
     
    #send message
    cmd_message = subject+"\r\n"+sender+"\r\n"+message+"\r\n.\r\n"
    cs.send(cmd_message)
    recv11 = cs.recv(1024)
    print "recv11: ",
    print recv11
    if recv11[:3] != "250":
        print "250 - Reply NOT RECIEVED from server - "+mailserver
     
    #send quit command to terminate
    cmd_quit = "QUIT\r\n"
    cs.send(cmd_quit)
    recv12 = cs.recv(1024)
    print "recv12: ",
    print recv12
    if recv12[:3] != "221":
        print "221 - Reply NOT RECIEVED from server - "+mailserver
     
if __name__ == "__main__":
    main()
