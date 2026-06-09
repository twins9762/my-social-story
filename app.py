import streamlit as st

# 1. 웹 페이지 기본 설정
st.set_page_config(page_title="사회적 상황 이야기 제작소", page_icon="📘", layout="wide")

st.title("📘 사회적 상황 이야기 & 감정카드 자동 생성기")
st.caption("상황을 입력하면 AI가 맞춤형 치료 콘텐츠를 생성합니다. 생성된 내용은 자유롭게 수정할 수 있습니다.")

# 2. 데이터 유지를 위한 세션 상태(Session State) 초기화
if "generated" not in st.session_state:
    st.session_state.generated = False
    st.session_state.story_text = ""
    st.session_state.image_prompt = ""
    st.session_state.emotion_text = ""

# 3. 사이드바 - 상황 입력 구역
st.sidebar.header("🎯 상황 설정")
user_situation = st.sidebar.text_area(
    "어떤 상황에 대한 이야기가 필요하신가요?",
    placeholder="예: 치과 치료를 무서워하는 아이, 친구 장난감 차례대로 빌리기 등"
)

generate_btn = st.sidebar.button("✨ AI 콘텐츠 생성하기", use_container_width=True)

# 4. 생성 버튼을 눌렀을 때 작동
if generate_btn and user_situation:
    st.session_state.generated = True
    
    # 가상의 생성 결과물 세팅 (테스트용 예시)
    st.session_state.story_text = f"[{user_situation}에 대한 이야기]\n\n우리는 가끔 이런 상황을 만납니다. 그럴 때는 마음을 차분히 먹고 대처하면 좋습니다. 첫째, 크게 숨을 쉽니다. 둘째, 도움을 요청합니다."
    st.session_state.image_prompt = f"한국인 어린이가 {user_situation} 상황에서 차분하게 대처하는 따뜻한 동화책 스타일의 일러스트"
    st.session_state.emotion_text = "😀 기쁨 / 😢 불안 / 🤝 안도감"


# 5. 메인 화면: 생성 및 편집 구역
if st.session_state.generated:
    st.success("✅ 콘텐츠 생성 완료! 아래에서 내용을 확인하고 마음에 안 드는 부분은 바로 수정하세요.")
    
    # 3단 레이아웃 분할 (이야기 | 시각 자료 | 감정 카드)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📝 1. 사회적 상황 이야기 (수정 가능)")
        st.session_state.story_text = st.text_area(
            "스토리를 편집하세요:", 
            value=st.session_state.story_text, 
            height=300
        )
        
    with col2:
        st.subheader("🎨 2. 시각 자료 생성 프롬프트")
        st.session_state.image_prompt = st.text_area(
            "이미지 생성용 설명을 편집하세요:", 
            value=st.session_state.image_prompt, 
            height=100
        )
        st.image("https://via.placeholder.com/400x300.png?text=AI+Visual+Image", caption="생성된 시각 자료 예시")
        if st.button("🔄 이미지 다시 생성"):
            st.toast("새로운 프롬프트로 이미지를 다시 그립니다!")

    with col3:
        st.subheader("🏷️ 3. 관련 감정 카드 (수정 가능)")
        st.session_state.emotion_text = st.text_area(
            "감정 키워드를 편집하세요:", 
            value=st.session_state.emotion_text, 
            height=100
        )
        st.info("💡 팁: 아이와 함께 이 감정들에 대해 이야기해 보세요.")
        
    st.divider()
    
    # 6. 최종 저장 및 다운로드 기능
    st.subheader("💾 최종 결과물 저장")
    final_submit = st.button("🚀 이대로 최종 확정 및 저장하기", type="primary")
    if final_submit:
        st.balloons()
        st.success("수정된 내용이 성공적으로 저장되었습니다! PDF 인쇄를 준비합니다.")

else:
    st.info("← 왼쪽 사이드바에 상황을 입력하고 'AI 콘텐츠 생성하기' 버튼을 눌러주세요.")
