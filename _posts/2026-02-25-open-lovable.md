---
layout: post
title: "Open Lovable"
subtitle: "Công cụ mã nguồn mở sử dụng AI để tạo ứng dụng React hoàn chỉnh từ mô tả văn bản hoặc sao chép giao diện từ bất kỳ website nào."
tags: [github]
---

## Giới thiệu

Open Lovable là một dự án mã nguồn mở được phát triển bởi đội ngũ Firecrawl, đóng vai trò là giải pháp thay thế miễn phí cho Lovable.dev. Repository này giải quyết vấn đề khởi tạo giao diện người dùng (Frontend) nhanh chóng bằng cách cho phép người dùng 'trò chuyện' với AI để xây dựng ứng dụng. Điểm đặc biệt nhất là khả năng sử dụng Firecrawl để quét (scrape) một website bất kỳ và biến nó thành code React/Next.js sạch, giúp các lập trình viên tiết kiệm hàng giờ code giao diện thủ công. Ứng dụng thực tế bao gồm việc tạo nhanh các bản mẫu (prototype), học hỏi cách xây dựng UI từ các trang web nổi tiếng, hoặc dựng khung sườn cho dự án mới.

## Tính năng chính

- **Website Cloning:** Nhập URL của bất kỳ trang web nào, hệ thống sẽ dùng Firecrawl để phân tích và AI sẽ viết lại code React tái tạo giao diện đó.
- **Chat-to-App:** Giao diện hội thoại cho phép bạn ra lệnh bằng ngôn ngữ tự nhiên (ví dụ: 'Thêm nút đăng nhập màu xanh', 'Sửa lại header') để chỉnh sửa ứng dụng theo thời gian thực.
- **Sandbox an toàn:** Tích hợp môi trường Sandbox (E2B hoặc Vercel) để chạy và xem trước code do AI tạo ra một cách an toàn, cô lập.
- **Hỗ trợ đa mô hình AI:** Tương thích với nhiều LLM mạnh mẽ như GPT-4o, Claude 3.5 Sonnet, Gemini, hoặc các model mã nguồn mở khác.
- **Tech Stack hiện đại:** Code được tạo ra sử dụng Next.js, React, Tailwind CSS và Shadcn UI, đảm bảo chất lượng và dễ bảo trì.

## Hướng dẫn cài đặt Local (macOS)

Để chạy Open Lovable trên macOS, bạn cần cài đặt sẵn Node.js (khuyên dùng bản LTS) và Git.

1. **Clone repository:**
   ```bash
   git clone https://github.com/firecrawl/open-lovable.git
   cd open-lovable
   ```

2. **Cài đặt dependencies:**
   Khuyên dùng pnpm để cài đặt nhanh hơn:
   ```bash
   npm install -g pnpm
   pnpm install
   ```

3. **Cấu hình biến môi trường:**
   Copy file mẫu và điền API Key:
   ```bash
   cp .env.example .env.local
   ```
   Mở file `.env.local` và điền các thông tin quan trọng:
   - `FIRECRAWL_API_KEY`: Lấy tại firecrawl.dev (để tính năng clone web hoạt động).
   - `OPENAI_API_KEY` (hoặc Anthropic/Gemini key): Để AI sinh code.
   - Cấu hình Sandbox (chọn E2B hoặc Vercel).

4. **Chạy ứng dụng:**
   ```bash
   pnpm dev
   ```
   Truy cập `http://localhost:3000` để bắt đầu sử dụng.

## Hướng dẫn Docker

Dự án hiện tại chưa cung cấp sẵn Dockerfile chính thức trong root, nhưng bạn có thể tạo một `Dockerfile` cơ bản cho ứng dụng Next.js như sau:

1. Tạo file `Dockerfile` trong thư mục gốc:
   ```dockerfile
   FROM node:18-alpine
   WORKDIR /app
   COPY package*.json ./
   RUN npm install
   COPY . .
   RUN npm run build
   EXPOSE 3000
   CMD ["npm", "start"]
   ```

2. Build Docker Image:
   ```bash
   docker build -t open-lovable .
   ```

3. Run Container (nhớ truyền file env):
   ```bash
   docker run -p 3000:3000 --env-file .env.local open-lovable
   ```

## Ví dụ Code (Cấu hình .env)

Phần quan trọng nhất để Open Lovable hoạt động là cấu hình đúng các API Key. Dưới đây là ví dụ nội dung file `.env.local` tiêu chuẩn:

```ini
# Cấu hình AI Provider (Ví dụ dùng OpenAI)
OPENAI_API_KEY="sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx"

# Cấu hình Firecrawl (Bắt buộc để clone website)
FIRECRAWL_API_KEY="fc-xxxxxxxxxxxxxxxxxxxxxxxx"

# Cấu hình Sandbox (Ví dụ dùng E2B - Khuyên dùng cho trải nghiệm tốt nhất)
SANDBOX_PROVIDER="e2b"
E2B_API_KEY="e2b_xxxxxxxxxxxxxxxxxxxxxxxx"

# Tùy chọn: Chọn model mặc định
NEXT_PUBLIC_DEFAULT_MODEL="gpt-4o"
```

### Sources
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpbEp7nRohKm00_LOLUP8LsEAjZm6hThZ-NC2-n1-FHC1TNlnMKAtynMhecmPTYgKQhoefqATAijT1_nRm2umoOr6CGHJ6MKfwcG9t9n6_bc-U4K7eYPpS9n2_lUKe7foc1f2I_7I=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5362Dnj8XucLpUveyhlVJtuA3ztJj_Q9SLrb9P5wvIFAI9TFrsmEUTcYa5ZzG5fzIlnP4Ps5oi_ZnIP6FmmXwBfcrL_MzVsKPVWFMRzuu7j_zjI78axv--8XsrAa7doN4U1nkaT7Ns27DYUMZIQ_-0DYG4udA3MQGpN94C8TSuHeiS1spvmCcSo43TE2L6d-p1utgHZ8H0aeZKAxVVoeg0Mg7yPV9)
- [mindplix.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI7E2yuHIZ0hwiejbmMx2gj_YHkXkFsBMyX_XO5FUE58fbdY21U9S4qJjmVo90_zmsEBHVXwAqoB_TfcRrnNDmE3TrOQXbKq-bdWGOvluhMH_Rn6jnkDrjAkN68VEtDsk_ilTPlbKBmv0=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVGqB8hMw-k0W_0Bbb-wuCKwJaYGPkHOTyGr7sE6VbqltYaymRRv-7pl4F1C8b_AKIXm4xFqJg8AanF5pD7EiR6c-t5ci42fjeHmc0f41YwPxiEtTUEACSLgYXUJxm3bJuIS-wUB9OjefGAus8usVUZfnb5YZYN_mDqybItloFSeAmLL6w_4Uqa_1BXxJxyrEzyL-bOxDGJo4UslagGx35lD56Ns_4th6wgmzYqZxNgTVjsU-AwkwAfrC_wW8=)
- [brightcoding.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxHESnGy8idoQA-MMMFO9-rbKgbbQQYo7e0D4xrZqRFwuxFszEHEX2NrDHdU-cuJHGCTulxMMBOaJVzuRl52m--FxTaTnpDZpod6QDQxr5BF8WKUVdcdnuKZKe_ukM9jCJjNpLDtobuK7qpQEenFY5401c-qUu221ScsuqBGOgdQXldu67qFaVxeeZ3DzJyn9iOKVBkcdQnSEomwhRGd-cKU33zxltrabfKkc8Ym0iVPcX-w==)
- [hexmos.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNtXcrbqL8Y0ApsXg1oZpqvUKa97Hj5fPFciTvCQtjQmUTur6atWsGqhjn7dWZ-e5PzoEk7526EwJ4ijI7tlmu0d4g3JFQlVv86vnN6cinTYqyqnNmP8u3SH9DsL8gvU8SRGUABOqbqMwyemuEdT15lgS080LKMnYKKpaPlZ-smDsncv0Hdg==)


### Github Page 

https://github.com/firecrawl/open-lovable

