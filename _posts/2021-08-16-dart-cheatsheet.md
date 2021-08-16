---
layout: post
title: Dart cheatsheet
subtitle:
cover-img: https://images.unsplash.com/photo-1488998427799-e3362cec87c3
thumbnail-img: https://dart.dev/assets/shared/dart/logo+text/horizontal/white-e71fb382ad5229792cc704b3ee7a88f8013e986d6e34f0956d89c453b454d0a5.svg
tags: [dart, flutter]
---

Elixir cheatsheet - basic Dart program

### Hello world

```dart
void main() {
  print('Hello world');
}
```

### Types

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

### Functions

```dart
int add(int a, int b) {
  return a + b;
}

// arrow syntax

int add(int a, int b) => a + b;

// omit the types
add(int a, int b) => a + b;
```

### Conditional expressions

```dart
final bool isPublic = user?.isPublic ?? false;
final String visibility = isPublic ? 'public' : 'private';
```

### If and else

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
bool? isSnowing() => false;
bool isRaining() => true;
void bringRainCoat() => print("bring rain coat");
void wearJacket() => print("wear jacket");
void nothing() => print("nothing");

```

### For loops

```dart
String toSnakeCase(final String text) {
  final List<String> list = [];
  for (var char in text.split('')) {
    final String charLowerCase = char.toLowerCase();
    final String item =
        (char.toUpperCase() == char && char != "_" && list.isNotEmpty) ? "_$charLowerCase" : charLowerCase;
    list.add(item);
  }

  return list.join("");
}
```

### While and do-while

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

### Switch and case

```dart

void handleStatus(final String status) {
  switch (status) {
    case 'new':
      subtractStock();
      break;
    case 'picking':
      prepareShippingLabel();
      break;
    case 'packed':
      prepareReadToShip();
      break;
    default:
      nothing();
      break;
}

```

### Exceptions

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

### Extension methods

```dart
//  "14".parseInt();
//  "14X".parseInt(defaultValue: -1);
extension NumberParsing on String {
  int parseInt({int defaultValue = 0}) {
    try {
      return int.parse(this);
    } catch (e) {
      return defaultValue;
    }
  }
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

  double distanceTo(final Point other) {
    var dx = (x ?? xOrigin) - (other.x ?? xOrigin);
    var dy = (y ?? yOrigin) - (other.y ?? yOrigin);
    return sqrt(dx * dx + dy * dy);
  }

  static double distanceBetween(final Point a, final Point b) {
    return a.distanceTo(b);
  }
}
```

### Note

[Cover Photo](https://unsplash.com/photos/pUAM5hPaCRI)

[Thumbnail Photo](https://dart.dev/assets/shared/dart/logo+text/horizontal/white-e71fb382ad5229792cc704b3ee7a88f8013e986d6e34f0956d89c453b454d0a5.svg)
