from app.voice.voice_assistant import VoiceAssistant

voice = VoiceAssistant()

question = voice.listen()

voice.speak(f"You said: {question}")