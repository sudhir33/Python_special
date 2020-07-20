#pip install speechrecognition
#pip install pipwin
#pipwin install pyaudio
#pip install pyttsx3

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Please say something")
    audio = r.listen(source)
    print("Recognizing Now .... ")
    # recognize speech using google
    try:
        data=r.recognize_google(audio)
        print("You have said \n" + data)
        print("Audio Recorded Successfully \n ")
    except Exception as e:
        print("Error :  " + str(e))
    # write audio

    with open("myvoice.wav", "wb") as f:
        f.write(audio.get_wav_data())


    
