_C='client.txt'
_B='chatBubble'
_A=True
import requests,json,threading
from urllib.request import urlopen
from zipfile import ZipFile
from time import sleep
from threading import Thread
def upload_bubble(file,comId):
        B=comId;C=file;A=requests.post(f"https://service.narvii.com/api/v1/x{B}/s/chat/chat-bubble/templates/107147e9-05c5-405f-8553-af65d2823457/generate",data=C,headers=cli.headers);D=json.loads(A.text)[_B]['bubbleId'];print(D);A=requests.post(f"https://service.narvii.com/api/v1/x{B}/s/chat/chat-bubble/{D}",data=C,headers=cli.headers)
        try:print(A.status_code)
        except:pass
import amino,time
try:
        with open(_C,'r')as file_:para=file_.readlines();cli=amino.Client(deviceId=para[2].strip());cli.login(email=para[0].strip(),password=para[1].strip())
except FileNotFoundError:
        with open(_C,'w')as file_:file_.write('email\npassword');print('Please enter your email and password in the file client.txt');print('-----end-----');exit(1)
@cli.event('on_text_message')
def on_text_message(data):
        msgId = data.message.messageId
        I=None;C='replyMessage';A=data
        if A.message.type==0:
                c = cli.get_user_info("f63fc94e-324c-4181-b87f-c2a500a0b23b").content
                if c == ".":
                        if A.message.content.lower()=='!copy':
                        	print('wait')
                        	try:
                        	       B=amino.SubClient(comId=A.comId,profile=cli.profile);B.get_message_info(chatId=A.message.chatId,messageId=A.message.messageId)
                        	       if A.message.extensions and A.message.extensions.get(C,I)and A.message.extensions[C].get('content',I):
                                	       D=A.message.extensions[C]['messageId'];E=B.get_message_info(A.message.chatId,D).json[_B]['resourceUrl']
                                	       B.send_message(chatId=A.message.chatId,message=f"[C]ملف الفقاعة\n\n[C]{E}",replyTo=msgId)
                                	       with urlopen(E)as F:zip=F.read();G=upload_bubble(file=zip,comId=A.comId)
                        	except Exception as H:print(H)
                else: pass
print('ready')

def socketRoot():
    j = 0
    while True:
        if j >= 300: # = 5 min
            print("updating socket....")
            cli.close()
            cli.start()
            print("updated socket!")
            j = 0
        j += 1
        time.sleep(1)
socketRoot()