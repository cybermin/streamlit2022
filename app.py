import streamlit as st
import pandas as pd



# 제목
st.title('대학 기숙사 분석')
#st.header('데이터 표시')

# 데이터 프레임 불러오기
df = pd.read_csv('기숙사수용현황.csv', encoding='cp949')
df = df[df['학교종류'] == '대학교']

#st.subheader('동적 데이터 프레임 표시')
#st.dataframe(df)

#st.subheader('정적 데이터 프레임 표시')
#st.table(df)


#st.header('대학')
#st.matric(label='전국대학수', value=len(df['학교'].unique()))
#st.write(len(df['학교'].unique()))

num1 = len(df['학교'].unique())
num2 = len(df[df['설립구분'] != '사립']['학교'].unique())
num3 = len(df[df['설립구분'] == '사립']['학교'].unique())
col1, col2, col3 = st.columns(3)
col1.metric("전국대학수", num1, "")
col2.metric("국공립학교수", num2, f'{round(num2/num1,2)*100}%')
col3.metric("사립학교수", num3, f'{round(num3/num1,2)*100}%')