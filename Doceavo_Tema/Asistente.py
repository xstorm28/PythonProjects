import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio






# escuchar microfono y devolver audio como texto

def transformar_audio():
    #almacenar el reconocedor en una variable
    r =sr.Recognizer()
    #configurar el microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print('Ya puedes hablar')
        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google
            pedido =r.recognize_google_cloud(audio,language ='es-mx')

            #prueba
            print('Dijiste: ' + pedido)

            #devolver a pedido
            return pedido

        #en caso de no comprender el audii
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print('No comprendi lo que dijiste')
            #devolver error
            return 'sigo esperando'
        #en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print('No hay servicio')
            # devolver error
            return 'sigo esperando'
        #error insesperado
        except:
            # prueba de que no comprendio el audio
            print('Algo ha salido mal')
            # devolver error
            return 'sigo esperando'
transformar_audio()








