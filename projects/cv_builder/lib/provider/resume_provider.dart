import 'package:cv_builder/model/resume.dart';
import 'package:cv_builder/provider/reader_provider.dart';

abstract class ResumeProvider {
  Future<Resume> getResume();
}

class LocalResumeProvider extends ResumeProvider {
  @override
  Future<Resume> getResume() async {
    final Map<String, dynamic> json =
        await ReaderProvider().readJSONFile("assets/jsons/mock.json");
    return Resume.fromJson(json);
  }
}
