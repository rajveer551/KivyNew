from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
import os

class Notepad(App):

    def build(self):
        self.file_path = None
        layout = BoxLayout(orientation='vertical')

        self.text_input = TextInput()
        layout.add_widget(self.text_input)

        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)

        save_button = Button(text='Save', on_press=self.save_file)
        open_button = Button(text='Open', on_press=self.open_file)

        button_layout.add_widget(save_button)
        button_layout.add_widget(open_button)

        layout.add_widget(button_layout)

        return layout

    def save_file(self, instance):
        if self.file_path:
            with open(self.file_path, 'w') as f:
                f.write(self.text_input.text)
        else:
            self.save_as_file()

    def save_as_file(self):
        content = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        content.add_widget(file_chooser)

        popup = Popup(title='Save File As', content=content, size_hint=(0.9, 0.9), auto_dismiss=False)

        def save(path):
            self.file_path = path
            with open(path, 'w') as f:
                f.write(self.text_input.text)
            popup.dismiss()

        file_chooser.bind(on_submit=lambda instance: save(instance.selection[0]))

        popup.open()

    def open_file(self, instance):
        content = BoxLayout(orientation='vertical')
        file_chooser = FileChooserListView()
        content.add_widget(file_chooser)

        popup = Popup(title='Open File', content=content, size_hint=(0.9, 0.9), auto_dismiss=False)

        def load(path):
            self.file_path = path
            with open(path, 'r') as f:
                self.text_input.text = f.read()
            popup.dismiss()

        file_chooser.bind(on_submit=lambda instance: load(instance.selection[0]))

        popup.open()

if __name__ == '__main__':
    Notepad().run()
