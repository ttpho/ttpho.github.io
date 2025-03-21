---
layout: post
title:  JSON to classes with Ollama
subtitle: Dart + Olama Server, convert JSON to classes 
cover-img: https://plus.unsplash.com/premium_photo-1661963874418-df1110ee39c1
tags: [ollama, dartJ]
---

### Overview

[DartJ](https://dartj.web.app/), a website I built, specializes in converting JSON into class models for Dart, Swift, and Kotlin. 
The fundamental mechanism behind this conversion is a depth-first tree traversal algorithm. 

Now, I'm presenting a novel approach that leverages Ollama to transform JSON into class/struct models for a specified programming language, with the generated code being outputted to a file

![Untitled Diagram drawio](https://github.com/user-attachments/assets/7f3a4c88-ff6f-40a9-87fd-13afaf92dd21)



### Demo



#### JSON input 

### Ollma Setup 

[Ollama Install & Pull model](https://github.com/ollama/ollama?tab=readme-ov-file#ollama)

```
% ollama ls
NAME                    ID              SIZE      MODIFIED          
qwen2.5-coder:latest    2b0496514337    4.7 GB    About an hour ago    
codellama:13b           9f438cb9cd58    7.4 GB    3 days ago           
codegemma:7b            0c96700aaada    5.0 GB    3 days ago           
```

### Class/Struct




