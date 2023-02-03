# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 10:00:36 2023

https://zenn.dev/ohtaman/articles/streamlit_tips

@author: sa_tsukida
"""

import streamlit as st

st.write('テスト')

def first_page():
    p='1'
    st.markdown(f"""
    # Welcome to the {p} Page!
    
    This is the first page.
    
    ![](https://picsum.photos/704/300?first)
    """)


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
    

PAGES = [
    {'dat': '11/26', 'contents': first_page},
    {'dat': '12/17', 'contents': second_page},
    {'dat': '1/14', 'contents': last_page}
]


def set_page(page_index):
    st.experimental_set_query_params(page=str(page_index))


def get_page_index():
    query = st.experimental_get_query_params().get('page')
    if query is not None and query[0].isdecimal():
        return min(int(query[0]), len(PAGES) - 1)
    else:
        return 0


def main():
    page_index = get_page_index()

    with st.sidebar:
        st.selectbox(
            '開催日',
            range(len(PAGES)),
            format_func=lambda x: PAGES[x]['dat'],
            index=page_index,
            key='select_page_index',
            on_change=lambda: set_page(st.session_state['select_page_index'])
        )
        
    # Show the page
    PAGES[page_index]['contents']()
    
    # Footer
    #st.progress((page_index + 1)/len(PAGES))
    cols = st.columns(6)
    with cols[2]:
        st.button(
            'Prev',
            on_click=lambda: set_page(page_index - 1),
            disabled=(page_index == 0) # disable button if on first page.
        )
    with cols[3]:
        st.button(
            'Next',
            on_click=lambda: set_page(page_index + 1),
            disabled=(len(PAGES) - 1 == page_index) # disable button if on last page.
        )

if __name__ == '__main__':
    main()
