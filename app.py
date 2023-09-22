#ler dados da planilha
#inserir cada celula de cada linha em um campo do sistema

import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
#["Murilo Barros, Cadeiras, 434, Esportes"]
    #nome
    pyautogui.click(1699,415,duration=1.5)
    pyautogui.write(linha[0].value)
    
    #produto
    pyautogui.click(1685,442,duration=1.5)
    pyautogui.write(linha[1].value)
   
    #quantidade434714981749
    pyautogui.click(1700,464,duration=1.5)
    pyautogui.write(str(linha[2].value))
    #categoria
    pyautogui.click(1758,491,duration=1.5)
    pyautogui.write(linha[3].value)
    
    pyautogui.click(1644,522,duration=1.5)
    pyautogui.click(953,584,duration=1.5)
    
