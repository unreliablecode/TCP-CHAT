import socket #line:1
import _thread #line:2
def encrypt (toEncrypt ,EncryptionKey):#line:4
    O00OOOO0000OO00O0 =""#line:5
    for O00OO0O0O0000O000 in toEncrypt :#line:6
        if O00OO0O0O0000O000 .isalpha ():#line:7
            O000O00OO0O00OO0O =65 if O00OO0O0O0000O000 .isupper ()else 97 #line:8
            OOO00OO00OOOOOO00 =chr ((ord (O00OO0O0O0000O000 )-O000O00OO0O00OO0O + EncryptionKey )%26 +O000O00OO0O00OO0O )#line:9
        else :#line:10
            OOO00OO00OOOOOO00 =O00OO0O0O0000O000 #line:11
        O00OOOO0000OO00O0 +=OOO00OO00OOOOOO00 #line:12
    return O00OOOO0000OO00O0 #line:13
def decrypt (toDecrypt ,DecryptionKey ):#line:15
    return encrypt (toDecrypt ,-DecryptionKey)#line:16
def main ():#line:18
    print ('='*70 )#line:19
    print ("unreliable pychat")#line:20
    print ("made by unreliablecode")#line:21
    print ("Encryption Key Harus Sama dengan lawan bicara (integer)")#line:22
    print ("v6.1023")#line:23
    print ('='*70 )#line:24
    hostname ='chat.unreliablecode.net'#line:25
    hostport =12345 #line:26
    global key #line:27
    try :#line:28
        key =int (input ('Enter Encryption Key:'))#line:29
    except :#line:30
        exit ()#line:31
    try :#line:33
        theSocket =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:34
        theSocket .connect ((hostname ,hostport ))#line:35
    except Exception as O0O0000O0O00OOO00 :#line:36
        print (f"Connection to {hostname}:{hostport} failed: {O0O0000O0O00OOO00}")#line:37
        return #line:38
    O0000OOO0OOOOOOOO =input ("Enter the room name: ")#line:40
    theSocket .send (O0000OOO0OOOOOOOO .encode ())#line:41
    print (f"Connected to {O0000OOO0OOOOOOOO}\n")#line:43
    O0O0O00000OO0OOO0 =_thread .start_new_thread (receive_messages ,(theSocket ,))#line:45
    while True :#line:48
        O0O0OOOOOO00O0O0O =encrypt (input (),key )#line:49
        if O0O0OOOOOO00O0O0O .lower ()=="exit":#line:50
            theSocket .close ()#line:51
            break #line:52
        theSocket .send (O0O0OOOOOO00O0O0O .encode ())#line:53
def receive_messages (O0OOOO000O00O000O ):#line:55
    while True :#line:56
        try :#line:57
            OO000O00OO0OOOO00 =O0OOOO000O00O000O .recv (1024 ).decode ()#line:58
            OOO0O000OO0O00000 =OO000O00OO0OOOO00 #line:59
            if (OO000O00OO0OOOO00 !='Enter your username: '):#line:60
                OOO0O000OO0O00000 =decrypt (OO000O00OO0OOOO00 ,key )#line:61
            print (OOO0O000OO0O00000 )#line:62
        except Exception as O00OO0OO000O00000 :#line:63
            print (f"Error receiving message: {O00OO0OO000O00000}")#line:64
            break #line:65
if __name__ =="__main__":#line:69
    main ()#line:70
