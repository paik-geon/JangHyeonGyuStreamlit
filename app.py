import streamlit as st

st.set_page_config(
    page_title="Mood "
)

st.title("너를 위로해줄게!!")
st.title('힘든 일 있으면 말해!!')
  
anxeity = st.checkbox("불안")
sorrow = st.checkbox("슬픔")
anger= st.checkbox("분노")



if anxeity == True and sorrow == True and anger == True:
    st.title("당신은 할 수 있어요! 힘내세요")

if anxeity == True and sorrow == True and anger == False:
    st.title("괜찮아요! 할 수 있어요!")

if anxeity == True and sorrow == False and anger == True:
    st.title("침착하세요 당신은 해낼 거에요")

if anxeity == False and sorrow == True and anger == True:
    st.title("당신의 슬픔의 원인을 찾아보세요 한결 나아질 거에요")

if anxeity == False and sorrow == False and anger == True:
    st.title("진정하세요 분명 당신의 잘못이 아닐 거에요")

if anxeity == False and sorrow == True and anger == False:
    st.title("당신에게 힘이 되는 사람이 나타날 거에요 그때까지 기다려요")

if anxeity == True and sorrow == False and anger == False:
    st.title("걱정마세요 다 잘될 거에요 한걸음 물러나서 생각해보세요")


if anxeity == False and sorrow == False and anger == False:
    st.title("당신은 정상 입니다 앞으로도 행복하길 바라요")

summit = st.button("Test start")

