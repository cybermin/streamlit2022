import streamlit as st
import pandas as pd
 


# 제목
st.title('대학 기숙사 분석')
#st.header('데이터 표시')

# 데이터 프레임 불러오기
df = pd.read_csv('기숙사수용현황분석.csv')
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

st.header('지역별 기숙사 현황')
dfg = df.groupby(['지역']).mean()
dfg = dfg[['기숙사수용률', '입사경쟁률']]

#st.dataframe(dfg)
st.line_chart(dfg['기숙사수용률'])
st.bar_chart(dfg['입사경쟁률'])

#사이드바 
with st.sidebar:
    gubun = st.radio(
     "설립구분선택",
     ('국공립', '사립'))
    
    if gubun == '국공립':
        dfradio =df[df['설립구분'] != '사립']
    else:
        dfradio =df[df['설립구분'] == '사립']

    area = st.text_input('지역입력', '부산')
    dfarea = df[df['지역'] == area]
 

st.subheader(gubun + '현황')
dfradiog = dfradio.groupby(['지역']).mean()
dfradiog = dfradiog[['기숙사수용률', '입사경쟁률']]
st.line_chart(dfradiog['기숙사수용률'])
st.bar_chart(dfradiog['입사경쟁률'])

st.subheader(area + '현황')
dfareag = dfarea.groupby(['학교']).mean()
st.line_chart(dfareag['기숙사수용률'])
st.bar_chart(dfareag['입사경쟁률'])
