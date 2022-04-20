---
layout: post
title: Platform-specific code
cover-img: https://images.unsplash.com/photo-1518727713078-80d11060492e
thumbnail-img: https://pub.dev/static/img/flutter-logo-32x32.png
tags: [dart, flutter, platform, channels, Android, iOS, settings]
---
This guide describes how to write custom platform-specific code.


As I read this [article](https://docs.flutter.dev/development/platform-integration/platform-channels?tab=type-mappings-swift-tab), I thought it would be confusing for a beginner. 

In this post I took a simpler approach, for example opening the settings screen on Android and iOS from your app.


# Overview 

- Scope: Android(Kotlin) and iOS(Swift 5)

- Feature: open setting screen form your app.


### iOS

Open Settings screen 


<img src="https://user-images.githubusercontent.com/3994863/164125197-ce5a992f-0c08-4a76-b484-b8ecf79388b0.gif" width = 200>


### Android

Open Settings screen 

<img src="https://user-images.githubusercontent.com/3994863/164044499-19871bb5-fc19-4b28-9831-b35b94c14de1.gif" width = 200>


# Flutter Channel

## Create channel 

All channel names used in a single app must be unique; 
prefix the channel name with a unique ‘domain prefix’, for example:

1. Define App Id 

This is application Id(Android) or bundle Id (iOS)

```dart
static const String appID = "com.example";

```

2. Define Feature Name 

```dart
featureName= "settings";

```

3. Define Channel 

```dart
final String channelName= "$appID/$featureName";

static const MethodChannel platform = MethodChannel(channelName);

```

## Invoke a method on the method channel

### Create method name 

1. Define method name 

```dart 
static const String methodOpenAppSettingScreen = "openAppSettingScreen";

```

2. Define method invoke

invoke a method on the method channel, specifying the concrete method to call using the String identifier `openAppSettingScreen`. 

The call might fail—for example if the platform does not support the platform API (such as when running in a simulator)—so wrap the invokeMethod call in a try-catch statement.

```dart 

Future<bool> openAppSettingScreen({final Function? onError}) async {
    try {
      final bool result =
          await platform.invokeMethod(methodOpenAppSettingScreen);
      return result;
    } on PlatformException catch (e) {
      if (kDebugMode) {
        print(e.toString());
      }
      return false;
    }
  }

```

The method `await platform.invokeMethod(methodOpenAppSettingScreen)` return data type `bool`.

When you calling platform-specific iOS and Android code using platform channels, you must return same data type.

Check the table shows how Dart values are received on the platform side and vice versa:

- Flutter(Dart): bool
- Android(Kotlin) : Boolean
- iOS(Swift): Bool



### Add an Android(Kotlin) platform-specific implementation

1. Create configure Flutter Engine

- open file `MainActivity.kt` 
- create method `configureFlutterEngine`


<img width="837" alt="Screen Shot 2022-04-19 at 21 23 23" src="https://user-images.githubusercontent.com/3994863/164033221-9ca9f62c-af30-4c75-a6d3-fc1dd00a88e3.png">


```kotlin

class MainActivity: FlutterActivity() {

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
    }
}
```

- Add channel name and method name 

The channel name and method name  are must be same value as Flutter channel


```kotlin 
    companion object {
        private const val APP_ID: String = "com.example"
        private const val FEATURE_NAME: String = "settings"
        private const val CHANNEL_NAME: String = "$APP_ID/$FEATURE_NAME"
        private const val METHOD_OPEN_APP_SETTING_SCREEN: String = "openAppSettingScreen"
    }
```

- Implement open setting screen 

```kotlin 

    fun openSettingScreen(): Boolean {
        val intentSetting = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS).apply {
            data = Uri.fromParts("package", packageName, null)
        }
        return try {
            startActivity(intentSetting)
            true
        } catch (e: Exception) {
            false
        }
    }

```

Remember method `openSettingScreen` will return `Boolean` type.


- Detect channel name on method `configureFlutterEngine`

```kotlin

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL_NAME).setMethodCallHandler {
                call, result ->
            if (call.method == METHOD_OPEN_APP_SETTING_SCREEN) {
                // TODO
                return@setMethodCallHandler
            }
        }
    }

```

- Implement method and handle result 

```kotlin 


    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL_NAME).setMethodCallHandler {
                call, result ->
            if (call.method == METHOD_OPEN_APP_SETTING_SCREEN) {
                result.success(openSettingScreen())
                return@setMethodCallHandler
            }
        }
    }

```



### Add an iOS platform-specific implementation

1. Create configure Flutter Engine

- open file `AppDelegate.swift` on `Xcode` 

```swift

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }

```

- define `controller`

```swift 

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let controller : FlutterViewController = window?.rootViewController as! FlutterViewController
    
    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}

```
- Add channel name and method name 

The channel name and method name  are must be same value as Flutter channel

```swift

    let appID = "com.example"
    let featureName = "settings"
    let methodOpenAppSettingScreen = "openAppSettingScreen"
    
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        let controller : FlutterViewController = window?.rootViewController as! FlutterViewController
        let channelName = "\(self.appID)/\(self.featureName)"
        
        
        GeneratedPluginRegistrant.register(with: self)
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }

```


- Implement open setting screen 

```swift 
    
    private func openSettingScreen() -> Bool {
        if let url = URL(string:UIApplication.openSettingsURLString) {
            if UIApplication.shared.canOpenURL(url) {
                if #available(iOS 10.0, *) {
                    do {
                        try  UIApplication.shared.open(url, options: [:], completionHandler: nil)
                        return true
                    } catch {
                        return false
                    }
                    
                }
                return UIApplication.shared.openURL(url)
                
            }
        }
        
        return false
    }

```
Remember method `openSettingScreen` will return `Bool` type.

- Find Flutter channel on method `application` and detect method name

```swift 

    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        let controller : FlutterViewController = window?.rootViewController as! FlutterViewController
        let channelName = "\(self.appID)/\(self.featureName)"
        
        let settingChannel = FlutterMethodChannel(name: channelName,
                                                  binaryMessenger: controller.binaryMessenger)
        settingChannel.setMethodCallHandler({
            (call: FlutterMethodCall, result: @escaping FlutterResult) -> Void in
            if (call.method == self.methodOpenAppSettingScreen) {
                // TODO
            }
            
        })
        
        GeneratedPluginRegistrant.register(with: self)
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }

```


- Implement method and handle result 

```swift 
    
    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        let controller : FlutterViewController = window?.rootViewController as! FlutterViewController
        let channelName = "\(self.appID)/\(self.featureName)"
        
        let settingChannel = FlutterMethodChannel(name: channelName,
                                                  binaryMessenger: controller.binaryMessenger)
        settingChannel.setMethodCallHandler({
            (call: FlutterMethodCall, result: @escaping FlutterResult) -> Void in
            if (call.method == self.methodOpenAppSettingScreen) {
                result(self.openSettingScreen())
            }
            
        })
        
        GeneratedPluginRegistrant.register(with: self)
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }
    

```    


# Apply Channel Method

```dart 

Future<void> _onSetting() async {
    final SettingChannel settingChannel = SettingChannel();
    await settingChannel.openAppSettingScreen();
}

```

### Source code 

https://github.com/ttpho/flutter-setting-app/blob/main/settings/lib/main.dart



### Note

[Cover Photo](https://unsplash.com/photos/ltFKYpgoKto)

[Thumbnail Photo](https://pub.dev/static/img/flutter-logo-32x32.png)
