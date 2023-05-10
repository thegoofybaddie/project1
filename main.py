import streamlit as st
import pandas as pd
from dataframe import df
from graph import box, histogram,pie
from tab0 import student_list
from tab1 import score
from tab2 import kmeans

st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')


tabs_titles = ('Danh sách',
               'Biểu đồ',
               'Phân nhóm',
               'Phân loại')
tabs = st.tabs(tabs_titles)


                
with tabs[0]:
    student_list()

   
with tabs[1]:
    tabs1_titles = ('Số lượng hs',
                    'Điểm')
    tabs1 = st.tabs(tabs1_titles)
    with tabs1[1]:
        score()

with tabs[2]:
    kmeans()
    
















