---
layout: post
title: "AutoFigure"
subtitle: "Hệ thống AI tự động tạo và tinh chỉnh hình minh họa khoa học chất lượng cao từ văn bản."
tags: [github]
---

## Giới thiệu

AutoFigure (phát triển bởi ResearAI) là một framework agentic tiên tiến được thiết kế để giải quyết bài toán tạo hình minh họa khoa học (scientific illustrations) - một công việc thường tốn nhiều thời gian và đòi hỏi kỹ năng thiết kế. Dự án này sử dụng Large Language Models (LLMs) để tự động chuyển đổi các mô tả văn bản dài hoặc nội dung phương pháp nghiên cứu (methodology) từ các bài báo khoa học thành các sơ đồ, biểu đồ vector (SVG/XML) đạt chuẩn xuất bản. Ứng dụng thực tế của AutoFigure bao gồm việc hỗ trợ các nhà nghiên cứu vẽ sơ đồ kiến trúc mô hình, lưu đồ thuật toán (flowcharts) và các hình ảnh minh họa phức tạp chỉ bằng các câu lệnh hoặc input từ file PDF.

## Tính năng chính

- **Text-to-Figure**: Tạo hình minh họa trực tiếp từ mô tả ngôn ngữ tự nhiên.
- **Paper-to-Figure**: Tự động trích xuất phần phương pháp (methodology) từ bài báo nghiên cứu và chuyển hóa thành sơ đồ trực quan.
- **Cơ chế Review-Refine**: Sử dụng hệ thống đa tác vụ (Dual-agent) gồm Generator (tạo hình) và Evaluator (đánh giá) để tự động tinh chỉnh hình ảnh qua nhiều vòng lặp nhằm đạt chất lượng tốt nhất.
- **Editable Output**: Xuất ra định dạng Vector (SVG) hoặc XML tương thích với draw.io (mxGraph), cho phép người dùng chỉnh sửa thủ công dễ dàng sau khi tạo.
- **Style Transfer (AutoFigure-Edit)**: Khả năng học theo phong cách thiết kế từ một hình ảnh tham chiếu.

## Hướng dẫn cài đặt Local (macOS)

Để cài đặt AutoFigure trên macOS, bạn cần có Python 3.10+ và git.

1. **Clone repository:**
   ```bash
   git clone https://github.com/ResearAI/AutoFigure.git
   cd AutoFigure
   ```

2. **Tạo môi trường ảo (Khuyến nghị dùng Conda):**
   ```bash
   conda create -n autofigure python=3.10
   conda activate autofigure
   ```

3. **Cài đặt dependencies:**
   ```bash
   pip install -e .
   ```

4. **Cài đặt Playwright (bắt buộc để render hình ảnh):**
   ```bash
   playwright install chromium
   ```

5. **Thiết lập biến môi trường:**
   Tạo file `.env` hoặc export trực tiếp API Key của LLM (ví dụ: OpenAI, Anthropic hoặc OpenRouter).
   ```bash
   export OPENAI_API_KEY="sk-proj-..."
   # Hoặc nếu dùng OpenRouter
   export GENERATION_API_KEY="sk-or-..."
   ```

## Hướng dẫn Docker

Hiện tại repository chưa cung cấp Dockerfile chính thức, dưới đây là file cấu hình Docker gợi ý để chạy project này:

1. **Tạo file `Dockerfile`:**
   ```dockerfile
   FROM python:3.10-slim

   WORKDIR /app

   # Cài đặt git và các thư viện hệ thống cần thiết
   RUN apt-get update && apt-get install -y git

   # Copy source code
   COPY . /app

   # Cài đặt dependencies
   RUN pip install --no-cache-dir -e .
   RUN pip install playwright
   
   # Cài đặt trình duyệt cho playwright
   RUN playwright install chromium --with-deps

   # Thiết lập biến môi trường (có thể override khi run)
   ENV OPENAI_API_KEY="your_key_here"

   CMD ["python", "server.py"]
   ```

2. **Build và Run:**
   ```bash
   docker build -t autofigure .
   docker run -p 8000:8000 --env-file .env autofigure
   ```

## Ví dụ Code (Example Code)

Dưới đây là đoạn code Python mẫu minh họa cách sử dụng `AutoFigureAgent` để tạo một sơ đồ từ văn bản:

```python
import os
from autofigure import AutoFigureAgent, Config

# 1. Cấu hình API Key (đảm bảo bạn đã có key từ OpenRouter hoặc OpenAI)
# Bạn có thể đặt trực tiếp hoặc lấy từ biến môi trường
config = Config(
    generation_api_key=os.getenv("OPENAI_API_KEY"),
    provider="openai" # hoặc "openrouter"
)

# 2. Khởi tạo Agent
agent = AutoFigureAgent(config)

# 3. Định nghĩa yêu cầu (Prompt)
prompt = """
Vẽ một sơ đồ quy trình (flowchart) mô tả kiến trúc Transformer.
Bao gồm: Input Embedding, Positional Encoding, Multi-Head Attention, và Feed Forward.
"""

# 4. Thực thi tạo hình
# Kết quả sẽ trả về đường dẫn file hoặc nội dung SVG/XML
try:
    result = agent.generate(description=prompt)
    print("Đã tạo hình thành công:", result)
except Exception as e:
    print("Lỗi khi tạo hình:", e)
```

### Sources
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv0kwHks0R8MsywmJHSYTnXGef29P99O_woKyx6HAzyp6HZkphd-BhZq9UaHnMTECTmvt1JYU7NhU151zjMN3-ZYt6tK6NTUwyYuseyr5-hFxx7qsKDEg-h3Soj44ElMTVG3xre_5gE0dUUYk3Ij2o60_I6MAE)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUYMeqwx7zc0mvoLlK5wlAghHU2VCDMOVh87DpA-2IJXFroe1sHPmaFxCPK7HIzc2ckIP-iNs9NCl33hMxH1D6PHFdBHd4YBOUg7ieRrAh4oumvZE0t6VzKqRYe7992bPQhlQ=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOqgrQYwh0ya2g_5ZDxlI2JOox5iFeqdWN-TZnRQX5louL8Kj_EAreLfrukVQ0M72OG9cNNYSGm4hi-lRLU3FS6hAUxCWF3zTFFlgfcSKJLMc7lE37M8IRCRa1XXt0Uz3e9_Vl8_E=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQUyTBzYuSWoCGLUB1RwOQFiaPPegAnatRIlXQzcG_T60RyycNAzX1k4JsMHmkgBzTY-54I7VBENq6Z9hJTtiKg19SADkhgRa7nHDNnpiefh5DF8IQszOxNsewL2c3YHzO)
- [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaTxRtjEeQLKUd1spsM-HtEhL-bYVESgA-V6HLGD45HCtT5o-WBOkwMOAYXxEAbn6uWlv42pR3RXyQZCDkDRoO3z37-jVAVLodd7pJ7080pPUToBMPw7nIsGeY4-2FHPUSEYxw3vkVdFWklqg60PQM11HDdatU_cYCxhYNEsmmBNvf504-WhsBQHuljKk1aDCaXpm0MES-Soi-pGGiMZrTMljhdxDnIdMgauUfpKu4nBFwJqa4WjOK_kEqwQ==)
- [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhxcp0pYsaOno3uF1YMaOUa9RiXCsfCODeO7peEIhBt0Yg216TkmdHmvDLMuU7YyHVEvbmTZ2BBTKpCdXm-58tXFUc9QPAFxYboncz4mg08FtrGvi2E60tQVLAYqqSZxB-H3-Agw==)


### Github Page 

https://github.com/ResearAI/AutoFigure

