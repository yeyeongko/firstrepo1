import streamlit as st

# MBTI 특성 정의
def get_mbti_description(mbti_type):
    descriptions = {
        'INTJ': "🔍 전략가, 독립적이며 창의적인 사고를 가진 INTJ님! 장기적 목표를 설정하고 이를 달성하기 위해 전략적으로 접근해요.",
        'ENTP': "💡 발명가, 창의적이고 분석적인 사고를 가진 ENTP님! 새로운 아이디어와 도전에 열정적이며 문제를 다양한 각도에서 바라봐요.",
        'ISFP': "🎨 예술가, 감성적이고 개방적인 성격을 가진 ISFP님! 순간을 즐기며 감각적이고 실용적인 아름다움을 추구해요.",
        'ESFJ': "🤝 친구, 사회적이고 협력적인 성격을 가진 ESFJ님! 사람들과의 관계를 소중히 여기며 배려가 깊고 적극적으로 돕는 타입이에요.",
        'INTP': "🧠 사색가, 논리적이고 분석적인 사고를 가진 INTP님! 복잡한 문제를 해결하고 독창적인 아이디어를 탐구하는 것을 즐겨요.",
        'ENTJ': "👔 지휘자, 지도력과 목표 지향적인 성격을 가진 ENTJ님! 효율적이고 체계적으로 일을 추진하며 큰 그림을 생각해요.",
        'ISFJ': "🛡️ 수호자, 세심하고 책임감 있는 성격을 가진 ISFJ님! 다른 사람을 도우며 전통과 안정성을 중시해요.",
        'ESFP': "🎉 연예인, 외향적이고 실용적인 성격을 가진 ESFP님! 순간을 즐기며 사람들과의 활동에서 에너지를 얻어요.",
        'INFJ': "🌟 조언자, 깊은 통찰력과 공감능력을 가진 INFJ님! 다른 사람의 잠재력을 발견하고 도와주며 이상적인 목표를 추구해요.",
        'ENFJ': "🌈 교사, 열정적이고 사교적인 성격을 가진 ENFJ님! 다른 사람들의 성장을 지원하며 공동체를 위해 헌신해요.",
        'INFP': "💭 중재자, 이상적이고 감성적인 성격을 가진 INFP님! 내면의 가치와 신념을 중요시하며 깊이 있는 관계를 맺어요.",
        'ENFP': "🔥 활동가, 열정적이고 창의적인 성격을 가진 ENFP님! 새로운 가능성을 추구하고 사람들과의 관계에서 활력을 얻어요.",
        'ISTJ': "📊 관리자, 신뢰성과 책임감 있는 성격을 가진 ISTJ님! 체계적이고 논리적인 접근으로 일을 처리하며 안정성을 중시해요.",
        'ESTJ': "📈 실행가, 실용적이고 조직적인 성격을 가진 ESTJ님! 목표를 설정하고 조직적으로 이를 달성하며 규칙을 중시해요.",
        'ISTP': "🔧 장인, 실용적이고 현실적인 성격을 가진 ISTP님! 문제를 직접 해결하며 독립적으로 작업하는 것을 선호해요.",
        'ESTP': "🚀 도전가, 활발하고 실용적인 성격을 가진 ESTP님! 즉각적인 결과를 중시하며 활동적이고 새로운 경험을 추구해요."
    }
    return descriptions.get(mbti_type, "알 수 없는 유형입니다. 다른 MBTI 유형을 입력해 주세요!")

# MBTI 호환성 분석
def get_compatibility(mbti_type):
    compatibility = {
        'INTJ': ('ENTP', 'ESFJ'),
        'ENTP': ('INTJ', 'ISFJ'),
        'ISFP': ('ESFJ', 'INTJ'),
        'ESFJ': ('ISFP', 'INTP'),
        'INTP': ('ENTJ', 'ESFP'),
        'ENTJ': ('INTP', 'ISFP'),
        'ISFJ': ('ESFJ', 'ENTP'),
        'ESFP': ('ENFP', 'INTP'),
        'INFJ': ('ENFJ', 'ESTP'),
        'ENFJ': ('INFJ', 'ISTJ'),
        'INFP': ('ENFP', 'ESTJ'),
        'ENFP': ('INFP', 'ISTJ'),
        'ISTJ': ('ESTJ', 'ENFP'),
        'ESTJ': ('ISTJ', 'INFP'),
        'ISTP': ('ESTP', 'ENFJ'),
        'ESTP': ('ISTP', 'INFJ')
    }
    return compatibility.get(mbti_type, ('없음', '없음'))

# 웹 앱 제목
st.title('MBTI 성격 유형 분석기 🌟')

# 사용자 입력
mbti = st.selectbox(
    '당신의 MBTI 유형을 선택하세요!',
    ['INTJ', 'ENTP', 'ISFP', 'ESFJ', 'INTP', 'ENTJ', 'ISFJ', 'ESFP',
     'INFJ', 'ENFJ', 'INFP', 'ENFP', 'ISTJ', 'ESTJ', 'ISTP', 'ESTP']
)

# MBTI 설명
description = get_mbti_description(mbti)
st.write(description)

# 호환성 추천
compatible, incompatible = get_compatibility(mbti)
st.write(f"🤝 가장 잘 맞는 유형: {compatible}")
st.write(f"🚫 가장 맞지 않는 유형: {incompatible}")

# 추가 기능으로 재미있는 퀴즈나 팁 등을 추가할 수 있습니다.

