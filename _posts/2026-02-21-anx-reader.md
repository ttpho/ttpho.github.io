---
layout: post
title: "Anx Reader"
subtitle: "Trình đọc sách điện tử đa nền tảng nguồn mở tích hợp AI và đồng bộ WebDAV."
tags: [github]
---

## Giới thiệu

Anx Reader là một ứng dụng đọc sách điện tử (e-book reader) mã nguồn mở được phát triển bằng Flutter. Dự án này giải quyết vấn đề phân mảnh trong trải nghiệm đọc sách kỹ thuật số bằng cách cung cấp một giao diện thống nhất, hiện đại trên mọi nền tảng (Android, iOS, Windows, macOS, Linux). Điểm khác biệt lớn nhất của Anx Reader so với các ứng dụng truyền thống là khả năng tích hợp trí tuệ nhân tạo (AI) để hỗ trợ người đọc tóm tắt nội dung, dịch thuật và tra cứu ngữ nghĩa ngay trong lúc đọc, đồng thời hỗ trợ đồng bộ dữ liệu đám mây qua giao thức WebDAV giúp bạn đọc tiếp mạch lạc khi chuyển đổi giữa điện thoại và máy tính.

## Tính năng chính

- **Hỗ trợ đa định dạng:** Đọc mượt mà các định dạng phổ biến như EPUB, MOBI, AZW3, FB2, PDF và TXT.
- **Tích hợp AI mạnh mẽ:** Sử dụng các mô hình ngôn ngữ lớn (OpenAI, Gemini, Claude, DeepSeek) để tóm tắt sách, giải thích từ vựng, dịch thuật đoạn văn và tạo bản đồ tư duy (mind map).
- **Đồng bộ đa nền tảng:** Tự động đồng bộ sách, tiến độ đọc, ghi chú (notes) và highlights giữa các thiết bị thông qua WebDAV (Nextcloud, Google Drive, v.v.).
- **Thống kê đọc sách:** Cung cấp biểu đồ nhiệt (heatmap) và báo cáo chi tiết về thời gian đọc theo ngày, tuần, tháng, năm.
- **Tùy biến cao:** Điều chỉnh font chữ, khoảng cách dòng, lề, theme (Sáng/Tối/Sepia), và hỗ trợ Text-to-Speech (chuyển văn bản thành giọng nói).

## Hướng dẫn cài đặt Local (macOS)

Bạn có thể tải file `.dmg` trực tiếp từ mục Releases trên GitHub. Nếu muốn tự build từ source để phát triển, hãy làm theo các bước sau:

1. **Cài đặt Flutter SDK:**
   Đảm bảo bạn đã cài đặt Flutter và CocoaPods. Nếu chưa, dùng Homebrew:
   ```bash
   brew install --cask flutter
   brew install cocoapods
   ```

2. **Clone repository:**
   ```bash
   git clone https://github.com/Anxcye/anx-reader.git
   cd anx-reader
   ```

3. **Cài đặt dependencies:**
   ```bash
   flutter pub get
   ```

4. **Generate code (Quan trọng):**
   Dự án sử dụng code generation cho đa ngôn ngữ và Riverpod state management:
   ```bash
   flutter gen-l10n
   dart run build_runner build --delete-conflicting-outputs
   ```

5. **Chạy ứng dụng:**
   ```bash
   flutter run -d macos
   ```

## Hướng dẫn Docker

Vì Anx Reader là ứng dụng Client (Mobile/Desktop), Docker thường không được dùng để chạy ứng dụng trực tiếp cho người dùng cuối. Tuy nhiên, bạn có thể sử dụng Docker để build phiên bản Web của ứng dụng. Dưới đây là một `Dockerfile` mẫu để build Anx Reader cho Web:

```dockerfile
# Stage 1: Build Flutter Web
FROM ghcr.io/cirruslabs/flutter:stable AS build

WORKDIR /app
COPY . .

# Cài đặt dependencies và generate code
RUN flutter pub get
RUN flutter gen-l10n
RUN dart run build_runner build --delete-conflicting-outputs

# Build web release
RUN flutter build web --release

# Stage 2: Serve với Nginx
FROM nginx:alpine
COPY --from=build /app/build/web /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Cách chạy:**
```bash
docker build -t anx-reader-web .
docker run -p 8080:80 anx-reader-web
```
Truy cập `http://localhost:8080` để trải nghiệm (lưu ý: tính năng có thể hạn chế so với bản native).

## Ví dụ Code (Example Code)

Dưới đây là ví dụ minh họa cách cấu hình WebDAV trong ứng dụng (thường nhập qua giao diện UI, nhưng đây là cấu trúc dữ liệu JSON mô phỏng cấu hình bạn cần chuẩn bị):

```json
{
  "webdav_config": {
    "url": "https://webdav.your-cloud-provider.com/remote.php/webdav/",
    "username": "your_username",
    "password": "your_app_password",
    "sync_folder": "/AnxReader/Data",
    "sync_interval_minutes": 15,
    "sync_items": [
      "reading_progress",
      "highlights",
      "notes",
      "book_files"
    ]
  },
  "ai_config": {
    "provider": "openai",
    "api_key": "sk-proj-xxxxxxxx...",
    "model": "gpt-4o-mini",
    "prompt_template": "Summarize the following text in Vietnamese:"
  }
}
```

*Lưu ý: Trong ứng dụng thực tế, bạn sẽ nhập các thông số này vào mục **Settings > Sync** và **Settings > AI**.*

### Sources
- [sourceforge.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-O-Y6kGaQmjJ9wg9zNWIUi1jC8YPBjkPjBgfYsAnLbQMLjwqxROYbeU_WOYs34ZpnwJHWx16xbmfrlcQp1t0MB_mpNAUWi0lkFhEZ0ziFedlUu2cOnr8kYmkfniEEv0XbRvbz1a91nEP4MZMIbw==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy2U1sYQRIe9wGKbjv0Q11R9rT4oIfvHWMNNwMJd0CwMFXRiu-u39yf4F-YxBf6lVfBrrZIBs7Pw-Trvq17_Xz6Kzs_9XjJOtUY2VwXpUosQ0rUr-5SiwAqZeIEvigRA==)
- [hellogithub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFH_R9zr3rffwVaCrSWvVT2OP_U16wR8t_rvWjqqL7ge_YAxlxlmJCFVEU3iP08covalmeri_AcB3T9pLpqlErPV9-uOh5AbIQcliqJGdLsPVkyzIWKLN1TZtRYuYvV6NR_9XaC75a2HzB1SdcgmbSdzLR3HduUnO87uHPKPFESNe8=)
- [anxcye.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHOKXfrzaAh8vT9KDYynnzaBCKsTT04E3CLMomSWHKTogaPbc8XvSp-agVtiwAjGC2O7qcKQMg0NOKHyNqWRGJ4yu8OrgHsxx6lEP7jA7vGIKxcxvJCA==)
- [newreleases.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5amUyZbhqnESehDT1v6gh9q0ZI77DHRztOWSwg0FFEAh7OgVhm9GJE-UpjNApg_gGT_fhC2HKMyyKF1Haj96R9-clI_94_7XoXkHnmDOq6MNCa03miULed6AyisUiped7a7IApyxr3XVz4rU-br0pqY-pKl5SNb-hcgtrtFFQhfaVksD6Ip8=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7Zs3u0eo8JUGgX1cxjf1D3Liqt4JyMkEkdT-HHzqomaAMBeNSoRVS7GLGCoRs75LhE0RymEPpwzYsUaLOy2j5KL7SnNZ2_nozC_hw7oYu_vtwW7dETswEqj7hR7cDg6RVYwJPyU-CzA==)
- [anxcye.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwhUAaKyY6X8SS8CtLgd7rdxiUmF1Nzvfvcq3oVkvwBY6uRvX3nmn_W5R0HD5aoDBKDgigZxzaFf0j8lZ8lrvIZMuikPLftfq2QPYet0Ii05On)
- [apple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmFZH1yQqIgy0kAoTLd04o7NdVm7sr1f0YiFPo9uUFqoshPvrt3bdXBnyYkcVg82hnHMIUiGaeSLlXNgATkYk_twsB2SZhxM7aV4Ip8RLHoia_Mp66HbzXgWkmFYrKeXYdiJko3WYamnVXCFA1C2fT)
- [apple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-cqXdhD6SAsVfkjdN2OX_eiL7OhZXvVFf4Zd_SFPCLNIdfbFe_Li73vGS3uwehz3nlUCdfX_D8M71o16He144geg-WvMs2mvl6KdGkcoaOZ6i7P329myjTVoPjw1GpqURJBegoCClVy8GTR2AM41o)
- [newreleases.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAVMvcoKznmRDO-Vfej52oZ5PWvCGd6cWWDg8bl_N2vIPMKw4hhjxo_4rADSgC4rEWRO0FaKPRSe9CLaj_LV1lviXWgpZsvybvv5LZMXS5p6NvzsP78M33CVuedz2yVdgCkGCCNpKsiPBSv37elN3oZDcLtjypOv0D-3kLdQrGF17FKP-PXi7WHg==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELbl5of6O2yz4SB0O_AfE_NYM0mdWllLH84QlpLh-h-dx1zuLswUXI0YYbyb24akwve4cloAx-OJQXSbUALJII4XeJ2yVbJNeIWhoHZxbfAC5jpmu8tTs2mRJr4KvJ_0WzWaiXtVlTbw==)
- [mgks.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo4Gk8u-fEYRQ23DvIPz8kEAVb5JAOnl3g5COrUjhHu1UZ8ifKrSHEOLWa94nqfLsNWVJxUFvz0QuBwa71YSp1E_3DyCyIjNB2HH4yzaq2UoQ0Nef0Od0t8f_qnfeMhV-KX3kxmI1HKCSRNZh2YcDINARg)


### Github Page 

https://github.com/Anxcye/anx-reader

