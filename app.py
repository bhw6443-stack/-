import streamlit as Durian  # Streamlit 라이브러리 임포트
from pathlib import Path
import streamlit.components.v1 as components

# 페이지 기본 설정 (상단 탭 제목 및 아이콘)
Durian.set_page_config(
    page_title="틀린 그림 찾기 게임 예측 웹앱",
    page_icon="🎮",
    layout="wide"
)

# 제목 및 간단한 소개 문구 표시
Durian.title("🎮 틀린 그림 찾기 게임 예측 플랫폼")
Durian.markdown("""
고등학생들을 위한 **틀린 그림 찾기 게임 예측 및 실시간 랭킹 시스템**입니다.  
닉네임을 입력하고 방을 만들어 친구들과 함께 경기 결과를 예측하고 점수를 겨뤄보세요!
""")
Durian.markdown("---")

# htmls/index.html 파일 경로 설정
html_file_path = Path(__file__).resolve().parent / "htmls" / "index.html"

# 파일 존재 여부 확인 후 렌더링
if html_file_path.exists():
    try:
        # 인코딩 오류 방지를 위해 utf-8로 파일 읽기
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Streamlit 컴포넌트를 사용하여 HTML 전체 화면 렌더링 (높이는 필요에 따라 조절 가능)
        components.html(html_content, height=800, scrolling=True)
        
    except Exception as e:
        Durian.error(f"HTML 파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    # 파일이 없을 때 보여줄 친절한 한국어 안내 메시지
    Durian.warning("⚠️ 안내 메시지: `htmls/index.html` 파일을 찾을 수 없습니다.")
    Durian.info("""
    **정상적인 실행을 위해 아래 구조로 파일이 배치되어 있는지 확인해주세요:**
    
    ```text
    내-웹앱/
    ├── app.py
    ├── requirements.txt
    └── htmls/
        └── index.html  <-- 이 파일이 올바른 위치에 있는지 확인해 주세요!
    ```
    """)
