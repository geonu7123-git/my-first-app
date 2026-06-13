import streamlit as st
import random

# ─── 페이지 기본 설정 ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MBTI × Pokémon",
    page_icon="⚡",
    layout="centered",
)

# ─── CSS 스타일링 ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;900&family=Press+Start+2P&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 40%, #0f3460 100%);
    min-height: 100vh;
}

/* 헤더 */
.hero-title {
    text-align: center;
    font-family: 'Press Start 2P', monospace;
    font-size: 1.4rem;
    color: #FFD700;
    text-shadow: 0 0 20px #FFD700aa, 3px 3px 0px #e67e00;
    line-height: 2;
    padding: 1rem 0 0.5rem;
}
.hero-sub {
    text-align: center;
    color: #a0c4ff;
    font-size: 1.05rem;
    margin-bottom: 2rem;
    letter-spacing: 0.03em;
}

/* 선택 박스 */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.07) !important;
    border: 2px solid #FFD70066 !important;
    border-radius: 14px !important;
    color: #fff !important;
    font-size: 1.15rem !important;
    font-family: 'Nunito', sans-serif !important;
}
div[data-baseweb="select"] svg { color: #FFD700 !important; }

/* 버튼 */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #FFD700, #FF8C00) !important;
    color: #1a1a2e !important;
    font-family: 'Press Start 2P', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 900 !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1rem 2rem !important;
    letter-spacing: 0.05em !important;
    box-shadow: 0 4px 20px #FFD70066 !important;
    transition: transform 0.1s, box-shadow 0.1s !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px #FFD700aa !important;
}
.stButton > button:active {
    transform: translateY(1px) !important;
}

/* 결과 카드 */
.result-card {
    background: linear-gradient(135deg, rgba(255,215,0,0.12), rgba(255,140,0,0.08));
    border: 2px solid #FFD70055;
    border-radius: 24px;
    padding: 2rem 2rem 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 8px 40px rgba(255,215,0,0.15), inset 0 0 60px rgba(255,255,255,0.02);
    position: relative;
    overflow: hidden;
}
.result-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 60% 40%, rgba(255,215,0,0.07) 0%, transparent 60%);
    pointer-events: none;
}

.pokemon-name {
    font-family: 'Press Start 2P', monospace;
    font-size: 1.2rem;
    color: #FFD700;
    text-shadow: 2px 2px 0 #e67e00;
    margin: 0.5rem 0;
}
.pokemon-emoji {
    font-size: 5rem;
    display: block;
    text-align: center;
    filter: drop-shadow(0 4px 16px rgba(255,215,0,0.5));
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.type-badge {
    display: inline-block;
    padding: 0.25rem 0.9rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
    margin: 0.2rem;
    letter-spacing: 0.04em;
}
.section-label {
    font-family: 'Press Start 2P', monospace;
    font-size: 0.6rem;
    color: #FFD700aa;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin: 1.2rem 0 0.4rem;
}
.desc-text {
    color: #d4e8ff;
    font-size: 1.0rem;
    line-height: 1.7;
}
.trait-chip {
    display: inline-block;
    background: rgba(160,196,255,0.15);
    border: 1px solid rgba(160,196,255,0.3);
    color: #a0c4ff;
    border-radius: 8px;
    padding: 0.3rem 0.75rem;
    font-size: 0.85rem;
    margin: 0.2rem;
    font-weight: 600;
}
.compat-card {
    background: rgba(255,255,255,0.05);
    border-radius: 14px;
    padding: 0.8rem 1rem;
    margin: 0.4rem 0;
    border-left: 3px solid;
    font-size: 0.92rem;
    color: #d4e8ff;
}

/* 구분선 */
.divider {
    border: none;
    border-top: 1px solid rgba(255,215,0,0.2);
    margin: 1rem 0;
}

/* selectbox label */
.stSelectbox label {
    color: #a0c4ff !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
}

/* 숨기기 */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─── 데이터 ────────────────────────────────────────────────────────────────────
MBTI_DATA = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🔮",
        "types": [("사이킥", "#7C5CBF", "#fff"), ("냉혹", "#2c3e50", "#ecf0f1")],
        "nickname": "전략가 포켓몬",
        "personality": (
            "혼자 조용한 곳에서 책을 읽다가 "
            "갑자기 세상을 바꿀 계획을 세우는 타입이에요. "
            "겉으론 차갑지만 자기 세계관이 확고하고, "
            "한번 목표를 정하면 누구도 못 말려요 🌑"
        ),
        "traits": ["독립적", "직관적", "완벽주의", "통찰력", "냉철함"],
        "best": ("ENTP", "💡 아이디어 폭격으로 자극을 줘요"),
        "worst": ("ESFP", "⚡ 에너지 방향이 완전 반대"),
        "quote": "\"나는 인간이 만든 것이 아니다. 나는 내가 만들어낸 존재다.\"",
    },
    "INTP": {
        "pokemon": "폴리곤Z",
        "emoji": "🖥️",
        "types": [("노말", "#A8A878", "#fff"), ("분석형", "#2980b9", "#fff")],
        "nickname": "탐구자 포켓몬",
        "personality": (
            "잠도 못 자고 새벽 3시에 '왜 하늘은 파랄까' 를 검색하는 타입 🌌 "
            "관심 없는 건 눈에 안 보이지만, "
            "흥미가 생기면 전문가보다 더 깊이 파고들어요. "
            "논리 오류에 매우 예민합니다."
        ),
        "traits": ["논리적", "창의적", "호기심 왕", "집중력", "유연한사고"],
        "best": ("ENTJ", "🏆 목표를 구체화해줘서 시너지 폭발"),
        "worst": ("ESTJ", "📋 규칙과 자유 사이의 충돌"),
        "quote": "\"모든 것은 데이터다. 감정도 패턴일 뿐.\"",
    },
    "ENTJ": {
        "pokemon": "루카리오",
        "emoji": "🥊",
        "types": [("격투", "#C03028", "#fff"), ("강철", "#B8B8D0", "#333")],
        "nickname": "지휘관 포켓몬",
        "personality": (
            "팀프로젝트에서 자동으로 리더가 되는 타입이에요 👑 "
            "비효율을 참지 못하고, 항상 '더 잘할 수 있어' 를 외쳐요. "
            "카리스마는 있지만 가끔 너무 앞서가서 주변이 못 따라가기도 해요."
        ),
        "traits": ["리더십", "결단력", "카리스마", "효율추구", "목표지향"],
        "best": ("INTP", "🧠 분석력으로 완벽한 팀워크"),
        "worst": ("ISFP", "🌸 페이스가 너무 달라요"),
        "quote": "\"약점은 고치는 것이 아니라 전략으로 보완한다.\"",
    },
    "ENTP": {
        "pokemon": "게코가",
        "emoji": "🦎",
        "types": [("물", "#6890F0", "#fff"), ("재치", "#F8D030", "#333")],
        "nickname": "발명가 포켓몬",
        "personality": (
            "토론을 게임처럼 즐기고 반대 의견도 재미로 내는 타입 🎲 "
            "아이디어가 넘쳐나지만 실행은… 음. "
            "지루한 건 못 참고 항상 새로운 자극을 찾아다녀요. "
            "대화 상대 중 제일 재미있는 사람이에요."
        ),
        "traits": ["창의적", "논쟁 즐김", "임기응변", "호기심", "에너자이저"],
        "best": ("INTJ", "⚔️ 아이디어를 현실로 만드는 콤비"),
        "worst": ("ISFJ", "🏡 안정 vs 변화 충돌"),
        "quote": "\"규칙은 깨지려고 있는 거야. 나는 새 규칙을 만들거든.\"",
    },
    "INFJ": {
        "pokemon": "루gia",
        "emoji": "🌊",
        "types": [("비행", "#A890F0", "#fff"), ("사이킥", "#7C5CBF", "#fff")],
        "nickname": "예언자 포켓몬",
        "personality": (
            "조용하지만 사람 마음을 꿰뚫어 보는 타입이에요 🔭 "
            "말이 없어 보여도 속에는 거대한 이상향이 있어요. "
            "공감 능력이 너무 강해서 가끔 지치기도 해요. "
            "세상에서 가장 희귀한 MBTI!"
        ),
        "traits": ["공감력", "통찰", "이상주의", "신중함", "깊은 생각"],
        "best": ("ENFP", "✨ 열정과 깊이의 황금 조합"),
        "worst": ("ESTP", "🌪️ 깊이 vs 즉흥의 충돌"),
        "quote": "\"나는 세상이 어때야 하는지 알고 있다.\"",
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "🦊",
        "types": [("노말", "#A8A878", "#fff"), ("감성", "#FFB7C5", "#333")],
        "nickname": "몽상가 포켓몬",
        "personality": (
            "혼자서 머릿속에 소설 열 편을 쓰고 있는 타입 📖 "
            "겉으론 조용해 보이지만 내면 세계는 우주보다 넓어요. "
            "가치관이 맞으면 엄청난 열정을 보여주지만, "
            "억지로 뭔가 하라고 하면 바로 에너지가 0이 됩니다."
        ),
        "traits": ["감수성", "창의적", "진정성", "이상주의", "공감왕"],
        "best": ("ENFJ", "💞 진심으로 이해해주는 최고 짝꿍"),
        "worst": ("ESTJ", "📊 현실 vs 이상의 충돌"),
        "quote": "\"나는 세상에 맞추기보다 세상을 바꾸고 싶다.\"",
    },
    "ENFJ": {
        "pokemon": "피카츄",
        "emoji": "⚡",
        "types": [("전기", "#F8D030", "#333"), ("카리스마", "#E74C3C", "#fff")],
        "nickname": "주인공 포켓몬",
        "personality": (
            "모든 사람의 감정을 케어하느라 자기가 지쳐있는 타입 💛 "
            "선생님, 리더, 친구 역할을 동시에 해내요. "
            "사람들에게 영감을 주는 재능이 있어요. "
            "그리고 당연히 모두에게 사랑받습니다!"
        ),
        "traits": ["따뜻함", "리더십", "공감력", "영감 제공", "소통 달인"],
        "best": ("INFP", "💫 서로의 감수성을 꽃피워줘요"),
        "worst": ("ISTP", "🔧 감정 vs 논리 간극"),
        "quote": "\"당신이 성장하는 걸 보는 게 내 기쁨이에요.\"",
    },
    "ENFP": {
        "pokemon": "마릴리",
        "emoji": "🎪",
        "types": [("물", "#6890F0", "#fff"), ("요정", "#EE99AC", "#fff")],
        "nickname": "활동가 포켓몬",
        "personality": (
            "5분 전에 만난 사람과 절친이 되는 타입이에요 🎉 "
            "세상 모든 것에 가능성을 보고, 항상 설레요. "
            "계획을 세워도 더 재밌는 게 생기면 바로 갈아타고... "
            "그래도 결국엔 잘 됩니다. 왜냐면 운이 좋거든요 🍀"
        ),
        "traits": ["사교적", "열정적", "자유로움", "낙천적", "상상력"],
        "best": ("INTJ", "🌟 꿈에 전략을 더해줘요"),
        "worst": ("ISTJ", "📅 자유 vs 규칙 충돌"),
        "quote": "\"가능성은 무한해! 일단 해보자고!\"",
    },
    "ISTJ": {
        "pokemon": "강철톤",
        "emoji": "🛡️",
        "types": [("강철", "#B8B8D0", "#333"), ("바위", "#B8A038", "#fff")],
        "nickname": "수호자 포켓몬",
        "personality": (
            "약속 시간 10분 전에 도착하고 항상 준비돼 있는 타입 ⏰ "
            "규칙과 절차를 중요하게 생각하고, "
            "맡은 일은 끝까지 완수해요. "
            "신뢰도 99999%의 든든한 존재예요."
        ),
        "traits": ["책임감", "신뢰성", "꼼꼼함", "체계적", "의리"],
        "best": ("ESFP", "🎊 완벽한 균형의 안정감"),
        "worst": ("ENFP", "🎪 체계 vs 즉흥의 충돌"),
        "quote": "\"한 번 약속하면 반드시 지킨다.\"",
    },
    "ISFJ": {
        "pokemon": "푸린",
        "emoji": "🎀",
        "types": [("노말", "#A8A878", "#fff"), ("요정", "#EE99AC", "#fff")],
        "nickname": "수호천사 포켓몬",
        "personality": (
            "남의 생일은 다 기억하는데 자기 생일은 그냥 넘기는 타입 🎂 "
            "배려심이 어마어마하고, 주변 사람들을 조용히 챙겨요. "
            "갈등을 싫어해서 참고 참다가 한 번씩 폭발하기도 해요... "
            "제발 자기 자신도 좀 챙기세요 🥺"
        ),
        "traits": ["배려심", "충성스러움", "섬세함", "인내력", "따뜻함"],
        "best": ("ESFP", "🌺 활기차게 이끌어줘요"),
        "worst": ("ENTP", "💥 평화 vs 도발 충돌"),
        "quote": "\"당신이 행복하면 나도 행복해요.\"",
    },
    "ESTJ": {
        "pokemon": "거북왕",
        "emoji": "🐢",
        "types": [("물", "#6890F0", "#fff"), ("얼음", "#98D8D8", "#333")],
        "nickname": "관리자 포켓몬",
        "personality": (
            "엑셀로 인생 계획을 짜고 그대로 실행하는 타입 📊 "
            "공정함과 질서를 중요하게 생각해요. "
            "책임지는 걸 두려워하지 않고 오히려 좋아해요. "
            "비효율적인 상황을 보면 자동으로 개선안이 떠올라요."
        ),
        "traits": ["조직력", "결단력", "공정함", "실용적", "추진력"],
        "best": ("ISFP", "🎨 부드러움이 균형을 맞춰줘요"),
        "worst": ("INFP", "🌈 현실 vs 이상의 충돌"),
        "quote": "\"계획이 없으면 실패를 계획하는 것이다.\"",
    },
    "ESFJ": {
        "pokemon": "냐오화",
        "emoji": "🌸",
        "types": [("불꽃", "#F08030", "#fff"), ("노말", "#A8A878", "#fff")],
        "nickname": "집사 포켓몬",
        "personality": (
            "모임에 간식 챙겨오고 자리 배치까지 신경 쓰는 타입 🍱 "
            "사람들의 기분을 항상 읽고, 분위기 메이커예요. "
            "인정받고 싶은 마음이 크고, 사람들에게 잘 보이고 싶어해요. "
            "진짜 따뜻한 사람입니다 ☀️"
        ),
        "traits": ["사교적", "배려심", "따뜻함", "현실적", "조화 추구"],
        "best": ("ISFJ", "🤝 서로를 완벽하게 이해해요"),
        "worst": ("INTP", "🤔 감성 vs 논리의 벽"),
        "quote": "\"모두가 웃는 걸 볼 때 나도 제일 행복해요.\"",
    },
    "ISTP": {
        "pokemon": "리자드",
        "emoji": "🔥",
        "types": [("불꽃", "#F08030", "#fff"), ("독립", "#7B68EE", "#fff")],
        "nickname": "장인 포켓몬",
        "personality": (
            "설명서를 안 읽어도 다 고칠 수 있는 타입이에요 🔧 "
            "말보다 행동으로 보여주고, 혼자 있는 시간을 사랑해요. "
            "위기 상황에서 냉정하게 대처하는 능력 탑클래스. "
            "감정 표현이 서툴러도 진심은 행동으로 나타나요."
        ),
        "traits": ["독립적", "냉철함", "실용적", "집중력", "문제해결"],
        "best": ("ESTJ", "⚙️ 실행력의 완벽한 결합"),
        "worst": ("ENFJ", "💬 침묵 vs 대화 충돌"),
        "quote": "\"말하는 시간에 직접 고치는 게 빠르다.\"",
    },
    "ISFP": {
        "pokemon": "이상해꽃",
        "emoji": "🌺",
        "types": [("풀", "#78C850", "#fff"), ("독", "#A040A0", "#fff")],
        "nickname": "예술가 포켓몬",
        "personality": (
            "카페에서 혼자 그림 그리거나 음악 듣는 걸 좋아하는 타입 🎨 "
            "감각이 예민하고 아름다운 것에 반응해요. "
            "자기 속도로 살아가는 걸 중요하게 생각하고, "
            "강요받는 걸 아주 싫어해요. 자유로운 영혼입니다 🕊️"
        ),
        "traits": ["감수성", "예술적", "자유로움", "온화함", "관찰력"],
        "best": ("ESFJ", "🌻 활발함이 꽃을 피워줘요"),
        "worst": ("ENTJ", "⚡ 압박 vs 자유 충돌"),
        "quote": "\"아름다운 순간들이 모여 인생이 된다.\"",
    },
    "ESTP": {
        "pokemon": "모부기",
        "emoji": "🚀",
        "types": [("물", "#6890F0", "#fff"), ("땅", "#E0C068", "#333")],
        "nickname": "사업가 포켓몬",
        "personality": (
            "지루한 걸 못 참고 항상 액션이 있어야 하는 타입 💥 "
            "사교성이 폭발적이고, 순발력이 최고예요. "
            "계획보다 즉흥이 더 잘 맞고, "
            "위험한 도전도 두근거림으로 받아들여요. 진짜 살아있는 느낌!"
        ),
        "traits": ["행동파", "사교적", "현실적", "대담함", "순발력"],
        "best": ("ISFJ", "🏠 든든한 안전망이 돼줘요"),
        "worst": ("INFJ", "🌙 현재 vs 미래 충돌"),
        "quote": "\"생각보다 먼저 움직여라!\"",
    },
    "ESFP": {
        "pokemon": "잠만보",
        "emoji": "💫",
        "types": [("노말", "#A8A878", "#fff"), ("물", "#6890F0", "#fff")],
        "nickname": "연예인 포켓몬",
        "personality": (
            "어딜 가든 분위기를 장악하고 모두를 웃게 만드는 타입 🎤 "
            "현재 이 순간을 사랑하고, 즐기는 데 천재예요. "
            "계획보다 감성이 앞서고, "
            "솔직하고 유쾌한 에너지가 모두를 끌어당겨요. "
            "함께하면 무조건 재밌어집니다! 🎉"
        ),
        "traits": ["유쾌함", "즉흥적", "사교적", "현재집중", "에너지"],
        "best": ("ISTJ", "⚓ 안정감을 주는 최고 조합"),
        "worst": ("INTJ", "🔮 즉흥 vs 전략 충돌"),
        "quote": "\"지금 이 순간이 제일 중요해! 즐기자고!\"",
    },
}

TYPE_COLORS = {
    "불꽃": ("#F08030", "#fff"),
    "물": ("#6890F0", "#fff"),
    "풀": ("#78C850", "#fff"),
    "전기": ("#F8D030", "#333"),
    "사이킥": ("#F85888", "#fff"),
    "강철": ("#B8B8D0", "#333"),
    "바위": ("#B8A038", "#fff"),
    "노말": ("#A8A878", "#fff"),
    "독": ("#A040A0", "#fff"),
    "얼음": ("#98D8D8", "#333"),
    "비행": ("#A890F0", "#fff"),
    "격투": ("#C03028", "#fff"),
    "요정": ("#EE99AC", "#333"),
    "땅": ("#E0C068", "#333"),
}

MBTI_LIST = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP",
]

# ─── UI ────────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">⚡ MBTI × POKÉMON ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">당신의 MBTI에 꼭 맞는 포켓몬을 찾아드려요 🔍</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    mbti = st.selectbox(
        "✨ 나의 MBTI를 선택하세요",
        options=[""] + MBTI_LIST,
        format_func=lambda x: "선택하세요 👇" if x == "" else x,
    )
    btn = st.button("🔍 나의 포켓몬 찾기!")

if btn:
    if not mbti:
        st.warning("⚠️ MBTI를 먼저 선택해주세요!")
    else:
        # 풍선 효과 🎈
        st.balloons()

        d = MBTI_DATA[mbti]

        # 결과 카드
        st.markdown(f"""
        <div class="result-card">
            <div style="text-align:center; margin-bottom:1rem;">
                <span style="background:rgba(255,215,0,0.18); color:#FFD700;
                    font-family:'Press Start 2P',monospace; font-size:0.6rem;
                    padding:0.4rem 1rem; border-radius:999px; letter-spacing:0.15em;">
                    {mbti} 유형
                </span>
            </div>
            <span class="pokemon-emoji">{d['emoji']}</span>
            <div style="text-align:center; margin: 0.8rem 0 0.3rem;">
                <span class="pokemon-name">{d['pokemon']}</span>
            </div>
            <div style="text-align:center; color:#a0c4ffbb; font-size:0.88rem; margin-bottom:1rem;">
                {d['nickname']}
            </div>
        """, unsafe_allow_html=True)

        # 타입 뱃지
        badge_html = '<div style="text-align:center; margin-bottom:0.5rem;">'
        for tname, bg, fg in d["types"]:
            badge_html += f'<span class="type-badge" style="background:{bg};color:{fg};">{tname}</span>'
        badge_html += "</div>"
        st.markdown(badge_html, unsafe_allow_html=True)

        st.markdown('<hr class="divider">', unsafe_allow_html=True)

        # 성격 설명
        st.markdown(f"""
            <div class="section-label">✦ 성격 분석</div>
            <div class="desc-text">{d['personality']}</div>
        """, unsafe_allow_html=True)

        # 특성 칩
        chips = "".join(f'<span class="trait-chip">{t}</span>' for t in d["traits"])
        st.markdown(f"""
            <div class="section-label" style="margin-top:1.2rem;">✦ 핵심 특성</div>
            <div>{chips}</div>
        """, unsafe_allow_html=True)

        st.markdown('<hr class="divider">', unsafe_allow_html=True)

        # 궁합
        best_mbti, best_desc = d["best"]
        worst_mbti, worst_desc = d["worst"]
        st.markdown(f"""
            <div class="section-label">✦ 궁합</div>
            <div class="compat-card" style="border-color:#2ecc71;">
                💚 <strong style="color:#2ecc71;">최고 궁합</strong> &nbsp;
                <span style="background:rgba(46,204,113,0.2); padding:0.1rem 0.5rem;
                    border-radius:6px; font-weight:700; color:#2ecc71;">{best_mbti}</span>
                &nbsp; {best_desc}
            </div>
            <div class="compat-card" style="border-color:#e74c3c;">
                ❤️‍🔥 <strong style="color:#e74c3c;">조심 궁합</strong> &nbsp;
                <span style="background:rgba(231,76,60,0.2); padding:0.1rem 0.5rem;
                    border-radius:6px; font-weight:700; color:#e74c3c;">{worst_mbti}</span>
                &nbsp; {worst_desc}
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<hr class="divider">', unsafe_allow_html=True)

        # 명언
        st.markdown(f"""
            <div class="section-label">✦ {d['pokemon']}의 한마디</div>
            <div style="text-align:center; color:#FFD700; font-size:1.05rem;
                font-style:italic; line-height:1.8; padding: 0.5rem 0 1rem;">
                {d['quote']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 다시 하기 안내
        st.markdown("""
        <div style="text-align:center; color:#a0c4ff88; font-size:0.82rem; margin-top:1.5rem;">
            다른 MBTI도 궁금하다면 위에서 다시 선택해보세요 🔄
        </div>
        """, unsafe_allow_html=True)
