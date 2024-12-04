import strings as strings
import app_controls as ac
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

system_message = [{
                "role": "system",
                "content": strings.behaviour},
            {
                "role": "assistant",
                "content": strings.greetings}]

def get_model_response(query, messages):
    messages = [{"role": m["role"], "content": m["content"]} for m in messages] + [
                {"role": "user", "content": query}]
    try:
        response = client.chat.completions.create(
            model=ac.chat_model,
            messages=messages,
            # temperature=ac.temperature,
            max_tokens=ac.gen_max_tokens,
            top_p=ac.top_p,
            frequency_penalty=ac.frequency_penalty,
            presence_penalty=ac.presence_penalty
        )
        resp_content = response.choices[0].message.content
        return resp_content
    except Exception as e:
        return f"An error occurred: {str(e)}"