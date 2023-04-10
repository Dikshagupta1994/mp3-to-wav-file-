import pydub
from pydub import AudioSegment
input_file='sample-3s.mp3'
output_file='result.wav'


sound=AudioSegment.from_mp3(input_file)
sound.export(output_file,format='wav')







