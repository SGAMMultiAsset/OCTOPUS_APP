# streamlit run "D:\OCTOPUS\10.App\SGAM.py"

import streamlit as st
from pyparsing import empty
import os
from PIL import Image
import webbrowser

### 로컬 DB 설정
app_path = os.path.abspath('/OCTOPUS/')  # (절대)

### 전체 화면 폭
st.set_page_config("스마일게이트 자산운용 디지털플랫폼 데모버전", layout="wide")

### 화면 비율(여백/중앙/여백)
### 순서: 헤더/센터1/센터2/하단
empty1,con1,empty2 = st.columns([0.2,1.0,0.2])
empty1,con2,empty2 = st.columns([0.2,1.0,0.2])
empyt1,con3,con4,empty2 = st.columns([0.2,0.2,0.8,0.2])
empyt1,con5,con6,empty2 = st.columns([0.2,0.2,0.8,0.2])
empyt1,con7,con8,empty2 = st.columns([0.2,0.2,0.8,0.2])
empyt1,con9,con10,empty2 = st.columns([0.2,0.2,0.8,0.2])
empty1,con11,empty2 = st.columns([0.3,0.5,0.3])

# 콘텐츠 배치
def main() :

    with empty1 :
         empty()
# 헤더
    with con1 :
        st.image("http://www.smilegateam.com/images/common/logo.png", width=120,)
        st.title("스마일게이트 자산운용 디지털플랫폼 - 데모버전")
# 헤더
    with con2 :
        url = 'https://w.namu.la/s/55fa9032bb058c16f690c77d33389822894cdedbec83bd77945a131fe4838b0b784c83e180dbf5101e3c56746e8934f60974f3fa90d384906c5c1b9e7787032c6fd8ad7ff6c5e125d47583d62d266f6a9dd68712b644a559ccefdac8a2b256b45186a014d154538e2e89f0e774e5a948'
        st.image(url)
        st.text('사진출처 : https://namu.wiki/w/%ED%95%9C%EC%9C%A0%EC%95%84')
        
        img = Image.open(app_path+'/gui/SGAM.png')
        st.image(img)
# 센터1
    with con3 :
            st.markdown('''
            <a href="https://docs.streamlit.io">
            <img src="https://media.tenor.com/images/ac3316998c5a2958f0ee8dfe577d5281/tenor.gif" />
            </a>''',
            unsafe_allow_html=True
            )

            url = "http://www.smilegateam.com/kr/business/philosophy.php"
            if st.button('스마일게이트 자산운용', key='button1'):
               webbrowser.open_new_tab(url)

    with con4 :           
            st.title('투자자성향분석 화면')
            st.button('투자성향분석 확인하기')
# 센터2  
    with con5 :
            st.markdown('''
            <a href="https://docs.streamlit.io">
            <img src="https://media.tenor.com/images/ac3316998c5a2958f0ee8dfe577d5281/tenor.gif" />
            </a>''',
            unsafe_allow_html=True
            )

# 센터3
    with con6 :
            st.title('자산배분현황 화면')
            st.button('자산배분현황 확인하기')

    with con7 :
            url = "http://www.smilegateam.com/kr/business/philosophy.php"
            if st.button('스마일게이트 자산운용', key='button2'):
                webbrowser.open_new_tab(url)
# 센터4
    with con8 :
            st.title('상품선택현황 화면')
            st.button('상품선택현황 확인하기')

    with con9 :
            url = "http://www.smilegateam.com/kr/business/philosophy.php"
            if st.button('스마일게이트 자산운용', key='button3'):
                webbrowser.open_new_tab(url)
# 센터5
    with con10 :
            st.title('리밸런싱현황 화면')
            st.button('리밸런싱현황 확인하기')

# 하단
    with con11 :
            st.title('리밸런싱현황 화면')
            st.video('https://youtu.be/ERZ-1m_1B54') 

if __name__ == "__main__":
	main()


# 로컬에 있는 이미지를 링크로 만드는 코드
# import streamlit as st
# import os
# import base64

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# @st.cache(allow_output_mutation=True)
# def get_img_with_href(local_img_path, target_url):
#     img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
#     bin_str = get_base64_of_bin_file(local_img_path)
#     html_code = f'''
#         <a href="{target_url}">
#             <img src="data:image/{img_format};base64,{bin_str}" />
#         </a>'''
#     return html_code

# gif_html = get_img_with_href('tenor.gif', 'https://docs.streamlit.io')
# st.markdown(gif_html, unsafe_allow_html=True)
