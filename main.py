from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

quotes = [
    "«Беҳтарин сармоя — ин илму дониш аст.»",
    "«Вақт аз тилло ҳам қимматтар аст.»",
    "«Ҳар рӯз — имконияти навест барои беҳтар шудан.»",
    "«Амал аз ҳазор ваъда беҳтар аст.»",
    "«Боварӣ ба худ калиди муваффақият аст.»",
    "«Қатра ба қатра дарё шавад.»"
]

class DailyQuotesApp(App):
    def build(self):
        self.title = "Daily Quotes"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.quote_label = Label(
            text=random.choice(quotes),
            font_size=24,
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1)
        )
        self.quote_label.bind(size=self.quote_label.setter('text_size'))
        
        btn = Button(
            text="Ҳикмати нав",
            font_size=20,
            size_hint=(1, 0.3),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        btn.bind(on_press=self.change_quote)
        
        layout.add_widget(self.quote_label)
        layout.add_widget(btn)
        return layout

    def change_quote(self, instance):
        self.quote_label.text = random.choice(quotes)

if __name__ == '__main__':
    DailyQuotesApp().run()
