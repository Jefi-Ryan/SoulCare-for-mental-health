# openvino-rag-server.py

import os
import time
from dotenv import load_dotenv

from fastapi import FastAPI

from transformers import AutoTokenizer, pipeline

from optimum.intel.openvino import OVModelForCausalLM


load_dotenv(verbose=True)

os.environ['CACHE_DIR'] = r"D:\huggingface_cache"
cache_dir         = os.environ['CACHE_DIR']
ov_config         = {"PERFORMANCE_HINT":"LATENCY", "NUM_STREAMS":"1", "CACHE_DIR":cache_dir}


path = r"D:\Downloads\gemma-2b-ft-openvino"
model_id = path
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
model = OVModelForCausalLM.from_pretrained(model_id=path, ov_config=ov_config, cache_dir=cache_dir)

# -------------------------

def run_generation(prompt):
    alpaca_prompt = """
        You are a therapist. Your goal is to provide mental health support and counseling to users. Ensure that your responses are empathetic, supportive, and non-judgmental. Prioritize the user’s well-being and safety at all times.
        Write a response that is appropriate for the input.

        ### Input:
        {}

        ### Response:
        {}"""

    inputs = tokenizer(
        [
            alpaca_prompt.format(
                prompt,  # input
                "",  # output - leave this blank for generation!
            )
        ], return_tensors="pt")

    outputs = model.generate(**inputs, max_new_tokens=128, use_cache=True)
    return tokenizer.batch_decode(outputs)


app = FastAPI()

@app.get('/chatbot/')
async def root(query:str=None):
    if query:
        ans = run_generation(query)
        return {'response':f'{ans}'}
    return {'response':''}


# API reference
# http://127.0.0.1:8000/docs

# How to run (You need to have uvicorn and streamlit -> pip install uvicorn streamlit)
# uvicorn openvino-rag-server:app