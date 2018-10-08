from pydub import AudioSegment
sound = AudioSegment.from_mp3("/home/evolyuta/PycharmProjects/Coursework/Music/Slipknot - Dead Memories.mp3")
sound.export("/home/evolyuta/PycharmProjects/Coursework/Music/Slipknot - Dead Memories.wav", format="wav")