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
max_num1 = f"{df['배출량'].max():,}"
max_area1 = f"{df[df['배출량'] == df['배출량'].max()]['시군구명']}"
 
st.write(str(df[df['배출량'] == df['배출량'].max()]['시군구명']))

col1, col2 = st.columns(2)
col1.metric('배출량 최대값 :', max_num1)
#col2.metric('배출량 최대 지역 :', max_area1)