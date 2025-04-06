import string
import easyocr

reader=easyocr.Reader(['en'],gpu=False)

# mapping dic for char convertion 
dict_char2int={'0':'O','I':'1','J':'3','A':'4','G':'6','S':'5'} 
dict_int2char={'O':'0','1':'I','3':'J','4':'A','6':'G','5':'S'} 


if __name__=="__main__":
    pass