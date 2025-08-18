from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from styles import Styles
from mydatabase import Database


Builder.load_string("""
#: import CTextInput custom_widgets
#: import CButton custom_widgets
#: import SignUpText custom_widgets

<SignUp>:
    name: 'signup'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        
        BoxLayout:
            size_hint: 1, 0.4
            Image:
                source: 'images/dice.png'
        
        AnchorLayout:
            size_hint: 1, 0.5
            anchor_y: 'top' 
             
            BoxLayout:
                spacing: dp(10)
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                
                Label:
                    id: warning_text
                    text: 'Create Your Account'
                    size_hint_y: None
                    height: self.texture_size[1]
                    color: root.secondary_color
                    halign: 'left'
                    text_size: self.width, None
                    font_name: 'keaniaone-regular.ttf'
                                    
                CTextInput:
                    id: email
                    hint_text: 'Email'
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    on_text_validate: root.next_field()
                
                CTextInput:
                    id: password
                    hint_text: 'Password'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text_validate: root.next_field()
                    
                CTextInput:
                    id: cpassword
                    hint_text: 'Confirm Password'
                    size_hint_y: None
                    height: dp(50)
                    password: True
                    multiline: False
                    on_text_validate: root.next_field()
                    
                CButton:
                    text: 'Sign Up'
                    size_hint_y: None
                    height: dp(50)
                    on_press: root.create_entry()
                
        AnchorLayout:
            size_hint: 1, 0.1
            anchor_x: 'center'
                
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                spacing: dp(10)
                padding: dp(10)
                
                Label:
                    color: root.secondary_color
                    text: 'Already have an account?'
                    size_hint_x: None
                    size: self.texture_size
                    
                SignUpText:
                    text: 'Login'
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switch_to_login()
            
            
            
""")


class SignUp(Screen):
    secondary_color = Styles.secondary_color
    warning_color = Styles.warning_color

    def next_field(self):
        if self.ids.email.focus:
            self.ids.password.focus = True
        elif self.ids.password.focus:
            self.ids.cpassword.focus = True

    def cleaned_email(self):
        email = self.ids.email.text
        domain = email.find('@')

        if domain < 1 or '.' not in email:
            return None
        else:
            return email

    def create_entry(self):

        if (9 <= len(self.ids.email.text) < 306) and (5 < len(self.ids.password.text) < 100):
            email = self.cleaned_email()
            password = self.ids.password.text
            c_password = self.ids.cpassword.text


            if password == c_password:
                if Database.is_valid(email):
                    Database.insert_data(email, password)
                    self.ids.warning_text.color = SignUp.secondary_color
                    self.manager.current = 'login'
                else:
                    self.ids.warning_text.text = 'This email already exists'
                    self.ids.warning_text.color = SignUp.warning_color
        else:
            self.ids.warning_text.text = 'Your email or password must be more than 10 characters'
            self.ids.warning_text.color = SignUp.warning_color

    def switch_to_login(self):
        self.ids.warning_text.color = SignUp.secondary_color
        self.ids.email.text = ''
        self.ids.password.text = ''
        self.ids.cpassword.text = ''
        self.manager.current = 'login'
