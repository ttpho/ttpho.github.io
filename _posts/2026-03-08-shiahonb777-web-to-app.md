---
layout: post
title: "shiahonb777/web-to-app"
subtitle: "Ứng dụng Android native giúp chuyển đổi bất kỳ URL trang web nào thành một ứng dụng Android độc lập với sự hỗ trợ của AI."
tags: [github]
---

## Giới thiệu

Repository shiahonb777/web-to-app cung cấp một ứng dụng Android gốc (native) cho phép người dùng chuyển đổi các URL trang web thành một ứng dụng Android (APK) độc lập [1.1]. Dự án này giải quyết bài toán đóng gói web app (như H5, React, Vue, Next.js) thành ứng dụng di động mà không yêu cầu kiến thức phức tạp về lập trình Android. Trong thực tế, bạn có thể ứng dụng dự án này để tạo các app phục vụ hệ thống nội bộ doanh nghiệp, công cụ hiển thị dạng kiosk, ứng dụng học tập cho trẻ em (kiểm soát thời gian), hoặc đơn giản là tạo app truy cập nhanh cho trang web yêu thích với tính năng chặn quảng cáo và bảo vệ quyền riêng tư.

## Tính năng chính

1. Website/Media/HTML to App: Hỗ trợ chuyển đổi URL, file media (ảnh/video), hoặc các project frontend thành app di động. 2. One-Click Build: Tự động build file APK độc lập trực tiếp trên điện thoại mà không cần sử dụng Android Studio. 3. Hỗ trợ AI: Tích hợp AI để hỗ trợ lập trình bằng ngôn ngữ tự nhiên và tự động thiết kế icon chuyên nghiệp. 4. Tiện ích mở rộng (Extension Modules): Cung cấp 10 module tích hợp sẵn và hơn 30 template cho phép tùy biến tính năng trang web như chặn quảng cáo hoặc ép giao diện tối. 5. Bảo mật nâng cao: Hỗ trợ mã hóa APK bằng thuật toán AES-256-GCM, giả mạo User-Agent, chặn quảng cáo ở cấp độ tên miền (domain-level hosts blocking) và cung cấp môi trường cách ly (multi-instance).

## Hướng dẫn cài đặt Local (macOS)

Do đây là dự án mã nguồn mở Android, việc chạy local trên macOS yêu cầu môi trường SDK của Android. Bước 1: Cài đặt trình quản lý gói Homebrew. Bước 2: Cài đặt Java JDK (ví dụ chạy lệnh: brew install --cask temurin). Bước 3: Cài đặt phần mềm Android Studio qua lệnh: brew install --cask android-studio. Bước 4: Thiết lập biến môi trường ANDROID_HOME trỏ về thư mục SDK trong file cấu hình .zshrc của bạn. Bước 5: Mở Terminal và clone mã nguồn bằng lệnh: git clone https://github.com/shiahonb777/web-to-app.git. Bước 6: Khởi động Android Studio, chọn Open và trỏ đến thư mục vừa clone, sau đó đợi Gradle đồng bộ hóa các thư viện phụ thuộc. Bước 7: Kết nối điện thoại thật qua USB hoặc khởi động máy ảo (Emulator), nhấn nút Run trong Android Studio để cài đặt app lên thiết bị.

## Hướng dẫn Docker (nếu có)

Vì đây là một dự án di động thuần túy, ứng dụng mặc định không cung cấp Dockerfile để chạy dịch vụ. Tuy nhiên, nếu bạn muốn dùng Docker để tự động hóa quá trình build file APK (CI/CD) trên macOS mà không cần cài Android Studio, bạn có thể tự viết một Dockerfile cơ bản như sau: Khai báo image với 'FROM mingc/android-build-box:latest'. Thiết lập thư mục làm việc 'WORKDIR /app'. Copy toàn bộ mã nguồn vào container 'COPY . .'. Cấp quyền thực thi cho Gradle 'RUN chmod +x ./gradlew'. Thiết lập lệnh build mặc định 'CMD ["./gradlew", "assembleDebug"]'. Để chạy, bạn dùng lệnh 'docker build -t web-to-app-builder .' và sau đó là 'docker run --rm -v $(pwd)/app/build/outputs/apk:/app/app/build/outputs/apk web-to-app-builder'. File APK thành phẩm sẽ xuất hiện trong thư mục app/build/outputs/apk của bạn.

## Ví dụ Code (Example Code)

Dự án cung cấp khả năng can thiệp vào trang web thông qua các Tiện ích mở rộng (Extension Modules) sử dụng mã JavaScript. Dưới đây là một đoạn mã JavaScript mẫu minh họa cách bạn có thể viết một module để ép buộc trang web hiển thị chế độ ban đêm (Dark Mode) khi chạy bên trong app: (function() { var style = document.createElement('style'); style.type = 'text/css'; style.innerHTML = 'body, html { background-color: #121212 !important; color: #ffffff !important; }'; document.head.appendChild(style); console.log('Chế độ Dark Mode đã được kích hoạt thành công qua Extension Module!'); })(); Bạn có thể chèn đoạn script này vào phần User Scripts của app để tự động áp dụng style cho mọi website được bọc thành ứng dụng.

### Sources
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGrTXtMiCzJ1G1kIBX7tbh_S0wjy19-_kL8Ggrr7lV9o6SScWrXHviwdF3Wt9O8Cum9Xkv-clOjX3MBPWkuZan8fALNzO0a_v313oMbq439McYdakjpfrYtV7KGEe_IK2WalIT)
- [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH69LtDUY-O_x9mELQMFpmFSc3_PXORdZR3C2CjxK0PkabFZmAb60zRn-7hRAJYBjLTekreZOUeG-mwSUhMioZvkgsMYajl_PA7mNu5REKfThuKernzXf-06zTJatbGO8hc5kvGujHBZCQ8MPEe_iK1EvsofTDYD0x0ibiF4YKePYxIVqu0CidH7XdXR5pInNCAmAGkjqMhwQDGekUnlSjegzU=)


### Github Page 

https://github.com/shiahonb777/web-to-app

