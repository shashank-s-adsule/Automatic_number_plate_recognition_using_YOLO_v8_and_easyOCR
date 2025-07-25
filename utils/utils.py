import string
import easyocr
import torch
import cv2

reader=easyocr.Reader(['en'],gpu=torch.cuda.is_available())

# mapping dic for char convertion 
char2int={'0':'O','I':'1','J':'3','A':'4','G':'6','S':'5'} 
int2char={'O':'0','1':'I','3':'J','4':'A','6':'G','5':'S'}

indian_state_codes = [
    "AN",  # Andaman and Nicobar Islands
    "AP",  # Andhra Pradesh
    "AR",  # Arunachal Pradesh
    "AS",  # Assam
    "BR",  # Bihar
    "CH",  # Chandigarh
    "CG",  # Chhattisgarh
    "DD",  # Daman and Diu
    "DL",  # Delhi
    "DN",  # Dadra and Nagar Haveli
    "GA",  # Goa
    "GJ",  # Gujarat
    "HR",  # Haryana
    "HP",  # Himachal Pradesh
    "JH",  # Jharkhand
    "JK",  # Jammu and Kashmir
    "KA",  # Karnataka
    "KL",  # Kerala
    "LA",  # Ladakh
    "LD",  # Lakshadweep
    "MH",  # Maharashtra
    "ML",  # Meghalaya
    "MN",  # Manipur
    "MP",  # Madhya Pradesh
    "MZ",  # Mizoram
    "NL",  # Nagaland
    "OD",  # Odisha (formerly OR)
    "PB",  # Punjab
    "PY",  # Puducherry
    "RJ",  # Rajasthan
    "SK",  # Sikkim
    "TN",  # Tamil Nadu
    "TS",  # Telangana
    "TR",  # Tripura
    "UP",  # Uttar Pradesh
    "UK",  # Uttarakhand
    "WB",  # West Bengal
]


# genral OCR for lincation plate
def read_license_plate_video(img):
    """Extracts license plate text from a cropped image.\n\tParameters:
    img (np.ndarray): Cropped image of the license plate.\n
    Returns:
    str: Recognized text."""
    detects=reader.readtext(img)
    Flag=True
    # print(detects)
    # print(len(detects),len(detects[0]))

    TEXT,SCORE="",0.0
    results=[]
    for detect in detects:
        if(len(detect)==0): continue
        bbox,text,score=detect
        TEXT= TEXT+" "+text
        SCORE+=score

    if len(TEXT)>15 or len(TEXT)<5: Flag=False
    if Flag:
        text=TEXT.strip()
        TEXT="" +text[0]
        # format OCR
        for i in range(1,len(text)):
            if(text[i]==' '): continue
            if TEXT[-1].isalpha() and text[i].isalpha(): TEXT+=text[i]
            elif TEXT[-1].isdigit() and text[i].isdigit(): TEXT+=text[i]
            else: TEXT=TEXT+" "+text[i]

        TEXT=TEXT.split(" ")
        # print(TEXT)
        # check Flag
        if(len(TEXT)!=4): Flag=False
        if Flag:
            if TEXT[0] not in indian_state_codes: Flag=False
            for i in TEXT[1]:
                if not i.isdigit() and len(i)>2: Flag=False
            for i in TEXT[2]:
                if not i.isalpha() and len(i)>2: Flag=False
            for i in TEXT[3]:
                if not i.isdigit() and len(i)>4: Flag=False

    # print(Flag)
    TEXT=" ".join(TEXT)
    try:
        SCORE/=len(detects)
    except ZeroDivisionError:
        SCORE=0.0
    
    results=[TEXT,SCORE,Flag]
    
    # print(results)
    
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
    img=cv2.imread(r"C:\Users\shash\OneDrive\Desktop\mod\car1\230.png")
    # img=cv2.imread(r"D:\code\repo\ANPR\dataset\images\false_extract.png")
    # ans=read_license_plate1(img)
    ans=read_license_plate_video(img)
    print(ans)