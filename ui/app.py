import gradio as gr
import requests
def chat(message,history,provider,model):
    payload = {
        "question":message,
        "provider":provider,
        "model":model if model else None
    }
    try:
        response = requests.post(
             "http://127.0.0.1:8000/chatbot/chat",
             json = payload,
             timeout = 60
        )
        if response.status_code != 200:
            answer =  f"Lỗi{response.status_code}"
        else:
            answer =  response.json()["answer"]
    except Exception as e:
        print(f"Error: {str(e)}")
        answer =  f"Lỗi:{str(e)}"
    history.append({"role":"user","content":message})
    history.append({"role":"assistant","content":answer})
    return history,""
with gr.Blocks() as demo:
    provider_dropdown = gr.Dropdown(
        choices = ['Deepseek','Gemini'],
        value = "deepseek",
        label = "Provider"
    )
    model_dropdown = gr.Dropdown(
        choices = [
            "deepseek-chat",
            "deepseek-reasoner",
            "gemini-2.5-flash-lite",
            "gemini-2.5-flash"
        ],
        value = "deepseek-chat",
        label = "Model"
    )
    chatbot = gr.Chatbot(
       label = "Conversation",
       height = 400
    )
    textbox = gr.Textbox(
        placeholder = "Nhập tin nhắn ...",
        label = "Tin nhắn"
    )
    send_button = gr.Button("Gửi")
    send_button.click(
        fn = chat,
        inputs = [textbox,chatbot,provider_dropdown,model_dropdown],
        outputs = [chatbot,textbox]
    )
if __name__ == "__main__":
    demo.launch(share = True)
