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
    say_list = message.split()
    num_1, sign, num_2 = int((say_list[-3]).strip()), (say_list[-2]).strip(), int((say_list[-1]).strip())
    resul = [say_list[0].strip(),say_list[-2].strip()]
    if sign == "+" or 'плюс' in sign:
        res = num_1 + num_2
    elif sign == "-" or 'минус' in sign:
        res = num_1 - num_2
    elif sign == "х" or 'умножить' in sign:
        res = num_1 * num_2
    elif sign == "/" or 'разделить' in sign:
        if num_2 != 0:
            res = num_1 / num_2
        else:
            say_message("Делить на ноль невозможно")
            return say_list
    say_message("{0} {1} {2} = {3}".format(say_list[-3], say_list[-2], say_list[-1], res))


def say_message(message):

    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
    str(time.time())+"_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Голосовой ассистент: "+message)


if __name__ == '__main__':
    say_message("скажи сколько будет 2+2 когда наиграешься скажи выход")

    while True:
        command = listen_command()  # слушает команду
        do_tris_command(command)
