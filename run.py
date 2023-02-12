from transformers import T5Tokenizer, T5ForConditionalGeneration, AutoTokenizer, AutoModel, BertTokenizer
import pywebio
import torch
#tokenizer = T5Tokenizer.from_pretrained("ChatYuan-large-v1")
#model = T5ForConditionalGeneration.from_pretrained("ChatYuan-large-v1")

# 加载模型
#save_directory = 'C:/Users/Administrator/Documents/ClueAI/ChatYuan-large-v1/'
tokenizer = T5Tokenizer.from_pretrained("./ChatYuan-large-v1/")
model = T5ForConditionalGeneration.from_pretrained("./ChatYuan-large-v1/")


# 修改运行设备为gpu，推理更快。
device = torch.device('cuda')
model.to(device)






def preprocess(text):
  text = text.replace("\n", "\\n").replace("\t", "\\t")
  return text

def postprocess(text):
  return text.replace("\\n", "\n").replace("\\t", "\t")

def answer(text, sample=True, top_p=1, temperature=0.7):
  '''sample：是否抽样。生成任务，可以设置为True;
  top_p：0-1之间，生成的内容越多样'''
  text = preprocess(text)
  encoding = tokenizer(text=[text], truncation=True, padding=True, max_length=768, return_tensors="pt").to(device)
  if not sample:
    out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_new_tokens=512, num_beams=1, length_penalty=0.6)
  else:
    out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_new_tokens=512, do_sample=True, top_p=top_p, temperature=temperature, no_repeat_ngram_size=3)
  out_text = tokenizer.batch_decode(out["sequences"], skip_special_tokens=True)
  return postprocess(out_text[0])





def main():
  pywebio.output.put_markdown('# 中文AI对话')
  pywebio.output.put_markdown("_基于元语智能模型：https://huggingface.co/ClueAI/ChatYuan-large-v1_")
  #pywebio.output.put_markdown("**等待模型加载...**")
  print("模型加载完成。")
  pywebio.output.put_markdown("**模型加载完成**")
  pywebio.output.put_markdown("***")

  #for i, input_text in enumerate(input_list):
  i=1
  output_text=""
  #假定一开始的输出是空。
  while i>=1:
    #input_text = input("用户：")
    input_text = pywebio.input.input("您：")
    input_text = "用户：" + input_text + "\n\nChatYuan："
    print(f"问答{i}".center(50, "="))
    all_input = input_text + output_text+"\n\n"
    #总输入=用户本次输入+上一次的机器人输出
    #output_text = answer(input_text)
    output_text = answer(all_input)
    #next_input="用户：" + input_text + "\n\nChatYuan："+ output_text
    print(f"{input_text}{output_text}"+"\n\n")
    pywebio.output.put_text(f"{input_text}{output_text}"+"\n\n")
    i=i+1

pywebio.platform.tornado_http.start_server(main,port=7132,remote_access=True,auto_open_webbrowser=True,allowed_origins="https://chat.eekda.cn")