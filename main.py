from pathlib import Path
JOKE = 'AI coding agents are amazing pair programmers: they turn “I’ll just fix one bug” into a pull request, a new framework, and a heartfelt apology to production. Version 2.'
Path('/output/entry.txt').write_text(JOKE, encoding='utf-8')
