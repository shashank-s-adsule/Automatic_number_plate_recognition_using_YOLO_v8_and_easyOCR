import string
import easyocr
import torch
# import cv2

reader=easyocr.Reader(['en'],gpu=torch.cuda.is_available())

# mapping dic for char convertion 
char2int={'0':'O','I':'1','J':'3','A':'4','G':'6','S':'5'} 
int2char={'O':'0','1':'I','3':'J','4':'A','6':'G','5':'S'} 

# genral OCR for lincation plate
def read_license_plate(img):
    """Extracts license plate text from a cropped image.\n\tParameters:
    img (np.ndarray): Cropped image of the license plate.\n
    Returns:
    str: Recognized text."""
    detects=reader.readtext(img)
    Flag=True
    # print(detects)
    # print(len(detects),len(detects[0]))


    results=[]
    for detect in detects:
        if(len(detect)==0): continue
        bbox,text,score=detect
        
        if(len(text)>13 or len(text)<10 or score<0.6): Flag=False
        text=text.split(" ")
        # check text [check for mismatch d=letters also ]
        if Flag:
            if(text[0].isalpha() & len(text[0])==2) & (text[1].isdecimal() & len(text[1])<=2) & (text[2].isalpha() & len(text[2])==2) & (text[3].isdecimal() & len(text[3])<=4):
                continue
            else: Flag=False

        text=" ".join(text)
        
        results.append([text,score,Flag])        
    
    return results

# OCR for only indian number plate
def read_license_plate1(img):
    """Extracts license plate text from a cropped image.\n\tParameters:
    img (np.ndarray): Cropped image of the license plate.\n
    Returns:
    str: Recognized text."""
    
    detects=reader.readtext(img)
    print(detects)

    results=[]
    for detect in detects:
        if(len(detect)==0): continue
        bbox,text,score=detect
        
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
    # img=cv2.imread(r"D:\code\repo\ANPR\dataset\images\9.png")
    img=cv2.imread(r"D:\code\repo\ANPR\temp\crop\540.png")
    ans=read_license_plate(img)
    print(ans)