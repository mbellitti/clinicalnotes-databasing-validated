from pathlib import Path
from vllm import LLM, SamplingParams
from pathlib import Path
import prompt_templates
from nbse_report_schema_minimal import Report
from itertools import batched

prompt_template = prompt_templates.TABULAR_TEMPLATE_SCHEMA

txt_path = Path("data/NBSE_txt")
output_path = Path("results/tabular_extracted_flashinfer/")

# Initialize vLLM
model_name = "Qwen/Qwen3-32B" # this is the best at complying with schema
# model_name = "Qwen/Qwen3-14B"
# model_name = "Qwen/Qwen3-8B"
# model_name = "Qwen/Qwen3-4B"
# model_name = 'Qwen/Qwen3-30B-A3B-Instruct-2507' # models from this family fail on vllm 0.1.10 with some mysterious error
max_tokens = 32768
temperature = 0.7
top_p = 0.8
top_k = 20
max_model_len = 32768
cache_dir = "/projectnb/vkolagrp/bellitti/hf_cache"

llm = LLM(model=model_name, max_model_len=max_model_len, tensor_parallel_size=2)

sampling_params = SamplingParams(
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=top_p,
    top_k=top_k,
)

for batch in batched(txt_path.glob("*.txt"), 256):

    messages_list = []

    for txt_file in batch:

        report_text = txt_file.read_text(encoding="utf-8")

        prompt = prompt_template.format(
            schema=Report.model_json_schema(), report=report_text
        )

        messages = [{"role": "user", "content": prompt}]

        messages_list.append(messages)

    outputs = llm.chat(
        messages_list, sampling_params, chat_template_kwargs={"enable_thinking": False}
    )

    for txt_file, output in zip(batch, outputs):

        with open(output_path / (txt_file.stem + ".json"), "w") as outfile:
            outfile.write(output.outputs[0].text.strip())
