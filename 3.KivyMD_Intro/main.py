from kivymd.app import MDApp
from kivy.lang import Builder

class Main(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def action(self, which):
        label = self.root.ids.txt
        label.text = f"This text is displayed after pressing {which} button"

    def build(self):
        return Builder.load_file('main.kv')


Main().run()