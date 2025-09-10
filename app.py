from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envファイルからAPIキーを取得
import os
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini",   
    temperature=0.7,       
    openai_api_key=api_key
)

st.title("サンプルアプリ②: LLMでアドバイス")

st.write("##### 動作モード1: 食事のアドバイス")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでアドバイスを生成できます。")
st.write("##### 動作モード2: 仕事のアドバイス")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでアドバイスを生成できます。")

selected_item = st.radio(
    "アドバイスを選択してください。",
    ["食事のアドバイス", "仕事のアドバイス"]
)

st.divider()
input_message = st.text_area("相談内容を入力してください")

if selected_item == "食事のアドバイス":
    st.write("あなたの食事に関するアドバイスを提供します。")
    
elif selected_item == "仕事のアドバイス":
    st.write("あなたの仕事に関するアドバイスを提供します。")
    

if st.button("実行"):
    st.divider()

    if input_message.strip() == "":
        st.warning("相談内容を入力してください。")
    else:
        if selected_item == "食事のアドバイス":
            system_prompt = "あなたは食事に関するアドバイザーです。食事の質問以外の場合は分かりませんと回答してください。"
        else:
            system_prompt = "あなたは仕事やキャリア、職場での人間関係に関するアドバイザーです。仕事の質問以外の場合は分かりませんと回答してください。"

        with st.spinner("アドバイスを生成中..."):
            response = llm.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=input_message)
            ])

        # 結果を表示
        st.write("### アドバイス")
        st.write(response.content)