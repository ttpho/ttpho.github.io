---
layout: post
title: Dart cheatsheet
subtitle:
cover-img: https://images.unsplash.com/photo-1488998427799-e3362cec87c3
thumbnail-img: https://dart.dev/assets/shared/dart/logo+text/horizontal/white-e71fb382ad5229792cc704b3ee7a88f8013e986d6e34f0956d89c453b454d0a5.svg
tags: [dart, flutter]
---

Elixir cheatsheet.

### A basic Dart program

#### Hello world

```dart
void main() {
  print('Hello world');
}
```

#### Types

```dart
String? name = "Dart";
  int? age = 11;
  final double pi = 3.14;
  final bool isActive = false;
  final List<String> list = ["🌾", "💐", "🌹"];
  final Set<String> halogens = {
    'fluorine',
    'chlorine',
    'bromine',
    'iodine',
    'astatine'
  };
  final Map<String, dynamic> gifts = {
    // Key:    Value
    'first': 'partridge',
    'second': 'turtledoves',
    'fifth': 'golden rings'
  };
```

#### Functions

```dart
int add(int a, int b) {
  return a + b;
}

// arrow syntax

int add(int a, int b) => a + b;

// omit the types
add(int a, int b) => a + b;
```

#### Conditional expressions

```dart
final bool isPublic = user?.isPublic ?? false;
final String visibility = isPublic ? 'public' : 'private';
```

#### Control flow

##### if and else

```dart
void doSomeThing() {
  // don't change: `isRaining() == true` -> `isRaining()`
  // because `isRaining()` can return 3 options: null, true or false
  if (isRaining() == true) {
    bringRainCoat();
  } else if (isSnowing()) {
    wearJacket();
  } else {
    nothing();
  }
}
// without else sate use `return`
void doSomeThingWithoutElse() {
  if (isRaining() == true) {
    bringRainCoat();
    return;
  }
  if (isSnowing()) {
    wearJacket();
    return;
  }

  nothing();
}

bool? isSnowing() => false;

bool isRaining() => true;

void bringRainCoat() => print("bring rain coat");
void wearJacket() => print("wear jacket");
void nothing() => print("nothing");

```

##### for loops

```dart
String toSnakeCase(final String text) {
  final List<String> list = [];
  for (var char in text.split('')) {
    final bool isUpperCase = char.toUpperCase() == char && char != "_";
    final bool isNotEmpty = list.isNotEmpty;
    final String charLowerCase = char.toLowerCase();
    final String item =
        (isUpperCase && isNotEmpty) ? "_$charLowerCase" : charLowerCase;
    list.add(item);
  }

  return list.join("");
}

String toCamelCase(final String text) {
  final List<String> list = [];
  for (var char in text.split('_')) {
    final bool isEmpty = list.isEmpty;
    final String lowerCase = char.toLowerCase();
    final String upperCaseFist = lowerCase.length > 1
        ? "${lowerCase[0].toUpperCase()}${lowerCase.substring(1)}"
        : char.toUpperCase();
    final String item = isEmpty ? char : upperCaseFist;
    list.add(item);
  }

  return list.join("");
}

String split(final String text, final String from, final String to) {
  final List<String> list = [];
  for (var char in text.split(from)) {
    final String item = char.trim();
    if (item.isNotEmpty) {
      list.add(item);
    }
  }

  return list.join(to);
}
```

##### while and do-while

```dart
  final List<String> list = ["🌾", "💐", "🌹"];
  while (list.isNotEmpty) {
    list.removeLast();
  }
```

```dart
  final List<String> list = ["🌾", "💐", "🌹"];
  do {
    list.removeLast();
  } while (list.isNotEmpty);
```

##### switch and case

```dart

void handleStatus(final String status) {
  switch (status) {
  case 'pending':
    sendEmailWarnig();
    break;
  case 'new':
    subtractStock();
    break;
  case 'picking':
     prepareShippingLabel();
    break;
  case 'packed':
    prepareReadToShip();
    break;
  case 'done':
    executeOpen();
    break;
  case 'cancel':
     restoreStock();
    break;
  default:
    nothing();
    break;
}

```

#### Exceptions

```dart
try {
  featDataFromServer();
} catch (e) {
  print('Error: $e');
} finally {
  close();
}

```

### Enum

```dart
//  Status.values.forEach((v) => print('value: $v, index: ${v.index}'));
enum Status {
   pending,
   new_,
   picking,
   packed,
   done,
   cancel
}
```

### Class

```dart
import 'dart:math';

const double xOrigin = 0;
const double yOrigin = 0;

class Point {
  double? x;
  double? y;

  Point(double? x, double? y) {
    // There's a better way to do this, stay tuned.
    this.x = x;
    this.y = y;
  }

  Point.origin()
      : x = xOrigin,
        y = yOrigin;

  Point.fromJson(Map<String, double> json)
      : x = json['x'] ?? xOrigin,
        y = json['y'] ?? yOrigin;

  Point.withAssert(this.x, this.y) : assert(x != null && x > 0);

  Point copyWith({double? x, double? y}) => Point(x ?? this.x, y ?? this.y);

  static double distanceBetween(final Point a, final Point b) {
    var dx = (a.x ?? xOrigin) - (b.x ?? xOrigin);
    var dy = (a.y ?? yOrigin) - (b.y ?? yOrigin);
    return sqrt(dx * dx + dy * dy);
  }
}
```

### Note

[Cover Photo](https://unsplash.com/photos/pUAM5hPaCRI)

[Thumbnail Photo](https://dart.dev/assets/shared/dart/logo+text/horizontal/white-e71fb382ad5229792cc704b3ee7a88f8013e986d6e34f0956d89c453b454d0a5.svg)
