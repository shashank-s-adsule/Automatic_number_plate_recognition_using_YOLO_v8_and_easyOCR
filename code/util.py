import string, easyocr

reader=easyocr.Reader(['en'],gpu=False)

# mapping dic for char convertion 
dict_char2int={'0':'O','I':'1','J':'3','A':'4','G':'6','S':'5'} 
dict_int2char={'O':'0','1':'I','3':'J','4':'A','6':'G','5':'S'} 



def write_csv(resultes,output_path):

    with open(output_path,'w') as f:
        f.write('{},{},{},{},{},{},{}\n'.format('frame_no',"car_id","car_bbox","license_plate_bbox","license_plate_bbox_score","license_number","license_number_score"))

        for frame_no in resultes.keys():
            for car_id in resultes[frame_no].keys():
                print(resultes[frame_no][car_id])
                if 'car' in resultes[frame_no][car_id].keys() and \
                    'license_plate' in resultes[frame_no][car_id].keys() and \
                    'text' in resultes[frame_no][car_id]['license_plate'].keys():
                    f.write('{},{},{},{},{},{},{}\n'.format(frame_no,car_id,"[{}{}{}{}]".format(
                        resultes[frame_no][car_id]['car']['bbox'][0],
                        resultes[frame_no][car_id]['car']['bbox'][1],
                        resultes[frame_no][car_id]['car']['bbox'][2],
                        resultes[frame_no][car_id]['car']['bbox'][3]
                    ),
                    "[{}{}{}{}]".format(
                        resultes[frame_no][car_id]['license_plate']['bbox'][0],
                        resultes[frame_no][car_id]['license_plate']['bbox'][1],
                        resultes[frame_no][car_id]['license_plate']['bbox'][2],
                        resultes[frame_no][car_id]['license_plate']['bbox'][3]
                    ),
                    resultes[frame_no][car_id]['license_plate']['bbox_score'],
                    resultes[frame_no][car_id]['license_plate']['text'],
                    resultes[frame_no][car_id]['license_plate']['text_score']))
        
        f.close()
                

    return None

def license_compile_format(text):           #for licensplat number =7
    
    if(len(text)!=7): return False

    if (text[0]in string.ascii_uppercase or text[0] in dict_int2char.keys()) and\
        (text[1] in string.ascii_uppercase or text[1] in dict_int2char.keys()) and\
        (text[2] in ['0','1','2','3','4','5','6','7','8','9']  or text[2] in dict_char2int.keys()) and\
        (text[3] in ['0','1','2','3','4','5','6','7','8','9']  or text[3] in dict_char2int.keys()) and\
        (text[4] in string.ascii_uppercase or text[4] in dict_int2char.keys()) and\
        (text[5] in string.ascii_uppercase or text[5] in dict_int2char.keys()) and\
        (text[6] in string.ascii_uppercase or text[6] in dict_int2char.keys()):
        return True
    else: return False


# def license_complie_format1(text):
#     pass

def license_format(text):
    license_plate_out=''
    mapping={0:dict_int2char,1:dict_int2char,4:dict_int2char,5:dict_int2char,6:dict_int2char,  2:dict_char2int,3:dict_char2int}

    for i in [0,1,2,3,4,5,6]:
        if(text[i] in mapping[i].keys()):
            license_plate_out+=mapping[i][text[i]]
        else:
            license_plate_out+=text[i]
    return license_plate_out

def read_license_plate(license_plate_crop):
    detections=reader.readtext(license_plate_crop)

    # print(detections)           #debuging
    bbox,text,score=None,None,None
    for detection in detections:
        bbox,text,score=detection
        text=text.upper().replace(' ','')
        
        ## uncomment for real testing
        if(license_compile_format(text)):
            return license_format(text),score

    return text,score           #debuging

def get_car(license_plate,vehicle_track_id):
    
    # print(license_plate)      #debugging
    
    x1,y1,x2,y2,score,class_id=license_plate

    # print(x1,y1,x2,y2,score,class_id)     #debugging
    
    founded=False

    for j in range(len(vehicle_track_id)):
         xcar1,ycar1,xcar2,ycar2,car_id=vehicle_track_id[j]

         if(x1>xcar1 and y1>ycar1 and x2<xcar2 and y2<ycar2):
            car_idx=j

            founded=True
            break
    if founded:
        return vehicle_track_id[car_idx]
    
    return -1,-1,-1,-1,-1