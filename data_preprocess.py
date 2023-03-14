import os
import cv2
import numpy as np
import pandas as pd
import xmltodict
import json
from tqdm import tqdm

class DataProcessor:
    def __init__(self, xml_file, img_dir, img_size=(224, 224)):
        self.xml_file = xml_file
        self.img_dir = img_dir
        self.img_size = img_size
        self.dataframe = self.get_labels()
        
    def get_labels(self):
        # read XML
        with open(self.xml_file, 'r') as f:
            xml_data = f.read()

        # XML2JSON
        dict_data = xmltodict.parse(xml_data)
        df = pd.read_json(json.dumps(dict_data))
        df_track = pd.DataFrame(df.annotations.track)

        img_x, img_y = 3840, 2160
        df_labels = pd.DataFrame()
        for id in df_track['@id']:
            label = df_track[df_track['@id'] == str(id)]
            df_label = pd.DataFrame(label['box'][int(id)])[['@frame','@xtl','@ytl','@xbr','@ybr']]
            df_label['@frame'] = df_label['@frame'].astype(int)
            df_label['@xtl'] = df_label['@xtl'].astype(float)/img_x
            df_label['@ytl'] = df_label['@ytl'].astype(float)/img_y
            df_label['@xbr'] = df_label['@xbr'].astype(float)/img_x
            df_label['@ybr'] = df_label['@ybr'].astype(float)/img_y
            df_label['label'] = label['@label'].values[0]
            df_labels = pd.concat([df_labels, df_label])

        return df_labels
    
    def get_images(self):
        # images list
        num_list = self.dataframe['@frame'].tolist()
        files = ['frame_' + str(num) + '.jpg' for num in num_list]

        # read list
        images = []
        for filename in tqdm(files, ascii=True, desc='Loading train images'):
            img = cv2.imread(os.path.join(self.img_dir, filename))
            img = cv2.resize(img, self.img_size)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            images.append(np.array(img))
        return images