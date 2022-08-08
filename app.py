import streamlit as st
import pandas as pd

# 제목
st.title('부산 RFID음식물 쓰레기 분석')
st.header('1. 데이터 불러오기')
st.subheader('1-1. 판다스로 csv 파일 읽기')

# 데이터 프레임 불러오기
df = pd.read_csv('부산RFID음식물쓰레기.csv')
st.dataframe(df)


# 지표 표시
max_num = f"{df['배출량'].max():,}"

st.metric('배출량 최대값 :', max_num)