# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:00:36 2023

https://zenn.dev/ohtaman/articles/streamlit_tips

マルチ-ページ
https://techblog.cccmk.co.jp/entry/2022/12/06/094302
https://kajiblo.com/streamlit-sidebar/

streamlitで別ページ（タブ）にデータを持ち越す
https://qiita.com/niship2/items/f0c825c6f0d291583b27

複数遷移
st.experimental_set_query_params

Streamlit入門 – テーマの変更, ページの設定
https://data-analytics.fun/2022/07/10/streamlit-theme-page-settings/

カラー
https://www.colordic.org/

@author: sa_tsukida
"""

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="sttest", 
    page_icon='ccc.JPG', 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': """
         # 画像生成風アプリ
         このアプリは画像生成風アプリで、実際にはキングスライムしか表示しません。
         """
     })

#st.write('テスト')

f = open('myfile.txt', 'r', encoding='UTF-8')
data = f.read()
f.close()

link='https://picsum.photos/704/300?second'



def first_page():
    st.write('first_page')
#    p=data
#    st.markdown(f"""
#    # {p} 
#    []({link})
#    """
#    )
#    img=Image.open('ccc.JPG')
#    st.image(img,caption='jpg_title',use_column_width=True)
#
#    # 見た目を3分割して写真を配置
#    num=3
#    col= st.columns(num)
#
#    for i in list(range(0,num,1)):
#        with col[i]:
#            st.header("図"+str(i+1))
#            
#            st.image(str(i+1)+".JPG", use_column_width=True)
#            # ×　st.footer("図"+str(i+1))



def second_page():
    p='2'
    st.markdown(f"""
    # Welcome to the {p} Page!
    
    This is the second page.
    
    ![](https://picsum.photos/704/300?second)
    """)

    
def last_page():
    p='last'
    st.markdown(f"""
    # Welcome to the {p} Page!
    
    This is the last page.
    
    ![](https://picsum.photos/704/300?last)
    """)

def main():
    
    st.header('Configuration： Theme')
    st.checkbox(label='Check')
    st.slider(label='Slider')
    st.selectbox(label='Choose Your Favourite', options=['Snowpeak', 'Rakuten', 'Toyota Motors'])
    
   
    
    #セレクトボックスのリストを作成
    pagelist = ["1","2","3"]
    #サイドバーのセレクトボックスを配置
    selector=st.sidebar.selectbox( "ページ選択",pagelist)
    if selector=="1":
        first_page()
        path="./2/2"
        st.image(f"{path}.JPG", use_column_width=True)
        if st.button('ページ1ボタン'):
            st.title("ページ1のタイトル")
            
    elif selector=="2":
        if st.button('ページ2ボタン'):
            st.title("ページ2のタ.イトル")
    elif selector=="3":
        if st.button('ページ3ボタン'):
            st.title("ページ3のタイトル")
            
#PAGES = [
#    {'dat': '11/26', 'contents': first_page},
#    {'dat': '12/17', 'contents': second_page},
#    {'dat': '1/14', 'contents': last_page}
#]
#
#
#def set_page(page_index):
#    st.experimental_set_query_params(page=str(page_index))
#
#
#def get_page_index():
#    query = st.experimental_get_query_params().get('page')
#    if query is not None and query[0].isdecimal():
#        return min(int(query[0]), len(PAGES) - 1)
#    else:
#        return 0
#
#
#def main():
#    page_index = get_page_index()
#
#    with st.sidebar:
#        st.selectbox(
#            '開催日',
#            range(len(PAGES)),
#            format_func=lambda x: PAGES[x]['dat'],
#            index=page_index,
#            key='select_page_index',
#            on_change=lambda: set_page(st.session_state['select_page_index'])
#        )
#        
#    # Show the page
#    PAGES[page_index]['contents']()
#    
#    # Footer
#    #st.progress((page_index + 1)/len(PAGES))
#    cols = st.columns(6)
#    with cols[2]:
#        st.button(
#            'Prev',
#            on_click=lambda: set_page(page_index - 1),
#            disabled=(page_index == 0) # disable button if on first page.
#        )
#    with cols[3]:
#        st.button(
#            'Next',
#            on_click=lambda: set_page(page_index + 1),
#            disabled=(len(PAGES) - 1 == page_index) # disable button if on last page.
#        )

if __name__ == '__main__':
    main()
