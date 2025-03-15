# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import codecs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

validate = 0

# def SearchSlowo(slowoTranslation):
#     with codecs.open("slowka.txt", 'r', 'utf-8') as FILE:
#         index = 0
#         content = FILE.readlines()
#         for line in content:
#             # print(line)
#             # content_n = line.replace("\\n", " ")
#             # print(content_n)
#             content_f = line.split('|')
#             print(str(index) + " " + slowoTranslation + " " + content_f[0])
#             if str(slowoTranslation) == str(content_f[0]):
#                 return index+1;
#             index += 1
#     return 0

# def TranslateSlowo(indexLini):
#     file = open("slowka.txt")
#     content_of_file = file.readlines()
#     linia = content_of_file[indexLini - 1]
#     linia = linia.split("|")
#     return str(linia[0])


def translator(slowoTranslation):
    global validate
    with codecs.open("slowka.txt", 'r', 'utf-8') as FILE:
        content = FILE.readlines()
        print(content)
        ilosc = len(content)
        licznik = 0
        for line1 in content:
            licznik+=1
            line = str(line1)
            line.replace("\\n"," ")
            print(line)
            content_f = line.split('|')
            print(content_f[0])
            print(content_f[1])
            #print("Na instalingu do przetlumaczenia " + slowoTranslation + " Do przetlumaczenia " + content_f[1] + " Przetlumaczenie " + content_f[0])
            if str(content_f[1]) == str(slowoTranslation):
                validate = 1
                print("STOP")
                return str(content_f[0])
            else:
                if licznik==(ilosc+1):
                    validate = 0
                    return "null"
                else:
                    continue

print('\033' + 'Copyright @kacperpsg' + '\033')
PATH = "dist/chromedriver.exe"

# Dostep do strony - Uzyskiwanie
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
serv=Service(PATH)
driver = webdriver.Chrome(service=serv, options=options)

driver.get("https://instaling.pl/teacher.php?page=login")

# Logowanie
loginInput = driver.find_element(By.ID,"log_email")
loginInput.send_keys(str("kacpas217")) #there type your Login
loginInput.send_keys(Keys.RETURN)
passwordInput = driver.find_element(By.ID,"log_password")
passwordInput.send_keys(str("bhgth")) #there type your Password
buttonLogin = driver.find_element(By.XPATH,"//button[text()='ZALOGUJ']")
buttonLogin.click()

# Pytanie Czy Dokanczasz sesje czy ja zaczynasz
qstFrst = input("Zaczynasz Sesje (1) | Dokanczasz Sesje (2) >>> ")
try:
    if qstFrst == "1":
        buttonZacznij = driver.find_element(By.XPATH,"//a[text()='Zacznij codzienną sesję']")
        buttonZacznij.click()
        buttonDalej = driver.find_element(By.XPATH,"//h4[text()='Zacznij  swoją codzienną sesję']")
        buttonDalej.click()
    else:
        buttonDokoncz = driver.find_element(By.XPATH,"//a[text()='Dokończ sesję']")
        buttonDokoncz.click()
        buttonKont = driver.find_element(By.XPATH,"//h4[text()='Kontynuuj sesję']")
        buttonKont.click()
except:
    print("There's some error.")


# r = requests.get("https://instaling.pl/ling2/html_app/app.php?child_id=1669579")
#
# print(r.text)

# Działanie Programu
while True:
    slowo = str(driver.find_element(By.CLASS_NAME,"translations").get_attribute("textContent"))
    #print(str(slowo))
    tranWord = translator(slowo)
    if validate == 1:
        inputAns = driver.find_element(By.ID,"answer")
        time.sleep(0.5)
        inputAns.send_keys(tranWord)  # answer
        check = driver.find_element(By.ID,"check")
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", check)
        time.sleep(0.5)
        driver.find_element(By.XPATH,"//h4[text()='Następne']").click()
        # driver.find_element_by_id("nextword").click()
    elif validate == 0:
        print("This word doesn’t exist in list :: Getting Answer and Saving to File")
        time.sleep(0.5)
        check = driver.find_element(By.XPATH,"//h4[text()='Sprawdź']")
        check.click()
        time.sleep(0.5)
        slowo_NWM = driver.find_element(By.ID,"word").text
        slowo_Tlumaczenie = driver.find_element(By.ID,"answer_translations").text
        slowoNWM = str(slowo_NWM)
        slowoTlumaczenie = str(slowo_Tlumaczenie)

        with codecs.open("slowka.txt", 'a+', 'utf-8') as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(slowoNWM + " | " + slowoTlumaczenie)
            file_object.close()
            #print(file_object, " translations ")

        time.sleep(0.5)
        driver.find_element(By.XPATH,"//h4[text()='Następne']").click()
        time.sleep(2)





