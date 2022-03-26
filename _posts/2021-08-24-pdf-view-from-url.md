---
layout: post
title: Flutter App - View PDF from PDF URL link
cover-img: https://images.unsplash.com/photo-1603406136476-85d8c3ec76a5
thumbnail-img: https://pub.dev/static/img/flutter-logo-32x32.png
tags: [dart, flutter]
---

Load and present a PDF file from URL in Flutter

### Overview

![URL PDF View](/assets/img/2021-08-24/url-pdf-view.png)

### Fetch PDF content

Use [Dio](https://pub.dev/packages/dio) lib to load PDF URL link to

```dart
Future<Uint8List> _fetchPdfContent(final String url) async {
    try {
      final Response<List<int>> response = await Dio().get<List<int>>(
        url,
        options: Options(responseType: ResponseType.bytes),
      );
      return Uint8List.fromList(response.data);
    } catch (e) {
      print(e);
      return null;
    }
  }
```

### Display PDF content

Use [printing](https://pub.dev/packages/printing) to display PDF content from `Uint8List`.

```dart
PdfPreview(
      allowPrinting: false,
      allowSharing: false,
      canChangePageFormat: false,
      initialPageFormat:
          PdfPageFormat(100 * PdfPageFormat.mm, 120 * PdfPageFormat.mm),
      build: (format) => content,
    );
```

### Put Together

User `FutureBuilder` to build `Widget` loading content from URL.

```dart
class _MyHomePageState extends State<MyHomePage> {
  final String _url =
      "https://www.au-sonpo.co.jp/corporate/upload/article/89/article_89_1.pdf";


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: FutureBuilder<Uint8List>(
        future: _fetchPdfContent(_url),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return PdfPreview(
              allowPrinting: false,
              allowSharing: false,
              canChangePageFormat: false,
              initialPageFormat:
                  PdfPageFormat(100 * PdfPageFormat.mm, 120 * PdfPageFormat.mm),
              build: (format) => snapshot.data,
            );
          }
          return Center(
            child: CircularProgressIndicator(),
          );
        },
      )
    );
  }

  Future<Uint8List> _fetchPdfContent(final String url) async {
    try {
      final Response<List<int>> response = await Dio().get<List<int>>(
        url,
        options: Options(responseType: ResponseType.bytes),
      );
      return Uint8List.fromList(response.data);
    } catch (e) {
      print(e);
      return null;
    }
  }
}

```

#### Demo

![Demo](https://user-images.githubusercontent.com/3994863/126652864-45c69e73-1b4a-4f5a-b5a1-a9f20c6ac059.png)

#### Source code

https://github.com/ttpho/PDFViewer

### Note

[Cover Photo](https://unsplash.com/photos/g-d-S9gF2sY)

[Thumbnail Photo](https://dart.dev/assets/shared/dart/logo+text/horizontal/white-e71fb382ad5229792cc704b3ee7a88f8013e986d6e34f0956d89c453b454d0a5.svg)
