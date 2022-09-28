---
layout: post
title: Conver Android, iOS Resouce to JSON
subtitle: Conver content Android strings.xml file, content iOS Localizable.strings file to JSON content
cover-img: https://user-images.githubusercontent.com/3994863/191051637-6302bf6c-9f24-4bac-8f97-21f00d5bd502.png
thumbnail-img: https://pub.dev/static/img/flutter-logo-32x32.png
tags: [dart, flutter]
---

In this tutorial, I want conver content file Android `string.xml`, iOS `Localizable.string` to JSON content. This is usefull, when to port Android/iOS project to Flutter Porject.


### Overview

- Parser XML use [xml](https://pub.dev/packages/xml)
- Use `key`, `value` to Dart `Map` 
- Convert Dart `Map`  to JSON string.

### Android strings.xml

- `strings.xml` XML content 

```xml 

<resources xmlns:tools="http://schemas.android.com/tools">
    <string name="logout">Logout</string>
    <string name="contact_us">Contact Us</string>
    <string name="customer_service">Customer Service</string>
    <string name="store">Store</string>
    <string name="privacy_policy">Privacy Policy</string>
    <string name="policies">Policies</string>
    <string name="terms">Terms</string>
    <string name="subscription_terms">Subscription Terms</string>
</resources>

```

- Parser XML by element name `string`, `key` by `atribute` and `value` by `node`. 

```dart

Map<String, String> _fromAndroidXmlString(final String xmlString) {
  final document = XmlDocument.parse(xmlString);
  final stringElemnets = document.findAllElements('string');
  final Map<String, String> map = {};
  for (final element in stringElemnets) {
    final attributes = element.attributes;
    final textFirstChild = element.firstChild?.text ?? "";
    if (attributes.isNotEmpty && textFirstChild.isNotEmpty) {
      map[attributes.first.value] = textFirstChild;
    }
  }

  return map;
}
```

- Result 

```json

{
  "logout": "Logout",
  "contact_us": "Contact Us",
  "customer_service": "Customer Service",
  "store": "Store",
  "privacy_policy": "Privacy Policy",
  "policies": "Policies",
  "terms": "Terms",
  "subscription_terms": "Subscription Terms"
}

```


### iOS Localizable.strings

- `Localizable.strings` content 

```dart

/* Correct message */
"correctly" = "correctly";

/* Incorrect message */
"incorrectly" = "incorrectly";

/* No comment provided by engineer. */
"Mexico.Answer" = "September 16";

/* No comment provided by engineer. */
"Mexico.Choices" = "January 5;February 24;March 21;May 5;September 16;November 1;November 20";

/* No comment provided by engineer. */
"Mexico.Question" = "What day is Mexican Independence Day?";

/* No comment provided by engineer. */
"Next" = "Next";
```

- Read line by line, with each line, left string before `=` conver to `key`, right string after `=` conver to `value`

```dart

Map<String, String> _fromLocalizableString(final String localizableString) {
  final Map<String, String> map = {};
  localizableString
      .split("\n")
      .where((element) => element.contains("=") && element.endsWith(";"))
      .forEach((line) {
    final list = line.split("=").map((e) => e.trim()).toList();
    if (list.length == 2) {
      final String leftString = list.first;
      final String key = leftString.substring(1, leftString.length - 1);
      final String rightString = list.last;
      final String value = rightString.substring(1, rightString.length - 2);
      map[key] = value;
    }
  });

  return map;
}
```

- Result 

```json

{
  "Catalan.Answer": "Catalan",
  "Catalan.Choices": "Spanish;Catalan;French;Portuguese;Italian",
  "Catalan.Question": "Which language is spoken in Andorra?",
  "correctly": "correctly",
  "DC.Answer": "Washington D.C.",
  "DC.Choices": "New York City;San Francisco;Atlanta;Washington D.C.;Dallas;Los Angeles",
  "DC.Question": "What is the capital of the United States?",
  "incorrectly": "incorrectly",
  "Mexico.Answer": "September 16",
  "Mexico.Choices": "January 5;February 24;March 21;May 5;September 16;November 1;November 20",
  "Mexico.Question": "What day is Mexican Independence Day?",
  "Next": "Next"
}

```

### Conver Map to JSON 

```dart 
String toJsonStringWithFormat(final Map<String, String> map) =>
    JsonEncoder.withIndent('  ').convert(map);
```

### Note
[Source Code](https://github.com/ttpho/resource_to_json)

[Thumbnail Photo](https://pub.dev/static/img/flutter-logo-32x32.png)
