---
layout: post
title: Using Java for Flutter code generator for your assets, json files
cover-img: https://raw.githubusercontent.com/ttpho/BuildAssets/master/imgs/3.png
thumbnail-img: https://upload.wikimedia.org/wikipedia/commons/5/5d/Duke_%28Java_mascot%29_waving.svg
tags: [java, dart, flutter]
---

Using asset path string directly is not safe.
What happens if you change the image file name or delete the image file.

In some cases, if the number of files is too large, too many must be defined in the `pubspec.yaml` file.

#### Setup Project Flutter

- Step 1. Download and move this file [BuildAssets.java](https://github.com/ttpho/BuildAssets/blob/master/BuildAssets.java) into your project.

- Step 2. Open file `pubspec.yaml`

Add 2 lines, below line `uses-material-design: true`

```java
# === Generated Code Start ===
# === Generated Code End ===
```

<img src="https://raw.githubusercontent.com/ttpho/BuildAssets/master/imgs/1.png"/>

- Step 3. Open terminal and run

```java
javac BuildAssets.java
java BuildAssets
```

<img src="https://raw.githubusercontent.com/ttpho/BuildAssets/master/imgs/2.png"/>

- Step 4. Open `pubspec.yaml` and enjoy

#### Gen code

| CMD                                                     | Output                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| java BuildAssets JSON <package>.<class_name>.dart       | with command: `% java BuildAssets JSON local.manager.reader_json.dart` to gen file `reader_json.dart` into folder `lib/local/manager/`, the file is included static class `ReaderJson` <img src="https://raw.githubusercontent.com/ttpho/BuildAssets/master/imgs/5.png" />  |
| java BuildAssets AssetImage <package>.<class_name>.dart | with command: `java BuildAssets AssetImage local.manager.all_assets.dart` to gen file `all_assets.dart` into folder `lib/local/manager/`, the file is included static class `AllAssets` <img src="https://raw.githubusercontent.com/ttpho/BuildAssets/master/imgs/4.png" /> |

#### Idea

The idea from Chromium source code:

`BuildConfigGenerator.groovy` gen code from build.gradle to create `BUILD.gn`file.

`https://chromium.googlesource.com/chromium/src/+/refs/heads/master/third_party/android_deps/buildSrc/src/main/groovy/BuildConfigGenerator.groovy`

#### Tutorial

In Flutter Project

- Create folder `assets\svgs` and put all svg files into this folder.
  <img width="573" alt="Screen Shot 2021-08-29 at 10 54 08" src="https://user-images.githubusercontent.com/3994863/131237773-d7dbb9a5-fa9a-4dd8-ab2e-9da8a21c6fb8.png">

- File `pubspec.yaml` added

```yaml
flutter:
  # The following line ensures that the Material Icons font is
  # included with your application, so that you can use the icons in
  # the material Icons class.
  uses-material-design: true
  # === Generated Code Start ===
  # === Generated Code End ===
```

- Run

```java
javac BuildAssets.java
java BuildAssets
```

- Open files `pubspec.yaml` and check result
  <img width="908" alt="Screen Shot 2021-08-29 at 10 57 25" src="https://user-images.githubusercontent.com/3994863/131237836-dc2be570-2abe-4e58-9025-2501e952bdfe.png">

- Run

```java
java BuildAssets AssetImage svg_file.dart
```

- Open files `svg_file.dart` and check result

<img width="1132" alt="Screen Shot 2021-08-29 at 11 18 19" src="https://user-images.githubusercontent.com/3994863/131238244-f9e39d12-03f8-4b30-a4a4-2d04d79dcabc.png">

#### Source code

https://github.com/ttpho/BuildAssets
