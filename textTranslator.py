import os, platform, subprocess, time, traceback
from translate import Translator
from subprocess import call
from textblob import TextBlob
import requests
import nlpcloud


import inspect
from PIL import Image
from IPython.display import display, Image
# from googletrans import Translator
import pprint  # googletrans


# pytesseract
# cv2
# easyocr

def animate_Rocket():
    distanceFromTop = 20
    while True:
        print("\n" * distanceFromTop)
        print("          /\        ")
        print("          ||        ")
        print("          ||        ")
        print("         /||\        ")
        time.sleep(0.2)
        os.system('clear')
        distanceFromTop -= 1
        if distanceFromTop == 15:
            break
            # distanceFromTop = 20

class Colors:
    reset = "\033[0m"
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"  # Black
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"  # Red
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"  # Green
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"

def period_wait():
    period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    # multi = [2,2,2,2,2,2,2,2,2,2]
    period_len = len(period)
    for z, x in enumerate(period):
        print(x), time.sleep(.2)
        if z <= period_len:
            z += 1;
            print(f"{yellow}{x * z}{reset}");
            continue
        elif z == period_len:
            break
def clear(): os_name = platform.system(); _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')
def display_header():
    print('X' * 75)
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
    one = f'{bblue}[SCRIPT] *** A/V Converter *** {bblue}'
    two = f'[USAGE] - [1] The Program will can: 1.] re-encode AV Conntainers to whatever format needed. IE- .MP4 -> .MOV'
    three = f'[USAGE] - [2] Trim AV, with Min/Max Values && duration '
    four = f'[USAGE] - [3] Compresses the AV, by rescaling resolution and resizing file'
    five = f'[USAGE] - [5] Play Videos.{reset}'
    six = f'{red}[+]-[+] copyright material from Adel Al-Aali [+]-[+] {reset}'
    seven = f'[+] Future Addtion: Attach to OS.Listwalker and impliment Generator/text feed to auto convert large lists  [+]'
    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    # print(f"{seven:^70}")
    print(f"{x * 20: ^70}")
    print()
    print()


############
# ---------#
###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset


# translator = Translator(service_urls=[
#     'translate.google.com',
#     'translate.google.co.kr',
# ])
# Translator = translator.detect('hello assholes')
# print(Tranlsator)
# self.translator.detect(self.inQuestion)
# self.inQuestion = inQuestion
# self.translator = Translator
#  self.spanish_translator = translator.Translator(self.inQuestion)
class TextTranslate():
    def __init__(self):
        super(TextTranslate).__init__()
        print(f'[+]-[+] Img-Txt Translator [+]-[+]')
        print(f'[+] Input the text for translatin : \n[*]** ')
        self.inQuestion = input('')
        self.blobber = TextBlob(self.inQuestion)
        self.Translator = Translator()
        self.url = "https://nlp-translation.p.rapidapi.com/v1/translate"
        self.querystring = {"text": self.inQuestion, "to": "es", "from": "en"}
        self.headers = {
            'x-rapidapi-host': "nlp-translation.p.rapidapi.com",
            'x-rapidapi-key': "b3fc8c54beeb2d6a128a7eb10a461cbd36f4485e"
        }

        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        print(response.text)

        # self.blobber.detect_language()
        # self.lang01 = self.blobber.detect_language(self.inQuestion)
        self.translation = self.Translator.detect(self.inQuestion)
        print(self.translation)
        time.sleep(1.5)

    def __repr__(self):
        return f"\n <From __REPR__  [self]: {self},[translator]:"  # {self.translator} \n

    def __str__(self):
        return f"\n <From __STR__  [self]: {self},[translator]:"  # {self.translator}

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        print(f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]');
        pass

    def translate_text(self):
        try:
            print('\n', 'X' * 50)
            print(f'[+] Translating :: [WILDCARD] \n \n\t\t --->[{self.inQuestion=}]');
            print(
                f'[+] {bblue} Decoding [{self.inQuestion}].. ')
            print(f'[+] Detected Language [BLOBBER]\n\t\t ---> {self.lang01}].. {reset}')
            print(
                f"[+] Translated Text [GOOGLE]: \n \n\t\t {yellow} --->[{Translator.translate(self.inQuestion.text, dest='en')} <--{reset}")
            print('X' * 50, '\n')

            time.sleep(2)

        except Exception as e:
            print(f"{str(e)} {traceback.print_exc()}")
        pass

    # print(f"[+] Detected Language [GOOGLE] \n\t\t --->{self.translator.detect(self.inQuestion, dest='en')}") # print(f'[+] Translated Text [BLOBBER] {self.blobber.translate(to="en")}].. ')
    def translate_to_spanish(self):
        try:
            print('\n', 'X' * 50);
            print(f'[+] Translating :: [SPANISH] \n [{self.inQuestion}]{reset}')
            print(
                f'{bblue}[+]-[SPANISH]-[+] Translated Text [+]-[BLOBBER]-[+]\n\t\t {reset}{yellow} ---> {self.blobber.translate(to="es")}] <--{reset} ');
            print('X' * 50, '\n')
        except AttributeError:
            print(f'{red} ill fix you later--google{reset}');
            pass
        except Exception as e:
            print('{str(e)} -->\n\t\t traceback.print_exc()');
            pass

    def translate_to_french(self):
        try:
            print('\n', 'X' * 50)
            print(f'[+] ::  Translating :: [FRENCH]\n\t\t **[{self.inQuestion=}]')
            print(
                f'[+]-[FRENCH]-[+] Translated Text [+]-[BLOBBER]-[+]\n\t\t{yellow} {bblue} ---> {self.blobber.translate(to="fr")}].. {reset} <-- {reset}')
            # print(f"[+]-[FRENCH]-[+] Translated Text [+]-[GOOGLE]-[+]\n\t\t ---> [{self.translator.translate(self.inQuestion, dest='fr')}")
            print('X' * 50, '\n')
        except AttributeError:
            print(f'{red} ill fix you later--google');
            pass
        except Exception as e:
            print(f"{str(e)} {traceback.print_exc()}{reset}")
        pass

    def translate_to_latin(self):
        try:
            print('\n', 'X' * 50)
            print(f'[+] ::  Translating :: [GOOGLE]\n\t\t **[{self.inQuestion}]')
            print(
                f'[+]-[LATIN]-[+] Translated Text [+]-[BLOBBER]-[+] {yellow}\n\t\t ---> {self.blobber.translate(to="la")}].. {reset}')
            # print(f"[+]-[LATIN]-[+] Translated Text [+]-[GOOGLE]-[+]\n\t\t ---> [{self.translator.translate(self.inQuestion, dest='la')}")
            print('X' * 50, '\n')
        except AttributeError:
            print(f'{red} ill fix you later--google{reset}')
            pass
        except Exception as e:
            print(f"{str(e)}, traceback.print_exc()")
            pass


def main():
    TextTranslate()


if __name__ == '__main__':
    animate_Rocket()
    main()

#
# class ImageTranslate():
#     def __init__(self):
#         self.cwd = os.getcwd()
#         super(ImageTranslate).__init__()
#         print(f'[+] Enter Image Location and Image name in single str. [+]\n\t\t [+][{self.cwd}]\n[+]** ')
#         self.img_loc = input('')
#         self.cv2 = cv2
#         self.pytesseract = pytesseract.tesseract_cmd()
#         self.custom_config00 = r'--oem 3 --psm 6'
#         self.pp = pprint.PrettyPrinter(indent=3)
#         self.translator_img = Translator()
#         self.latin_translator = Translator(to_lang="zh");
#         self.spanish_translator = self.translator_img(to_lang="es")
#         self.reader = easyocr.Reader(['en'])
#         self.cv_img = cv2.imread(self.img_loc)
#         self.cv_img = cv2.cvColor(self.cv_img, cv2.COLOR_BGR2RGB)
#         self.data_read = self.reader.readtext(self.img_loc)
#         print('dataread', self.data_read)
#         self.translation = self.translator_img.detect(self.data_read)
#         print('translation', self.translation)
#         ## reading text using text blob
#         self.blobber = TextBlob(self.reader)
#         print()
#         print(self.blobber)
#         print()
#         self.blobber = TextBlob(self.data_read)
#
#     def __enter__(self):
#         print('enter method called'); return self
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print('exit method called'); print(f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]')
#
#     def __repr__(self):
#         return f"\n <From __REPR__  [self]: {self},[translator]: {self.translator} \n "
#
#     def __str__(self):
#         return f"\n <From __STR__  [self]: {self},[translator]: {self.translator}"
#
#     def display_Originals(self):  ### Display images
#         try:
#             display(Image.open(self.img_loc))
#             if display:
#                 print(f'[+] Display Opened at [{time.ctime()}]')
#             else:
#                 print(f'[-] Viewer Could not Open Picture ')
#                 pass
#             cv2.imshow(self.img_loc)
#             if cv2.imshow:
#                 print(f'[+] CV2 display opened [+]')
#                 cv2.waitKey()
#                 key = cv2.waitKey(0) & 0xFF  # 1 ms delay
#                 if key == ord('q'):
#                     print(f'{red} [-] ** User Quit Key Hammered ** [-]')
#             else:
#                 print(f'{red}[-] Viewer Could not Open Picture {reset}')
#         except Exception as e:
#             print(e)
#
#
#     class image_foreplay():
#         def __init__(self):
#             self.cv_image = self.cv_img
#
#         def __enter__(self):
#             print('[SYSTEM] SCRIPT INITATED ENTER METHOD '); return self
#
#         def __exit__(self, exc_type, exc_value, exc_traceback):
#             print('[SYSTEM]**Exit-Method Called'); print(
#                 f'****[{self}],\n ***[{exc_type}],\n**[{exc_value}],\n*[{exc_traceback}]')
#
#         def greyScale(self):  ### Display images
#             ## convert to grey scale
#             greyScale = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2GRAY)
#             cv2.imshow('Grey Scale', greyScale)
#             cv2.waitKey(5000)
#             custom_config = r'--oem 3 --psm 6 outputbase digits'
#
#             Grey_cv2_dimen = pytesseract.image_to_string(greyScale, config=custom_config)  ## detecting height and width
#             width, height = greyScale.shape
#             print(f'[+] [GREYSCALE] :: Dimenensions --> {width} x {height}')
#             greyScale_boxes = pytesseract.image_to_string(greyScale)
#             return greyScale_boxes, Grey_cv2_dimen, width, height
#
#         def blur(self):
#             blur = cv2.GaussianBlur(self.cv2_img, (7, 7), cv2.BORDER_DEFAULT)
#
#             self.cv2.imshow('blur', self.cv2_img)
#             cv2.waitKey(5000)
#             if cv2.waitKey(5000) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#
#         def cascade(self):
#             cascade = cv2.Canny(self.cv2_img, 125, 175)
#             cv2.imshow('cascade', cascade)
#             cv2.waitKey(5000)
#
#             if cv2.waitKey(5000) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#
#         def dialated(self):
#             dilated = cv2.dilate(dilated, (3, 3), iterations=1)
#
#             cv2.imshow('dilated', dilated)
#             cv2.waitKey(5000)
#             if cv2.waitKey(5000) & 0xFF == ord('q'): cv2.destroyAllWindows()
#
#
# #  print(f'[+] Detected Language [GOOGLE] {self.translator.detect(self.inQuestion)}') print(f'[+] Translated Text BLOBBER] .. '#print(f"[+] Translated Text [GOOGLE]: \n [{self.translator.translate(self.inQuestion, dest='en')}")
# def text_from_img(self, data):
#     try:
#         print('\n', 'X' * 50)
#         print(f'[+] Translating :: [WILDCARD] \n [{self.inQuestion=}]')
#         print(
#             f'[+] Decoding [{self.data_read}].. ')
#         print(f'[+] CV2 read_data {"X" * 50} \n\n[{self.cvImg_data}]')
#         custom_config = r'--oem 3 --psm 6 outputbase digits'
#         print(f'[+] CV2 read_data [WITH CUSTOM CONFIG PARAM ]{"X" * 50} \n\n[{self.cvImg_data}]')
#         print('[+] Reading Data using Blobber')
#         print(f'[+]data_read {self.data_read}')  # reader
#         print(f'blobber{self.blobber}')
#         print(f'cv2 {self.cv2_data}')
#         pprint.pprint(self.cvImg_data)
#         print(
#             f'[+]-[FRENCH]-[+] Translated Text [+]-[BLOBBER]-[+]\n\t\t{yellow} {bblue} ---> {self.blobber.translate(to="fr")}].. {reset} <-- {reset}')
#         print(f'[+] Detected Language [BLOBBER] {self.lang01}].. ')
#
#         print('X' * 50, '\n')
#         self.pp.pprint([text[-2] for text in self.data_read])
#         print('\n', 'X' * 50)
#         print('[+] Reparsing, just incase non-english verbagh [+] ')
#         print(self.translation)
#
#     except AttributeError:
#         print(f'{red} ill fix you later--google{reset}')
#         pass
#     except Exception as e:
#         traceback.print_exc()
#         print(f"{str(e)}")
#     pass
#
#
# def img_draw(self, type, _boxes, _dimen, _width, _height):
#     print(f'[+] Drawing [{type}] \n[{time.ctime()}]')
#     _boxes_len = len(_boxes)
#     _dimen_len = len(_dimen)
#     print(f'[{_width}x{_height} --> [{_dimen}]]')
#     for gb in _boxes.splitlines():
#         print(f'[+]--{gb}')
#         gbSplit = gb.split(''); print(gbSplit)  ## creates list for easier element access
#     if _boxes_len == _dimen_len:
#         print(f"{yellow} [+] Succesfully parsed through boxes:: \n\t\t**[FILE] [{file}]\n\t\t {time.ctime()}")
#     if cv2.waitKey(5000) & 0xFF == ord('q'): cv2.destroyAllWindows()
#
#
# def translate_to_spanish(self):
#     try:
#         print(f'[+] Translating :: [SPANISH] \n [{self.inQuestion=}]')
#         self.spanish_translator = Translator(to_lang="es")
#         print(f'[+] Translating :: \m [{self.data_read}]')
#         print(self.spanish_translator.translate(self.data_read))
#
#     except AttributeError:
#         print(f'{red} ill fix you later--google{reset}')
#         pass
#     except Exception as e:
#         traceback.print_exc()
#         print(f"{str(e)}")
#         pass
#
#
#
# def translate_to_latin(self):
#     try:
#         self.spanish_translator = Translator(to_lang="es")
#         print(f'[+] Translating :: \m [{self.data_read}]')
#         print(self.spanish_translator.translate(str(self.data_read)))
#     except AttributeError:
#         print(f'{red} ill fix you later--google{reset}')
#         pass
#     except Exception as e:
#         traceback.print_exc()
#         print(f"{str(e)}")
#         pass
#
#
# def translate_to_spanish0(self):
#     try:
#         print('\n', 'X' * 50)
#         print(f'[+] Translating :: [SPANISH] \n [{self.inQuestion=}]')
#         print(f'[+]-[SPANISH]-[+] Translated Text [+]-[BLOBBER]-[+] {self.blobber.translate(to="es")}].. ')
#         print('X' * 50, '\n')
#
#     except AttributeError:
#         print(f'{red} ill fix you later--google{reset}')
#         pass
#     except Exception as e:
#         traceback.print_exc()
#         print(f"{str(e)}")
#         pass
#
#
# def translate_to_french(self):
#     try:
#         print('\n', 'X' * 50)
#         print(f'[+] ::  Translating :: [FRENCH]\n\t\t **[{self.inQuestion}]')
#         print(f'[+]-[FRENCH]-[+] Translated Text [+]-[BLOBBER]-[+] {str(self.blobber.translate(to="fr"))}].. ')
#         # print(f"[+]-[FRENCH]-[+] Translated Text [+]-[GOOGLE]-[+] [{self.translator.translate(self.inQuestion, dest='fr')}")
#         print('X' * 50, '\n')
#     except AttributeError:
#         print(f'{red} ill fix you later--google{reset}')
#         pass
#     except Exception as e:
#         traceback.print_exc()
#         print(f"{str(e)}")
#         pass
#
#
# def translate_to_latin0(self):
#     try:
#         print('\n', 'X' * 50)
#         print(f'[+] ::  Translating :: [GOOGLE]\n\t\t **[{self.inQuestion=}]')
#         print(f'[+]-[LATIN]-[+] Translated Text [+]-[BLOBBER]-[+] {self.blobber.translate(to="la")}].. ')
#         # print(f"[+]-[LATIN]-[+] Translated Text [+]-[GOOGLE]-[+] [{self.translator.translate(self.inQuestion, dest='la')}")
#         print('X' * 50, '\n')
#     except AttributeError:
#         print(f'{red} ill fix you later--google{reset}')
#         pass
#     except Exception as e:
#         traceback.print_exc()
#         print(f"{str(e)}")
#         pass
#
#
# if __name__ == '__main__':
#     img_parser = ImageTranslate()
#
# #
# class googletrans.models.Translated(src, dest, origin, text, pronunciation, extra_data=None, **kwargs)
# Translate result object
#
# Parameters:
# src – source language (default: auto)
# dest – destination language (default: en)
# origin – original text
# text – translated text
# pronunciation – pronunciation
# class googletrans.models.Detected(lang, confidence, **kwargs)
# Language detection result object
#
# Parameters:
# lang – detected language
# confidence – the confidence of detection result (0.00 to 1.00)


# print(f'[+] Quick Auto Translator [TEXT/IMG]')
# print('[+] The Img-Text translator will first attempt to translate just english, then reparse for non [en] lang. ')
# with ImageTranslate as parseIMG:
#     parseIMG.display_img()
#
#
#
# googletrans.models
# class googletrans.models.Translated(src, dest, origin, text, pronunciation, extra_data=None, **kwargs)
# Translate result object
#
# Parameters:
# src – source language (default: auto)
# dest – destination language (default: en)
# origin – original text
# text – translated text
# pronunciation – pronunciation
# class googletrans.models.Detected(lang, confidence, **kwargs)
# Language detection result object
#
# Parameters:
# lang – detected language
# confidence – the confidence of detection result (0.00 to 1.00)
#
#
# >>> from googletrans.gtoken import TokenAcquirer
# >>> acquirer = TokenAcquirer()
# >>> text = 'test'
# >>> tk = acquirer.do(text)
# >>> tk
# 950629.577246


#
# translator= Translator(to_lang="zh")
# translation = translator.translate("This is a pen.")
# to_lang = 'zh'
# secret = '<your secret from Microsoft or DeepL>'
# translator = Translator(provider='<the name of the provider, eg. microsoft or deepl>', to_lang=to_lang, secret_access_key=secret)
# translator.translate('the book is on the table')
#
# LANGUAGES = {
#     'af': 'afrikaans',
#     'sq': 'albanian',
#     'am': 'amharic',
#     'ar': 'arabic',
#     'hy': 'armenian',
#     'az': 'azerbaijani',
#     'eu': 'basque',
#     'be': 'belarusian',
#     'bn': 'bengali',
#     'bs': 'bosnian',
#     'bg': 'bulgarian',
#     'ca': 'catalan',
#     'ceb': 'cebuano',
#     'ny': 'chichewa',
#     'zh-cn': 'chinese (simplified)',
#     'zh-tw': 'chinese (traditional)',
#     'co': 'corsican',
#     'hr': 'croatian',
#     'cs': 'czech',
#     'da': 'danish',
#     'nl': 'dutch',
#     'en': 'english',
#     'eo': 'esperanto',
#     'et': 'estonian',
#     'tl': 'filipino',
#     'fi': 'finnish',
#     'fr': 'french',
#     'fy': 'frisian',
#     'gl': 'galician',
#     'ka': 'georgian',
#     'de': 'german',
#     'el': 'greek',
#     'gu': 'gujarati',
#     'ht': 'haitian creole',
#     'ha': 'hausa',
#     'haw': 'hawaiian',
#     'iw': 'hebrew',
#     'he': 'hebrew',
#     'hi': 'hindi',
#     'hmn': 'hmong',
#     'hu': 'hungarian',
#     'is': 'icelandic',
#     'ig': 'igbo',
#     'id': 'indonesian',
#     'ga': 'irish',
#     'it': 'italian',
#     'ja': 'japanese',
#     'jw': 'javanese',
#     'kn': 'kannada',
#     'kk': 'kazakh',
#     'km': 'khmer',
#     'ko': 'korean',
#     'ku': 'kurdish (kurmanji)',
#     'ky': 'kyrgyz',
#     'lo': 'lao',
#     'la': 'latin',
#     'lv': 'latvian',
#     'lt': 'lithuanian',
#     'lb': 'luxembourgish',
#     'mk': 'macedonian',
#     'mg': 'malagasy',
#     'ms': 'malay',
#     'ml': 'malayalam',
#     'mt': 'maltese',
#     'mi': 'maori',
#     'mr': 'marathi',
#     'mn': 'mongolian',
#     'my': 'myanmar (burmese)',
#     'ne': 'nepali',
#     'no': 'norwegian',
#     'or': 'odia',
#     'ps': 'pashto',
#     'fa': 'persian',
#     'pl': 'polish',
#     'pt': 'portuguese',
#     'pa': 'punjabi',
#     'ro': 'romanian',
#     'ru': 'russian',
#     'sm': 'samoan',
#     'gd': 'scots gaelic',
#     'sr': 'serbian',
#     'st': 'sesotho',
#     'sn': 'shona',
#     'sd': 'sindhi',
#     'si': 'sinhala',
#     'sk': 'slovak',
#     'sl': 'slovenian',
#     'so': 'somali',
#     'es': 'spanish',
#     'su': 'sundanese',
#     'sw': 'swahili',
#     'sv': 'swedish',
#     'tg': 'tajik',
#     'ta': 'tamil',
#     'te': 'telugu',
#     'th': 'thai',
#     'tr': 'turkish',
#     'uk': 'ukrainian',
#     'ur': 'urdu',
#     'ug': 'uyghur',
#     'uz': 'uzbek',
#     'vi': 'vietnamese',
#     'cy': 'welsh',
#     'xh': 'xhosa',
#     'yi': 'yiddish',
#     'yo': 'yoruba',
#     'zu': 'zulu',
