import streamlit as st

# ─── 페이지 설정 ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MBTI × LoL 챔피언",
    page_icon="⚔️",
    layout="centered",
)

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Noto+Sans+KR:wght@400;500;700&display=swap');

html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }

.stApp {
    background: linear-gradient(160deg, #0a0a14 0%, #0d1117 40%, #0a0f1e 70%, #110a0a 100%);
    min-height: 100vh;
}

.hero-wrap { text-align:center; padding:2.2rem 0 0.5rem; }
.hero-eyebrow {
    font-family:'Cinzel',serif; font-size:0.7rem; letter-spacing:0.35em;
    color:#C89B3C; text-transform:uppercase; margin-bottom:0.6rem;
}
.hero-title {
    font-family:'Cinzel',serif; font-size:clamp(1.6rem,5vw,2.6rem); font-weight:900;
    line-height:1.15;
    background:linear-gradient(135deg,#C89B3C 0%,#F0E6BE 45%,#C89B3C 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    margin-bottom:0.4rem;
}
.hero-sub { color:#7a8fa6; font-size:0.95rem; margin-bottom:0.5rem; letter-spacing:0.02em; }
.gold-line {
    width:120px; height:2px;
    background:linear-gradient(90deg,transparent,#C89B3C,transparent);
    margin:0.8rem auto 1.8rem;
}

/* 셀렉트박스 */
div[data-baseweb="select"] > div {
    background:rgba(200,155,60,0.07) !important; border:1.5px solid #C89B3C55 !important;
    border-radius:10px !important; color:#e8dfc8 !important;
    font-size:1.05rem !important; font-family:'Noto Sans KR',sans-serif !important;
}
div[data-baseweb="select"] > div:hover { border-color:#C89B3Caa !important; }
div[data-baseweb="select"] svg { color:#C89B3C !important; }
div[data-baseweb="select"] li { background:#0d1117 !important; color:#e8dfc8 !important; }
.stSelectbox label {
    color:#C89B3C !important; font-weight:700 !important;
    font-size:0.88rem !important; letter-spacing:0.08em !important;
    text-transform:uppercase !important;
}

/* 버튼 */
.stButton > button {
    width:100%;
    background:linear-gradient(135deg,#7a5c1e 0%,#C89B3C 50%,#7a5c1e 100%) !important;
    color:#0a0a14 !important; font-family:'Cinzel',serif !important;
    font-size:0.85rem !important; font-weight:700 !important; border:none !important;
    border-radius:10px !important; padding:0.85rem 2rem !important;
    letter-spacing:0.12em !important; box-shadow:0 4px 24px rgba(200,155,60,0.35) !important;
    transition:all 0.2s !important;
}
.stButton > button:hover {
    box-shadow:0 6px 32px rgba(200,155,60,0.55) !important;
    transform:translateY(-1px) !important;
}
.stButton > button:active { transform:translateY(1px) !important; }

/* 결과 카드 전체 래퍼 */
.result-wrap {
    background:linear-gradient(160deg,rgba(200,155,60,0.08) 0%,rgba(10,10,20,0.97) 60%);
    border:1.5px solid #C89B3C44; border-radius:20px;
    padding:0 0 1.6rem; margin:1.8rem 0 1rem; position:relative; overflow:hidden;
    box-shadow:0 0 60px rgba(200,155,60,0.08), inset 0 0 40px rgba(200,155,60,0.03);
}
.result-wrap::before {
    content:''; position:absolute; top:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg,transparent,#C89B3C,transparent);
}

/* 코너 장식 */
.corner { position:absolute; width:18px; height:18px; border-color:#C89B3C88; border-style:solid; }
.corner-tl { top:8px; left:8px; border-width:2px 0 0 2px; }
.corner-tr { top:8px; right:8px; border-width:2px 2px 0 0; }
.corner-bl { bottom:8px; left:8px; border-width:0 0 2px 2px; }
.corner-br { bottom:8px; right:8px; border-width:0 2px 2px 0; }

/* 스플래시 이미지 영역 */
.splash-wrap {
    position:relative; width:100%; height:320px; overflow:hidden;
    border-radius:18px 18px 0 0;
}
.splash-img {
    width:100%; height:100%; object-fit:cover; object-position:top center;
    display:block; filter:brightness(0.88) contrast(1.05);
    transition:transform 0.6s ease;
}
.splash-wrap:hover .splash-img { transform:scale(1.03); }
.splash-overlay {
    position:absolute; bottom:0; left:0; right:0; height:55%;
    background:linear-gradient(to top, #0a0a14 0%, rgba(10,10,20,0.5) 60%, transparent 100%);
}
.splash-mbti-pill {
    position:absolute; top:14px; left:14px;
    border:1px solid #C89B3Ccc; background:rgba(10,10,20,0.75);
    color:#C89B3C; font-family:'Cinzel',serif; font-size:0.62rem;
    padding:0.3rem 1rem; border-radius:999px; letter-spacing:0.2em;
    backdrop-filter:blur(4px);
}
.splash-lane-pill {
    position:absolute; top:14px; right:14px;
    border:1px solid rgba(255,255,255,0.2); background:rgba(10,10,20,0.75);
    color:#b8c8d8; font-size:0.72rem;
    padding:0.3rem 0.85rem; border-radius:999px;
    backdrop-filter:blur(4px);
}

/* 챔피언 아이콘 오버레이 */
.champ-icon-wrap {
    position:absolute; bottom:-28px; left:50%; transform:translateX(-50%);
    width:64px; height:64px; border-radius:50%;
    border:3px solid #C89B3C; overflow:hidden;
    box-shadow:0 0 20px rgba(200,155,60,0.6);
    background:#0a0a14;
}
.champ-icon-img { width:100%; height:100%; object-fit:cover; }

/* 카드 하단 텍스트 영역 */
.card-body { padding:2.8rem 1.8rem 0.5rem; text-align:center; }
.champ-name {
    font-family:'Cinzel',serif; font-size:1.75rem; font-weight:900;
    background:linear-gradient(135deg,#C89B3C,#F0E6BE,#C89B3C);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    margin:0.1rem 0;
}
.champ-title { color:#7a8fa6; font-size:0.85rem; letter-spacing:0.08em; margin-bottom:0.8rem; }

.role-badge {
    display:inline-block; padding:0.28rem 0.85rem; border-radius:6px;
    font-size:0.78rem; font-weight:700; margin:0.2rem 0.12rem;
    letter-spacing:0.04em; border:1px solid;
}

/* 섹션 공통 */
.card-section { padding:0 1.8rem; }
.section-eyebrow {
    font-family:'Cinzel',serif; font-size:0.58rem; letter-spacing:0.25em;
    color:#C89B3Caa; text-transform:uppercase; margin:1.4rem 0 0.5rem;
}
.desc-body { color:#b8c8d8; font-size:0.97rem; line-height:1.8; }
.trait-chip {
    display:inline-block; background:rgba(200,155,60,0.1);
    border:1px solid rgba(200,155,60,0.3); color:#C89B3C;
    border-radius:6px; padding:0.28rem 0.75rem;
    font-size:0.82rem; margin:0.2rem 0.12rem; font-weight:600;
}
.compat-row {
    display:flex; align-items:flex-start; gap:0.75rem;
    background:rgba(255,255,255,0.03); border-radius:10px;
    padding:0.8rem 1rem; margin:0.4rem 0; border-left:3px solid;
    font-size:0.9rem; color:#b8c8d8; line-height:1.6;
}
.quote-block {
    text-align:center; color:#C89B3Ccc; font-family:'Cinzel',serif;
    font-size:0.92rem; font-style:italic; line-height:1.9;
    padding:0.5rem 0 0.8rem; letter-spacing:0.02em;
}
.sep { border:none; border-top:1px solid rgba(200,155,60,0.15); margin:1rem 0; }

#MainMenu, footer, header { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ─── 이미지 URL 헬퍼 ──────────────────────────────────────────────────────────
DDRAGON = "https://ddragon.leagueoflegends.com/cdn"
PATCH   = "14.24.1"   # 최신 패치로 업데이트하려면 이 값만 바꾸세요

def splash_url(champ_id: str, skin: int = 0) -> str:
    """로딩 화면 세로형 이미지 (308×560) — 별도 라이브러리 불필요"""
    return f"{DDRAGON}/img/champion/loading/{champ_id}_{skin}.jpg"

def icon_url(champ_id: str) -> str:
    """챔피언 정사각 아이콘 (120×120)"""
    return f"{DDRAGON}/{PATCH}/img/champion/{champ_id}.png"

# ─── 데이터 ────────────────────────────────────────────────────────────────────
MBTI_DATA = {
    "INTJ": {
        "champion": "제드", "champ_id": "Zed",
        "title": "그림자의 주인", "icon": "🥷",
        "roles": [("암살자","#e74c3c"),("닌자","#7f8c8d")],
        "lane": "📍 미드 / 정글",
        "personality": (
            "처음부터 끝까지 혼자서 계획하고, 혼자서 실행하고, 혼자서 이기는 타입이에요. "
            "팀원이 '우리 같이 가요'라고 해도 이미 반대쪽 정글을 청소하고 있어요 🌑 "
            "감정보다 효율, 공감보다 전략. 적이 뭘 할지 두 수 앞을 읽고 플레이해요. "
            "하지만 게임 오래 하면 챔피언처럼 '나는 적이 없다, 그림자만 있을 뿐'이 되는 거 아닌지 걱정됩니다."
        ),
        "traits": ["전략가","완벽주의","독립적","냉철함","통찰력"],
        "best":  ("ENTP", "💡 아이디어로 판을 흔들어줘서 시너지 폭발"),
        "worst": ("ESFP", "🎉 진지한 전략 vs 즉흥 한타... 서로 답답해요"),
        "playstyle": "📌 솔로 캐리형 — 맵 리딩으로 혼자 게임 터뜨리는 스타일",
        "quote": "\"그림자는 빛이 없어도 존재한다.\"",
    },
    "INTP": {
        "champion": "리산드라", "champ_id": "Lissandra",
        "title": "빙설의 마녀", "icon": "❄️",
        "roles": [("메이지","#3498db"),("CC기","#9b59b6")],
        "lane": "📍 미드",
        "personality": (
            "이론은 완벽하게 세워져 있는데 실전 가면 '어... 잠깐만' 하는 타입 🤔 "
            "패치 노트 분석하는 시간이 실제 게임 시간보다 길고, "
            "챔피언 풀이 왜 저게 최선인지 20분 동안 설명할 수 있어요. "
            "감정 기복 없이 냉정하게 리뷰하지만, 본인 실수는 '변수였어'로 처리합니다 🧊"
        ),
        "traits": ["분석적","논리적","호기심","객관적","이론파"],
        "best":  ("ENTJ", "🏆 이론에 추진력을 더해주면 무적"),
        "worst": ("ESTJ", "📋 내 방식대로 하게 놔줘요, 제발"),
        "playstyle": "📌 계산 플레이형 — CC 연계와 포지셔닝으로 싸우는 스타일",
        "quote": "\"차가움이란 감정의 부재가 아니라, 완전한 통제다.\"",
    },
    "ENTJ": {
        "champion": "다리우스", "champ_id": "Darius",
        "title": "녹서스의 손", "icon": "⚔️",
        "roles": [("파이터","#e67e22"),("탱커","#95a5a6")],
        "lane": "📍 탑",
        "personality": (
            "팀원들이 뭉개고 있으면 혼자서 텔포 타고 가서 적 탑을 갈아버리는 타입 👑 "
            "리더십이 자동으로 발동되고, 비효율적인 플레이를 보면 즉시 핑 열 개. "
            "이기는 방법을 정확히 알고 있고, 그대로 실행해요. "
            "팀원들이 따라오면 무조건 이기고... 안 따라오면 혼자라도 이겨요 💪"
        ),
        "traits": ["리더십","결단력","추진력","카리스마","목표지향"],
        "best":  ("INTP", "🧠 분석력과 결합하면 최강 조합"),
        "worst": ("ISFP", "🌸 왜 저렇게 느릿느릿 하는 거야..."),
        "playstyle": "📌 압박 점령형 — 사이드 운영으로 게임 흐름을 지배하는 스타일",
        "quote": "\"패배는 선택이다. 나는 선택하지 않겠다.\"",
    },
    "ENTP": {
        "champion": "야스오", "champ_id": "Yasuo",
        "title": "용서받지 못한 자", "icon": "🌪️",
        "roles": [("파이터","#e67e22"),("메이지","#3498db")],
        "lane": "📍 미드 / 바텀",
        "personality": (
            "다 풀리면 딜은 진짜 무시무시하지만 그 전까진 죽는 걸 즐기는 타입 🌀 "
            "'야스오 원트릭이에요' 하는 순간 팀원들 숨 막히는 거 알면서도 꺼내요. "
            "도전 자체를 게임으로 생각하고, 불리한 상황에서 오히려 집중력이 올라가요. "
            "이기면 천재, 지면 '팀이 안 따라와서'... 그래도 같이 하면 재밌어요 😏"
        ),
        "traits": ["창의적","도전적","임기응변","자신감","재치"],
        "best":  ("INTJ", "⚔️ 미친 플레이를 받쳐줄 전략가"),
        "worst": ("ISFJ", "😮‍💨 내 플레이 스타일을 이해해줘요..."),
        "playstyle": "📌 하이리스크 하이리턴형 — 아슬아슬한 한타가 진짜 재미",
        "quote": "\"바람은 용서하지 않는다.\"",
    },
    "INFJ": {
        "champion": "소라카", "champ_id": "Soraka",
        "title": "별의 아이", "icon": "⭐",
        "roles": [("서포터","#2ecc71"),("힐러","#f1c40f")],
        "lane": "📍 바텀 (서포터)",
        "personality": (
            "자기 HP 깎아서 팀원 살리고 정작 본인이 죽는 타입이에요 🌟 "
            "팀원의 체력창을 항상 주시하고, 위기가 오기 전에 이미 예측하고 있어요. "
            "사람들의 감정을 너무 깊이 느껴서 팀원이 져도 내가 더 미안해요. "
            "세상에서 가장 희귀하고 소중한 포지션입니다. (실제로 서포터 구인 어렵잖아요 😭)"
        ),
        "traits": ["공감력","헌신적","통찰","이타심","예지력"],
        "best":  ("ENFP", "✨ 무한 긍정 에너지가 나를 살려줘요"),
        "worst": ("ESTP", "💥 제발 들이받기 전에 한 번만 생각해요"),
        "playstyle": "📌 팀 뒷받침형 — 팀원을 살리는 것이 곧 캐리",
        "quote": "\"별빛은 어둠 속에서만 보인다.\"",
    },
    "INFP": {
        "champion": "룰루", "champ_id": "Lulu",
        "title": "요정의 마법사", "icon": "🧚",
        "roles": [("서포터","#2ecc71"),("요정","#EE99AC")],
        "lane": "📍 바텀 (서포터) / 미드",
        "personality": (
            "팀원을 다람쥐로 만들면서 '이게 최선이었어요'라고 하는 타입 🐿️ "
            "세상을 본인만의 독특한 시각으로 바라보고, "
            "뭔가 가치 있는 일을 하고 싶어서 서포터를 골랐어요. "
            "마음이 여려서 팀원이 화내면 살짝 상처받지만, "
            "머릿속에 이미 다음 판에서 이길 시나리오가 완성돼 있어요 📖"
        ),
        "traits": ["감수성","창의적","이상주의","진정성","공감왕"],
        "best":  ("ENFJ", "💞 내 진심을 알아주는 유일한 사람"),
        "worst": ("ESTJ", "📊 왜 모든 걸 수치로 따지는 거예요..."),
        "playstyle": "📌 유틸 마법형 — 독특한 CC기로 팀원을 보호하는 스타일",
        "quote": "\"상상력은 가장 강력한 마법이야.\"",
    },
    "ENFJ": {
        "champion": "레나타 글라스크", "champ_id": "Renata",
        "title": "바이렌트의 철의 손", "icon": "💼",
        "roles": [("서포터","#2ecc71"),("전략가","#8e44ad")],
        "lane": "📍 바텀 (서포터)",
        "personality": (
            "팀원 모두를 챙기면서 은근히 게임 판도를 본인이 쥐고 흔드는 타입 💛 "
            "'우리 다 같이 할 수 있어!' 라고 말하면서 사실 혼자 다 계획해놨어요. "
            "팀원의 성장을 진심으로 응원하고, "
            "게임에서 지더라도 '우리 다음 판엔 더 잘할 수 있어!'라고 말해요 (그리고 진심이에요) 🌟"
        ),
        "traits": ["따뜻함","리더십","공감력","영감 제공","소통 달인"],
        "best":  ("INFP", "💫 감수성의 시너지로 팀 분위기 최고"),
        "worst": ("ISTP", "🔧 공감 제로인 반응에 살짝 상처받아요"),
        "playstyle": "📌 팀 총괄형 — 한타 판도를 바꾸는 한 방의 마스터",
        "quote": "\"당신의 성공이 곧 나의 성공입니다.\"",
    },
    "ENFP": {
        "champion": "세라핀", "champ_id": "Seraphine",
        "title": "별빛 연주자", "icon": "🎵",
        "roles": [("서포터","#2ecc71"),("메이지","#3498db")],
        "lane": "📍 바텀 (서포터) / 미드",
        "personality": (
            "게임 시작 전 '같이 즐겁게 해요!!' 하고 게임 끝나도 '수고했어요 💕' 하는 타입 🎉 "
            "적팀한테도 칭찬하는 따뜻한 사람이고, "
            "열정이 넘쳐서 판마다 다른 챔피언 해보고 싶은 충동이 있어요. "
            "좀 산만해 보여도 결정적인 순간엔 팀을 살리는 한 방이 있어요!"
        ),
        "traits": ["열정적","사교적","낙천적","자유로움","상상력"],
        "best":  ("INTJ", "🌟 내 꿈에 전략을 더해줘요"),
        "worst": ("ISTJ", "📅 왜 그렇게 정해진 대로만 해요?"),
        "playstyle": "📌 무드메이커형 — 팀 전체를 살리는 광역 버프의 여왕",
        "quote": "\"음악은 세상을 하나로 연결해!\"",
    },
    "ISTJ": {
        "champion": "말파이트", "champ_id": "Malphite",
        "title": "암석의 파편", "icon": "🪨",
        "roles": [("탱커","#95a5a6"),("개시기","#e67e22")],
        "lane": "📍 탑",
        "personality": (
            "매 판 같은 빌드, 같은 룬, 같은 플레이... 그리고 항상 이기는 타입 ⏰ "
            "신뢰도가 엄청나고, 약속한 한타 개시는 100% 실행해요. "
            "'말파이트 궁 하나에 게임 끝낸다'라는 공식을 믿고, 믿게 만들어요. "
            "변수를 싫어하고 예측 가능한 플레이를 선호해요. 근데 그게 왜 이겨요... 👍"
        ),
        "traits": ["책임감","신뢰성","꼼꼼함","체계적","의리"],
        "best":  ("ESFP", "🎊 활발함이 나를 즐겁게 해줘요"),
        "worst": ("ENFP", "🎪 변수가 너무 많아서 머리 아파요"),
        "playstyle": "📌 한타 개시형 — 궁 하나로 게임 끝내는 믿음의 탱커",
        "quote": "\"나는 천천히, 그러나 반드시 부순다.\"",
    },
    "ISFJ": {
        "champion": "타릭", "champ_id": "Taric",
        "title": "별빛의 방패", "icon": "🛡️",
        "roles": [("서포터","#2ecc71"),("탱커","#95a5a6")],
        "lane": "📍 바텀 (서포터)",
        "personality": (
            "원딜이 무빙을 안 해도 내 몸으로 막아주는 타입 💙 "
            "배려가 몸에 배어 있고, 팀원이 위험하면 자동으로 달려가요. "
            "자기 표현은 서툴러도 행동으로 다 보여줘요. "
            "근데 가끔 참고 참다가 '아 진짜 왜 저기서 들어가요!!' 하는 거 다 이해해요 🫡"
        ),
        "traits": ["배려심","충성스러움","인내력","섬세함","따뜻함"],
        "best":  ("ESFP", "🌺 활기가 나를 살려줘요"),
        "worst": ("ENTP", "😤 왜 매번 어그로를 끌어요..."),
        "playstyle": "📌 수호자형 — 원딜을 목숨 걸고 지키는 철벽 서포터",
        "quote": "\"진정한 아름다움은 희생 속에 있다.\"",
    },
    "ESTJ": {
        "champion": "갱플랭크", "champ_id": "Gangplank",
        "title": "새벽빛 해적왕", "icon": "🏴‍☠️",
        "roles": [("파이터","#e67e22"),("전략가","#8e44ad")],
        "lane": "📍 탑",
        "personality": (
            "맵 전체에 barrel 깔아두고 엑셀처럼 관리하는 타입 📊 "
            "골드 효율, 쿨타임, 맵 컨트롤을 동시에 계산해요. "
            "체계가 없는 팀원을 보면 핑 열두 개 찍고 싶지만 참아요 (가끔은 못 참아요). "
            "후반으로 갈수록 강해지는 챔피언처럼, 계획대로 흘러가면 무적이에요 ⚓"
        ),
        "traits": ["조직력","공정함","결단력","실용적","추진력"],
        "best":  ("ISFP", "🎨 부드러운 균형이 나를 편하게 해줘요"),
        "worst": ("INFP", "🌈 현실을 좀 봐요, 이상만으론 이길 수 없어요"),
        "playstyle": "📌 파밍 운영형 — 후반 스케일로 게임을 압도하는 스타일",
        "quote": "\"바다의 법칙은 강자가 만든다.\"",
    },
    "ESFJ": {
        "champion": "나미", "champ_id": "Nami",
        "title": "조류의 지휘자", "icon": "🌊",
        "roles": [("서포터","#2ecc71"),("인챈터","#3498db")],
        "lane": "📍 바텀 (서포터)",
        "personality": (
            "챗에서 제일 먼저 '안녕하세요!' 치고 게임 내내 팀원 챙기는 타입 ☀️ "
            "원딜 체력 낮으면 본능적으로 힐이 나가고, 시야도 열심히 해줘요. "
            "팀원이 칭찬해주면 더 잘하고, "
            "욕 들으면 실력이 흔들리는 섬세한 마음의 소유자예요. "
            "진심으로 팀을 위하는 사람입니다 💙"
        ),
        "traits": ["사교적","따뜻함","배려심","현실적","조화 추구"],
        "best":  ("ISFJ", "🤝 서로를 완벽하게 이해하는 조합"),
        "worst": ("INTP", "🤔 논리로만 대화하면 조금 외로워요"),
        "playstyle": "📌 팀 케어형 — 버프와 힐로 원딜을 신으로 만드는 서포터",
        "quote": "\"파도는 함께 출렁일 때 가장 강하다.\"",
    },
    "ISTP": {
        "champion": "카이사", "champ_id": "Kaisa",
        "title": "공허의 딸", "icon": "🚀",
        "roles": [("원거리 딜러","#e74c3c"),("암살자","#9b59b6")],
        "lane": "📍 바텀 (원딜)",
        "personality": (
            "설명 없이 그냥 잘 함. 그게 다임. 🔧 "
            "화려한 플레이는 없지만 CS 하나도 안 놓치고 적 잡을 때 타이밍이 완벽해요. "
            "팀원이 '왜 거기 있었어요?'라고 물으면 '그냥요'라고 대답해요. "
            "감정 기복 없이 꾸준히, 적이 뭘 하든 내 할 것만 해요. 실력파입니다 💯"
        ),
        "traits": ["독립적","냉철함","실용적","집중력","문제해결"],
        "best":  ("ESTJ", "⚙️ 실행력이 합쳐지면 최강"),
        "worst": ("ENFJ", "💬 저 사실 대화 많이 안 해도 돼요"),
        "playstyle": "📌 솔로 사냥형 — 진입기로 낙오된 적을 혼자 처리하는 스타일",
        "quote": "\"공허가 나를 바꿨지만, 내 의지는 바꾸지 못했다.\"",
    },
    "ISFP": {
        "champion": "릴리아", "champ_id": "Lillia",
        "title": "주눅든 새싹", "icon": "🌸",
        "roles": [("정글러","#27ae60"),("메이지","#3498db")],
        "lane": "📍 정글",
        "personality": (
            "캠프에서 혼자 꽃을 키우다가 갑자기 나타나서 잠 재우는 타입 🌺 "
            "자기만의 템포가 있고, 강요받는 걸 정말 싫어해요. "
            "혼자 있는 시간(정글링)을 사랑하고, 팀원이 뭐라 해도 내 방식대로 해요. "
            "진짜 잘 풀리면 적팀 전체가 꿈나라 가는 거... 보고 싶지 않으세요? 🎨"
        ),
        "traits": ["감수성","자유로움","예술적","온화함","관찰력"],
        "best":  ("ESFJ", "🌻 따뜻하게 이끌어줘요"),
        "worst": ("ENTJ", "⚡ 제발 핑 그만 찍어요, 알아서 해요"),
        "playstyle": "📌 독자 운영형 — 내 템포로 정글 돌며 한 방에 게임 터뜨리기",
        "quote": "\"꽃은 서두르지 않아도 피어난다.\"",
    },
    "ESTP": {
        "champion": "바이", "champ_id": "Vi",
        "title": "필트오버의 집행자", "icon": "🥊",
        "roles": [("파이터","#e67e22"),("정글러","#27ae60")],
        "lane": "📍 정글 / 탑",
        "personality": (
            "생각보다 주먹이 먼저 나가는 타입이에요 💥 "
            "'일단 들어가고 생각은 나중에'가 인생 모토예요. "
            "순발력이 어마어마하고, 위기 상황에서 오히려 더 흥분해요. "
            "이기면 '내가 다 했어!', 지면 '한타만 잘 했으면 됐는데!' 어느 쪽이든 재미있는 사람 🎲"
        ),
        "traits": ["행동파","대담함","순발력","사교적","현실적"],
        "best":  ("ISFJ", "🏠 든든한 안전망이 되어줘요"),
        "worst": ("INFJ", "🌙 너무 깊게 생각하면 타이밍 놓쳐요"),
        "playstyle": "📌 돌격 개시형 — 먼저 들어가서 싸움 판 만들고 팀 따라오기",
        "quote": "\"말은 필요 없어. 주먹으로 보여주지.\"",
    },
    "ESFP": {
        "champion": "케이틀린", "champ_id": "Caitlyn",
        "title": "필트오버의 보안관", "icon": "🎯",
        "roles": [("원거리 딜러","#e74c3c"),("저격수","#7f8c8d")],
        "lane": "📍 바텀 (원딜)",
        "personality": (
            "어딜 가든 존재감이 폭발하는 타입이에요 ✨ "
            "울트 하나로 분위기를 장악하고, CS도 잘 먹고, 빠른 공격속도로 딜도 쏙쏙. "
            "게임 내내 채팅창에 '나이스!' '잘한다!'를 흘리고 다녀요. "
            "지는 게임도 '그래도 우리 열심히 했잖아요!'로 마무리하는 국민 원딜이에요 🎉"
        ),
        "traits": ["유쾌함","사교적","에너지","현재집중","솔직함"],
        "best":  ("ISTJ", "⚓ 믿음직한 탱커가 나를 지켜줄 때 최고"),
        "worst": ("INTJ", "🔮 진지한 분위기에서 나 좀 숨막혀요"),
        "playstyle": "📌 라인전 지배형 — 강력한 사거리와 함정으로 상대를 제압",
        "quote": "\"법은 내가 집행한다. 빠르고 정확하게.\"",
    },
}

MBTI_LIST = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP",
]

# ─── 헤더 ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-eyebrow">League of Legends × MBTI</div>
    <div class="hero-title">당신의 MBTI<br>챔피언을 찾아드립니다</div>
    <div class="hero-sub">16가지 유형, 16명의 챔피언 — 당신은 누구와 닮았을까요? 🎮</div>
</div>
<div class="gold-line"></div>
""", unsafe_allow_html=True)

# ─── 선택 UI ───────────────────────────────────────────────────────────────────
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    mbti = st.selectbox(
        "MBTI 유형 선택",
        options=[""] + MBTI_LIST,
        format_func=lambda x: "▼  내 MBTI를 선택하세요" if x == "" else x,
    )
    clicked = st.button("⚔️  나의 챔피언 소환하기")

# ─── 결과 ──────────────────────────────────────────────────────────────────────
if clicked:
    if not mbti:
        st.warning("⚠️ MBTI를 먼저 선택해주세요!")
    else:
        st.balloons()
        d = MBTI_DATA[mbti]
        cid = d["champ_id"]

        img_splash  = splash_url(cid, 0)
        img_icon    = icon_url(cid)
        champ_emoji = d["icon"]

        # ── 카드 상단: 스플래시 이미지 ──────────────────────────────────────
        st.markdown(f"""
        <div class="result-wrap">
            <div class="corner corner-tl"></div>
            <div class="corner corner-tr"></div>
            <div class="corner corner-bl"></div>
            <div class="corner corner-br"></div>

            <!-- 스플래시 아트 -->
            <div class="splash-wrap">
                <img class="splash-img" src="{img_splash}"
                     onerror="this.style.display='none';document.getElementById('fallback-{cid}').style.display='block';"
                     alt="{d['champion']} splash art">
                <div id="fallback-{cid}" style="display:none; width:100%; height:100%;
                     background:linear-gradient(135deg,#1a1208,#0a0a14);
                     align-items:center; justify-content:center;">
                    <span style="font-size:5rem;">{champ_emoji}</span>
                </div>
                <div class="splash-overlay"></div>
                <span class="splash-mbti-pill">{mbti}</span>
                <span class="splash-lane-pill">{d['lane']}</span>

                <!-- 챔피언 아이콘 (원형) -->
                <div class="champ-icon-wrap">
                    <img class="champ-icon-img" src="{img_icon}" alt="{d['champion']} icon"
                         onerror="this.style.display='none'">
                </div>
            </div>

            <!-- 챔피언 이름 & 칭호 -->
            <div class="card-body">
                <div class="champ-name">{d['champion']}</div>
                <div class="champ-title">{d['title']}</div>
        """, unsafe_allow_html=True)

        # 역할 뱃지
        badge_html = '<div style="text-align:center; margin-bottom:0.2rem;">'
        for label, color in d["roles"]:
            badge_html += (
                f'<span class="role-badge" '
                f'style="background:rgba(0,0,0,0.4); border-color:{color}55; color:{color};">'
                f'{label}</span>'
            )
        badge_html += "</div></div>"   # card-body 닫기
        st.markdown(badge_html, unsafe_allow_html=True)

        # ── 카드 하단: 텍스트 섹션 ───────────────────────────────────────────
        st.markdown('<div class="card-section">', unsafe_allow_html=True)
        st.markdown('<hr class="sep">', unsafe_allow_html=True)

        # 성격 분석
        st.markdown(f"""
            <div class="section-eyebrow">✦ 성격 분석</div>
            <div class="desc-body">{d['personality']}</div>
        """, unsafe_allow_html=True)

        # 핵심 특성
        chips = "".join(f'<span class="trait-chip">{t}</span>' for t in d["traits"])
        st.markdown(f"""
            <div class="section-eyebrow" style="margin-top:1.3rem;">✦ 핵심 특성</div>
            <div>{chips}</div>
        """, unsafe_allow_html=True)

        # 플레이 스타일
        st.markdown(f"""
            <div class="section-eyebrow" style="margin-top:1.3rem;">✦ 플레이 스타일</div>
            <div class="desc-body">{d['playstyle']}</div>
        """, unsafe_allow_html=True)

        st.markdown('<hr class="sep">', unsafe_allow_html=True)

        # 궁합
        best_mbti, best_desc   = d["best"]
        worst_mbti, worst_desc = d["worst"]
        st.markdown(f"""
            <div class="section-eyebrow">✦ 팀 궁합</div>
            <div class="compat-row" style="border-color:#2ecc71;">
                <span style="font-size:1.2rem;">💚</span>
                <div>
                    <strong style="color:#2ecc71;">최고 파트너</strong>
                    &nbsp;
                    <span style="background:rgba(46,204,113,0.15); color:#2ecc71;
                        padding:0.1rem 0.6rem; border-radius:5px; font-weight:700;
                        font-size:0.85rem;">{best_mbti}</span>
                    <br><span style="font-size:0.88rem;">{best_desc}</span>
                </div>
            </div>
            <div class="compat-row" style="border-color:#e74c3c;">
                <span style="font-size:1.2rem;">🔥</span>
                <div>
                    <strong style="color:#e74c3c;">주의 조합</strong>
                    &nbsp;
                    <span style="background:rgba(231,76,60,0.15); color:#e74c3c;
                        padding:0.1rem 0.6rem; border-radius:5px; font-weight:700;
                        font-size:0.85rem;">{worst_mbti}</span>
                    <br><span style="font-size:0.88rem;">{worst_desc}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<hr class="sep">', unsafe_allow_html=True)

        # 챔피언 명언
        st.markdown(f"""
            <div class="section-eyebrow">✦ {d['champion']}의 한마디</div>
            <div class="quote-block">{d['quote']}</div>
        </div>   <!-- card-section -->
        </div>   <!-- result-wrap -->
        """, unsafe_allow_html=True)

        # 안내
        st.markdown("""
        <div style="text-align:center; color:#7a8fa6; font-size:0.8rem; margin-top:1.2rem; margin-bottom:2rem;">
            다른 MBTI 유형도 확인해보세요 🔄 &nbsp;|&nbsp; All is fair in the Rift ⚔️
        </div>
        """, unsafe_allow_html=True)
