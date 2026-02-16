---
layout: post
title: "aithing (AI Thing)"
subtitle: "Công cụ tự động hóa AI cục bộ, ưu tiên quyền riêng tư cho macOS, giúp quản lý các tác vụ phức tạp thông qua hệ thống Agents đa năng."
tags: [github]
---

## Giới thiệu

Aithing (AI Thing) là một ứng dụng native trên macOS được thiết kế để chạy các tác nhân AI (AI Agents) một cách tự động và bảo mật ngay trên máy tính của bạn. Vấn đề chính mà aithing giải quyết là sự phụ thuộc vào các nền tảng đám mây đắt đỏ và lo ngại về quyền riêng tư dữ liệu. Với aithing, mọi cuộc hội thoại, tệp tin và API key đều được lưu trữ cục bộ (Local). Ứng dụng này hoạt động như một "nhạc trưởng", cho phép bạn kết nối các mô hình AI mạnh mẽ (như Claude, GPT-4) với các công cụ làm việc hàng ngày (GitHub, Notion, Google Workspace) để tự động hóa các quy trình công việc phức tạp, chạy nền (background automation) mà không làm gián đoạn công việc chính của bạn.

## Tính năng chính

- **Privacy First (Ưu tiên quyền riêng tư):** Dữ liệu, lịch sử chat và API keys được lưu trữ hoàn toàn trên máy cá nhân, không gửi về máy chủ trung gian.
- **BYOK (Bring Your Own Keys):** Hỗ trợ sử dụng API key cá nhân từ các nhà cung cấp lớn như Anthropic, OpenAI và Gemini.
- **Model Context Protocol (MCP):** Hỗ trợ chuẩn kết nối MCP, cho phép tích hợp các công cụ (tools) và server MCP (remote hoặc local) để mở rộng khả năng của AI.
- **Đa Agents (Multiple Agents):** Kết nối và điều phối nhiều Agent chuyên biệt như GitHub Agent, Notion Agent, v.v. trong cùng một luồng làm việc.
- **Tự động hóa chạy nền:** Thiết lập các tác vụ định kỳ hoặc một lần để AI tự động thực hiện mà không cần người dùng giám sát.
- **Model Switching:** Chuyển đổi linh hoạt giữa các mô hình AI khác nhau ngay trong một cuộc hội thoại.

## Hướng dẫn cài đặt Local (macOS)

Vì đây là ứng dụng native cho macOS (viết bằng Swift), bạn có hai cách để cài đặt:

**Cách 1: Tải bản Release (Khuyên dùng cho người dùng phổ thông)**
1. Truy cập trang [Releases](https://github.com/thisisnsh/aithing/releases) của repository.
2. Tải xuống file `.dmg` hoặc `.zip` mới nhất.
3. Mở file và kéo ứng dụng vào thư mục `Applications`.

**Cách 2: Build từ Source (Cho lập trình viên)**
1. Cài đặt **Xcode** từ Mac App Store (yêu cầu macOS phiên bản mới nhất).
2. Mở Terminal và clone repository:
   ```bash
   git clone https://github.com/thisisnsh/aithing.git
   cd aithing
   ```
3. Mở project bằng Xcode:
   ```bash
   open Package.swift
   # Hoặc mở file .xcodeproj nếu có
   ```
4. Đợi Xcode tải các dependencies (Swift Package Manager).
5. Chọn Target là `aithing` và nhấn nút **Run** (biểu tượng Play) hoặc phím tắt `Cmd + R` để build và chạy ứng dụng.

## Hướng dẫn Docker (MCP Server)

Bản thân ứng dụng `aithing` là phần mềm macOS GUI nên không chạy trong Docker. Tuy nhiên, bạn có thể sử dụng Docker để chạy các **MCP Server** (các công cụ mở rộng cho aithing). Dưới đây là cách tạo một MCP Server đơn giản bằng Python để `aithing` có thể kết nối:

**1. Tạo file `Dockerfile`:**
```dockerfile
# Sử dụng Python slim image
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt thư viện mcp (Model Context Protocol)
RUN pip install mcp

# Copy source code server vào container
COPY server.py .

# Expose port (nếu dùng SSE) hoặc dùng stdio
CMD ["python", "server.py"]
```

**2. Build và Run Docker Image:**
```bash
# Build image
docker build -t my-mcp-server .

# Run container (Ví dụ chạy chế độ stdio qua pipe hoặc SSE server)
# Lưu ý: Aithing thường kết nối qua stdio hoặc SSE URL.
docker run -i --rm my-mcp-server
```
Sau đó, trong cấu hình của `aithing`, bạn thêm cấu hình để kết nối đến container này (thông qua lệnh `docker run` trong phần cấu hình MCP command).

## Ví dụ Code (MCP Server Configuration)

Để mở rộng khả năng của `aithing`, bạn thường sẽ cấu hình một file JSON để kết nối với các MCP Server. Dưới đây là ví dụ cấu hình để kết nối `aithing` với một server SQLite cục bộ (giả lập cách aithing "nói chuyện" với công cụ bên ngoài):

```json
{
  "mcpServers": {
    "sqlite-db": {
      "command": "uvx",
      "args": [
        "mcp-server-sqlite",
        "--db-path",
        "/Users/username/my-data.db"
      ],
      "env": {
        "PATH": "/usr/local/bin:/usr/bin"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Documents/Project"
      ]
    }
  }
}
```

*Đoạn cấu hình trên (thường đặt trong file config của ứng dụng hoặc settings) cho phép Agent trong aithing truy cập trực tiếp vào cơ sở dữ liệu SQLite và thư mục dự án của bạn để đọc/ghi file.*

### Sources
- [lobehub.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZQwr_Hnq9jr6L0UqD2QZMb_gH5cLbPCD1cCllUkpe_k1dUStU1a5_Jtjt_jlSfnaYIjm4IfXyCxx_neaBj7JoYYlwygYmrl_AzdRy-B509jmXq8T_pi7UdUVC2wV2T41InZq1-sXuWPi35ozEC_5HYVJEyg==)
- [backslash.security](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIL265cEgL2bhU0W9nv7rdtVk2-OnS2NtTkb-iR1bfqtyI-M5CjW1o9PgO9vMflIxra_whmOhekk7e7tGh9NqsVCSkdTAfVUjG-p9_7GsePiZ7tRNq1eJAsAwHW5jGVenoK8eb6YxnDTr_Bt2pUYjnCtS_xXWh1vxvydgZF0ZOhkw=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP0hA3UvVEaSM1RmxMoIJuQHEpuYUhRU6vW8vwSBx0QB6ugXarqIczvjKt2RucrU_ebLgvfpGCSBW-b3ibQLwtUPcb3BTR9eP1lVoZWHktqU9Qr51qmh9-YaGZ4WE3bCq2Z1ciXyOZjUGqxAJppwfahpjRb5L2FfcjsBa4eNtNiMiBfdYfOepYwHrfb-zj_h2RKWSxGEWbmaM=)
- [docker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7o2OjjK0dcpaMWv5EVpdPHsnWqlT4a02kM6JWSu_fhhesEBPtio7RVUwi2KUNvUxelTwWup2wXNCtD3KHDUYhORlvhYRAFpz82BWsD9tl7rAIRaESTbEUnH9FBfQJu2IKGOxbrE_WSDAn1pWEcMIQcU1fKfAyW9ILzAhJznI=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPdW3Gu40thd_X1UTH2XQziZlSvGnIY8j83T7wGtppN4lul63dAqM16WfkkhezKQt8LT3jK1nvMlv1UCZ3q1hFpLoqY8ZaTaNBq4_dnMEq7rlUxbEuw4T0kojH7d7OiBLg4IxJBHDUCOk-AW2KhMFkom6O_TonM_hoR4vueTmOuOq-fPKUkuOab7ABq9AlXTKm1qLGZiKCseeBYA53tlUT4NT0xlYx9I7orQ==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSX77KjYV4bSvyVKMBl3sQOm1Nfv9OAZZlBLSA8gcfVZ7qg6To3C8oLAV8O-McdDR5xSvfAykYe9sIM5waiiAFcNnoGzAL-hgRdKZykrC1It3YPzYBGQcme34k538aZ6qVlQArtZx9Z0Y=)
- [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlfs5WHsECDpEgqqXSG0-cPIW_31aCQ_ef55xSMCziKsKxDM4Z6ZVHqa0OomdmRkNoHa0br_bDtc8mfJytv5mzUr-jNCApwCFYkp3G6HOIKVOvvQHVsdC9y21yrMlz9kKq-1BXjLDAnobnXA9nNu3MlBgDkqWSHfDElYpyvZJqGSfFPg==)
- [docker.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4F4qlKnCBd5h_GuPCS8aCD0x4tpUU1gCIh7AuV-BvjHNLkV3rAaWj7jtuveOM80eMdAwzq300ZOVHL4cstIBQoGd9TZwcIrrkgWLdkhJhcrK5lfJHeDPezLLdg5D3RLBtV5rcGlD7lCIWYTuhUEiSDCsRtzegeHHE_9M66g==)


### Github Page 

https://github.com/thisisnsh/aithing

