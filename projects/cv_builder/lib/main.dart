import 'dart:ui';

import 'package:cv_builder/material/text_style_manger.dart';
import 'package:cv_builder/repository/resume_repository.dart';
import 'package:flutter/material.dart';
import 'model/resume.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}

class DivideWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return const Divider(
      height: 1,
      thickness: 1,
    );
  }
}

class SpaceHorontialWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return const SizedBox(width: 16);
  }
}

class SpaceVerticalWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return const SizedBox(height: 16);
  }
}

class AbountMeWidget extends StatelessWidget {
  final ColorTheme? colorTheme;
  final Resume? resume;

  const AbountMeWidget({Key? key, this.resume, this.colorTheme})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    final TextStyleManager styleManager = TextStyleManager();
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "ABOUT ME",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.group,
            colorTheme,
          ),
        ),
        SpaceVerticalWidget(),
        Text(
          resume?.formSettings?.aboutme ?? "",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.normal,
            colorTheme,
          ),
        ),
      ],
    );
  }
}

class TextLineWidget extends StatelessWidget {
  final ColorTheme? colorTheme;
  final String? text;

  const TextLineWidget({
    Key? key,
    this.colorTheme,
    this.text,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    final TextStyleManager styleManager = TextStyleManager();
    final textStyle = styleManager.buildTextStyle(
      context,
      TextStyleElement.normal,
      colorTheme,
    );
    return RichText(
      text: TextSpan(
        style: DefaultTextStyle.of(context).style,
        children: [
          TextSpan(
            text: "•  ",
            style: textStyle?.copyWith(
              color: styleManager.buildColor(
                colorTheme,
              ),
            ),
          ),
          TextSpan(
            text: text ?? "",
            style: textStyle,
          ),
        ],
      ),
    );
  }
}

class InfomationGroupWidget extends StatelessWidget {
  final ColorTheme? colorTheme;
  final List<GroupInfomation>? listGroupInfomation;
  final String? groupTitle;

  const InfomationGroupWidget({
    Key? key,
    this.colorTheme,
    this.listGroupInfomation,
    this.groupTitle,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final TextStyleManager styleManager = TextStyleManager();
    final List<GroupInfomation> groups = listGroupInfomation ?? [];
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SpaceVerticalWidget(),
        Text(
          groupTitle ?? "",
          style: styleManager.buildTextStyle(
              context, TextStyleElement.group, colorTheme),
        ),
        SpaceVerticalWidget(),
        groups.isEmpty
            ? Container()
            : Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: groups
                    .map((e) => InfomationElementWidget(
                          colorTheme: colorTheme,
                          groupInfomation: e,
                        ))
                    .toList(growable: false),
              ),
      ],
    );
  }
}

class InfomationElementWidget extends StatelessWidget {
  final ColorTheme? colorTheme;
  final GroupInfomation? groupInfomation;
  const InfomationElementWidget({
    Key? key,
    this.colorTheme,
    this.groupInfomation,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final TextStyleManager styleManager = TextStyleManager();
    final List<String> summaryArr = groupInfomation?.summaryArr ?? [];
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          groupInfomation?.title ?? "",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.title,
            colorTheme,
          ),
        ),
        SpaceVerticalWidget(),
        Text(
          groupInfomation?.location ?? "",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.normal,
            colorTheme,
          ),
        ),
        SpaceVerticalWidget(),
        summaryArr.isEmpty
            ? Container()
            : Container(
                margin: const EdgeInsets.only(left: 8.0, right: 8.0),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: summaryArr
                      .map((text) => TextLineWidget(
                            colorTheme: colorTheme,
                            text: text,
                          ))
                      .toList(growable: false),
                ),
              ),
        SpaceVerticalWidget(),
      ],
    );
  }
}

class InfomationDetalWidget extends StatelessWidget {
  final Resume? resume;
  final ColorTheme? colorTheme;

  const InfomationDetalWidget({Key? key, this.resume, this.colorTheme})
      : super(key: key);
  @override
  Widget build(BuildContext context) {
    if (resume == null) {
      return Container();
    }
    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          mainAxisSize: MainAxisSize.max,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            AbountMeWidget(
              colorTheme: colorTheme,
              resume: resume,
            ),
            SpaceVerticalWidget(),
            DivideWidget(),
            InfomationGroupWidget(
              colorTheme: colorTheme,
              groupTitle: "EXPERIENCE",
              listGroupInfomation: resume?.formSettings?.work,
            ),
            DivideWidget(),
            InfomationGroupWidget(
              colorTheme: colorTheme,
              groupTitle: "EDUCATION",
              listGroupInfomation: resume?.formSettings?.education,
            ),
            DivideWidget(),
            InfomationGroupWidget(
              colorTheme: colorTheme,
              groupTitle: "PROJECTS",
              listGroupInfomation: resume?.formSettings?.projects,
            ),
          ],
        ),
      ),
    );
  }
}

class PersonNameWidget extends StatelessWidget {
  final Resume? resume;
  final ColorTheme? colorTheme;

  const PersonNameWidget({
    Key? key,
    this.resume,
    this.colorTheme,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final TextStyleManager styleManager = TextStyleManager();

    if (resume == null) {
      return Container();
    }

    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          resume?.formSettings?.name ?? "",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.full_name,
            colorTheme,
          ),
        ),
        Text(
          resume?.formSettings?.lastName ?? "",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.full_name,
            colorTheme,
          ),
        ),
        Text(
          resume?.formSettings?.jobTitle ?? "",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.job_title,
            colorTheme,
          ),
        ),
      ],
    );
  }
}

class IconTextWidget extends StatelessWidget {
  final String? text;
  final IconData? iconData;
  final Color? iconColor;
  final TextStyle? textStyle;

  const IconTextWidget({
    Key? key,
    this.text,
    this.iconData,
    this.iconColor,
    this.textStyle,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Wrap(
      crossAxisAlignment: WrapCrossAlignment.center,
      children: [
        Icon(
          this.iconData,
          color: this.iconColor,
        ),
        SpaceHorontialWidget(),
        Text(
          this.text ?? "",
          style: textStyle,
        ),
      ],
    );
  }
}

class ImageTextWidget extends StatelessWidget {
  final String? text;
  final Image? image;
  final TextStyle? textStyle;

  const ImageTextWidget({
    Key? key,
    this.text,
    this.image,
    this.textStyle,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Wrap(
      crossAxisAlignment: WrapCrossAlignment.center,
      children: [
        SizedBox(
          child: image ?? Container(),
          width: 24,
          height: 24,
        ),
        SpaceHorontialWidget(),
        Text(
          this.text ?? "",
          style: textStyle,
        ),
      ],
    );
  }
}

class ContactWidget extends StatelessWidget {
  final Resume? resume;
  final ColorTheme? colorTheme;

  const ContactWidget({
    Key? key,
    this.resume,
    this.colorTheme,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    if (resume == null) {
      return Container();
    }
    final TextStyleManager styleManager = TextStyleManager();
    final Color color = styleManager.buildColor(colorTheme);
    final TextStyle? textStyle = styleManager.buildTextStyle(
      context,
      TextStyleElement.normal,
      colorTheme,
    );

    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          "CONTACT",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.part,
            colorTheme,
          ),
        ),
        IconTextWidget(
          text: resume?.formSettings?.phoneNumber,
          iconData: Icons.phone,
          iconColor: color,
          textStyle: textStyle,
        ),
        IconTextWidget(
          text: resume?.formSettings?.email,
          iconData: Icons.email,
          iconColor: color,
          textStyle: textStyle,
        ),
        IconTextWidget(
          text: resume?.formSettings?.location,
          iconData: Icons.location_on,
          iconColor: color,
          textStyle: textStyle,
        ),
      ],
    );
  }
}

class SkillItemWidget extends StatelessWidget {
  final String? text;
  final Color? color;
  final TextStyle? textStyle;

  const SkillItemWidget({
    Key? key,
    this.text,
    this.color,
    this.textStyle,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Padding(
        padding: const EdgeInsets.only(
          left: 8,
          right: 8,
          top: 4,
          bottom: 4,
        ),
        child: Text(
          text ?? "",
          style: textStyle?.copyWith(
            color: Colors.white,
          ),
        ),
      ),
      decoration: BoxDecoration(
        color: this.color,
        borderRadius: BorderRadius.circular(15),
      ),
    );
  }
}

class ProfessionalSkillsWidget extends StatelessWidget {
  final Resume? resume;
  final ColorTheme? colorTheme;

  const ProfessionalSkillsWidget({
    Key? key,
    this.resume,
    this.colorTheme,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    if (resume == null) {
      return Container();
    }
    final TextStyleManager styleManager = TextStyleManager();
    final Color color = styleManager.buildColor(colorTheme);
    final List<String> jobSkills = resume?.formSettings?.jobSkills ?? [];

    final TextStyle? textStyle = styleManager.buildTextStyle(
      context,
      TextStyleElement.normal,
      colorTheme,
    );
    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          "PROFESSIONAL SKILLS",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.part,
            colorTheme,
          ),
        ),
        SpaceVerticalWidget(),
        Wrap(
          direction: Axis.horizontal,
          spacing: 8.0,
          runSpacing: 4.0,
          children: jobSkills
              .map((skill) => SkillItemWidget(
                    color: color,
                    text: skill,
                    textStyle: textStyle,
                  ))
              .toList(growable: false),
        )
      ],
    );
  }
}

class SkillWidget extends StatelessWidget {
  final ColorTheme? colorTheme;
  final List<String>? groups;
  const SkillWidget({
    Key? key,
    this.colorTheme,
    this.groups,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final TextStyleManager styleManager = TextStyleManager();
    final List<String> groupSkill = groups ?? [];
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "SOFT SKILLS",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.part,
            colorTheme,
          ),
        ),
        SpaceVerticalWidget(),
        groupSkill.isEmpty
            ? Container()
            : Container(
                margin: const EdgeInsets.only(left: 8.0, right: 8.0),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: groupSkill
                      .map((text) => TextLineWidget(
                            colorTheme: colorTheme,
                            text: text,
                          ))
                      .toList(growable: false),
                ),
              ),
        SpaceVerticalWidget(),
      ],
    );
  }
}

class LanguageItemWidget extends StatelessWidget {
  final Languages? languages;
  final TextStyleManager? styleManager;
  final ColorTheme? colorTheme;

  const LanguageItemWidget({
    Key? key,
    this.languages,
    this.styleManager,
    this.colorTheme,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    final String level = (languages?.level ?? "").replaceAll("%", "");
    final int percent = int.tryParse(level) ?? 0;
    final Color color = styleManager?.buildColor(colorTheme) ?? Colors.white;

    return Column(
      mainAxisSize: MainAxisSize.max,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          languages?.lang ?? "",
          style: styleManager?.buildTextStyle(
            context,
            TextStyleElement.normal,
            colorTheme,
          ),
        ),
        Container(
          height: 10,
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
            color: color.withAlpha(128),
            borderRadius: BorderRadius.circular(45),
          ),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Expanded(
                flex: percent,
                child: Container(
                  height: 10,
                  decoration: BoxDecoration(
                    color: color,
                    borderRadius: BorderRadius.circular(45),
                  ),
                  alignment: Alignment.center,
                ),
              ),
              Expanded(
                child: Container(),
                flex: 100 - percent,
              ),
            ],
          ),
        ),
        SpaceVerticalWidget(),
      ],
    );
  }
}

class LanguageWidget extends StatelessWidget {
  final ColorTheme? colorTheme;
  final List<Languages>? languages;
  const LanguageWidget({
    Key? key,
    this.colorTheme,
    this.languages,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final TextStyleManager styleManager = TextStyleManager();
    final List<Languages> langs = languages ?? [];
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          "PROFESSIONAL SKILLS",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.part,
            colorTheme,
          ),
        ),
        SpaceVerticalWidget(),
        langs.isEmpty
            ? Container()
            : Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: langs
                    .map((lang) => LanguageItemWidget(
                          languages: lang,
                          styleManager: styleManager,
                          colorTheme: colorTheme,
                        ))
                    .toList(growable: false),
              ),
        SpaceVerticalWidget(),
      ],
    );
  }
}

class SocialWidget extends StatelessWidget {
  final ColorTheme? colorTheme;
  final Resume? resume;

  const SocialWidget({
    Key? key,
    this.colorTheme,
    this.resume,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    if (resume == null) {
      return Container();
    }
    final TextStyleManager styleManager = TextStyleManager();
    final String linkedin = resume?.formSettings?.linkedin ?? "";
    final String linkedinLink = "linkedin.com/in/$linkedin/";
    final String twitter = resume?.formSettings?.twitter ?? "";
    final String twitterLink = "twitter.com/$twitter";
    final String github = resume?.formSettings?.github ?? "";
    final String githubLink = "github.com/$github";
    final String website = resume?.formSettings?.website ?? "";
    final textStyle = styleManager.buildTextStyle(
      context,
      TextStyleElement.normal,
      colorTheme,
    );
    return Wrap(
      direction: Axis.vertical,
      spacing: 8.0,
      runSpacing: 4.0,
      children: <Widget>[
        Text(
          "SOCIAL",
          style: styleManager.buildTextStyle(
            context,
            TextStyleElement.part,
            colorTheme,
          ),
        ),
        linkedin.isNotEmpty
            ? ImageTextWidget(
                text: linkedinLink,
                image: Image.asset("assets/images/linkedin.png"),
                textStyle: textStyle,
              )
            : Container(),
        twitter.isNotEmpty
            ? ImageTextWidget(
                text: twitterLink,
                image: Image.asset("assets/images/twitter.png"),
                textStyle: textStyle,
              )
            : Container(),
        github.isNotEmpty
            ? ImageTextWidget(
                text: githubLink,
                image: Image.asset("assets/images/github.png"),
                textStyle: textStyle,
              )
            : Container(),
        website.isNotEmpty
            ? ImageTextWidget(
                text: website,
                image: Image.asset("assets/images/website.png"),
                textStyle: textStyle,
              )
            : Container(),
      ],
    );
  }
}

class PersonInfoWidget extends StatelessWidget {
  final Resume? resume;
  final ColorTheme? colorTheme;

  const PersonInfoWidget({
    Key? key,
    this.resume,
    this.colorTheme,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    if (resume == null) {
      return Container();
    }
    return SingleChildScrollView(
      padding: const EdgeInsets.all(20.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        mainAxisSize: MainAxisSize.max,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          PersonNameWidget(
            colorTheme: colorTheme,
            resume: resume,
          ),
          SpaceVerticalWidget(),
          ContactWidget(
            resume: resume,
            colorTheme: colorTheme,
          ),
          SpaceVerticalWidget(),
          ProfessionalSkillsWidget(
            resume: resume,
            colorTheme: colorTheme,
          ),
          SpaceVerticalWidget(),
          SkillWidget(
            colorTheme: colorTheme,
            groups: resume?.formSettings?.softSkills ?? [],
          ),
          SpaceVerticalWidget(),
          LanguageWidget(
            colorTheme: colorTheme,
            languages: resume?.formSettings?.languages ?? [],
          ),
          SocialWidget(
            colorTheme: colorTheme,
            resume: resume,
          ),
          SpaceVerticalWidget(),
        ],
      ),
    );
  }
}

class MyApp extends StatelessWidget {
  final String _title = "Resume";
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: _title),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, this.title}) : super(key: key);

  final String? title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  ColorTheme _colorTheme = ColorTheme.carmine_pink;

  Future<Resume> _fetchResume() async {
    final Resume resume = await ResumeRepository().getResume();
    return resume;
  }

  void _refresh() {
    setState(() {
      _colorTheme = ColorTheme.turbo;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title!),
      ),
      body: FutureBuilder<Resume>(
          future: _fetchResume(),
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(
                    flex: 3,
                    child: PersonInfoWidget(
                      colorTheme: _colorTheme,
                      resume: snapshot.data,
                    ),
                  ),
                  Expanded(
                    flex: 7,
                    child: InfomationDetalWidget(
                      colorTheme: _colorTheme,
                      resume: snapshot.data,
                    ),
                  ),
                ],
              );
            }
            return Container();
          }),
      floatingActionButton: FloatingActionButton(
        onPressed: _refresh,
        tooltip: 'Refesh',
        child: Icon(Icons.refresh),
      ),
    );
  }
}
