import torch
import soundfile as sf

import sounddevice as sd

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

text = "Hello world! This is Silero text to speech with playback."
audio = model.apply_tts(text=text, speaker='en_0', sample_rate=sample_rate)

# Play audio
sd.play(audio, sample_rate)
sd.wait()

# Also save it
sf.write('Silero_TTS_HelloWorld2.wav', audio, sample_rate)