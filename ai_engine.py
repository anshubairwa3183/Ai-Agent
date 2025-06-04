import requests
import yaml

def generate_plan(task_description):
    system_prompt = (
        "You are an AI assistant that generates a step-by-step plan for a user's task. "
        "Return only the steps and commands or code needed."
    )

    # Format Ollama-compatible prompt
    full_prompt = f"{system_prompt}\n\nUser Task: {task_description}"

    # Send request to local Ollama instance
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": full_prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        raise Exception(f"Ollama error: {response.status_code} - {response.text}")
