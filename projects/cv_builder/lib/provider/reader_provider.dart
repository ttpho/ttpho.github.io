import 'dart:convert';
import 'dart:async' show Future;
import 'package:flutter/services.dart' show rootBundle;

class ReaderProvider {
  Future<Map<String, dynamic>> readJSONFile(final String filePath) async {
    final String configContentFile = await rootBundle.loadString(
      filePath,
      cache: true,
    );

    return await json.decode(configContentFile) as Map<String, dynamic>;
  }
}
