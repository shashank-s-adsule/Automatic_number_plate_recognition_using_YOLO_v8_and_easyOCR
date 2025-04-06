import string
import easyocr
import torch

reader=easyocr.Reader(['en'],gpu=torch.cuda.is_available())

# mapping dic for char convertion 
char2int={'0':'O','I':'1','J':'3','A':'4','G':'6','S':'5'} 
int2char={'O':'0','1':'I','3':'J','4':'A','6':'G','5':'S'} 


def read_license_plate(img):
    """Extracts license plate text from a cropped image.\n\tParameters:
    img (np.ndarray): Cropped image of the license plate.\n
    Returns:
    str: Recognized text."""
    
    detect=reader.readtext(img)
    print(detect[1])
    results=[]
    for bbox,text,score in detect:
        if(len(text)>13 or len(text)<10 or score<0.8): continue
        text=text.split(" ")
        # check text [check for mismatch d=letters also ]
        check=(text[0].isalpha() & len(text[0])==2) & (text[1].isdecimal() & len(text[1])<=2) & (text[2].isalpha() & len(text[2])==2) & (text[3].isdecimal() & len(text[3])<=4)
        if not check: continue
        else:
            text=" ".join(text)
        
        results.append([text,score])        
    
    return results


if __name__=="__main__":
    print("utils")
    read_license_plate(None)