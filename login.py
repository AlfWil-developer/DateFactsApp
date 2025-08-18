from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from mydatabase import Database

from styles import Styles


Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
#: import SignUpText custom_widgets


<Login>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint: 1, 0.35
            Image:
                source: 'images/dice.png'
                
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y: 'top'
        
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(20)
                size_hint_y: None
                height: self.minimum_height
                
                Label:
                    id: warning_text
                    text: 'Login to your Account'
                    text_size: self.size
                    halign: 'left'
                    font_name: 'keaniaone-regular.ttf'
                    size_hint_y: None
                    size: self.texture_size
                    font_size: '16sp'
                    color: root.secondary_color
                
                CTextInput:
                    id: email
                    padding: dp(15)
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: 'Email'
                    on_text_validate: root.next_field()
                    
                CTextInput:
                    id: password
                    padding: dp(15)
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: 'Password'
                    password: True
                    on_text_validate: root.login()
                
                CButton:
                    text: 'Login'
                    size_hint_y: None
                    height: dp(48)
                    on_press: root.login()
                    
        AnchorLayout:
            size_hint: 1, 0.1
            anchor_x: 'center'
        
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                spacing: dp(10)
                padding: dp(10)
                
                Label:
                    text: "Don't have an account?"
                    color: root.secondary_color
                    size_hint_x: None
                    size: self.texture_size
                    
                SignUpText:
                    text: 'Sign Up'
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switch_to_signup()
        

""")


class Login(Screen):
    email = None
    secondary_color = Styles.secondary_color
    warning_color = Styles.warning_color

    @staticmethod
    def get_email():
        return Login.email

    def next_field(self):
        if self.ids.email.focus:
            self.ids.password.focus = True


    def login(self):
        Login.email = self.ids.email.text
        password = self.ids.password.text

        if Database.is_exist(Login.email, password):
            self.manager.current = 'home'
        else:
            self.ids.warning_text.color = Login.warning_color
            self.ids.warning_text.text = 'Invalid Username or Password'

    def switch_to_signup(self):
        self.ids.email.text = ''
        self.ids.password.text = ''
        self.ids.warning_text.color = Login.secondary_color
        self.manager.current  = 'signup'

