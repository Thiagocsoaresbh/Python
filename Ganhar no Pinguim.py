# ----------------------------------------------------------------------#
# Ganhar automaticamente no jogo Pinguins numa fria                     #
# @autor: Thiago César Soares                                           #
# Email: contato@thiagocsoares.com.br                                   #
# Site: www.thiagocsoares.com.br                                        #
# Data: 17/12/2021                                                      #
# ----------------------------------------------------------------------#

# ----------------------------------------------------------------------#
# Bibliotecas necessárias: PyAutoGui e Time                             #  
# Objetivo: O código iniciará o Google Chrome e abrirá automaticamente  #
# o site, executará todos os passos automaticamente e vencerá o jogo.   #
# ----------------------------------------------------------------------#


import pyautogui
import time

# Para interromper digite CTRL+C

pyautogui.alert('O código será executado. Não pressione nenhuma tecla ou mova o mouse até finalizar.')
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://rachacuca.com.br/jogos/pinguins-numa-fria/')
pyautogui.press('enter')
time.sleep(3) # Espera 1 segundo para dar tempo de carregar a head do site
pyautogui.moveTo(x=1193, y=788) # Move para a posição que iniciará e clica
pyautogui.click()
time.sleep(6) # Espera 6 segundos até terminar a contagem de 5 segundos do anúncio e clica
pyautogui.click()
pyautogui.moveTo(x=1222, y=694) # Se move para a posição de iniciar e clica
pyautogui.click()
pyautogui.moveTo(x=1184, y=775) # Se move para a segunda posição no botão iniciar e clica
pyautogui.click()
pyautogui.moveTo(x=1469, y=793) # Se move para a posição do pequeno pinguim azul e clica
pyautogui.click()
pyautogui.moveTo(x=1432, y=745) # Pinguim azul pai, clica para subir
pyautogui.click()
pyautogui.moveTo(x=1274, y=754) # Clica no iceberg na posição direita e clica para ir
pyautogui.click()
pyautogui.moveTo(x=1097, y=674) # Pinguim azul pai, lado esquerdo espera chegar e clica para descer
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1093, y=752) # Clica no Iceberg do lado esquerdo para voltar
pyautogui.click()   
pyautogui.moveTo(x=1419, y=670) # Move pinguim verde pequeno espera o iceberg voltar e clica
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1274, y=754) # Move para o iceberg na posição direita e clica
pyautogui.click()
pyautogui.moveTo(x=1097, y=674) # Espera 1 segundo chegar, clica no pinguim azul pequeno para descer
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1093, y=752) # Move para o iceberd lado esquerdo e clica para voltar
pyautogui.click()
pyautogui.moveTo(x=1442, y=619) # Clica pinguim pai verde para entrar
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1274, y=754) # Clica no iceberg na posição direita e clica para ir
pyautogui.click()
pyautogui.moveTo(x=1097, y=674) # Pinguim verde pai, lado esquerdo espera chegar e clica para descer
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1093, y=752) # Clica no Iceberg do lado esquerdo para voltar
pyautogui.click()
pyautogui.moveTo(x=1373, y=626) # Move pinguim vermelho pequeno espera o iceberg voltar e clica
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1274, y=754) # Move para o iceberg na posição direita e clica
pyautogui.click()
pyautogui.moveTo(x=1097, y=674) # Espera 1 segundo chegar, clica no pinguim verde pequeno para descer
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1093, y=752) # Move para o iceberd lado esquerdo e clica para voltar
pyautogui.click()
pyautogui.moveTo(x=1352, y=604) # Espera 1 segundo voltar e clica no pinguim pai vermelho para entrar
time.sleep(0.7)
pyautogui.click() 
pyautogui.moveTo(x=1274, y=754) # Clica no iceberg na posição direita e clica para ir
pyautogui.click()
pyautogui.moveTo(x=1108, y=705) # Pinguim vermelho pai, lado esquerdo espera chegar e clica para descer
time.sleep(0.7)
pyautogui.click()
pyautogui.moveTo(x=1107, y=706) # Clica no pinguim vermelho pequeno para descer
pyautogui.click()

print ("Fim")
