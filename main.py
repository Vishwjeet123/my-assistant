from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser
import datetime

class AssistantApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.output = Label(text="Assistant ready, how can I help you?", size_hint=(1, 0.7))
        self.input = TextInput(hint_text="Type your command", size_hint=(1, 0.15), multiline=False)
        self.button = Button(text="Send", size_hint=(1, 0.15))
        self.button.bind(on_press=self.process_command)

        self.layout.add_widget(self.output)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.button)
        return self.layout

    def process_command(self, instance):
        command = self.input.text.lower()
        self.input.text = ""

        if "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            self.output.text = f"The time is {now}"
        elif "exit" in command or "bye" in command:
            self.output.text = "Goodbye!"
        else:
            self.output.text = "Sorry, I can't do that yet"

AssistantApp().run()
