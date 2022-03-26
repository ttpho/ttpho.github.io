---
layout: post
title: Flutter Basic - To make space to have a specific width and/or height, what is the difference between Container and SizedBox
cover-img: https://images.unsplash.com/photo-1494961104209-3c223057bd26
thumbnail-img: https://pub.dev/static/img/flutter-logo-32x32.png
tags: [dart, flutter]
---

Compare Container and SizedBox with Size

### Overview

- [Container](https://api.flutter.dev/flutter/widgets/Container-class.html): A convenience widget that combines common painting, positioning, and sizing widgets.

- [SizedBox](https://api.flutter.dev/flutter/widgets/SizedBox-class.html): A box with a specified size.


To make space to have a specific width and/or height, what is the difference between
`Container( height: 200, width: 100, )` and `SizedBox( height: 200, width: 100, )`.

### Container class

#### Container define

Container -> StatelessWidget -> Widget

#### Container build widget with Size

When `height` or  `width` is not null, the `Container` created  `constraints` (BoxConstraints)

```dart
constraints =
        (width != null || height != null)
          ? constraints?.tighten(width: width, height: height)
            ?? BoxConstraints.tightFor(width: width, height: height)
          : constraints,
```

when `constraints` is not null, the `Container` build the `Widget` with parent is `ConstrainedBox`

```dart
 if (constraints != null)
      current = ConstrainedBox(constraints: constraints!, child: current);
```
`ConstrainedBox` and  `SizedBox` is `extends` from `SingleChildRenderObjectWidget`.

Widget tree 
```dart
Container
  ConstrainedBox
```

### SizedBox class 


#### SizedBox define

SizedBox -> SingleChildRenderObjectWidget -> RenderObjectWidget -> Widget

#### SizedBox build widget with Size

SizedBox don't build the `Widget` by method `Widget build(BuildContext context)`  as `Container`,
because it is not extend from `StatelessWidget`, 
SizedBox make Widget by method `RenderConstrainedBox createRenderObject(BuildContext context)` 

```dart
@override
  RenderConstrainedBox createRenderObject(BuildContext context)
    return RenderConstrainedBox(
      additionalConstraints: _additionalConstraints,
    );
  }

  BoxConstraints get _additionalConstraints {
    return BoxConstraints.tightFor(width: width, height: height);
  }
```

Widget tree 
```dart
SizedBox
```


### Put Together
- To make space to have a specific width and/or height,the `SizedBox` is better.
- Read Flutter/Dart - Open Source to understand source code.

### Note

`->` is `extends`

[Cover Photo](https://unsplash.com/photos/uBe2mknURG4)

[Thumbnail Photo](https://pub.dev/static/img/flutter-logo-32x32.png)
