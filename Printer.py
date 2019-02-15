class Printer():
    def log(self, *args):
        self.args = args
        return str(self.args)

class FormattedPrinter():
    def formated_log(self, *args):
        self.args = args
        return "*"*30 + "\n" + str(self.args) + "\n" + "*"*30

prt = Printer()
print(prt.log(1,2,3,4,5,6,7,8,98,0))

f_prt = FormattedPrinter()
print(f_prt.formated_log(1,2,3,4,5,6,7,8,98,0))
