# SoulCare - a mental health support chatbot

This project is part of Intel Unnati 2024.

Welcome to SoulCare repository! This project utilizes a fine-tuned version of Google's Gemma 2B model, optimized for providing mental health support to patients.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Metrics](#metrics)
- [Web App](#web-app)
- [Demo](#demo)
- [License](#license)

## Overview

This project aims to deliver a reliable and efficient mental health support chatbot. The core components of the project include:

- Fine-tuning the Gemma 2B model with specialized data.
- Optimizing the model for efficient inference using OpenVINO.
- Serving the model locally using FastAPI.
- Providing a user-friendly interface through a Streamlit web app.

## Features

- **Fine-Tuned Model:** Customized for mental health support with data collected from various HuggingFace repositories.
- **Efficient Inference:** Utilizes OpenVINO for optimized performance on Intel CPUs.
- **Local LLM Server:** Built with FastAPI, running on `localhost` at port `8000`.
- **User-Friendly Interface:** Interactive web app created with Streamlit.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Jefi-Ryan/SoulCare-for-mental-health
    cd SoulCare-for-mental-health
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install OpenVINO:**
    Follow the instructions to install [OpenVINO](https://docs.openvino.ai/latest/openvino_docs_install_guides_installing_openvino.html).

4. **Download the fine-tuned model from HuggingFace:**
   - [Click here](https://huggingface.co/JefiRyan/gemma-2b-mental-health-4000-steps-openvino) to visit huggingface repository to download our openvino model.\ ![image](https://github.com/Jefi-Ryan/SoulCare-for-mental-health/assets/114754832/1a1d0efc-7f8d-4c97-a447-e0c881c9b9ed)
   - [Click here](https://huggingface.co/JefiRyan/gemma-2b-it-mental-health-4000-steps) to visit huggingface repository to download our finetuned gemma model. \ ![image](https://github.com/Jefi-Ryan/SoulCare-for-mental-health/assets/114754832/6a245ca1-9459-4775-abee-bc98cb76256a)



## Usage

### Starting the FastAPI Server

1. **Run the FastAPI server:**
    ```bash
    uvicorn llm_server:app --host 0.0.0.0 --port 8000
    ```

    The server will start at `http://localhost:8000`.

### Launching the Streamlit Web App

1. **Run the Streamlit app:**
    ```bash
    streamlit run streamlit_app.py
    ```

    The web app will be accessible at `http://localhost:8501`.

## Model Details

- **Base Model:** Google's Gemma 2B
- **Fine-Tuning:** Conducted with data from various HuggingFace repositories to cater specifically to mental health support scenarios.
- **Conversion to OpenVINO:** The fine-tuned model is converted to OpenVINO format for optimized inference on Intel CPUs.

## Metrics
<div style="display: flex; flex-direction: row; justify-content: space-around;">
  <div style="flex: 1; text-align: center;">
    <h4>Train/Loss</h4>
    <img src="https://github.com/Jefi-Ryan/SoulCare-for-mental-health/assets/114754832/e039f5a3-6d54-46d1-a686-e10750c1ed09" alt="Train/Loss" width="400"/>
  </div>
  <div style="flex: 1; text-align: center;">
    <h4>Train/Grad Norm</h4>
    <img src="https://github.com/Jefi-Ryan/SoulCare-for-mental-health/assets/114754832/ddfc33f2-be6d-4fe7-86fe-4456773dda67" alt="Train/Grad Norm" width="400"/>
  </div>
</div>


## Web App

The Streamlit web app provides an intuitive interface for users to interact with the chatbot. It is designed to be user-friendly and accessible.

## Demo

![demo (1)](https://github.com/Jefi-Ryan/SoulCare-for-mental-health/assets/114754832/ff7441aa-4288-4155-8aef-38414a884332)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

We hope you find this project useful!
