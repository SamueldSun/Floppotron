hertz = [0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         0,
         31,
         33,
         35,
         37,
         39,
         41,
         44,
         46,
         49,
         52,
         55,
         58,
         62,
         65,
         69,
         73,
         78,
         82,
         87,
         93,
         98,
         104,
         110,
         117,
         123,
         131,
         139,
         147,
         156,
         165,
         175,
         185,
         196,
         208,
         220,
         233,
         247,
         262,
         277,
         294,
         311,
         330,
         349,
         370,
         392,
         415,
         440,
         466,
         494,
         523,
         554,
         587,
         622,
         659,
         698,
         740,
         784,
         831,
         880,
         932,
         988,
         1047,
         1109,
         1175,
         1245,
         1319,
         1397,
         1480,
         1568,
         1661,
         1760,
         1865,
         1976,
         2093,
         2217,
         2349,
         2489]

from mido import MidiFile
import time

file = 'SuperSmashBrosUltimate.mid'

mid = MidiFile(file)
numNotes = 0
stops = 0
allocation = [0, 0, 0]

drive1 = False
drive2 = False
drive3 = False


for msg in MidiFile(file):
    time.sleep(msg.time)
    if not msg.is_meta:
        data = str(msg)

        print(data)

        numNotes += 1
print(stops)