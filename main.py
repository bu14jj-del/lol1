from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.clock import Clock
from plyer import filestorage
from PIL import Image
import os

class ImageClickerApp(App):
    running = BooleanProperty(False)
    paused = BooleanProperty(False)
    click_count = 0
    
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.status_label = Label(text='Статус: Остановлен')
        layout.add_widget(self.status_label)
        
        self.count_label = Label(text='Кликов: 0')
        layout.add_widget(self.count_label)
        
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        self.start_btn = Button(text='Старт', on_press=self.start)
        btn_layout.add_widget(self.start_btn)
        
        self.stop_btn = Button(text='Стоп', on_press=self.stop, disabled=True)
        btn_layout.add_widget(self.stop_btn)
        
        self.pause_btn = Button(text='Пауза', on_press=self.pause, disabled=True)
        btn_layout.add_widget(self.pause_btn)
        
        layout.add_widget(btn_layout)
        return layout
    
    def start(self, *args):
        self.running = True
        self.paused = False
        self.start_btn.disabled = True
        self.stop_btn.disabled = False
        self.pause_btn.disabled = False
        self.status_label.text = 'Статус: Работает'
        Clock.schedule_interval(self.click_loop, 0.5)
    
    def stop(self, *args):
        self.running = False
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        self.pause_btn.disabled = True
        self.status_label.text = 'Статус: Остановлен'
        Clock.unschedule(self.click_loop)
    
    def pause(self, *args):
        self.paused = not self.paused
        if self.paused:
            self.status_label.text = 'Статус: Пауза'
            self.pause_btn.text = 'Продолжить'
        else:
            self.status_label.text = 'Статус: Работает'
            self.pause_btn.text = 'Пауза'
    
    def click_loop(self, dt):
        if not self.running or self.paused:
            return
        
        self.click_count += 1
        self.count_label.text = f'Кликов: {self.click_count}'
        print(f'Клик #{self.click_count}')

if __name__ == '__main__':
    ImageClickerApp().run()