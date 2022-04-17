---
layout: post
title: Push notification for Android/iOS and testing strategy
cover-img: https://images.unsplash.com/photo-1514464750060-00e6e34c8b8c
thumbnail-img: https://pub.dev/static/img/flutter-logo-32x32.png
tags: [dart, flutter]
---
Push notification for Android/iOS and testing strategy

### Overview 

Firebase Cloud Messaging (FCM) provides a reliable and battery-efficient connection between your server and devices that allows you to deliver and receive messages and notifications on Android, iOS.

1. Tooling to compose or build message requests.

    With `Elixir/Phoenix Framework`, you can use [pigeon](https://github.com/codedge-llc/pigeon)

    This is HTTP2-compliant wrapper for sending iOS and Android push notifications.


2. The FCM backend, which (among other functions) accepts message requests, performs fanout of messages via topics, and generates message metadata such as the message ID.


3. A platform-level transport layer, which routes the message to the targeted device, handles message delivery, and applies platform-specific configuration where appropriate.

    This transport layer includes:

    - Android transport layer (ATL) for Android devices with Google Play services
    - Apple Push Notification service (APNs) for Apple devices
    - Web push protocol for web apps


<img width=300 src="https://firebase.google.com/docs/cloud-messaging/images/diagram-FCM.png" >

### Device Token 

Register devices to receive messages from FCM. 

An instance of a client app registers to receive messages, obtaining a registration token that uniquely identifies the app instance.

Save the token to the server and update the timestamp whenever it changes, such as when:

- The app is restored on a new device
- The user uninstalls/reinstall the app
- The user clears app data.

### Sending message 

- Cloud Messaging API (Legacy) must be enabled.
- With Android, the APK must be created by SHA1 Key, you created/added into Firebase Project

Test Script.  Put your device token (`DEVICE_TOKEN`) and your Cloud Messaging API Key(`API_KEY`)

```

DATA='{"notification": {"body": "this is a body","title": "this is a title"}, "priority": "high", "data": {"click_action": "FLUTTER_NOTIFICATION_CLICK", "id": "1", "status": "done"}, "to": <DEVICE_TOKEN>}'
curl https://fcm.googleapis.com/fcm/send -H "Content-Type:application/json" -X POST -d "$DATA" -H "Authorization: key=<API_KEY>"

```


Result: 

```
{"multicast_id":2008572079450013199,"success":1,"failure":0,"canonical_ids":0,"results":[{"message_id":"0:1649952604447648%183068cf183068cf"}]}% 

```

### Receiving messages

- FCM via APNs does not work on iOS Simulators. To receive messages & notifications a real device is required.

- [TEST]You can test push notification with Android Emulator with Google Play Service.



### Notification Permission 


#### Android 

To help users focus on the notifications that are most important to them, `Android 13` introduces a new runtime permission for sending notifications from an app: `POST_NOTIFICATIONS`. 

Apps targeting `Android 13` will now need to request the notification permission from the user before posting notifications. 

For apps targeting **Android 12 or lower**, the system will handle the upgrade flow on your behalf.

<img width=200 src="https://user-images.githubusercontent.com/3994863/163345624-92cdb54d-8ba8-41a0-a547-982f4659cb8e.png" />

https://android-developers.googleblog.com/2022/03/second-preview-android-13.html


#### iOS 

Request permission to display alerts, play sounds, or badge the app’s icon in response to a notification.

<img width=200 src ="https://user-images.githubusercontent.com/3994863/163344997-9ed3ad4c-6d11-4b5b-9402-635856ab8d2b.png" />


### Android Notification Channels 


Starting in Android 8.0 (API level 26), all notifications must be assigned to a channel.

For each channel, you can set the visual and auditory behavior that is applied to all notifications in that channel. 

Then, users can change these settings and decide which notification channels from your app should be intrusive or visible at all.


### Notification Setting 


#### Android 

[Open the notification channel settings](https://developer.android.com/training/notify-user/channels#UpdateChannel)

```kotlin

val intent = Intent(Settings.ACTION_CHANNEL_NOTIFICATION_SETTINGS).apply {
    putExtra(Settings.EXTRA_APP_PACKAGE, packageName)
    putExtra(Settings.EXTRA_CHANNEL_ID, myNotificationChannel.getId())
}
startActivity(intent)

```


[TODO] Open the notification channel settings by Flutter

### iOS 

[Opening app's notification settings in the settings app](https://stackoverflow.com/a/61097213)

```swift

if let appSettings = URL(string: UIApplication.openSettingsURLString), UIApplication.shared.canOpenURL(appSettings) {
    UIApplication.shared.open(appSettings)
}

```


[TODO] Opening app's notification settings in the settings app by Flutter


### Note

[Cover Photo](https://unsplash.com/photos/33oxtOMk6Ac)

[Thumbnail Photo](https://pub.dev/static/img/flutter-logo-32x32.png)
