import 'package:flutter/material.dart';

enum ColorTheme {
  turbo,
  carmine_pink,
}

enum TextStyleElement {
  normal,
  title,
  group,
  part,
  full_name,
  job_title,
}

class TextStyleManager {
  Color buildColor(final ColorTheme? colorTheme) {
    switch (colorTheme) {
      case ColorTheme.turbo:
        return const Color(0xfff9ca24);
      case ColorTheme.carmine_pink:
        return const Color(0xffeb4d4b);
      default:
        return const Color(0xDD000000);
    }
  }

  TextStyle? buildTextStyle(
    final BuildContext context,
    final TextStyleElement? element,
    final ColorTheme? colorTheme,
  ) {
    final Color color = buildColor(colorTheme);
    switch (element) {
      case TextStyleElement.normal:
        return Theme.of(context).textTheme.caption;
      case TextStyleElement.title:
        return Theme.of(context).textTheme.subtitle1;
      case TextStyleElement.group:
        return Theme.of(context).textTheme.headline6?.copyWith(color: color);
      case TextStyleElement.part:
        return Theme.of(context).textTheme.headline6;
      case TextStyleElement.job_title:
        return Theme.of(context).textTheme.headline5;
      case TextStyleElement.full_name:
        return Theme.of(context).textTheme.headline4?.copyWith(color: color);
      default:
        return Theme.of(context).textTheme.caption;
    }
  }
}
