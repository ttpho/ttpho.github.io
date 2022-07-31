---
layout: post
title: Dart `toMap` dynamic method 
subtitle: gen method `toMap` for `Object` class 
cover-img: assets/img/2022-07-31/map.png
thumbnail-img: https://pub.dev/static/img/flutter-logo-32x32.png
tags: [dart, flutter]
---

Based on my experience, Dart does not provide convert an `Object` type to a `Map`. So, I try  create function like `toMap()` that manually convert the object to a key-value pair of map. In this post, I try create it dynamic


### Overview

For example:

```dart 
class Icon {
  final String name;
  final int color;

  Icon({required this.name, required this.color});

  Map<String, dynamic> toMap() => {
        'name': name,
        'color': color,
      };
}

```
So, later when you have a `Icon` object, you just can call `icon.toMap()`.

I do this in most of my entity classes.

In this post, I try create method `toMap()` dynamic and so I will reuse method `toMap()` for in most of my entity classes.


### Gen method `toMap` for `Object` class 

The approach that I use is post is using `dart:mirrors` library.

Basic reflection in Dart, with support for introspection and dynamic invocation.

Introspection is that subset of reflection by which a running program can examine its own structure. For example, a function that prints out the names of all the members of an arbitrary object.

Dynamic invocation refers the ability to evaluate code that has not been literally specified at compile time, such as calling a method whose name is provided as an argument (because it is looked up in a database, or provided interactively by the user).



`dart:mirrors` library provide `ClassMirror` class which has `declarations` property.

declarations property is a `Map<Symbol, DeclarationMirror>`.

declarations returns an immutable map of the declarations actually given in the class declaration.

This map includes all regular methods, getters, setters, fields, constructors and type variables actually declared in the class. Both static and instance members are included, but no inherited members are included. The map is keyed by the simple names of the declarations.

A `DeclarationMirror` reflects some entity declared in a Dart program. 
Implementers: `LibraryMirror`, `MethodMirror`, `TypeMirror`, and `VariableMirror`.


Main Approach: `InstanceMirror` -> `ClassMirror` -> `DeclarationMirror` -> `VariableMirror` (file name and value)



  ```dart

    extension ObjectExtensition on Object {
    Map<Symbol, dynamic> namedArguments() {
      final InstanceMirror instanceMirror = reflect(this);
      final ClassMirror classMirror = instanceMirror.type;

      final Map<Symbol, dynamic> map = {};

      for (var v in classMirror.declarations.values) {
        if (v is VariableMirror) {
          final InstanceMirror field = instanceMirror.getField(v.simpleName);
          if (field.hasReflectee) {
            map.putIfAbsent(
              v.qualifiedName,
              () => field.reflectee,
            );
          }
        }
      }

      return map;
    }

    Map<String, dynamic> _toMapWithValidFiledName({
      bool Function(String)? validFiledName,
    }) {
      final InstanceMirror instanceMirror = reflect(this);
      final ClassMirror classMirror = instanceMirror.type;

      final Map<String, dynamic> map = {};

      for (var v in classMirror.declarations.values) {
        final String name = MirrorSystem.getName(v.simpleName);
        final bool isValid = validFiledName?.call(name) ?? true;

        if (v is VariableMirror && isValid) {
          final InstanceMirror field = instanceMirror.getField(v.simpleName);
          if (field.hasReflectee) {
            final childMap = (field.reflectee as Object).toMap();

            map.putIfAbsent(
              name,
              () => childMap.isEmpty ? field.reflectee : childMap,
            );
          }
        }
      }

      return map;
    }

    Map<String, dynamic> toMap() {
      return _toMapWithValidFiledName(
        validFiledName: (_) => true,
      );
    }

    String toJsonString() => json.encode(toMap());

    String toJsonStringWithFormat() {
      final JsonEncoder encoder = JsonEncoder.withIndent('  ');
      return encoder.convert(toMap());
    }

    Map<String, dynamic> toMapIncludeFiledNames(
      List<String>? onlyIncludeFiledNames,
    ) {
      final finalOnlyIncludeFiledNames = onlyIncludeFiledNames ?? [];
      return _toMapWithValidFiledName(
        validFiledName: (name) =>
            finalOnlyIncludeFiledNames.isEmpty ||
            finalOnlyIncludeFiledNames.contains(name),
      );
    }

    Map<String, dynamic> toMapExceptFiledNames(
      List<String>? exceptFiledNames,
    ) {
      final finalExceptFiledNames = exceptFiledNames ?? [];

      return _toMapWithValidFiledName(
        validFiledName: (name) =>
            finalExceptFiledNames.isEmpty ||
            !finalExceptFiledNames.contains(name),
      );
    }
  }

  ```



{: .box-warning}
**Warning:** The dart:mirrors library is unstable and its API might change slightly as a result of user feedback. This library is only supported by the Dart VM and only available on some platforms.

### Tuorial 

Created Class `MennuItem` and convert an `Object` type to a `Map`, so the variables become key/value pairs with method `toMap()`

#### Input 

```dart 

class Icon {
  final String name;
  final int color;

  Icon({required this.name, required this.color});
}

class MenuItem {
  final String title;
  final bool isEnable;
  final int index;
  final Icon icon;
  final List<String> listTrackingCode;

  MenuItem({
    required this.title,
    required this.isEnable,
    required this.index,
    required this.icon,
    required this.listTrackingCode,
  });
}


```

#### Try 

```dart

void main(List<String> arguments) {
  final MenuItem item = MenuItem(
    title: "New tab",
    isEnable: true,
    index: 0,
    icon: Icon(
      color: 0xffffff,
      name: "icNewTab",
    ),
    listTrackingCode: ["new_tab"],
  );

  print("toMap()");
  print(item.toMap());

  print("toMapIncludeFiledNames()");
  print(item.toMapIncludeFiledNames(["listTrackingCode", "icon"]));

  print("toMapExceptFiledNames()");
  print(item.toMapExceptFiledNames(["listTrackingCode", "icon"]));

  print("toJsonStringWithFormat()");
  print(item.toJsonStringWithFormat());
}

```

#### Output 

```dart
toMap()
{title: New tab, isEnable: true, index: 0, icon: {name: icNewTab, color: 16777215}, listTrackingCode: [new_tab]}

toMapIncludeFiledNames()
{icon: {name: icNewTab, color: 16777215}, listTrackingCode: [new_tab]}

toMapExceptFiledNames()
{title: New tab, isEnable: true, index: 0}

toJsonStringWithFormat()
{
  "title": "New tab",
  "isEnable": true,
  "index": 0,
  "icon": {
    "name": "icNewTab",
    "color": 16777215
  },
  "listTrackingCode": [
    "new_tab"
  ]
}
```

### Note


[Thumbnail Photo](https://pub.dev/static/img/flutter-logo-32x32.png)
