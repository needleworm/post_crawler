from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import win32api, win32con, win32gui
import os


def make_url(querry):
    readurl = 'http://service.epost.go.kr/trace.RetrieveRegiPrclDeliv.postal?sid1='
    return readurl + querry


class crawler():
    def __init__(self):
        self.options = Options()
        #self.options.add_argument("headless")
        self.options.add_argument("window-size=848x1500")
        #self.options.add_argument("disable-gpu")
        self.driver = webdriver.Chrome(executable_path="C:/python_pkg/chromedriver.exe", chrome_options=self.options)
        #self.driver.set_window_size(848,1500)

    def save_screenshot(self, querry, out_dir):
        url = make_url(querry)
        self.driver.get(url)
        self.driver.save_screenshot(out_dir + "/"+querry + ".png")

    def kill(self):
        self.driver.quit()

    def save_screenshot_withhout_masking(self, querry, out_dir, key1, key2):
        url = make_url(querry)
        self.driver.get(url)
        if not self.unlock_masking(key1, key2):
            return False
        redbox_based_awake()
        self.driver.save_screenshot(out_dir + "/"+querry + ".png")
        return True

    def unlock_masking(self, key1, key2):
        button_location = (650, 170)
        time.sleep(5)
        key1_location = (185, 235)
        key2_location = (185, 263)
        popup_ok_location = (210, 310)

        click(button_location)
        redbox_based_sleep()
        click(key1_location)
        type_in(key1)
        click(key2_location)
        type_in(key2)
        time.sleep(0.1)
        click(popup_ok_location)
        if kill_error_page():
            return False
        return True


def click(location):
    x, y = location
    win32api.SetCursorPos(location)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def type_in(string):
    command = 'echo ' + string.strip() + '| clip'
    os.system(command)
    win32api.keybd_event(0x11, 0, 0x00, 0)
    win32api.keybd_event(0x56, 0, 0x00, 0)
    win32api.keybd_event(0x11, 0, 0x02, 0)
    win32api.keybd_event(0x56, 0, 0x02, 0)


def get_color(location):
    x, y = location
    return hex(win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y))


def redbox_based_sleep():
    redbox_location = (385, 123)
    while get_color(redbox_location) != "0x392ddd":
        time.sleep(0.01)


def redbox_based_awake():
    redbox_location = (385, 123)
    while get_color(redbox_location) == "0x392ddd":
        time.sleep(0.1)


def kill_error_page():
    error_button = (390, 170)
    quit_button = (400, 10)
    time.sleep(1)
    if get_color(error_button) != "0xffffff":
        click(quit_button)
        return True
    return False
