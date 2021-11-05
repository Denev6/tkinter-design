'''Project Palette
functions for palette project
'''

from tkinter import filedialog
from tkinter.constants import END
import tkinter.messagebox as msgbox
import os
import webbrowser

from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image
import requests

if __name__ == '__main__':
    from data import *
else:
    from palette.data import *

def get_path(path):
    return os.path.join(os.getcwd(), path)

def open_url(url):
    try:
        webbrowser.open(url)
    except webbrowser.Error as exp:
        msgbox.showerror('오류', f'url을 정상적으로 열 수 없습니다.\n{exp}')
    except Exception:
        return

def save_new_csv(entry_1, entry_2, entry_3):
    path_now = os.getcwd()
    filename = filedialog.asksaveasfilename(initialdir=path_now,\
        title="저장", filetypes=(("데이터 파일", "*.csv"), \
        ("all files", "*.*")), defaultextension=".csv")
    if filename == '':
        return
    else:
        data = {'FEATURE_1' : entry_1.get(), 
                'FEATURE_2' : entry_2.get(), 
                'FEATURE_3' : entry_3.get()}
        df = pd.DataFrame(data, index=[0])
        df.to_csv(filename, index=False, encoding='utf-8')

def open_csv(entry_1, entry_2, entry_3):
    filename = ""
    path_now = os.getcwd()
    filename = filedialog.askopenfilename(title="데이터 파일을 선택하세요", \
        filetypes=(("데이터 파일", "*.csv"),("all files","*.*")),\
            initialdir=path_now)
    if filename == '':
        return
    else:
        if os.path.isfile(filename):
            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_3.delete(0, END)
            try:
                df = pd.read_csv(filename, nrows=1)
                values = df.iloc[0, 0:3]
                entry_1.insert(0, values[0])
                entry_2.insert(0, values[1])
                entry_3.insert(0, values[2])
            except:
                msgbox.showwarning("파일 오류", '데이터 파일이 손상되었습니다.\n직접 데이터를 입력하거나\n새로운 데이터 파일을 저장해 주세요.')
        else:
            msgbox.showerror("파일 없음", '해당 파일을 찾을 수 없습니다.\n다시 선택해 주세요.')

def get_img(img_file_name, folder=None, extension='png'):
    if folder is None:
        img_path = get_path(f'img\{img_file_name}.{extension}')
    elif folder:
        img_path = get_path(f'img\{folder}\{img_file_name}.{extension}')
    try:
        image = Image.open(img_path)
    except:
        img_path = get_path('img\error.png')
        image = Image.open(img_path)
    return image

def show_ImgPage(class_name, master, *parameters):
    '''class_name = ImgPage'''
    return class_name(master, *parameters)

def crawl_naver_datalab():
    '''
    datalab.naver.com/robots.txt
    (21/11/05)
    User-Agent: *
    Allow: /$
    Allow: /index.naver
    Disallow: /
    '''
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
    url = 'https://datalab.naver.com/index.naver'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        try:
            container = soup.select_one('#content > div.spot.section_keyword > div.home_section.active > div > div.keyword_carousel > div > div > div:nth-child(12) > div')
            datetime = container.select_one('strong > span').get_text()
            items = container.select('div > ul.rank_list > li > a > span.title')
            text = '  < 최근 트렌드 >\n\n'
            i = 1
            for item in items:
                item = item.get_text()
                text += f'     {i}. {item}\n'
                i += 1
        except:
            text = '\n네이버 데이터랩\n기능을 사용할 수 없습니다.'
        text += f'\n  {datetime}\n  © NAVER Corp. All Rights Reserved.'
    else: 
        text = f'\n서버가 정상적으로 응답하지 않습니다.\nHTTP status code: {response.status_code}'
    return text


'''Functions only for test GUI'''

def get_texts(num):
    '''get sample texts
    
    Args:
        num(int): number of texts to return
        
    Returns:
        list: list of sample texts 
    '''
    return ['SAMPLE' for i in range(num)]

def get_images(num):
    '''get sample images
    
    Args:
        num(int): number of images to return
        
    Returns:
        list: list of sample images    
    '''
    img_info = 'SAMPLE'
    return [img_info for i in range(num)]

def get_urls(num):
    '''get sample urls
       : https://fpalette.netlify.app/
    
    Args:
        num(int): number of urls to return
        
    Returns:
        list: list of sample urls    
    '''
    url = 'https://fpalette.netlify.app/'
    return [url for i in range(num)]

def get_colors(num):
    '''get sample colors
    
    Args:
        num(int): number of colors to return
        
    Returns:
        list: list of sample colors    
    '''
    color = '#8FAADC'
    return [color for i in range(num)]

def get_Text_sample(num):
    '''get sample text
    
    Args:
        num(int): number of new lines
        
    Returns:
        str: lines of sample texts    
    '''
    text = ''
    for i in range(num):
        text += f'-- Text {i} --'
    return text