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


[![Watch the video](https://img.youtube.com/vi/I4fn677eO8w/maxresdefault.jpg)](https://youtu.be/I4fn677eO8w)




### Ollma Setup 

[Ollama Install & Pull model](https://github.com/ollama/ollama?tab=readme-ov-file#ollama)

```
% ollama ls
NAME                    ID              SIZE      MODIFIED          
qwen2.5-coder:latest    2b0496514337    4.7 GB    About an hour ago    
codellama:13b           9f438cb9cd58    7.4 GB    3 days ago           
codegemma:7b            0c96700aaada    5.0 GB    3 days ago           
```
### Build System prompt 

```dart
"""
I am a $lang developer.
I give you a JSON string, convert it to $lang classess. 
I want you to only reply the correction, do not write explanations.

For example, my JSON string

```json
${jsonAndClass.$1}
```

You will convert it to $lang classes 

${jsonAndClass.$2}

"""
```


### Excute Ollma

- LLM model: $model
- System promt: $sytemPrompt
- Json resource: $json

```curl

curl http://localhost:11434/api/chat -d '{
  "model": $model,
  "messages": [
    {
      "role": "assistant",
      "content": $sytemPrompt
    },
    {
      "role": "user",
      "content": $json
    }
  ]
}'

```

### Parser result 

```dart

  String llmToCode(String language, String codeContent) {
    final prefix = '```$language';
    final start = codeContent.indexOf(prefix);
    final end = codeContent.lastIndexOf('```');

    if (start == -1 || end == -1) {
      return codeContent;
    }
    return codeContent.substring(start + prefix.length, end).trim();
  }

```





