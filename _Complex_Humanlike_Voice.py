import time
import torch
import soundfile as sf
import sounddevice as sd

now = time.time()

# Download and load the model
device = torch.device('cpu')  # or 'cuda' if you have GPU
model, example_text = torch.hub.load(
    repo_or_dir='snakers4/silero-models',
    model='silero_tts',
    language='en',
    speaker='v3_en'  
)

model.to(device)

sample_rate = 48000 #`sample_rate` should be in [8000, 24000, 48000], current value is 48400
max_len = 1000 #Text string can not be longer than 1000 symbols
f = open("readme.txt") #if there are any quotations in the text it will fail
text_list = f.readlines()
this_text = "".join(txt.replace("\n", " ") for txt in text_list)
chunked_text = []
qa = []

def get_next_chunk(text):
    txt_len = len(text)
    start = 0
    while start < txt_len:
        stop = min(start + max_len, txt_len)
        chunk = text[start:stop]
        period_pos = chunk.rfind('.') #stop at the end of the last word in chunk
        if period_pos != -1 and stop <= txt_len:
            stop = start + period_pos + 1
            chunk = text[start:stop]
        chunked_text.append(chunk)
        qa.append(len(chunk))
        start = stop
        #print(f"appended chunk:{len(chunk)}")
    if sum(qa)==len(text):
        #print(f"PASSED: QA:{sum(qa)} and TEXT:{len(text)} are the same")
        pass
    else:
        print(f"FAIL: QA:{sum(qa)} and TEXT:{len(text)} are NOT the same")
    return qa, chunked_text
    
chunk = get_next_chunk(this_text)
print("Seconds: ",now - time.time())
now = time.time()

#Seconds:  -1.7168247699737549 
#cuda - AssertionError: Torch not compiled with CUDA enabled
#Speaker = AssertionError: Speaker not in the supported list ['v5_cis_base', 'v5_cis_base_nostress_jit', 'v5_cis_base_nostress', 'v5_cis_ext', 'v5_1_ru', 'v5_ru', 'v4_ru', 'v3_1_ru', 'ru_v3', 'aidar_v2', 'aidar_8khz', 'aidar_16khz', 'baya_v2', 'baya_8khz', 'baya_16khz', 'irina_v2', 'irina_8khz', 'irina_16khz', 'kseniya_v2', 'kseniya_8khz', 'kseniya_16khz', 'natasha_v2', 'natasha_8khz', 'natasha_16khz', 'ruslan_v2', 'ruslan_8khz', 'ruslan_16khz', 'v3_en', 'v3_en_indic', 'lj_v2', 'lj_8khz', 'lj_16khz', 'v3_de', 'thorsten_v2', 'thorsten_8khz', 'thorsten_16khz', 'v3_es', 'tux_v2', 'tux_8khz', 'tux_16khz', 'v3_fr', 'gilles_v2', 'gilles_8khz', 'gilles_16khz', 'aigul_v2', 'v3_xal', 'erdni_v2', 'v3_tt', 'dilyara_v2', 'v4_uz', 'v3_uz', 'dilnavoz_v2', 'v4_ua', 'v3_ua', 'mykyta_v2', 'v4_indic', 'v3_indic', 'v4_cyrillic', 'multi_v2']


for i in range (len(chunked_text)):
    audio = model.apply_tts(
        text=chunked_text[i], 
        speaker='en_0', 
        sample_rate=sample_rate
        )
    print("Seconds: ", now - time.time()) #6sec, 33sec
    sd.play(audio, sample_rate)
    sd.wait()
