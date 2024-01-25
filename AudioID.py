import sounddevice as sd

# Displays information on all available audio devices
devices = sd.query_devices()
for i, device in enumerate(devices):
    print(f"Device {i} - Nom: {device['name']}, Channels: {device['max_input_channels']}, Samplerate: {device['default_samplerate']}")