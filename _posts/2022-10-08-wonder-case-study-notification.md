---
layout: post
title: Android Wonder application - notification icon appear a grey square
subtitle: Case Study & How to fix gray icon issue in Android Notification
cover-img: https://images.unsplash.com/photo-1611262588019-db6cc2032da3
tags: [android, ios, ui-automation, blackbox-testing]
---

In this tutorial, I want to share bug notification icon appear a grey square on Android application and how to fix it.


### Case Study

Android [Wonder](https://play.google.com/store/apps/details?id=com.codeway.wonder) application `v1.4.3 (43)`, it has notification icon appear a grey square.

Notification icon on Home Screen: 

<img width=200 src="/assets/img/2022-10-08/home_screen.jpg" />

Notification icon on notification bar: 

<img width=200 src="/assets/img/2022-10-08/notification.jpg" />


App version info 

<img width=200 src="/assets/img/2022-10-08/app_info.jpg" />


### Android API  

- Before Android 5.0, the notifcation icon is icon as you set.

- From Android 5.0, [Material design style](https://android-doc.github.io/about/versions/android-5.0-changes.html) is updated.

```
Notifications are drawn with dark text atop white (or very light) backgrounds to match the new material design widgets. Make sure that all your notifications look right with the new color scheme. If your notifications look wrong, fix them:

Use setColor() to set an accent color in a circle behind your icon image.
Update or remove assets that involve color. The system ignores all non-alpha channels in action icons and in the main notification icon. You should assume that these icons will be alpha-only. The system draws notification icons in white and action icons in dark gray.
```

so this is reson your notification icon is dark gray.


### How to fix it

- Convert all parts of the image that you don’t want to show to transparent pixels. All colors and non transparent pixels are displayed in white. 

- Use Android Studio tools: `app -> New -> Image Asset -> Icon Type: Notification Icons`


<img width=300 src="/assets/img/2022-10-08/android_studio_step_1.png" />


<img width=300 src="/assets/img/2022-10-08/android_studio_step_2.png" />



- Config notification icon for Firebase push notification, `AndroidManifest.xml`



```xml 

<application>
...
          <meta-data
            android:name="com.google.firebase.messaging.default_notification_icon"
            android:resource="@drawable/ic_stat_name" />
...            
</application>
```

### Note


[Cover Photo](https://unsplash.com/photos/PHH_0uw9-Qw)
