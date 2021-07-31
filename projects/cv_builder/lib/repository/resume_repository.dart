import 'package:cv_builder/model/resume.dart';
import 'package:cv_builder/provider/resume_provider.dart';

class ResumeRepository {
  final ResumeProvider _resumeProvider = LocalResumeProvider();
  Future<Resume> getResume() async => _resumeProvider.getResume();
}
