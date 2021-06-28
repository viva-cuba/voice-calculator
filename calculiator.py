from gtts import gTTS
import playsound
import speech_recognition as sr
import os
import time
import random
import string


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
    if 'выход' in message:
        exit()
    try:
            say_list = message.split()
            num_1,num_2 = int and float((say_list[-3]).strip()), int and float((say_list[-1]).strip())
            resul = [say_list[0].strip(),say_list[-2].strip()]
            for i in resul:
                if 'разделить' in i or 'умножить' in i or 'fals' in i or 'плюс' in i or 'минус' in i or i == 'x' or i == '/' or i =='+' or i == '-' or i == '*':
                    result = i
                    break
                else:
                    result = resul[1]
            if result == "+" or 'плюс' in result:
                res = num_1 + num_2
            elif result == "-" or 'минус' in result:
                res = num_1 - num_2
            elif result == "х" or 'умножить' in result:
                res = num_1 * num_2
            elif result == "/" or 'разделить' in result:
                if num_2 != 0:
                    res = num_1 / num_2
                else:
                    say_message("Делить на ноль невозможно")
            say_message("{0} {1} {2} = {3}".format(say_list[-3], say_list[-2], say_list[-1], res))
    except:
        pass
    



def say_message(message):

    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
    str(time.time())+"_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Голосовой ассистент: "+message)


if __name__ == '__main__':
    say_message("скажи 2+2 когда наиграешься скажи выход")

    while True:
        command = listen_command()  # слушает команду
        do_tris_command(command)
