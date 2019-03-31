import pandas as pd #引入pandas库，用来读取csv文件
import numpy as np
def read_file(path):
    df = pd.read_csv(path)#定义一个dataframe来存储csv文件的内容

    print(df['img_name'])#获取csv文件中img_name的所有内容
    print(df['width'])#width
    print(df['height'])#heigt
    print(df['label'])#label
    name = np.array(df['img_name'])
    print(name)
    for i_name in name:
        print(i_name)

def write_file():
    name = ['001.jpg','002.jpg','003.jpg']#待写入数据
    df = pd.DataFrame({'img_name':name})
    df.to_csv('name.csv',index=False)

if __name__ == "__main__":
    read_file(path = 'label.csv')
    write_file()
