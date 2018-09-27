from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def make_url(querry):
    readurl = 'http://service.epost.go.kr/trace.RetrieveRegiPrclDeliv.postal?sid1='
    return readurl + querry


class crawler():
    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(executable_path="C:/python_pkg/chromedriver.exe", chrome_options=self.options)
        self.driver.set_window_size(848,1200)

    def save_screenshot(self, querry, out_dir):
        url = make_url(querry)
        self.driver.get(url)
        self.driver.save_screenshot(out_dir + "/"+querry + ".png")

    def kill(self):
        self.driver.quit()