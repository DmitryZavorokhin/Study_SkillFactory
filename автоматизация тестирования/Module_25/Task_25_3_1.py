from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

class TestPetfriendsHomework:

    def setup(self):
        self.user = "dmz8@mail.ru"
        self.password = "123"

    def open(self):
        self.driver = webdriver.Chrome('/user/d&v/Documents/chromedriver.exe')
        self.driver.get("https://petfriends.skillfactory.ru/login")

    def login(self):
        self.open()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys(self.user)
        self.driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "html > body > div > div > form > div:nth-of-type(3) > button").click()
        self.driver.find_element(By.XPATH, '//button[@class="navbar-toggler" and @type = "button"]').click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a'))).click()

    def close(self):
        self.driver.close()

    def test_all_pets_on_the_page(self):
        self.login()
        pet_num = self.driver.find_element(By.CSS_SELECTOR, "html > body > div > div > div")
        number_pets =int(pet_num.text.split("\n")[1].split(": ")[1])
        num_tags = self.driver.find_elements(By.TAG_NAME, "tr")
        stroka_table = 0
        for i in range(len(num_tags)):
            i += 1
        stroka_table = i-1
        assert stroka_table == number_pets
        print("\nЧисло питомцев: {}".format(number_pets))
        self.close()

    def test_half_pets_have_photo(self):
        self.login()
        images = self.driver.find_elements(By.TAG_NAME, 'img')
        names_num = 0
        for i in range(len(images)-1):
            if images[i].get_attribute('src') != '':
                names_num += 1
        assert (len(images)-1)/2 <= names_num
        print("\nЧисло питомцев с фото: {}, что больше, чем половина {}".format(names_num, int((len(images)-1)/2)))
        self.close()

    def test_same_names_of_pets(self):
        self.login()
        self.driver.implicitly_wait(2)
        num_tags = self.driver.find_elements(By.TAG_NAME, "tr")
        my_str = '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[1]/td[1]'
        my_str_little = my_str.split('/')[5]
        set_pets = set()
        for i in range(len(num_tags)):  #
            if i < len(num_tags) - 2:
                j = str(i)
                t = str(i + 1)
                my_str_little_0 = my_str_little
                my_str_little = my_str_little.replace(j, t)
                j = str(t)
                my_str = my_str.replace(my_str_little_0, my_str_little)
                name = self.driver.find_element(By.XPATH, my_str).text
                set_pets.add(name)
            elif i == len(num_tags) - 1:
                name = self.driver.find_element(By.XPATH,
                                                '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[{}]/td[1]'.format(
                                                    len(num_tags) - 1)).text
                set_pets.add(name)
        print("\nЧисло питомцев: {}, число питомцев с одинаковыми именами: {}".format(len(num_tags) - 1,
                                                                                    (len(num_tags) - 1 - len(
                                                                                        set_pets))))
        assert len(set_pets) == len(num_tags) - 1
        self.close()

    def test_unicum_info(self):
        self.login()
        self.driver.implicitly_wait(2)
        num_tags = self.driver.find_elements(By.TAG_NAME, "tr")
        for i in range(1,4):
            for j in range(1,len(num_tags)):
                my_str = '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[{}]/td[{}]'.format(j,i)
                info = self.driver.find_element(By.XPATH, my_str).text
                assert info !=""
        self.close()

    def test_same_pets(self):
        self.login()
        self.driver.implicitly_wait(2)
        set_pets = set()
        val_i =[]
        val_j = []
        num_tags = self.driver.find_elements(By.TAG_NAME, "tr")
        for i in range(1, len(num_tags)):

            val_j.append(list(val_i))
            # print("Вторым шагом добавляем значение {} в список {}".format(val_i, val_j))
            val_i.clear()
            for j in range(1, 4):

                my_str = '//*[@id="all_my_pets"]/table[1]/tbody[1]/tr[{}]/td[{}]'.format(i, j)
                info = self.driver.find_element(By.XPATH, my_str).text
                val_i.append(info)
                # print("добавляем значение {} в список {}". format(info,val_i))
        val_j.append(list(val_i))

        for i in range(len(val_j)):
            set_pets.add(val_j[i])
            print(val_j, set_pets)








