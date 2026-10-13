import pyautogui
import time
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('notepad Relatório de Execução Automática - RPA PyAutoGUI Ativo!status_bot.txt
')
pyautogui.press('enter')
time.sleep(2)
texto = "Relatório de Execução Automática - RPA PyAutoGUI Ativo!"
pyautogui.write(texto)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('status_bot.txt')
pyautogui.press('enter')

