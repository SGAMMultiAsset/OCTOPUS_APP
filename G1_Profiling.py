# streamlit run "D:\OCTOPUS\10.App\G1_Profiling.py"

import win32com.client as win32
import streamlit as st
import numpy as np
import pandas as pd
import os, sqlite3
from datetime import datetime


### 로컬 DB 설정

# 현재 절대경로 확인
abspath = os.path.abspath('/OCTOPUS/')


# SQLite3 DB 경로 지정
DB_DIR = os.path.join(abspath, "1.DB")
DB_FILE = 'octopusdb.sqlite3'
DB_PATH = os.path.join(DB_DIR, DB_FILE)

# SQLite3 DB에 쓰기
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS profiling(date_submitted DATE, Q1 TEXT, Q2 TEXT, Q3 TEXT, Q4 TEXT, Q5 TEXT, Q6 TEXT, Q7 TEXT, Q8 TEXT, Q9 TEXT, Q10 TEXT, Q11 TEXT, Q12 TEXT)')

def add_feedback(date_submitted, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12):
    c.execute('INSERT INTO profiling (date_submitted,Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11,Q12) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
              (date_submitted, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12))
    conn.commit()

### Streamlit 설정

def main():

    st.title("Smilegate Asset Management :smile:")

    st.header("Investor Risk/Return Profiling")

    d = st.date_input("Today's date", None, None, None, None)

    num = 0

# 투자경험
    question_1 = st.selectbox('고객님의 연령대는 어떻게 되십니까?',
                              ('', "만 19세 이하", "만 20세~30세", "만 31세~54세", "만 55세~64세", "만 65세 이상"))
    if question_1 == "만 19세 이하":
        num += 1
    elif question_1 == "만 20세~30세":
        num += 4
    elif question_1 == "만 31세~54세":
        num += 5
    elif question_1 == "만 55세~64세":
        num += 3
    elif question_1 == "만 65세 이상":
        num += 2
    st.write('고객님의 연령대는 - {}'.format(question_1), ' - 입니다')

# 투자목적
    question_2 = st.selectbox('고객님께서 투자하고자 하는 자금의 투자가능기간은 얼마나 되십니까?',
                              ('', "6개월 미만", "6개월 이상 ~ 1년 미만", "1년 이상 ~ 2년 미만", "2년 이상 ~ 3년 미만", "3년 이상"))
    if question_2 == "6개월 미만":
        num += 1
    elif question_2 == "6개월 이상 ~ 1년 미만":
        num += 2
    elif question_2 == "1년 이상 ~ 2년 미만":
        num += 3
    elif question_2 == "2년 이상 ~ 3년 미만":
        num += 4
    elif question_2 == "3년 이상":
        num += 5
    st.write('고객님의 투자가능기간은 - {}'.format(question_2), ' - 입니다')

# 투자경험
    question_3 = st.selectbox('고객님의 투자경험과 가장 가까운 금융 상품은 어느 것입니까?',
                              ('', "은행 예적금, 국채, 지방채, 보증채, MMF, CMA 등",
                               "금융채, 신용도가 높은 회사채, 채권형 펀드, 원금보장형 ELS 등",
                                "신용도가 중간 등급의 회사채, 원금의 일부만 보장되는 ELS, 혼합형 펀드 등",
                                 "신용도가 낮은 회사채, 주식, 원금 비보장 ELS, 시장 평균 수익률 추구 주식형 펀드 등",
                                  "ELW, 선물옵션, 시장수익률 초과 수익을 추구하는 주식형 펀드, 파생상품펀드, 주식 신용거래 등"))
    if question_3 == "은행 예적금, 국채, 지방채, 보증채, MMF, CMA 등":
        num += 1
    elif question_3 == "금융채, 신용도가 높은 회사채, 채권형 펀드, 원금보장형 ELS 등":
        num += 2
    elif question_3 == "신용도가 중간 등급의 회사채, 원금의 일부만 보장되는 ELS, 혼합형 펀드 등":
        num += 3
    elif question_3 == "신용도가 낮은 회사채, 주식, 원금 비보장 ELS, 시장 평균 수익률 추구 주식형 펀드 등":
        num += 4
    elif question_3 == "ELW, 선물옵션, 시장수익률 초과 수익을 추구하는 주식형 펀드, 파생상품펀드, 주식 신용거래 등":
        num += 5
    st.write('고객님의 투자경험은 - {}'.format(question_3), ' - 입니다')

# 투자경험
    question_4 = st.selectbox('고객님의 유사 금융투자상품의 투자경험 기간은 얼마나 되십니까?',
                              ('', "전혀 없음", "1년 미만", "1년 이상 ~ 3년 미만", "3년 이상 ~ 5년 미만", "5년 이상"))
    if question_4 == "전혀 없음":
        num += 1
    elif question_4 == "1년 미만":
        num += 2
    elif question_4 == "1년 이상 ~ 3년 미만":
        num += 3
    elif question_4 == "3년 이상 ~ 5년 미만":
        num += 4
    elif question_4 == "5년 이상":
        num += 5
    st.write('고객님의 투자경험 기간은 - 약 {}'.format(question_4), ' - 입니다')

# 투자목적
    question_5 = st.selectbox('고객님의 금융투자상품 취득 및 처분의 목적은 무엇입니까?',
                              ('', "채무상황", "생활비", "주택마련", "여유자금", "자산증식"))
    if question_5 == "채무상황":
        num += 1
    elif question_5 == "생활비":
        num += 2
    elif question_5 == "주택마련":
        num += 3
    elif question_5 == "여유자금":
        num += 4
    elif question_5 == "자산증식":
        num += 5
    st.write('고객님의 금융상품 취득 및 처분의 목적은 - {}'.format(question_5), ' - 입니다')

# 투자경험
    question_6 = st.selectbox('고객님께서 금융상품 투자에 대한 본인의 지식 수준이 어느 정도라고 생각 하십니까?',
                              ('', "[매우 낮은 수준] 금융투자상품에 대한 투자 경험이 없음",
                               "[낮은 수준] 널리 알려진 금융투자상품(주식,채권 및 펀드 등)의 구조 및 위험을 일정 부분 이해",
                                "[높은 수준] 널리 알려진 금융투자상품(주식,채권 및 펀드 등)의 구조 및 위험을 깊이 있게 이해",
                                  "[매우 높은 수준] 파생상품을 포함한 대부분의 금융투자상품의 구조 및 위험을 이해하고 있음"))
    if question_6 == "[매우 낮은 수준] 금융투자상품에 대한 투자 경험이 없음":
        num += 1
    elif question_6 == "[낮은 수준] 널리 알려진 금융투자상품(주식,채권 및 펀드 등)의 구조 및 위험을 일정 부분 이해":
        num += 2
    elif question_6 == "[높은 수준] 널리 알려진 금융투자상품(주식,채권 및 펀드 등)의 구조 및 위험을 깊이 있게 이해":
        num += 3
    elif question_6 == "[매우 높은 수준] 파생상품을 포함한 대부분의 금융투자상품의 구조 및 위험을 이해하고 있음":
        num += 4
    st.write('고객님의 금융상품에 대한 투자 수준은 - {}'.format(question_6), ' - 입니다')

# 투자위험 감수능력
    question_7 = st.selectbox('귀하가 금융상품 투자를 통해 기대하는 수익은 어느 정도입니까?\n*기대수익이 높은 만큼 위험도 높아짐',
                              ('', "투자원금에서 최소한의 손실만을 감수할 수 있음",
                               "투자원금 중 일부의 손실을 감수할 수 있음",
                                "기대수익이 높다면 위험이 높아도 상관하지 않음"))
    if question_7 == "투자원금에서 최소한의 손실만을 감수할 수 있음":
        num += 1
    elif question_7 == "투자원금 중 일부의 손실을 감수할 수 있음":
        num += 2
    elif question_7 == "기대수익이 높다면 위험이 높아도 상관하지 않음":
        num += 3
    st.write('귀하의 투자 기대 수준은 - {}'.format(question_7), ' - 입니다')

# 투자자산
    question_8 = st.selectbox('고객님의 보유 자산은 어느 정도입니까?',
                              ('', "1억원 미만", "2억원 미만", "5억원 미만", "10억원 미만", "10억원 이상"))
    if question_8 == "1억원 미만":
        num += 1
    elif question_8 == "2억원 미만":
        num += 2
    elif question_8 == "5억원 미만":
        num += 3
    elif question_8 == "10억원 미만":
        num += 4
    elif question_8 == "10억원 이상":
        num += 5
    st.write('고객님의 보유자산은 - 약 {}'.format(question_8), ' - 입니다')

# 투자자산
    question_9 = st.selectbox('향후 자신의 수입원에 대한 예상은 어떻게 되십니까?',
                              ('', "현재 일정한 수입이 발생하고 있으며, 향후 현재 수준을 유지하거나 증가할 것으로 예상",
                               "현재 일정한 수입이 발생하고 있으나, 향후 감소하거나 불안정할 것으로 예상",
                                "현재 일정한 수입이 없으며, 연금이 주 수입원임"))
    if question_9 == "현재 일정한 수입이 발생하고 있으며, 향후 현재 수준을 유지하거나 증가할 것으로 예상":
        num += 3
    elif question_9 == "현재 일정한 수입이 발생하고 있으나, 향후 감소하거나 불안정할 것으로 예상":
        num += 2
    elif question_9 == "현재 일정한 수입이 없으며, 연금이 주 수입원임":
        num += 1
    st.write('고객님은 - {}'.format(question_9), ' - 입니다')

# 투자목적
    question_10 = st.selectbox('고객님의 기대이익 수준은 어느 정도입니까?',
                              ('', "원금 기준 10%", "원금 기준 20%", "원금 기준 30%", "원금 기준 50%", "원금 기준 100%"))
    if question_10 == "원금 기준 10%":
        num += 1
    elif question_10 == "원금 기준 20%":
        num += 2
    elif question_10 == "원금 기준 30%":
        num += 3
    elif question_10 == "원금 기준 50%":
        num += 4
    elif question_10 == "원금 기준 100%":
        num += 5
    st.write('고객님의 기대이익 수준은 - 약 {}'.format(question_10), ' - 입니다')

# 손실
    question_11 = st.selectbox('고객님의 감내할 수 있는 손실의 수준은 어느 정도 입니까?',
                              ('', "원금의 -10%", "원금의 -20%", "원금의 -30%", "원금의 -50%", "원금의 -100%"))
    if question_11 == "원금의 -10%":
        num += 1
    elif question_11 == "원금의 -10%":
        num += 2
    elif question_11 == "원금의 -10%":
        num += 3
    elif question_11 == "원금의 -10%":
        num += 4
    elif question_11 == "원금의 -10%":
        num += 5
    st.write('고객님이 감내할 수 있는 손실 수준은 - 대략 {}'.format(question_11), ' - 입니다')

# 계산

    sum = ( num * 100 ) / 50

# 피드백
    question_12 = st.text_area("추가적인 코멘트가 있으시면 입력하세요.", "Type Here ...")
    st.text("시간 내주셔서 감사합니다!")

# 성향
    if sum <= 23:
        st.subheader("감사합니다!")
        st.write("귀하의 투자자 성향 진단 설문서 결과 ", "귀하의 투자 성향은 ", "안정형", " 입니다")
        st.info("안정형")
    elif sum > 23 and sum <= 40:
        st.subheader("감사합니다!")
        st.write("귀하의 투자자 성향 진단 설문서 결과 ", "귀하의 투자 성향은 ", "안정 추구형", " 입니다")
        st.info("안정 추구형")
    elif sum > 40 and sum <= 60:
        st.subheader("감사합니다!")
        st.write("귀하의 투자자 성향 진단 설문서 결과 ", "귀하의 투자 성향은 ", "위험 중립형", " 입니다")
        st.info("위험 중립형")
    elif sum > 60 and sum <= 80:
        st.subheader("감사합니다!")
        st.write("귀하의 투자자 성향 진단 설문서 결과 ", "귀하의 투자 성향은 ", "적극 투자형", " 입니다")
        st.info("적극 투자형")
    elif sum > 80:
        st.subheader("감사합니다!")
        st.write("귀하의 투자자 성향 진단 설문서 결과 ", "귀하의 투자 성향은 ", "공격 투자형", " 입니다")
        st.info("공격 투자형")

# 서명(Drawable Canvas)

# 제출
    if st.button("Submit profiling"):
        create_table()
        add_feedback(d, question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10, question_11, question_12)
        st.success("Profiling submitted")

if __name__ == '__main__':
    main()