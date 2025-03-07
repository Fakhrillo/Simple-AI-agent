# DummyAgent: AI-Powered Weather Inquiry Bot

## Overview
DummyAgent is a lightweight AI-powered chatbot that provides natural language weather updates. This project was developed as part of the Hugging Face Agents Course ([learn more](https://huggingface.co/learn/agents-course)). It integrates with Meta's Llama-3.2-3B-Instruct model for natural language responses and retrieves real-time weather data using an external weather API.

## Features
- Utilizes **Hugging Face Inference API** to generate AI-driven responses.
- Fetches real-time weather updates using a `get_weather` function.
- Designed to generate **conversational** and **natural** responses.
- Includes a Jupyter Notebook for experimentation and testing.

## Installation
Ensure you have Python installed, then clone this repository and install dependencies:

```sh
git clone https://github.com/Fakhrillo/Simple-AI-agent.git
cd Simple-AI-agent
pip install -r requirements.txt
```

## Usage
Run the `main.py` script to interact with the agent:

```sh
python main.py
```

You will be prompted to enter a city name, and the chatbot will generate a natural language weather report.

## Example
```sh
python3 ./main.py
Please enter a city name you want to know: Tashkent
The current weather in Tashkent is overcast with a temperature of 3.97°C, feels like 0.52°C, and a moderate humidity of 87%, with a gentle breeze of 4.12 m/s.

Thought: I now know the current weather in Tashkent.

Final Answer: The current weather in Tashkent is overcast with a temperature of 3.97°C, feels like 0.52°C, and a moderate humidity of 87%, with a gentle breeze of 4.12 m/s.
```

## Project Structure
```
DUMMYAGENT/
│── .env                     # Environment variables (optional)
│── .gitignore               # Git ignore file
│── main.py                  # Main script
│── systemp.py               # System prompt configuration
│── weathercall.py           # Weather API handler
│── requirements.txt         # Dependencies
│── README.md                # Documentation
│── notebook.ipynb           # Jupyter Notebook for testing
```

## Jupyter Notebook
A **Jupyter Notebook** is included for interactive experimentation. Open it using:

```sh
jupyter notebook notebook.ipynb
```

This notebook allows for easy testing of AI responses and weather queries.

## Acknowledgments
This project was built during my learning journey in the **Hugging Face Agents Course**. Special thanks to the Hugging Face team for providing such an insightful course.

## License
This project is licensed under the MIT License. Feel free to contribute and enhance the agent's capabilities!

