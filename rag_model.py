from ctransformers import AutoModelForCausalLM

MODEL_PATH = "C:/Users/Toto/OneDrive/Desktop/3rd/T2/AIE322/stardew_chatbot/mistral_model/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH, 
    model_type="mistral",
    gpu_layers=50  # ใช้ GPU ช่วยประมวลผล (ปรับตามสเปค)
)

def get_answer(question):
    return model(question)
