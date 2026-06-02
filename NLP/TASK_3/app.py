# ============================================
# AI CHATBOT USING HUGGING FACE + GRADIO
# ============================================

# Import required libraries
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

# Fix padding token issue
tokenizer.pad_token = tokenizer.eos_token

# Load pretrained model
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/DialoGPT-medium"
)

# Store conversation history
chat_history_ids = None


# Chatbot function
def chatbot_response(message, history):

    global chat_history_ids

    # Encode user input
    new_input_ids = tokenizer.encode(
        message + tokenizer.eos_token,
        return_tensors='pt'
    )

    # Append conversation history
    bot_input_ids = (
        torch.cat([chat_history_ids, new_input_ids], dim=-1)
        if chat_history_ids is not None
        else new_input_ids
    )

    # Create attention mask
    attention_mask = torch.ones(
        bot_input_ids.shape,
        dtype=torch.long
    )

    # Generate response
    chat_history_ids = model.generate(
        bot_input_ids,
        attention_mask=attention_mask,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9,
        repetition_penalty=1.2
    )

    # Decode chatbot response
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    return response


# Create Gradio Chat Interface
demo = gr.ChatInterface(
    fn=chatbot_response,
    title="AI Chatbot using Transformers",
    description="Conversational AI chatbot using Hugging Face DialoGPT"
)

# Launch application
demo.launch(share=True)