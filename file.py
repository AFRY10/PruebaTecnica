
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.exito.com')

#selectores

#dia sin iva
driver.find_element(By.ID, "aceptDiaIva").click()
#ingresamos ami cuenta
driver.find_element(By.XPATH, "//*[@id='header-container']/div[2]/div[4]/div/div[1]/div").click()

time.sleep(2)
#seleccionamos el inicio de sesion requerido
driver.find_element(By.XPATH, "//*/li[2]/div/button").click()

#Ingresar el correo
driver.find_element(By.XPATH, "//*/div/form/div[1]/label/div/input").send_keys('pruebasequal@gmail.com')
#Ingresar contraseña
driver.find_element(By.XPATH, "//*/div/form/div[2]/div/label/div/input").send_keys('Prueba123')

#Ingresamos
driver.find_element(By.XPATH, "//*//div/form/div[4]/div[2]/button").click()
time.sleep(2)

#Buscamos el atun
driver.find_element(By.ID, "downshift-0-input").send_keys('atun'+Keys.ENTER)

#ciudad
driver.find_element(By.ID, "react-select-2-input").send_keys('Medellín'+Keys.ENTER)

#siguiente
driver.find_element(By.XPATH, "//*/div[2]/div[2]/div[2]/button").click()

#seleccionara el atun ekono
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#gallery-layout-container > div:nth-child(2) > section > a > article > div.pointer.pt3.pb4.flex.flex-column.h-100 > div.vtex-flex-layout-0-x-flexRow.vtex-flex-layout-0-x-flexRow--product-info-container > div > div > div > div:nth-child(5) > div > div.exito-vtex-components-4-x-mainBuyButton").click()

#seleccionar domicilio
driver.find_element(By.XPATH, "//*/div/div/div[2]/div[2]/div[3]/button").click()
time.sleep(3)

#Insertar ciudad
driver.find_element(By.ID, "react-select-2-input").send_keys('Medellín'+Keys.ENTER)

#insertar direccion
driver.find_element(By.NAME, "address").send_keys('Calle 56s'+Keys.ENTER)

time.sleep(15)

#abrimos el carrito
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/a").click()
time.sleep(3)
#click en confirmar compra
driver.find_element(By.ID, "cart-to-orderform").click()


time.sleep(4)
driver.quit()







