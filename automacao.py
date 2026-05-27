import pyautogui 
import pandas as pd 
import time 

pyautogui.FAILSAFE = False 

dados = pd.read_csv("funcionarios.csv", dtype=str)

print('Abra o formulario em 5 segundos')
time.sleep(5)

for i, funcionario in dados.iterrows():
    #nome
    pyautogui.click(x=859, y=361)
    pyautogui.write(funcionario['nome'],interval=0.2)
    time.sleep(0.4)
    pyautogui.press('tab')

    #cargo
    pyautogui.click(x=877, y=457)
    pyautogui.write(funcionario['cargo'],interval=0.2)
    time.sleep(0.4)
    pyautogui.press('tab')

    #matricula
    pyautogui.click(x=873, y=555)
    pyautogui.write(funcionario['matricula'], interval=0.2)
    time.sleep(0.4)
    pyautogui.press('tab')

    #enviar
    pyautogui.click(x=956, y=624)
    time.sleep(0.4)

print('Finalizado')