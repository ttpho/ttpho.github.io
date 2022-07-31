import 'dart:mirrors';
import 'dart:convert';

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
