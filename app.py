from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from builtins import Exception
from time import sleep

service = Service(executable_path=GeckoDriverManager().install())

INFO = {
         'url'  : 'https://web.ciee.org.br/estudante',
         'usuario' : 'USUARIO', 
         'senha' : 'SENHA' 
       }
class Pagina:

    def pegar_elemento_clicavel(self, elemento):
        return WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(elemento))
    
    def pegar_elementos_presentes(self, elemento):
        return WebDriverWait(self.driver, 25).until(EC.presence_of_all_elements_located(elemento))

class Vagas(Pagina):
    def __init__(self) -> None:
        self.driver = webdriver.Firefox(service=service)
        self.input_usuario = (By.XPATH, '//*[@id="acesso-input"]')     
        self.botao_avancar1 = (By.XPATH, '/html/body/app-root/app-acesso/div/div/div[2]/app-validar-acesso/form/div[2]/div/button')
        self.input_senha = (By.XPATH, '//*[@id="senha-input"]')
        self.botao_avancar2 = (By.XPATH, '/html/body/app-root/app-acesso/div/div[2]/app-acesso-login/div/div[2]/form/div[2]/div/button')
        self.botao_vagas =(By.XPATH, "/html/body/app-root/app-estudante/section/div/div/aside/section/app-mostrar-menu-principal/app-menu-principal/ul/li[2]/div/a[4]/span")      
        self.todas_vagas = (By.XPATH, "html/body/app-root/app-estudante/section/div/div/div/section/div/section/ng-component/app-consultar-vagas/div/div/div/div[1]/div[2]/div/ul/li[2]/button")    
        self.filtro_vagas = (By.XPATH, "/html/body/app-root/app-estudante/section/div/div/div/section/div/section/ng-component/app-consultar-vagas/div/div/div/div[2]/div/div/div/div[1]/app-filtro-vagas-estudante/div/div/app-filtro-avancado/div/div/div/button")
        self.tipo_vagas = (By.CLASS_NAME,'k-input' )
        self.aplicar_filtro = (By.CLASS_NAME, 'btn-aplicar-busca')
        self.botao_detalhes_vaga = (By.CSS_SELECTOR, 'button.ng-star-inserted') 
        
    def iniciar(self):
        try:
            self.logar()
            self.chegar_nas_vagas()
            self.assimilar_vagas()
        except Exception as e:
            print(e)

    def logar(self) -> None:
        self.driver.get(INFO['url'])
        self.pegar_elementos_presentes(*self.input_usuario).send_keys(INFO['usuario'])
        self.driver.find_element(*self.botao_avancar1).click()
        sleep(0.5)
        self.pegar_elementos_presentes(*self.input_senha).send_keys(INFO['senha'])
        self.driver.find_element(*self.botao_avancar2).click()
    
    def chegar_nas_vagas(self) -> None:
        self.pegar_elemento_clicavel(self.botao_vagas).click()      
        self.pegar_elemento_clicavel(self.todas_vagas).click()      
        self.pegar_elemento_clicavel(self.filtro_vagas).click()
        self.pegar_elemento_clicavel(self.tipo_vagas).send_keys('Estágio')
        
        self.driver.find_element(*self.aplicar_filtro).click()
        self.driver.find_element(*self.aplicar_filtro).click()
    
    def abrir_vaga(self, url):
        self.driver.switch_to.new_window('tab')
        self.driver.get(url)

    def assimilar_vagas(self) -> None: 
        codigos = self.pegar_elementos_presentes((By.TAG_NAME, 'h4'))
        
        urls = []

        for codigo in codigos: 
            urls.append('https://web.ciee.org.br/estudante/vagas/detalhes-vaga/' + codigo.text)

        for url in urls:
            self.abrir_vaga(url) 
        

            

        


        
        
        
        

            
        
        
        
            
    





