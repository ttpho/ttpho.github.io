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

- Step 2. Open file `pubspec.yam`

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

#### Source code

https://github.com/ttpho/BuildAssets
