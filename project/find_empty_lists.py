from pathlib import Path
import re
text = Path('main.tex').read_text(encoding='utf-8')
# pattern to find begin{itemize} or begin{enumerate} and their corresponding end
pattern = re.compile(r'\\begin\{(itemize|enumerate)\}(.*?)\\end\{\1\}', re.S)
found = False
for m in pattern.finditer(text):
    env = m.group(1)
    body = m.group(2)
    if '\\item' not in body:
        found = True
        start = text.count('\n', 0, m.start()) + 1
        end = text.count('\n', 0, m.end()) + 1
        print(f'Empty {env} block lines {start}-{end}')
if not found:
    print('No empty itemize/enumerate blocks found')
