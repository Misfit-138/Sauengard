'''turns = 2
reward = 1000
total_reward = reward + (turns * 100)
print(total_reward)
'''

import msvcrt
print('Press s or n to continue:\n')
input_char = msvcrt.getch()
if input_char.upper() == 'S':
   print('YES')