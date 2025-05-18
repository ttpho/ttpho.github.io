---
layout: post
title: Auto commit with Ollama
subtitle: Automatically generate commit messages and automatically create a commit for each file
cover-img: https://images.unsplash.com/photo-1435224572021-b229e8e0760e
thumbnail-img: https://elixir-lang.org/images/logo/logo.png
tags: [ai, git]
---



### Overview 

Too lazy to write commit messages, let AI do it, but AI providers like OpenAI, Cursor AI, etc., are too expensive and have limited token input.

A Python script will read the git diff and use the Ollama model `gemma3:4b` to automatically generate commit messages and automatically create a commit for each file.

### Execute 

```
python3 auto_commit.py
```

### Github 

https://github.com/ttpho/git_diff_auto_commit

