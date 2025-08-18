from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from styles import Styles


Builder.load_string("""
<CButton>:
    canvas:
        Color:
            rgba: self.bg_color
        Line:
            width: 2
            rectangle: (self.pos[0], self.pos[1], self.width, self.height)
            
    background_color: self.bg_color
    background_normal: ''
    on_press: root.pressed()
    on_release: root.released()

<CTextInput>:
    background_color: self.bg_color
    background_normal: ''
    font_name: 'keaniaone-regular.ttf'
    font_size: '16sp'

<SignUpText>:
    color: self.bg_color
""")

class CButton(Button):
    bg_color = Styles.primary_color

    def pressed(self):
        self.background_color = (self.bg_color[0], self.bg_color[1], self.bg_color[3], 0.8)

    def released(self):
        self.background_color = self.bg_color


class CTextInput(TextInput):
    bg_color = Styles.textinput_bg


class SignUpText(ButtonBehavior, Label):
    bg_color = Styles.primary_color

