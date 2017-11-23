---
title: 'Hexo Post Image To Jekyll Post Image Converter'
date: 2017-11-23 22:24:00
tags:
categories:
  - Python
---

{% gist webgori/d74d9b438ae84015f54287638dec617f %}

글 안의 hexo 이미지 태그를 jekyll 이미지 태그로 변환시켜줌

사용법:
```
python HexoPostImageToJekyllPostImageConverter.py "hexo md file path" "jekyll image path"
python HexoPostImageToJekyllPostImageConverter.py "input.md" "/assets/"
```

결과:
```{% asset_img 20140816_093337-1024x576.jpg %} → ![](/assets/20140816_093337-1024x576.jpg)```