import streamlit as st
from gtts import gTTS
import io

# 스마트폰 화면에 맞게 타이틀 설정
st.set_page_config(page_title="Text to MP3 변환기", layout="centered")

st.title("📱 Text to MP3 변환기")
st.write("텍스트를 입력하고 오디오 파일로 변환해 보세요.")

# 1. 텍스트 입력창 (모바일에서 터치하기 편한 크기)
text_input = st.text_area("음성으로 바꿀 텍스트를 입력하세요:", height=200)

# 언어 선택 기능 추가 (한국어 / 영어)
lang_option = st.selectbox("언어를 선택하세요:", ["한국어", "영어"])
lang_code = 'ko' if lang_option == "한국어" else 'en'

# 2. 변환 버튼 및 다운로드
if st.button("🎵 MP3 음성 생성하기", use_container_width=True):
    if text_input.strip() == "":
        st.warning("텍스트를 먼저 입력해 주세요!")
    else:
        with st.spinner("음성 파일 생성 중..."):
            # 텍스트를 음성으로 변환
            tts = gTTS(text=text_input, lang=lang_code)
            
            # 파일로 직접 저장하는 대신 메모리 버퍼에 저장 (웹 다운로드용)
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            
            st.success("🎉 변환 완료!")
            
            # 스마트폰에서 바로 들어볼 수 있는 플레이어 표시
            st.audio(mp3_fp, format="audio/mp3")
            
            # 스마트폰에 파일로 저장할 수 있는 다운로드 버튼
            st.download_button(
                label="📥 MP3 파일 핸드폰에 다운로드",
                data=mp3_fp,
                file_name="voice_output.mp3",
                mime="audio/mp3",
                use_container_width=True
            )