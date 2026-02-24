---
layout: post
title: "Anx Reader"
subtitle: "Trình đọc sách điện tử đa nền tảng tích hợp AI, hỗ trợ đồng bộ WebDAV và thống kê thói quen đọc chi tiết."
tags: [github]
---

## Giới thiệu

Anx Reader là một ứng dụng đọc sách điện tử (e-book reader) mã nguồn mở được phát triển bằng Flutter, giải quyết vấn đề phân mảnh trong trải nghiệm đọc sách kỹ thuật số. Nó không chỉ hỗ trợ nhiều định dạng sách phổ biến (EPUB, PDF, MOBI...) mà còn tích hợp các công nghệ AI hiện đại (OpenAI, Gemini, Claude) để hỗ trợ tóm tắt, dịch thuật và tra cứu ngữ cảnh ngay trong lúc đọc. Ứng dụng đặc biệt hữu ích cho những người yêu sách muốn có một công cụ 'all-in-one' để quản lý thư viện, đồng bộ hóa tiến trình đọc giữa các thiết bị (điện thoại, máy tính) và theo dõi thói quen đọc sách thông qua các biểu đồ trực quan.

## Tính năng chính

- **Hỗ trợ đa định dạng:** Đọc mượt mà các file EPUB, MOBI, AZW3, FB2, TXT và PDF.
- **Tích hợp AI mạnh mẽ:** Sử dụng AI để tóm tắt nội dung, dịch thuật song ngữ, tra cứu từ điển và tạo bản đồ tư duy (Mind map) cho sách.
- **Đồng bộ hóa đa nền tảng:** Sử dụng giao thức WebDAV để đồng bộ sách, ghi chú (notes), highlight và tiến trình đọc giữa Android, iOS, Windows và macOS.
- **Thống kê thói quen đọc:** Cung cấp biểu đồ nhiệt (heatmap) và báo cáo chi tiết về thời gian đọc theo tuần, tháng, năm.
- **Tùy biến cao:** Cho phép điều chỉnh font chữ, khoảng cách dòng, lề, chủ đề (Sáng/Tối/Sepia) và hỗ trợ Text-to-Speech (đọc to văn bản).
- **Ghi chú & Xuất dữ liệu:** Hệ thống ghi chú đa dạng, hỗ trợ xuất ra Markdown, TXT hoặc CSV.

## Hướng dẫn cài đặt Local (macOS)

Để chạy dự án trên macOS, bạn cần cài đặt môi trường phát triển Flutter. Các bước thực hiện:

1. **Cài đặt Prerequisites:**
   - Cài đặt Flutter SDK (khuyên dùng qua FVM hoặc Homebrew): `brew install --cask flutter`
   - Cài đặt Rust (cần thiết cho một số module): `brew install rust`
   - Cài đặt Xcode và CocoaPods (cho macOS/iOS build): `sudo gem install cocoapods`

2. **Clone Repository:**
   ```bash
   git clone https://github.com/Anxcye/anx-reader.git
   cd anx-reader
   ```

3. **Cài đặt Dependencies:**
   ```bash
   flutter pub get
   ```

4. **Generate Code (Localization & Riverpod):**
   Dự án sử dụng code generation cho đa ngôn ngữ và quản lý trạng thái:
   ```bash
   flutter gen-l10n
   dart run build_runner build --delete-conflicting-outputs
   ```

5. **Chạy ứng dụng:**
   ```bash
   flutter run -d macos
   ```

## Hướng dẫn Docker

Vì Anx Reader là một ứng dụng Client (Mobile/Desktop), Docker không được sử dụng để 'chạy' ứng dụng này theo cách thông thường như Web Server. Tuy nhiên, bạn có thể sử dụng Docker để tạo môi trường build chuẩn hóa (Build Environment) nhằm tránh lỗi môi trường.

Dưới đây là gợi ý `Dockerfile` cơ bản để thiết lập môi trường build cho Android/Web:

```dockerfile
# Sử dụng image Flutter chính thức
FROM ghcr.io/cirruslabs/flutter:stable

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file cấu hình dependency trước để tận dụng cache layer
COPY pubspec.yaml pubspec.lock ./

# Tải dependencies
RUN flutter pub get

# Copy toàn bộ source code
COPY . .

# Generate code cần thiết
RUN flutter gen-l10n && dart run build_runner build --delete-conflicting-outputs

# Lệnh mặc định: Build file APK cho Android (hoặc web)
CMD ["flutter", "build", "apk", "--release"]
```

Để chạy build: `docker build -t anx-builder . && docker run --rm -v $(pwd)/build:/app/build anx-builder`

## Ví dụ Code (Example Code)

Dưới đây là một đoạn script Bash tóm tắt quy trình tự động hóa việc cài đặt và chạy thử ứng dụng (thường dùng cho lần đầu setup):

```bash
#!/bin/bash

echo "🚀 Bắt đầu thiết lập Anx Reader..."

# 1. Kiểm tra Flutter
if ! command -v flutter &> /dev/null; then
    echo "❌ Flutter chưa được cài đặt. Vui lòng cài Flutter SDK trước."
    exit 1
fi

# 2. Cập nhật dependencies
echo "📦 Đang tải các thư viện..."
flutter pub get

# 3. Code Generation (Quan trọng)
echo "⚙️ Đang generate code (L10n & Riverpod)..."
flutter gen-l10n
dart run build_runner build --delete-conflicting-outputs

# 4. Chạy ứng dụng trên thiết bị đang kết nối hoặc giả lập
echo "▶️ Đang khởi chạy ứng dụng..."
flutter run
```

### Sources
- [sourceforge.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM_wkEFvXOjd_tKsxcW05eoJ3v1qkZLkfpsefuh_MK0lVznaVWwZ-xvx8jwnQQlRdo0Tq7tJpQnQngmSc174XcPpNfEvZeMfI60bJ4YdwwnoUPp6vSQs1x_6jpK5Y39uGi018W22DSCQQdja2zBw==)
- [apple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWHZXbUu99irG7PWpE-5qglSDi6apUZ7bj1xjxlTeHshjzKb35ZIE0aCP4cjuXyB9rUxjNWbbZqGmEy1tzQuLImOsPQI7oFWteINhIwrP3x5DeLlygOjiGUFdnQNTT63f2TUKuIb1gSRm7Jf2FJ9HH)
- [sevensquaretech.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvr_02EZadasvpIX22qVrlf01n-tXrL7zGVYmBOyWHJHYXTjknVV5tL1O2mv_dwu_8AcjydRRq1iWptSj9EssZjvKjpM8qkCyOOYOnjcPI9vuMExX3WhyGNGecem-muJNdkHCX7HVEtiu0uj0hSgYuUpoAho4AtHAyzxny6wvhMg==)
- [anxcye.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf8g6LGuuxLp7aF8q6zX9CdQRkz3CcI8VNdrMk7MaUxGnXoW6usYv4K_TcMa8nn2Lsbuw9hF6w862ZHxNhmG_1wTtVJRo6O71yX2NT_mVy8vqD9RxUFw==)
- [signpath.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtoJUTfHpE32uhABfIMKAiq2p4vkFR8MoKlrB_f2vFhsuN1J9cde1V7sGfrC9jhvQeCILz85KodDUUAGbsugywqEEwXGEyLiwKQO7JJ5vcQtS34myJFZBzsRv0atxEwjTQUlQE)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6-cm-XDdZEL_-NcHA8JYZC3Zh93GjtW5Isio7gkbhNrC4QGgmlVseFgHC146TJLTxQjMuLa-w3j_nRWBc9TbNQ318Yhp9xkWBrdV5IOGQxZAB9ceia20XRBwWnlVwgA==)
- [apple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3t0bsYCgnejJffI6oIS13CmGku7b2WsPZFnPlkXyFGxT0NvQ5pczH6rFq-8x7B-cfM16LgmGy-QIYcbiqr3ohr2UprVyZnpG4Yc9-z3OhQUMxbGm3igKSc51qyLm2AS0nCj9zzLY0KbZjn3_Z_CMl)
- [sourceforge.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoTpky1Qy-HPffDnYJX5XOpIt95KdO3alEtUYrRizABPYA78ptz8LLk4sMA7Lah7np6wqsXIDJ_Rv9SyIssFfuNwAKr9jcu-R6ZYAw3u0QqJREwBFtC8-o8RYn4B0jUE65I4pQYKpLsPkBunUyIQ==)
- [flutter.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENOgLvHgwHnn9E1zYL5xusmn-QRkbLGV8K5aXTFYcQiT5Gpe1WtiyjH1oM819bHjj5TnHN3Lxos_f82L8YmRI7DXNyg1liMVOfHWlrOqw4KSj7HH6v3j_ex6g9E419WurIOOLbyJXOadc7XCKg-lDPdxBNTfiR7O8VGcO2GDOGFPm3XIX5pu8=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF36cwx_GIL7Y8uVsI_cqx96okfHI9ivnAM3avf_CwcW0Ox5U2rbZm9zKpkxq1G2R8roS6qeh_dYyHuiK1MmDpoBfMr8WVwd3vukiu6mPwyeNeALRd4AGN-dq6B88qKdg==)
- [docker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGFQtDb1nYZ-nXIGI9AgTjDLwhq6jYZBy45hKFaJ_1IU8_YAE0_R6FAl8mU4QUIDTrvrs55xtgvTRIz3t09ACvtu3MogF13OQN0p0isxeZoFNr0py1XfCCs8OffCgouG_O6Kal0f4OtA==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2_5QxOdR1FlwYEBoH8t6XnKPckcEeLBgF1uNGeeVdVHdbahqpDTCnZLCUoUwipwEUMHsNipPOpetiokRaIaMTfra0fvIbnhcL93ekqyhn9pg8sVE=)


### Github Page 

https://github.com/Anxcye/anx-reader

