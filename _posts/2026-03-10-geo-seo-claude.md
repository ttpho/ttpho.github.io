---
layout: post
title: "geo-seo-claude"
subtitle: "Công cụ Generative Engine Optimization (GEO) toàn diện tích hợp làm kỹ năng cho Claude Code."
tags: [github]
---

## Giới thiệu

Repository `geo-seo-claude` giải quyết bài toán chuyển dịch từ SEO truyền thống sang GEO (Generative Engine Optimization) [1.7]. Nó giúp tối ưu hóa khả năng hiển thị của website trên các công cụ tìm kiếm AI (như ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) thay vì chỉ nhắm vào Google crawler truyền thống. Ứng dụng thực tế: Công cụ này phân tích website qua các agent song song để đo lường điểm trích dẫn (citability score), kiểm tra quyền truy cập của bot, và cung cấp giải pháp để các marketer hoặc developer đón đầu lưu lượng truy cập từ AI.

## Tính năng chính

- Audit GEO toàn diện với 5 sub-agent chạy song song (AI Visibility, Platform Analysis, Technical SEO, Content Quality, Schema Markup).
- Chấm điểm trích dẫn (Citability scoring) để đánh giá mức độ nội dung sẵn sàng được AI tham chiếu.
- Kiểm tra quyền truy cập của các AI crawlers thông qua robots.txt.
- Phân tích và tạo file `llms.txt` chuẩn cho các LLM.
- Quét độ nhận diện thương hiệu (Brand authority) trên các nền tảng được AI trích dẫn.
- Phân tích và tạo dữ liệu cấu trúc (Schema markup).
- Tự động xuất báo cáo PDF trực quan kèm các biểu đồ điểm số.

## Hướng dẫn cài đặt Local (macOS)

Để chạy dự án trên macOS, yêu cầu hệ thống phải có Python 3.8+, Git và Claude Code CLI. Có thể cài đặt thêm Playwright (tuỳ chọn) để chụp ảnh màn hình.

**Cách 1: Cài đặt nhanh bằng một dòng lệnh**
Chạy lệnh sau trong Terminal:
`curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install.sh | bash`

**Cách 2: Cài đặt thủ công**
`git clone https://github.com/zubair-trabzada/geo-seo-claude.git`
`cd geo-seo-claude`
`./install.sh`

## Hướng dẫn Docker (nếu có)

Dự án được thiết kế làm kỹ năng (skill) chạy trực tiếp trong Claude Code CLI trên máy tính, nên không cung cấp sẵn `Dockerfile`. Nếu bạn muốn chạy cô lập bằng Docker, bạn có thể tự viết một `Dockerfile` cơ bản như sau:

```dockerfile
FROM python:3.10-slim
RUN apt-get update && apt-get install -y git curl npm
RUN npm install -g @anthropic-ai/claude-code
WORKDIR /app
RUN git clone https://github.com/zubair-trabzada/geo-seo-claude.git .
RUN bash ./install.sh
CMD ["/bin/bash"]
```
Cách chạy:
`docker build -t geo-seo-claude .`
`docker run -it geo-seo-claude`
Sau đó gõ `claude` để khởi động môi trường.

## Ví dụ Code (Example Code)

Do đây là công cụ tích hợp cho Claude Code, bạn sử dụng lệnh trực tiếp trong môi trường CLI của Claude thay vì viết code Python.
Mở Terminal, gõ `claude` để khởi động, sau đó sử dụng các lệnh sau:

```text
# Thực hiện một GEO + SEO audit toàn diện cho trang web
/geo audit https://example.com

# Đánh giá nhanh khả năng hiển thị trên AI trong 60 giây
/geo quick https://example.com

# Kiểm tra điểm số trích dẫn của nội dung đối với AI
/geo citability https://example.com

# Kiểm tra file robots.txt xem có chặn AI crawlers không
/geo crawlers https://example.com
```

### Sources
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHOJU4uWxifRWtupBV0MvIQZrwIC7Wb1uRnZj7YgUz0l0KnT_hsKlwFOr5LaW0kNHugnaOZRJNIihl5zmpnouvuv8u-hxWHU9qDj31EMwWXh88I_wXrZgj9YVuaQQ2o18XFl4XnyjqvJztaw==)
- [restless-brain.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8aizsbozKNjxJmQSKfnmuvh6JfVT_vxqgOYpvBK3EifLd4x2U8uTrq3Phq0MB4EsDkmCv0Kj1GZP8bGtBvuOYi9jbJReGDWklSLjnKAxCPYmRBdrB38zziGHng3Y0h9K2gvhZ4r-1c-dL0JzASQ2OrqdFMBOAA_TtzgUhieSkUmdcGwyd)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0E5Br3a2lQCzdxUzTqmaH_Ni-pIBZs1B-ch2JKIZxg7J2VPMbmvymCEdNbSS_mNH8PWpLDu7KSCzbJfEmwJhIXKvayhL2edUD2LpZ3pZr7F3Al-dF-YD0wk9eokwb7uTv2kA6RbLQNk0MMtnY_YGcveqoFQ==)


### Github Page 

https://github.com/zubair-trabzada/geo-seo-claude

