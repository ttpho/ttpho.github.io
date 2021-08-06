class Resume {
  FormSettings? formSettings;

  Resume({
    this.formSettings,
  });

  Resume.fromJson(Map<String, dynamic> json) {
    formSettings = json['formSettings'] != null
        ? new FormSettings.fromJson(json['formSettings'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.formSettings != null) {
      data['formSettings'] = this.formSettings?.toJson();
    }
    return data;
  }
}

class FormSettings {
  String? jobTitle;
  String? name;
  String? lastName;
  String? email;
  String? location;
  String? phoneNumber;
  String? aboutme;
  List<String>? jobSkills;
  List<String>? softSkills;
  List<Languages>? languages;
  String? linkedin;
  String? twitter;
  String? github;
  String? website;
  List<GroupInfomation>? education;
  List<GroupInfomation>? work;
  List<GroupInfomation>? projects;

  FormSettings({
    this.jobTitle,
    this.name,
    this.lastName,
    this.email,
    this.location,
    this.phoneNumber,
    this.aboutme,
    this.jobSkills,
    this.softSkills,
    this.languages,
    this.linkedin,
    this.twitter,
    this.github,
    this.website,
    this.education,
    this.work,
    this.projects,
  });

  FormSettings.fromJson(Map<String, dynamic> json) {
    jobTitle = json['jobTitle'];
    name = json['name'];
    lastName = json['lastName'];
    email = json['email'];
    location = json['location'];
    phoneNumber = json['phoneNumber'];
    aboutme = json['aboutme'];
    jobSkills = json['jobSkills'].cast<String>();
    softSkills = json['softSkills'].cast<String>();
    if (json['languages'] != null) {
      languages = [];
      json['languages'].forEach((v) {
        languages?.add(new Languages.fromJson(v));
      });
    }
    linkedin = json['linkedin'];
    twitter = json['twitter'];
    github = json['github'];
    if (json['education'] != null) {
      education = [];
      json['education'].forEach((v) {
        education?.add(new GroupInfomation.fromJson(v));
      });
    }
    if (json['work'] != null) {
      work = [];
      json['work'].forEach((v) {
        work?.add(new GroupInfomation.fromJson(v));
      });
    }
    if (json['projects'] != null) {
      projects = [];
      json['projects'].forEach((v) {
        projects?.add(new GroupInfomation.fromJson(v));
      });
    }
    this.website = json['website'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['jobTitle'] = this.jobTitle;
    data['name'] = this.name;
    data['lastName'] = this.lastName;
    data['email'] = this.email;
    data['location'] = this.location;
    data['phoneNumber'] = this.phoneNumber;
    data['aboutme'] = this.aboutme;
    data['jobSkills'] = this.jobSkills;
    data['softSkills'] = this.softSkills;
    if (this.languages != null) {
      data['languages'] = this.languages?.map((v) => v.toJson()).toList();
    }
    data['linkedin'] = this.linkedin;
    data['twitter'] = this.twitter;
    data['github'] = this.github;
    data['website'] = this.website;
    if (this.education != null) {
      data['education'] = this.education?.map((v) => v.toJson()).toList();
    }
    if (this.work != null) {
      data['work'] = this.work?.map((v) => v.toJson()).toList();
    }
    if (this.projects != null) {
      data['projects'] = this.projects?.map((v) => v.toJson()).toList();
    }

    return data;
  }
}

class Languages {
  String? lang;
  String? level;

  Languages({
    this.lang,
    this.level,
  });

  Languages.fromJson(Map<String, dynamic> json) {
    lang = json['lang'];
    level = json['level'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['lang'] = this.lang;
    data['level'] = this.level;
    return data;
  }
}

class GroupInfomation {
  String? title;
  String? location;
  String? from;
  String? to;
  String? current;
  String? summary;
  List<String>? summaryArr;

  GroupInfomation({
    this.title,
    this.location,
    this.from,
    this.to,
    this.current,
    this.summary,
    this.summaryArr,
  });

  GroupInfomation.fromJson(Map<String, dynamic> json) {
    title = json['title'];
    location = json['location'];
    from = json['from'];
    to = json['to'];
    current = json['current'];
    summary = json['summary'];
    summaryArr = json['summaryArr'].cast<String>();
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['title'] = this.title;
    data['location'] = this.location;
    data['from'] = this.from;
    data['to'] = this.to;
    data['current'] = this.current;
    data['summary'] = this.summary;
    data['summaryArr'] = this.summaryArr;
    return data;
  }
}
