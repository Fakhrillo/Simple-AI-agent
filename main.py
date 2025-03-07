from huggingface_hub import InferenceClient
from systemp import SYSTEM_PROMPT
from weathercall import get_weather

client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")

## Simple way to use it
# output = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "What can you do"
#         },
#     ],
#     stream=False,
#     max_tokens=1024
# )

# print(output.choices[0].message.content)

prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{SYSTEM_PROMPT}
<|eot_id|><|start_header_id|>user<|end_header_id|>
What's the current weather in Paris? Provide the update in a **natural way**.

Here is the latest weather data:
{get_weather("Paris")}

Avoid structured formats like tables or bullet points. Instead, make it sound natural and short.

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

output = client.text_generation(
    prompt,
    max_new_tokens=200,
    stop=["Observation:"]
)

new_prompt=prompt+output

final_output = client.text_generation(
    new_prompt,
    max_new_tokens=1024,
)

print(final_output)