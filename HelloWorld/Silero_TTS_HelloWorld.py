import torch
import soundfile as sf

# Download and load the model
device = torch.device('cpu')  # or 'cuda' if you have GPU

this_sample_rate = 48000 # `sample_rate` should be in [8000, 24000, 48000]

model, example_text = torch.hub.load(
    repo_or_dir='snakers4/silero-models',
    model='silero_tts',
    language='en',
    speaker='v3_en'
)

model.to(device)

# Generate speech
text = "Hello world! This is Silero text to speech."
audio = model.apply_tts(
    text=text,
    speaker='en_0',  # English speaker
    sample_rate=this_sample_rate
)

# Save to file
sf.write('Silero_TTS_HelloWorld.wav', audio, this_sample_rate)
print("Silero_TTS Audio file is saved to Silero_TTS_HelloWorld.wav")