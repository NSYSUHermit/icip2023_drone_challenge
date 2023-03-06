import pandas as pd
import xmltodict
import json

file = 'D:/Projects/ICIP2023_CHANLLENGE/flight-mbg02/ann/video02.xml'

# 讀取XML文件
with open(file, 'r') as f:
    xml_data = f.read()

# 將XML轉換成字典格式
dict_data = xmltodict.parse(xml_data)

# 將字典轉換為JSON格式
df = pd.read_json(json.dumps(dict_data))
pd.DataFrame(pd.DataFrame(df.annotations.track)['box'][0:1][0])

# 輸出JSON數據
print(pd.DataFrame(pd.DataFrame(df.annotations.track)['box'][0:1][0]))

from PIL import Image, ImageDraw
# 加載圖片
image = Image.open("D:/Projects/ICIP2023_CHANLLENGE/flight-mbg02/avi/photos/frame_67.jpg")
draw = ImageDraw.Draw(image)

# 繪製表格
data = pd.DataFrame(pd.DataFrame(df.annotations.track)['box'][0:1][0])
data['@xtl'] = data['@xtl'].astype(float)
data['@ytl'] = data['@ytl'].astype(float)
data['@xbr'] = data['@xbr'].astype(float)
data['@ybr'] = data['@ybr'].astype(float)


draw = ImageDraw.Draw(image)
data1 = data.iloc[0:1,:]
for index, row in data1.iterrows():
    draw.rectangle((row['@xtl'], row['@ytl'], row['@xbr'], row['@ybr']), outline='red')
    draw.text((row['@xtl'], row['@ytl']), str(row['@frame']), fill='red')
    # 保存繪製後的圖片
    image.save("D:/Projects/ICIP2023_CHANLLENGE/flight-mbg02/avi/photos/your_output_image.jpg")

