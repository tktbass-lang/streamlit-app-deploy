from dotenv import load_dotenv

load_dotenv()
import streamlit as st
from openai import OpenAI

# .envファイルからAPIキーを取得する場合
import os
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

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
        # プロンプトの組み立て
        if selected_item == "食事のアドバイス":
            system_prompt = "あなたは食事に関するアドバイザーです。食事の質問以外の場合は分かりませんと回答してください"
        else:
            system_prompt = "あなたは仕事やキャリア、職場での人間関係に関するアドバイザーです。仕事の質問以外の場合は分かりませんと回答してください"

        # LLM呼び出し（新API形式）
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # モデルは用途に応じて変更可
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_message}
            ],
            max_tokens=500
        )

        # 結果を表示
        st.write("### アドバイス")
        st.write(response.choices[0].message.content)