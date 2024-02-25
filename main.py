import kivy
from kivy.lang import Builder  # Import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from indic_numtowords import num2words
from kivy.core.clipboard import Clipboard



kivy.require('2.0.0')

# Load the Kv file
Builder.load_file('num2words.kv')

class ConverterLayout(BoxLayout):
    input_text = ObjectProperty()

    def convert_number(self) :
        input_text=self.ids.input_text.text  # Access the text property of the TextInput widget
        if input_text.isdigit() :
            word=num2words(int(input_text), lang='ta', variations=False)
            self.ids.output_label.text=word
        else :
            self.ids.output_label.text="Please enter a valid number."

    def copy_output_text(self):
        converted_text = self.ids.output_label.text
        Clipboard.copy(converted_text)

class NumberToWordsApp(App):
    def build(self):
        return ConverterLayout()

if __name__ == '__main__':
    NumberToWordsApp().run()
