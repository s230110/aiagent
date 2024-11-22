# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl')

# 2. 모델 설명
st.title('합불 분류 에이전트')
col1, col2,col3 = st.columns( 3 )     
with col1:
      st.subheader('모델 설명')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 278건')
      st.write(' - 테스트 데이터 : 119건')
      st.write(' - 모델 정확도 : 0.72')
# 3.데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화2')
      st.image('시각화2.png')    # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 증상을 입력하세요. 심장병 진단을 내려드립니다.')

a = st.number_input(' 나이 입력 ', value= 0)      #초기값은 0
b = st.number_input(' 성별 입력 (여자 = 0, 남자 = 1) ', value= 0 )     # 초기값은 0
c = st.number_input(' 가슴 통증 유무 ( 유 = 0, 무 = 1) ', value= 0 )     # 초기값은 0
d = st.number_input(' 안정시 혈압 수치 ', value=0)      #초기값은 0
e = st.number_input(' 최대 심박수 ', value=0 )     # 초기값은 0


if st.button(' 결과 확인하기 '):            # 사용자가 '결과 확인' 버튼을 누르면
        input_data = [[a,b,c,d,e]]     # 사용자가 입력한 a,b,c,d,e 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        if p[0] == 1 :
              st.success('심장병일 가능성이 높습니다. 병원에 방문해주세요.')
        else:
              st.success('심장병일 가능성이 낮습니다. 하지만 통증이 계속된다면 병원에 방문해주세요.')
