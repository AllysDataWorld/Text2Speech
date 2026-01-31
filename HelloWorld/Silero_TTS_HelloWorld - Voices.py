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


text = "Hello world! This is Silero text to speech."
audio = model.apply_tts(text=text, speaker='en_0', sample_rate=48000)

# Play audio
sd.play(audio, 48000)
sd.wait()

# Also save it
sf.write('hello_world.wav', audio, 48000)