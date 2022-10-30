from img_txtReader import TextTranslate, ImageTranslate
from TextTranslate import TextTranslate, translate_to_spanish, translate_to_french, translate_to_latin
from ImageTranslate import display_originals, greyScale,  blur, cascade, dialated, text_from_img, img_draw
import traceback


if __name__ == '__main__':
    try:
        with TextTranslate() as tt:
            print(f'[+] Translated Text')
            tt.TextTranslate(); tt.translate_text(); tt.translate_to_spanish(); tt.translate_to_french(); tt.translate_to_latin();
    except Exception as e: traceback.print_exc(); print(f"{str(e)}");pass

    try:
        with ImageTranslate() as it: print(f'[+] Displaying Original Text [+]'); it.display_orginals()
            with ImageTranslate.image_foreplay as fp: print('[+] Starting Image Forplay for GS [+]'); g_boxes, g_dimen, g_width, g_height = fp.greyScale()
                if fp.greyScale: print('[+] Sending to Text Parser and Vid Writer [+]')
                    try: w,x,y,z= it.text_from_img(g_boxes, g_dimen, g_width, g_height ); it.text_from_img
                    except Exception as e: print(f'[-] Error in Parsing Greyscale Video Manip \n  {traceback.print_exc} ')
                fp.blur(); fp.cascade(); fp.dialated(); img_draw(w,x,y,z)
    except Exception as e: print(f"{str(e)}{ traceback.print_exc()}"); pass


