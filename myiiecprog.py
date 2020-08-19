import pyttsx3
import os
pyttsx3.speak("welcome to my tools")

while True:
	print("Welcome,Tell me your requirement:" , end='')
	p= input()

	#print(p)
	#os.system(p)

	if   ("open" in p) and ("chrome" in p):
		os.system("chrome")
		pyttsx3.speak("chrome application launched")

	elif ("start" in p) or ("notepad" in p) and ("begin" in p) or ("stop" in p):
		os.system("notepad")
		pyttsx3.speak("notepad application launched")

	elif ("go ahead" in p) or ("player" in p) and ("media" in p) or("no need" in p):
		os.system("wmplayer")
		pyttsx3.speak("window media player launched")

	elif ("execute" in p) or ("player" in p) and ("vlc" in p) or ("stop" in p):
		os.system("vlc")
		pyttsx3.speak("vlc player launched")

	elif ("setup" in p) or ("player" in p) and ("Box" in p) or ("end" in p):
		os.system("VirtualBox")
		pyttsx3.speak("virtualbox application launched")

	elif ("flash" in p) or ("clear" in p) and ("adobe" in p) or ("close" in p):
		os.system("AcroRd32")
		pyttsx3.speak("ADOBEREADER launched")

	elif ("msedge" in p) or ("microsoft" in p) and ("appear" in p) or ("chrome" in p):
		os.system("msedge")
		pyttsx3.speak("Microsoftedge browser launched")

	elif ("clear" in p) or ("SCANNER" in p) and ("scan" in p) or ("stop" in p):
		os.system("SCANNER")
		pyttsx3.speak("Your scanner has launched")

	elif ("commence" in p) or ("play" in p) and ("mp10" in p) or ("erupt" in p):
		os.system("mediaplayer10")
		pyttsx3.speak("MPplayer10 launched")

	elif ("interrupt" in p) or ("quit" in p):
		break
	
	
	else:
		print("dont support")







