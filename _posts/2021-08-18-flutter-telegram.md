---
layout: post
title: Flutter App use Telegram bot
subtitle: Flutter App use Telegram bot for log urgent message
cover-img: https://images.unsplash.com/photo-1516434464077-12b1b87bb716
thumbnail-img: https://pub.dev/static/img/flutter-logo-32x32.png
tags: [dart, flutter, telegram]
---

In some cases, I want to print out urgent message that need to be checked immediately.
You can you `Firebase Crashlytics ` or `Sentry`, but I use Telegram, because it is free and I can share the urgent message for team.

### Setup Telegram Bot

- Step 1:

  Gen token, keep token
  Just talk to [BotFather](https://t.me/botfather) and follow a few simple steps.
  Once you've created a bot and received your authorization token, head down to the Bot API manual to see what you can teach your bot to do.

  ![BotFather](/assets/img/flutter_telegram/step1.png)

- Step 2:

  Create channel, public channel and keep chanel name
  ![Channel](/assets/img/flutter_telegram/step2.png)

- Step 3:

  add chat bot into Channel

  ![Add Chat Bot](/assets/img/flutter_telegram/step3.png)

### Build Telegram Client

`telegram_client.dart`

```dart
import 'dart:math';

import 'package:http/http.dart' as http;

class TelegramClient {
  final String chatId;
  final String botToken;
  TelegramClient({
    required this.chatId,
    required this.botToken,
  });

  // Text of the message to be sent, 1-4096 characters after entities parsing
  // https://core.telegram.org/bots/api#sendmessage
  String _limitMessage(final String message) =>
      message.substring(0, min(4096, message.length));

  Future<http.Response> sendMessage(final String message) {
    final Uri uri = Uri.https(
      "api.telegram.org",
      "/bot${this.botToken}/sendMessage",
      {
        "chat_id": this.chatId,
        "text": _limitMessage(message),
        "parse_mode": "html",
      },
    );
    return http.get(uri);
  }
}

```

### Flutter App log urgent message

Create `telegramClient` with:

- `botToken` is token from `Step 1`
- `chatId` is channel Id from `Step 2`

```dart
final TelegramClient telegramClient = new TelegramClient(
    chatId: "@flutter_logger",
    botToken: "XXXXXXXXX",
  );
```

Log urgent message

```dart
final String message = "Hello";
final response = await telegramClient.sendMessage(message);
print(response.statusCode);
```

Demo

![Demo](/assets/img/flutter_telegram/demo_result.png)

[Source code](https://github.com/ttpho/app_notification_flutter)

### Note

[Cover Photo](https://unsplash.com/photos/GGewLGcQD-I)

[Thumbnail Photo](https://pub.dev/static/img/flutter-logo-32x32.png)
