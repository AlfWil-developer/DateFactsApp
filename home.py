import certifi
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen

from login import Login
from mydatabase import Database
from styles import Styles


Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Home>:
    name: 'home'
    
    FloatLayout:
        Image:
            id: bg_image
            source: 'images/dice.png'
            fit_mode: 'contain'
            pos_hint: {'center_x': 0.5, 'center_y': 0.57}
            
        BoxLayout:
            orientation: 'vertical'
            
            BoxLayout:
                canvas.before:
                    Color:
                        rgba: root.bg_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                    
                size_hint_y: None
                height: dp(60) 
                
                Label:
                    text: 'Interesting Fact'
                    font_name: 'keaniaone-regular.ttf'
                    font_size: '20sp'
                    
                AnchorLayout:
                    anchor_x: 'right'
                    padding: [0, 0, dp(30), 0]
                    
                    Button:
                        canvas.before:
                            Rectangle:
                                pos: self.pos
                                size: self.size
                                source: 'images/history.png'
                        size_hint: None, None
                        size: dp(35),  dp(35)
                        background_normal: ''
                        background_color: 0, 0, 0, 0
                        on_press: root.switch_to_history()
                        
                    
            BoxLayout:
                
                Label:
                    id: result_placeholder
                    color: root.secondary_color
                    text_size: self.width, None
                    padding: [dp(20), dp(20)]
                    font_name: 'keaniaone-regular.ttf'
                    font_size: '18sp'
            
            AnchorLayout:
                anchor_x: 'center'    
                anchor_y: 'center'
                size_hint: 1, 0.3
                    
                BoxLayout:
                    orientation: 'vertical'
                    height: self.minimum_height
                    size_hint_y: None
                    padding: dp(30)
                    spacing: dp(10)
                    
                    BoxLayout:
                        spacing: dp(10)
                        size_hint: 1, 0.65
                        
                        BoxLayout:
                            orientation: 'vertical'
                            spacing: dp(10)
                            
                        
                            Label:
                                text: 'Day'
                                color: root.secondary_color
                                size_hint_y: None
                                size: self.texture_size
                                font_name: 'keaniaone-regular.ttf'
                                font_size: '18sp'
                                halign: 'left'
                                text_size: self.size
                                
                            CTextInput:
                                id: day
                                size_hint_y: None
                                height: dp(50)
                                multiline: False
                        
                        BoxLayout:
                            orientation: 'vertical'
                        
                            Label:
                                text: 'Month'
                                color: root.secondary_color
                                size_hint_y: None
                                size: self.texture_size
                                font_name: 'keaniaone-regular.ttf'
                                font_size: '18sp'
                                halign: 'left'
                                text_size: self.size
                                
                            CTextInput:
                                id: month
                                size_hint_y: None
                                height: dp(50)
                                multiline: False
                            
                    CButton:
                        text: 'Display Fact'
                        size_hint_y: None
                        height: dp(60)
                        font_name: 'keaniaone-regular.ttf'
                        font_size: '18sp'
                        on_press: root.get_fact()
""")


class Home(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def get_fact(self):
        day = self.ids.day.text
        month = self.ids.month.text

        url = f'https://numbersapi.p.rapidapi.com/{month}/{day}/date'

        headers = {
            "x-rapidapi-key": "7bf70a1930msh89fad5882437ee6p1ba1bbjsn22297f0c6354",
            "x-rapidapi-host": "numbersapi.p.rapidapi.com"
        }

        UrlRequest(
            url=url,
            req_headers=headers,
            on_success=self.response,
            ca_file=certifi.where(),
            verify=True
        )


    def response(self, req_body, response):
        self.ids.bg_image.color = (1, 1, 1, 0.3)
        self.ids.result_placeholder.text = response
        self.ids.day.text = ''
        self.ids.month.text = ''
        Database.insert_fact(Login.get_email(), response)

    def switch_to_history(self):
        self.ids.day.text = ''
        self.ids.month.text = ''
        self.ids.result_placeholder.text = ''
        self.ids.bg_image.color = (1, 1, 1, 1)
        self.manager.current = 'history'
