import pprint
from translate import Translator
from googletrans import Translator
import pytesseract, os, platform, subprocess, time, easyocr
from subprocess import call
from PIL import Image
from IPython.display import display, Image



class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


def period_wait():
    period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    # multi = [2,2,2,2,2,2,2,2,2,2]
    period_len = len(period)
    for z, x in enumerate(period):
        print(x)
        time.sleep(.2)
        if z <= period_len:
            z += 1
            print(f"{yellow}{x * z}{reset}")
            continue
        elif z == period_len:
            break


def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')


def display_header():
    # print('*' * 75)
    color_red = Colors()
    global red0
    red0 = color_red.fgRed
    global reset0
    reset0 = color_red.reset
    x = 'x'
    print(f"{'X' * 125:^70}")
    print(f"{'X' * 125:^70}")
    pretty = f'\t\t\t\t {red0}xxx [TEXT-TEXT] // [IMG-TXT Translator] {reset0}'
    print(f'{pretty : ^70}')
    print(f"{'X' * 125: ^70}")

    one = (
        f'{bblue}[SCRIPT] *** A/V Converter *** {bblue}')
    two = (
        f'[USAGE] - [1] The Program will can: 1.] re-encode AV Conntainers to whatever format needed. IE- .MP4 -> .MOV')
    three = (
        f'[USAGE] - [2] Trim AV, with Min/Max Values && duration ')
    four = (f'[USAGE] - [3] Compresses the AV, by rescaling resolution and resizing file')
    five = (
        f'[USAGE] - [5] Play Videos.{reset}')
    six = (f'{red}[+]-[+] copyright material from Adel Al-Aali [+]-[+] {reset}')
    seven = (f'[+] Future Addtion: Attach to OS.Listwalker and impliment Generator/text feed to auto convert large lists  [+]')

    print(f"{one:^70}"); print(f"{two:^70}"); print(f"{three:^70}"); print(f"{four:^70}"); print(f"{five:^70}"); print(f"{six:^70}")
    print(f"{seven:^70}"); print(f"{x * 20: ^70}")
    print(), print()


###########
color = Colors()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset

class TextTranslate():
    print(f'[+]-[+] Img-Txt Translator [+]-[+]')
    def __init__(self, toTranslate):
        super(TextTranslate).__init__()
        self.translator = Translator()
        self.translator.detect(toTranslate)
    def __repr__(self):
        return "<From __REPR__ [self]:%s [translator]:%s  >" % (self),(self.translator)
    def __str__(self):
        return "<From __STR__  [self]:%s [translator]:%s  >" % (self),(self.translator)

    def trans(self, sent):
        try:
            ans = self.translator.translate(sent)
            return ans
        except AttributeError:
            return 'Can\'t translate !'

print(f'[+] Input the text for translatin : \n[*]** ' )
inQuestion = input('')
with TextTranslate:
    ret = TextTranslate(inQuestion)
    print(f'[+] Translated Text')


class ImageTranslate():
    def __init__(self, toTranslate):
        super(ImageTranslate).__init__()
        self.pp = pprint.PrettyPrinter(indent=3)
        self.translator_img = Translator  ## backup translator
       # self.latin_translator = Translator(to_lang="zh")
        self.spanish_translator = Translator(to_lang="es")

        self.cwd = os.getcwd()
        self.reader = easyocr.Reader(['en']) # ocr reader
        print(f'[+] Enter Image Location and Image name in single str. [+]\n\t\t [+][{self.cwd}]\n[+]** ')
        self.img_loc = input('')
        self.data_read = self.reader.readtext(self.img_loc) ## read data info
        self.translation = self.translator_img.detect(self.data_read) ## may need to chanage to self.img_loc ?

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        print(f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]')

    def display_img(self): ### Display images
        display(Image.open(self.img_loc))
        if display:
            time00=time.time(); ctime00=time.ctime(time00)
            return f'[+] Display Opened at [{ctime00}]'
        else: return f'[-] Viewer Could not Open Picture'

    def text_from_img(self):
        self.pp.pprint([text[-2] for text in self.data_read])
        print('\n', 'X'* 50)
        print('[+] Reparsing, just incase non-english verbagh [+] ')
        print(self.translation)

    def translate_to_spanish(self):
        self.spanish_translator = Translator(to_lang="es")
        print(f'[+] Translating :: \m [{self.data_read}]')
        print(self.spanish_translator.translate(self.data_read))



print(f'[+] Quick Auto Translator [TEXT/IMG]' )
print('[+] The Img-Text translator will first attempt to translate just english, then reparse for non [en] lang. ')


with ImageTranslate as parseIMG:
    parseIMG. display_img()
