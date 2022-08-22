import streamlit as st
import pandas as pd



# 제목
st.title('대학 기숙사 분석')
st.header('1. 데이터 불러오기')
st.subheader('1-1. 판다스로 csv 파일 읽기')

# 데이터 프레임 불러오기
df = pd.read_csv('기숙사수용현황.csv', encoding='cp949')
st.dataframe(df)

