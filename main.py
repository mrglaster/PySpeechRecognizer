import speech_recognition as sr
import argparse
import os
import sys

def argsparser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, type=str)
    parser.add_argument('-lang', '--language', default='en', required=True, type=str)
    return parser


if __name__ == '__main__':
    print("Welcome to audio file speech recognition app!")
    print("If something went wrong, find your language here: https://cloud.google.com/speech-to-text/docs/languages ")
    print("Input example: en-US")
    parser = argsparser()
    namespace = parser.parse_args(sys.argv[1:])
    path = format(namespace.input)
    lang = format(namespace.language)
    if os.path.exists(path):
            r = sr.Recognizer()
            with sr.AudioFile(path) as source:
                print("Process starts!")
                audio = r.record(source)
                rec_m = r.recognize_google(audio, language=lang)
                if os.path.exists("output.txt"):
                    os.remove("output.txt")
                with open('output.txt', 'w') as f:
                    f.write(rec_m)
                print("Audio was recognized. File with results: output.txt")


