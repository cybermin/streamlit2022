# streamlit
+ python으로 데이터 분석을 위한 웹앱을 쉽게 만들어주는 라이브러리

## streamlit 설정
1. github로 로그인한 후 repository 생성
2. github에 app.py 생성
3. https://streamlit.io/ 에 로그인 
4. https://streamlit.io/cloud 로 로그인
5. New App 생성

## streamlit API

### Text elements
1. 앱제목 
    + st.title() : 제목 형식으로 텍스트 표시 
    + st.header(): 헤더 형식으로 텍스트 표시
    + st.subheader() : 부제 형식으로 텍스트 표시

### Data display elements
2. 데이터프레임 표시
    + st.dataframe(데이터프레임) : 데이터프레임 표시
    + st.table(데이터프레임) : 데이터프레임 정적 테이블로 표시
    + st.metric(지표, 값) : 지표가 어떻게 변경되었는지에 대한 선택적 지표와 함께 큰 굵은 글꼴로 지표를 표시

### Chart elements
3. 챠트 그리기
    + st.line_chart(my_data_frame)


