
state = {'chaos':2, 'sad':4, 'happy':3, 'angry':0, 'mad':0, 'good':0}

max_key = max(state, key=state.get)
print(max_key)