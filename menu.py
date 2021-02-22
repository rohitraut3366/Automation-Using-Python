import webbrowser
import speech_recognition as sr


print("welcome to my new tools\n\n",end="")
print("Enter your requirements.... we are listening:")
#ch=input()
r=sr.Recognizer()
with sr.Microphone() as source:
    print("start say")
    audio=r.listen(source)
    print("speech done")

ch=r.recognize_google(audio)
print(ch)
if "date" in ch:
    webbrowser.open("http://192.168.29.151/cgi-bin/f.py?c=date")
elif "calendar" in ch:
    webbrowser.open("http://192.168.29.151/cgi-bin/f.py?c=cal")
else:
    print("Can't understand")