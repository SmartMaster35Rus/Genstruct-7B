from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer, TextStreamer

model_path = "solidrust/Genstruct-7B-AWQ"
system_message = "You are Genstruct, incarnated as a powerful AI."

# Загрузка модели
model = AutoAWQForCausalLM.from_quantized(model_path, fuse_layers=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

# Преобразование запроса в токены
prompt_template = """\
<im_start>system {system_message}<im_end> <im_start>user {prompt}<im_end> <im_start>assistant"""
prompt = "You're standing on the surface of the Earth. " \
         "You walk one mile south, one mile west and one mile north. " \
         "You end up exactly where you started. Where are you?"

tokens = tokenizer(prompt_template.format(system_message=system_message, prompt=prompt), return_tensors='pt').input_ids.cuda()

# Генерация вывода
generation_output = model.generate(tokens, streamer=streamer, max_new_tokens=512)
