---
layout: post
title: Elixir/Phoenix use Telegram bot
subtitle: Elixir/Phoenix Project use Telegram bot for log urgent message
cover-img: https://images.unsplash.com/photo-1566574196420-07c7622aff9e
thumbnail-img: https://elixir-lang.org/images/logo/logo.png
tags: [elixir, phoenix, telegram]
---

In some cases, I use Telegram, to print out urgent message, because it is free and I can share the urgent message for team.

### Setup Telegram Bot

You can setup step by step from [here](https://ttpho.github.io/2021-08-17-flutter-telegram/)

### Build Telegram Client

I use [Tesla](https://github.com/teamon/tesla) to build Telegram Client.

`telegram_client.ex`

```elixir
defmodule App.Log.Telegram do
  def send_message(message) do
    OpolloCore.Integrations.Telegram.send_message(
      limit_and_encode_message(message),
      %{
        chat_id: System.get_env("TELEGRAM_CHAT_ID"),
        bot_token: System.get_env("TELEGRAM_BOT_TOKEN")
      }
    )
  end

  # Text of the message to be sent, 1-4096 characters after entities parsing
  # https://core.telegram.org/bots/api#sendmessage
  defp limit_and_encode_message(message) do
    message |> String.slice(0, 4096) |> URI.encode()
  end

  defp send(message, %{chat_id: chat_id, bot_token: bot_token}) do
    url =
      "https://api.telegram.org/bot#{bot_token}/sendMessage?chat_id=@#{chat_id}&text=#{message}"

    Tesla.get(url)
  end
end

```

### Setup

Setup `.env` with:

- `TELEGRAM_BOT_TOKEN` is token from `Step 1`
- `TELEGRAM_CHAT_ID` is channel Id from `Step 2`

```
export TELEGRAM_BOT_TOKEN=xxxxx
export TELEGRAM_CHAT_ID=yyyyyy
```

### Log message

```elixir
App.Log.Telegram.send_message("Hello")
```

### Note

[Cover Photo](https://unsplash.com/photos/pyup6OiFDRM)

[Thumbnail Photo](https://elixir-lang.org/images/logo/logo.png)
