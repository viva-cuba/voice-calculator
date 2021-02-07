from gtts import gTTS
import playsound
import speech_recognition as sr
import os
import time
import random



def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("слушаю тебя:")
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError as e:
        return "ошибка"


def do_tris_command(message):
    message = message.lower()

    if "привет" in message:
        say_message("здорова")

    elif "открой калькулятор" in message:
        say_message("диктуй")
        num_1 = int(listen_command())
        say_message(str(num_1))
        choise = listen_command()
        say_message(str(choise))
        num_2 = int(listen_command())
        say_message(str(num_2))
    
        if choise == "плюс":
            say_message(str('{} "плюс" {} = '.format(num_1, num_2)))
            say_message(str(num_1 + num_2))

        if choise == "минус":
            say_message(str('{} "минус" {} = '.format(num_1, num_2)))
            say_message(str(num_1 - num_2))

        if choise == "умножить":
            say_message(str('{} "умножить" {} = '.format(num_1, num_2)))
            say_message(str(num_1 * num_2))

        if choise == "разделить":
            say_message(str('{} "разделить" {} = '.format(num_1, num_2)))
            say_message(str(num_1 / num_2))

        if choise == "возвести в степень":
            say_message(str('{} "возводим в степень" {} = '.format(num_1, num_2)))
            say_message(str(num_1 ** num_2))

    elif "открой другой калькулятор" in message:
            say_message("говори")
            num_1 = float(listen_command())
            say_message(str(num_1))
            choise = listen_command()
            say_message(str(choise))
            num_2 = float(listen_command())
            say_message(str(num_2))

            if choise == "плюс":
                say_message(str('{} + {} = '.format(num_1, num_2)))
                say_message(str(num_1 + num_2))

                
            if choise =="минус":
                    say_message(str('{} - {} = '.format(num_1, num_2)))
                    say_message(str(num_1 - num_2))

            if choise =="умножить":
                    say_message(str('{} * {} = '.format(num_1, num_2)))
                    say_message(str(num_1 * num_2))
                    
            if choise =="разделить": 
                    say_message(str('{} / {} = '.format(num_1, num_2)))
                    say_message(str(num_1 / num_2))

            if choise =="возвести в степень": 
                    say_message(str('{} ** {} = '.format(num_1, num_2)))
                    say_message(str(num_1 ** num_2))

    elif "открой помощь" in message:
        f = open('помощь.txt', 'r', -1, 'utf-8')
        f_all = f.read()
        say_message(f_all)
        f.close()

    elif "прочитать помощь" in message:
        os.startfile("помощь.txt")

    elif "пока" in message:
        exit()

    else:
        say_message("что то не так давай снова")



def say_message(message):

    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
        str(time.time())+"_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Голосовой ассистент: "+message)


if __name__ == '__main__':
    say_message("привет! Я голосовой калькулятор. Скажи команду открой помощь и я расскажу как это работает")

    while True:
        command = listen_command()  # слушает команду
        do_tris_command(command)
