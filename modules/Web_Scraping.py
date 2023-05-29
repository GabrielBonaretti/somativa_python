from selenium import webdriver
from selenium.webdriver.common.by import By


class Web:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.celulares = []

    def abrir_kalunga(self):
        self.driver.get(f'https://www.kalunga.com.br/busca/1?q=celular')
        for i in range(1, 15):
            try:

                # Pegando nome + marca do celular + link
                try:
                    teste = self.driver.find_element(By.XPATH, f'//*[@id="div_box_produtos_1"]/div[1]/div[{i}]/div/div[2]/a')
                    nome_celular_extenso = teste.get_attribute("title")
                    nome_celular = nome_celular_extenso[:nome_celular_extenso.index(",")]
                except:
                    print("Erro nome")

                # Pegando preço
                try:
                    preco_celular = self.driver.find_element(By.XPATH, f'//*[@id="div_box_produtos_1"]/div[1]/div[{i}]/div/div[2]/div[2]/span').text
                    preco_celular_arrumado = preco_celular.split()
                    for t in preco_celular_arrumado:
                        try:
                            preco = float(t.replace(".", "").replace(",", "."))
                        except:
                            pass
                except:
                    print("Erro preco")

                # Verificar se é smartphone
                if "Smartphone" not in nome_celular:
                    break

                if "Samsung" in nome_celular:
                    self.celulares.append([nome_celular, "Samsung", preco])
                elif "Motorola" in nome_celular:
                    self.celulares.append([nome_celular, "Motorola", preco])
                elif "Nokia" in nome_celular:
                    self.celulares.append([nome_celular, "Nokia", preco])
                elif "LG" in nome_celular:
                    self.celulares.append([nome_celular, "LG", preco])
                else:
                    self.celulares.append([nome_celular, "Multi", preco])

            except:
                print("Foi não")

        return self.celulares


    def abrir_kabum(self):
        lista_sites = ["https://www.kabum.com.br/celular-smartphone/smartphones?page_number=1&page_size=20&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiTEciXX0=&sort=most_searched",
                       "https://www.kabum.com.br/celular-smartphone/smartphones?page_number=1&page_size=20&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiQXBwbGUiXX0=&sort=most_searched",
                       "https://www.kabum.com.br/celular-smartphone/smartphones?page_number=1&page_size=20&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiU2Ftc3VuZyJdfQ==&sort=most_searched",
                       "https://www.kabum.com.br/celular-smartphone/smartphones?page_number=1&page_size=20&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiWGlhb21pIl19&sort=most_searched",
                       "https://www.kabum.com.br/celular-smartphone/smartphones?page_number=1&page_size=20&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsiTW90b3JvbGEiXX0=&sort=most_searched"]
        for i in range(len(lista_sites)):
            self.driver.get(lista_sites[i])
            for j in range(1, 11):
                # Pegando nome + marca do celular
                try:
                    nome_celular_extenso = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[{j}]/a/div/button/div/h2/span').text
                    nome_celular = nome_celular_extenso[:nome_celular_extenso.index(",")]
                except:
                    print("Erro nome")

                # Pegando preço
                try:
                    preco_celular = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[{j}]/a/div/div/span[2]').text
                    try:
                        preco = float(preco_celular[3:].replace(".", "").replace(",", "."))
                    except:
                        print("errou primeiro")
                except:
                    print("to endoidando")

                if i == 0: 
                    self.celulares.append([nome_celular, "LG", preco])
                elif i == 1: 
                    self.celulares.append([nome_celular, "Apple", preco])
                elif i == 2: 
                    self.celulares.append([nome_celular, "Samsung", preco])
                elif i == 3: 
                    self.celulares.append([nome_celular, "Xiaomi", preco])
                else: 
                    self.celulares.append([nome_celular, "Motorola", preco])

        return self.celulares