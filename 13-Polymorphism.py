class English:
    def greet(self,name):
        print('Good morning',name)
class French:
    def greet(self,name):
        print("Bonjour",name)

def greetings(language,name):
    language.greet(name)

eng=English()
fr=French()
greetings(eng,'Prasanthi')
greetings(fr,'San')