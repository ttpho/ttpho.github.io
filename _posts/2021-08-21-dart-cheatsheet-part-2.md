---
layout: post
title: Dart cheatsheet - Part 2
subtitle: Dart cheatsheet - [String, List, Map]
cover-img: https://images.unsplash.com/photo-1607098263217-0f031bbced19
thumbnail-img: https://dart.dev/assets/shared/dart/logo+text/horizontal/white-e71fb382ad5229792cc704b3ee7a88f8013e986d6e34f0956d89c453b454d0a5.svg
tags: [dart, flutter]
---

Dart cheatsheet - Part 2 - [String, List, Map]

# String

##### Format

```dart
  final String name = "Po";
  final int age = 18;
  print("I am $name, $age years old");
  // I am Po, 18 years old
```

##### Turn a string into a number

```dart
  int.parse("1") // 1
  double.parse('1.1') // 1.1
  try {
    int.parse("1xx");
  } catch (e) {
     print(e.toString());
     // FormatException: 1xx
  }
```

##### Split

```dart
  final String text = "123213,321321";
  text.split(',') // [123213, 321321]
```

# List

##### Join

```dart
  final List<String> list = ["123213", "321321"];
  list.join(',') // "123213,321321"
```

##### Convert List to Map

```dart
  final List<Point> list = [Point(3, 4), Point(1, 2)];
  Map.fromIterable(list, key: (e) => e.x, value: (e) => e.y); // {3: 4, 1: 2}
```

##### List with index

```dart
  final List<Point> list = [Point(3, 4), Point(1, 2)];
  final List<String> listWithIndex = list.asMap().entries.map((entry) {
    final int index = entry.key;
    final Point value = entry.value;
    return "${index}:{${value.x},${value.y}}";
  }).toList(growable: false);
  // ["0:{3,4}", "1:{1,2}"]
```

##### Fold

```dart
  // compute the sum of all length
  final List<String> list = ['a', 'bb', 'ccc'];
  final int result = list.fold(
      0,
      (final int previousValue, final String element) => previousValue + element.length);
  print(result); // 6
```

# Map

##### New map from the provided iterables

```dart
  final List<String> keys = ['x', 'y', 'z'];
  final List<int> values = [1, 2, 3];

  Map<String, int>.fromIterables(keys, values);  // {x: 1, y: 2, z: 3}

```

##### Convert Map to List

```dart
  final Map<String, int> map = {"x": 3, "y": 4};
  final List<int> list = [];
  map.forEach((k, v) => list.add(v));
  print(list); // [3, 4]
```

### Note

[Cover Photo](https://unsplash.com/photos/n889iwhdiKg)

[Thumbnail Photo](https://dart.dev/assets/shared/dart/logo+text/horizontal/white-e71fb382ad5229792cc704b3ee7a88f8013e986d6e34f0956d89c453b454d0a5.svg)
