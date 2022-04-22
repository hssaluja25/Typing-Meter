from pprint import pprint as pp
import json
with open("user_history.txt","r") as f:
    content = f.read()
    user_history = json.loads(content)
    inv_map = {}
    for k, v in user_history.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    max_7 = list(inv_map.keys())
    max_7.sort(reverse=True)
    max7 = max_7[:7]
    
    
    count = 0
    max_7_mistyped_chars = []
    for times_mistyped in max_7:
        if (count<=6):
            if len(inv_map[times_mistyped])>1:
                for char in inv_map[times_mistyped]:
                    if (count<=6):
                        max_7_mistyped_chars.append(char)
                        count+= 1
            else:
                max_7_mistyped_chars.append(inv_map[times_mistyped][0])
                count+= 1
    win.addstr("\n Characters you need to practise on: ")
    win.addstr(str(max_7_mistyped_chars), self.Color.MAGENTA)

