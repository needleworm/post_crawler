from selenium import webdriver


def make_url(querry):
    readurl = 'http://service.epost.go.kr/trace.RetrieveRegiPrclDeliv.postal?sid1='
    return readurl + querry


class crawler():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/python_pkg/chromedriver.exe")

    def save_screenshot(self, querry, out_dir):
        url = make_url(querry)
        self.driver.get(url)
        self.driver.save_screenshot(out_dir + "/"+querry + ".jpg")

    def kill(self):
        self.driver.quit()