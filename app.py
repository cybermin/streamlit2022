import streamlit as st
import pandas as pd



# 제목
st.title('대학 기숙사 분석')
st.header('데이터 표시')

# 데이터 프레임 불러오기
df = pd.read_csv('기숙사수용현황.csv', encoding='cp949')


#st.subheader('동적 데이터 프레임 표시')
#st.dataframe(df)

#st.subheader('정적 데이터 프레임 표시')
#st.table(df)


st.header('지표 표시')
#st.matric(label='전국대학수', value=len(df['학교'].unique()))
st.write(len(df['학교'].unique()))