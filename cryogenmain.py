import ctypes
import subprocess
import sys
import keyboard
from PyQt5 import QtWebEngineCore, QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QAction
from adblockparser import AdblockRules
# class to load default template for our browser
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # engine view
        self.browser = QWebEngineView()
        # connecting the browser to default google search engine
        self.browser.setUrl(QUrl('https://cryogenx.netlify.app/'))
        # setting things up in center
        self.setCentralWidget(self.browser)
        # will open it in maximized mode
        self.showMaximized()
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # home button
        home_button = QAction("home", self)
        home_button.triggered.connect(self.fff)
        home_button.setIcon(QIcon("assets\\home.png"))
        navbar.addAction(home_button)
        #back button
        back_btn = QAction("back" , self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setIcon(QIcon("assets\\back.png"))
        navbar.addAction(back_btn)
        #forward button
        forward_btn = QAction("forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        forward_btn.setIcon(QIcon("assets\\forward.png"))
        navbar.addAction(forward_btn)
        # reload button
        reload_button = QAction("reload", self)
        reload_button.triggered.connect(self.browser.reload)
        reload_button.setIcon(QIcon("assets\\reload.png"))
        navbar.addAction(reload_button)
        # url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
        #button for screen shot
        qr_url_button = QAction("qr code for link", self)
        qr_url_button.setIcon(QIcon("assets\qr.png"))
        qr_url_button.triggered.connect(self.qrcode)
        navbar.addAction(qr_url_button)
        #button for screen shot
        scrn_shot_button = QAction("screenshot", self)
        scrn_shot_button.setIcon(QIcon("assets\screenshot.png"))
        scrn_shot_button.triggered.connect(self.screenshot)
        navbar.addAction(scrn_shot_button)
        mg_button = QAction("Magnifier", self)
        mg_button.setIcon(QIcon("assets\mg.png"))
        mg_button.triggered.connect(self.mg)
        navbar.addAction(mg_button)
        # button for WEB AUTOMATION and virtual voice assistant
        ai_button = QAction("AI", self)
        ai_button.setIcon(QIcon("assets\\ai.png"))
        ai_button.triggered.connect(self.ai)
        navbar.addAction(ai_button)
        #menu
        mainMenu = self.menuBar()
        serch_menu = mainMenu.addMenu('search engines')
        se_1 = QAction(QIcon('assets\ddg.png'), 'duckduckgo', self)
        se_1.triggered.connect(self.ddg)
        serch_menu.addAction(se_1)
        se_2 = QAction(QIcon('assets\download.png'), 'google', self)
        se_2.triggered.connect(self.google)
        serch_menu.addAction(se_2)
        serch_menu = mainMenu.addMenu("options")
        tsk = QAction(QIcon("assets\\tskmgr.jpg"), 'task manager', self)
        tsk.triggered.connect(self.taskmanager)
        serch_menu.addAction(tsk)
        vpn = QAction(QIcon("assets\\vpn.png"), 'Vpn', self)
        vpn.triggered.connect(self.vpn)
        serch_menu.addAction(vpn)
    # function home button to redirect it to homepage
    def fff(self):
        self.browser.setUrl(QUrl('https://cryogenx.netlify.app/'))
    # function home button to redirect it to duckduckgo.com
    def ddg(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
    # function home button to redirect it to google.com
    def google(self):
        self.browser.setUrl(QUrl('https://google.com'))
    # function url bar to navigate to desired webpage by typing in it
    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl("https://{u}".format(u=url)))

    # function updating the url bar with change in webpage
    def update_url(self, q):
        self.url_bar.setText(q.toString())
        print(self.url_bar.text())
    # function to connect task manager
    def taskmanager(self):
        keyboard.press_and_release("ctrl+shift+esc")
    # function to connect vpn
    def vpn(self):
        subprocess.call('OpenVPNConnect.exe', shell=True, cwd='C:\Program Files\OpenVPN Connect')
    # function to start web automation with virtual voice assistant
    def ai(self):
        ctypes.windll.user32.MessageBoxW(0, "Web Automation is not ready yet", "Error", 1)
    # funtion to take screen shot
    def screenshot(self):
        subprocess.run('python3 screenshot.py', shell=True)
    # function to create qr code of the link of current viewing website to view it fromt he mobile
    def qrcode(self):
        # Import QRCode from pyqrcode
        import pyqrcode
        # import subprocess
        import subprocess
        # String which represents the QR code
        s = self.url_bar.text()
        # Generate QR code
        url = pyqrcode.create(s)
        # Create and save the png file naming "myqr.png"
        url.png('myqr.png', scale=6)
        subprocess.run('python3 qrcodegui.py', shell=True)
    def mg(self):
        keyboard.press_and_release("windows + plus")
# reading the list containing ad links and adding them as block list
file = open("adlinks.txt", encoding="UTF-8")
raw_rules = file.readlines()
rules = AdblockRules(raw_rules)
#making class to initialise WebEngine Ad Url interceptor
class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
     #function to intercept incoming ad urls
     def interceptRequest(self, info):
        #changing requested/incoming urls into string in order to read it
        url = info.requestUrl().toString()
        # making condition to review the incoming links and classifying them as ad and blocking them
        # from getting info from block list (rules)
        if rules.should_block(url):
            print("block::::::::::::::::::::::", url)

            info.block(True)

app = QApplication(sys.argv)
interceptor = WebEngineUrlRequestInterceptor()
QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setRequestInterceptor(interceptor)
view = QtWebEngineWidgets.QWebEngineView()
QApplication.setApplicationDisplayName("cryogen")
window = MainWindow()
app.exec()