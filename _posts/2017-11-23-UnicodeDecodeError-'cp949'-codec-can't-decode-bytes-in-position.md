---
title: "UnicodeDecodeError 'cp949' codec can't decode bytes in position"
date: 2017-11-23 21:48:00
tags:
categories:
  - Python
---

```
python test.py
Traceback (most recent call last):
  File "test.py", line 7, in <module>
    content = f.readlines()
UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 48: illegal multibyte sequence
```

open(file, 'w') → open(file, 'w', encoding='UTF8')