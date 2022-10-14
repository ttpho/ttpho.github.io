---
layout: post
title: Part 2, Maestro - automate UI testing for your mobile app
subtitle: Use Maestro to automate UI testing for Apple Contacts App.
cover-img: https://images.unsplash.com/photo-1611120159972-050e0fbb7ab4
tags: [android, ios, ui-automation, blackbox-testing]
---

In this tutorial, I use `Maestro` to automate UI testing for [Contacts](https://apps.apple.com/us/app/contacts/id1069512615) app.


### Overview 

#### Setup

- Installed [Xcode](https://apps.apple.com/vn/app/xcode/id497799835)
- Installed [Facebook IDB](https://fbidb.io/) tool


#### Test step
- Step 1: Open Contacts app 

- Step 2: In home screen, click row `John Appleseed`, open Contact screen detail screen

<img width=200 src="/assets/img/maestro/ios_step_1.png" />

- Step 3: In contact screen detail , click button `Edit` , change to edit contact screen detail screen

<img width=200 src="/assets/img/maestro/ios_step_2.png" />


- Step 4: In edit contact screen detail screen, [1] click button `add phone`, [2] add input random phone number and [3] click button `Done` ,  change to  Contact screen detail screen

<img width=200 src="/assets/img/maestro/ios_step_3.png" />

<img width=200 src="/assets/img/maestro/ios_step_4.png" />


- Step 5: In Contact screen detail screen, verify `message` text display on this creen  

<img width=200 src="/assets/img/maestro/ios_step_5.png" />





#### Device ID for simulator iPhone

- Open simulator

```
open -a Simulator.app
```

- View UDIDs 

```
xcrun simctl list 'devices' 'booted'

```

<img width="500" src="https://user-images.githubusercontent.com/3994863/195757146-8657716b-1d00-4673-b039-2a5355f79be2.png">

- Run idb

```
idb_companion --udid <your_udids>

```


#### Excute

Run on terminal `maestro test flow_contacts_ios.yaml`


```yaml
# maestro test flow_contacts_ios.yaml
appId: com.apple.MobileAddressBook
---
# Step 1
- launchApp
# Step 2
- tapOn: "John Appleseed"
# Step 3
- tapOn: "Edit"
# Step 4.1
- tapOn: "Add phone"
# Step 4.2
- inputRandomNumber
# Step 4.3
- tapOn: "Done"
# Step 5
- assertVisible: "message"
```


#### Test record 
Video test record (x4)

<video width="500" controls>
  <source src="https://user-images.githubusercontent.com/3994863/195583400-b851e681-8ef1-45fd-b814-83fca24a7099.mov" type="video/mp4">
</video>


### Tip 

Get iOS App Bundle ID

- Step 1: Find Application ID 

With [Contacts](https://apps.apple.com/us/app/contacts/id1069512615) app has Application ID is: `1069512615`

`https://apps.apple.com/us/app/contacts/id1069512615`

- Step 2: Download App info 

```
https://itunes.apple.com/lookup?id=<application_id>&country=us

```

With [Contacts](https://apps.apple.com/us/app/contacts/id1069512615) app

`https://itunes.apple.com/lookup?id=1069512615&country=us`


- Step 3: Open file the file downloadled and search  `bundleId`

The value of `bundleId` is App Bundle ID


With [Contacts](https://apps.apple.com/us/app/contacts/id1069512615) app


<img width="500"  src="https://user-images.githubusercontent.com/3994863/195777032-e92b517f-8c07-4d73-991f-83659e059c26.png">

```json
{
 "resultCount":1,
 "results": [
{
"screenshotUrls":["https://is5-ssl.mzstatic.com/image/thumb/Purple125/v4/98/3f/24/983f24ca-0bc1-c37c-f94d-9d7e22cce500/pr_source.png/392x696bb.png", "https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/90/23/9d/90239d5d-0c3e-ac2c-2321-dcd062af3702/pr_source.png/392x696bb.png"], "ipadScreenshotUrls":["https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/6b/2e/10/6b2e105a-f9a5-d74f-d6ac-ca97db5e3c53/pr_source.png/576x768bb.png"], "appletvScreenshotUrls":[], 
"artworkUrl60":"https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/6f/72/1f/6f721f76-4794-847f-53aa-0a8ef481d6e7/AppIcon-0-0-1x_U007emarketing-0-0-0-10-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/60x60bb.jpg", 
"artworkUrl512":"https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/6f/72/1f/6f721f76-4794-847f-53aa-0a8ef481d6e7/AppIcon-0-0-1x_U007emarketing-0-0-0-10-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg", 
"artworkUrl100":"https://is3-ssl.mzstatic.com/image/thumb/Purple115/v4/6f/72/1f/6f721f76-4794-847f-53aa-0a8ef481d6e7/AppIcon-0-0-1x_U007emarketing-0-0-0-10-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/100x100bb.jpg", "artistViewUrl":"https://apps.apple.com/us/developer/apple/id284417353?mt=12&uo=4", "isGameCenterEnabled":false, 
"supportedDevices":["iPhone5-iPhone5", "iPadFourthGen-iPadFourthGen", "iPadFourthGen4G-iPadFourthGen4G", "iPhone5c-iPhone5c", "iPhone5s-iPhone5s", "iPadAir-iPadAir", "iPadAirCellular-iPadAirCellular", "iPadMiniRetina-iPadMiniRetina", "iPadMiniRetinaCellular-iPadMiniRetinaCellular", "iPhone6-iPhone6", "iPhone6Plus-iPhone6Plus", "iPadAir2-iPadAir2", "iPadAir2Cellular-iPadAir2Cellular", "iPadMini3-iPadMini3", "iPadMini3Cellular-iPadMini3Cellular", "iPodTouchSixthGen-iPodTouchSixthGen", "iPhone6s-iPhone6s", "iPhone6sPlus-iPhone6sPlus", "iPadMini4-iPadMini4", "iPadMini4Cellular-iPadMini4Cellular", "iPadPro-iPadPro", "iPadProCellular-iPadProCellular", "iPadPro97-iPadPro97", "iPadPro97Cellular-iPadPro97Cellular", "iPhoneSE-iPhoneSE", "iPhone7-iPhone7", "iPhone7Plus-iPhone7Plus", "iPad611-iPad611", "iPad612-iPad612", "iPad71-iPad71", "iPad72-iPad72", "iPad73-iPad73", "iPad74-iPad74", "iPhone8-iPhone8", "iPhone8Plus-iPhone8Plus", "iPhoneX-iPhoneX", "iPad75-iPad75", "iPad76-iPad76", "iPhoneXS-iPhoneXS", "iPhoneXSMax-iPhoneXSMax", "iPhoneXR-iPhoneXR", "iPad812-iPad812", "iPad834-iPad834", "iPad856-iPad856", "iPad878-iPad878", "Watch4-Watch4", "iPadMini5-iPadMini5", "iPadMini5Cellular-iPadMini5Cellular", "iPadAir3-iPadAir3", "iPadAir3Cellular-iPadAir3Cellular", "iPodTouchSeventhGen-iPodTouchSeventhGen", "iPhone11-iPhone11", "iPhone11Pro-iPhone11Pro", "iPadSeventhGen-iPadSeventhGen", "iPadSeventhGenCellular-iPadSeventhGenCellular", "iPhone11ProMax-iPhone11ProMax", "iPhoneSESecondGen-iPhoneSESecondGen", "iPadProSecondGen-iPadProSecondGen", "iPadProSecondGenCellular-iPadProSecondGenCellular", "iPadProFourthGen-iPadProFourthGen", "iPadProFourthGenCellular-iPadProFourthGenCellular", "iPhone12Mini-iPhone12Mini", "iPhone12-iPhone12", "iPhone12Pro-iPhone12Pro", "iPhone12ProMax-iPhone12ProMax", "iPadAir4-iPadAir4", "iPadAir4Cellular-iPadAir4Cellular", "iPadEighthGen-iPadEighthGen", "iPadEighthGenCellular-iPadEighthGenCellular", "iPadProThirdGen-iPadProThirdGen", "iPadProThirdGenCellular-iPadProThirdGenCellular", "iPadProFifthGen-iPadProFifthGen", "iPadProFifthGenCellular-iPadProFifthGenCellular", "iPhone13Pro-iPhone13Pro", "iPhone13ProMax-iPhone13ProMax", "iPhone13Mini-iPhone13Mini", "iPhone13-iPhone13", "iPadMiniSixthGen-iPadMiniSixthGen", "iPadMiniSixthGenCellular-iPadMiniSixthGenCellular", "iPadNinthGen-iPadNinthGen", "iPadNinthGenCellular-iPadNinthGenCellular", "iPhoneSEThirdGen-iPhoneSEThirdGen", "iPadAirFifthGen-iPadAirFifthGen", "iPadAirFifthGenCellular-iPadAirFifthGenCellular", "iPhone14-iPhone14", "iPhone14Plus-iPhone14Plus", "iPhone14Pro-iPhone14Pro", "iPhone14ProMax-iPhone14ProMax"], "features":["iosUniversal"], "advisories":[], "kind":"software", "currency":"USD", "minimumOsVersion":"10.0", "trackCensoredName":"Contacts", 
"languageCodesISO2A":["AR", "CA", "HR", "CS", "DA", "NL", "EN", "FI", "FR", "DE", "EL", "HE", "HI", "HU", "ID", "IT", "JA", "KO", "MS", "NB", "PL", "PT", "RO", "RU", "ZH", "SK", "ES", "SV", "TH", "ZH", "TR", "UK", "VI"], "fileSizeBytes":"1579008", "formattedPrice":"Free", "contentAdvisoryRating":"4+", "averageUserRatingForCurrentVersion":3.351059999999999927666749499621801078319549560546875, "userRatingCountForCurrentVersion":1279, "averageUserRating":3.351059999999999927666749499621801078319549560546875, "trackViewUrl":"https://apps.apple.com/us/app/contacts/id1069512615?uo=4", "trackContentRating":"4+", "currentVersionReleaseDate":"2021-09-20T17:40:09Z", "releaseNotes":"Bug Fixes and Feature Enhancements", "artistId":284417353, "artistName":"Apple", "genres":["Utilities"], "price":0.00, "releaseDate":"2016-05-26T21:15:49Z", "trackId":1069512615, "trackName":"Contacts", 
"description":"Access and edit your contacts from personal, business, and other accounts with the Contacts app.\n\nFeatures:\n\n• Add contacts manually. Or sync them from iCloud, Gmail, Exchange, or your Mac or PC.\n\n• Customize contact cards to quickly reach people in the ways you communicate with them most.\n\n• Tap information, such as an address or phone number, to open the corresponding app.\n\n• Create a “My Card” — located at the top of your Contacts list — to make accessing your own information easy.\n\n• Tap the search field at the top of the Contacts list to find a contact.\n\n• Create Favorites to quickly access key people in the Phone app.\n\n• Create custom labels for contact information.\n\n\nApple Watch Features:\n\n• The Contacts app on Apple Watch lets you create new contacts, as well as customize existing contacts right on your wrist.\n\n• You can also select people from your contact cards to use as a complication on your watch face for easy access.\n\n• You can now quickly share a contact card to your friends or family right from your wrist. \n\n• You choose the way in which you would like to communicate with your contact via phone, mail, text message right from your wrist.", "bundleId":"com.apple.MobileAddressBook", "sellerName":"Apple Inc.", "primaryGenreName":"Utilities", "primaryGenreId":6002, "genreIds":["6002"], "isVppDeviceBasedLicensingEnabled":true, "version":"1.3.6", "wrapperType":"software", "userRatingCount":1279}]
}

```

### Note


[Part 1, Use Maestro to automate UI testing for Dream by WOMBO app.](https://ttpho.github.io/2022-09-25-maestro/)

[Part 2, Use Maestro to automate UI testing for Apple Contacts App.](https://ttpho.github.io/2022-10-14-maestro-ios/)

Supported by [DartJ](https://dartj.web.app/)

[Cover Photo](https://unsplash.com/photos/6ZGnuKXJjQY)

