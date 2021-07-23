---
layout: post
title: Auto commit & push source code dynamic by Elixir
subtitle: Execute a command to commit and push the source code to GitHub in the Elixir/Phoenix project
cover-img: https://images.unsplash.com/photo-1435224572021-b229e8e0760e
thumbnail-img: https://elixir-lang.org/images/logo/logo.png
share-img: /assets/img/path.jpg
tags: [elixir, git]
---

Execute a command to commit and push the source code to GitHub in the Elixir/Phoenix project

### Setup

```
git config --global alias.add-commit '!git add -A && git commit'
```

### Module

```elixir
defmodule SourceCodeJob do
  def commit_all(message) do
    System.cmd("git", ["add-commit", "-m", message], into: IO.stream(:stdio, :line))
    System.cmd("git", ["push"], into: IO.stream(:stdio, :line))
  end
end
```

### Execute

```elixir
SourceCodeJob.commit_all("My commit message")
```
