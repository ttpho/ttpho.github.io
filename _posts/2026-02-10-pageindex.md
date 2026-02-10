---
layout: post
title: "PageIndex"
subtitle: "Hệ thống RAG vectorless dựa trên tư duy lập luận (reasoning-based), giúp AI tra cứu tài liệu dài chính xác như chuyên gia."
tags: [github]
---

## Giới thiệu

**PageIndex** là một framework mã nguồn mở mang tính cách mạng trong lĩnh vực RAG (Retrieval-Augmented Generation). Khác với các hệ thống RAG truyền thống dựa vào Vector Database (cắt nhỏ văn bản và tìm kiếm tương đồng), PageIndex sử dụng phương pháp **"Vectorless, Reasoning-based"**. 

Nó giải quyết vấn đề lớn nhất của RAG hiện tại: **độ chính xác thấp khi xử lý các tài liệu dài và phức tạp** (như báo cáo tài chính, tài liệu pháp lý, sách kỹ thuật). Thay vì chỉ tìm kiếm từ khóa, PageIndex xây dựng một cấu trúc cây phân cấp (như mục lục sách) và cho phép LLM thực hiện "tư duy" để điều hướng qua các phần của tài liệu, mô phỏng cách con người đọc và tra cứu thông tin.

## Tính năng chính

- **Vectorless Retrieval:** Không cần Vector Database, loại bỏ sự phức tạp của việc quản lý embeddings.
- **No Chunking:** Không cắt nhỏ tài liệu một cách máy móc. PageIndex giữ nguyên cấu trúc tự nhiên (chương, mục) của văn bản.
- **Hierarchical Tree Index:** Tạo chỉ mục dạng cây (Tree Structure) giúp AI nắm bắt ngữ cảnh toàn cục và chi tiết.
- **Reasoning-based Navigation:** AI sử dụng tư duy để định vị thông tin cần thiết thay vì chỉ so khớp từ ngữ (semantic similarity).
- **Explainability:** Kết quả trả về minh bạch, có thể truy xuất nguồn gốc chính xác (trang nào, mục nào).
- **Hỗ trợ MCP:** Tích hợp sẵn Model Context Protocol để kết nối dễ dàng với các AI Agent như Claude Desktop.

## Hướng dẫn cài đặt Local (macOS)

Để chạy PageIndex trên macOS, bạn cần cài đặt Python và lấy API Key.

**Bước 1: Cài đặt Python (nếu chưa có)**
Sử dụng Homebrew:
```bash
brew install python
```

**Bước 2: Tạo môi trường ảo (Khuyên dùng)**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Bước 3: Cài đặt thư viện PageIndex**
```bash
pip install pageindex
```

**Bước 4: Cấu hình API Key**
Bạn cần đăng ký tài khoản tại [dash.pageindex.ai](https://dash.pageindex.ai) để lấy API Key miễn phí (hoặc trả phí).
Sau đó thiết lập biến môi trường:
```bash
export PAGEINDEX_API_KEY='your_api_key_here'
```

## Hướng dẫn Docker

Repository này chủ yếu là thư viện Python. Để đóng gói một ứng dụng sử dụng PageIndex bằng Docker, bạn có thể sử dụng `Dockerfile` cơ bản sau:

1. Tạo file `Dockerfile`:
```dockerfile
# Sử dụng Python 3.10 slim để tối ưu dung lượng
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file requirements (nếu có) hoặc cài trực tiếp
RUN pip install --no-cache-dir pageindex

# Copy mã nguồn vào container
COPY . .

# Thiết lập biến môi trường (khuyên dùng file .env khi run)
ENV PAGEINDEX_API_KEY="your_api_key_here"

# Lệnh chạy ứng dụng
CMD ["python", "main.py"]
```

2. Build và Run container:
```bash
docker build -t pageindex-app .
docker run -e PAGEINDEX_API_KEY='your_real_key' pageindex-app
```

## Ví dụ Code (Example Code)

Dưới đây là đoạn code Python mẫu minh họa cách tạo index từ file PDF và thực hiện tra cứu thông tin:

```python
import os
from pageindex import PageIndexClient

# 1. Khởi tạo client
api_key = os.getenv("PAGEINDEX_API_KEY")
client = PageIndexClient(api_key=api_key)

# 2. Upload tài liệu và xây dựng cấu trúc cây (Tree Index)
# Thay 'tai_lieu.pdf' bằng đường dẫn file thực tế của bạn
print("Đang xử lý tài liệu...")
tree_index = client.build_tree_from_path("tai_lieu.pdf")

# 3. Thực hiện truy vấn (Reasoning Retrieval)
question = "Doanh thu quý 3 tăng trưởng bao nhiêu phần trăm?"
print(f"Câu hỏi: {question}")

# AI sẽ tư duy qua cấu trúc cây để tìm câu trả lời
response = client.query(tree_index, question)

# 4. In kết quả
print("\nCâu trả lời:")
print(response.answer)
print("\nNguồn tham khảo:", response.sources)
```

### Sources
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGoJq7TOS58quZ1uBow0jFjP5-2e6xV8M0qz4yiec1viveUC4-r3pstyvFOXXRaCnyyKssWJxaiQQTepCeAHGQr47agGWDGi3P_oTSp2bZ1oiFdkRoYleM3L7tUDRtYzED)
- [ycombinator.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH90d-PctGDRYHuny-nLa5dt0GmVc977xtup8EbgaKsTwEXn_I6RqTpqY74l2ZqcgOYZl2rFmxKbyaAu3KaENlJ5TUN3_owkp_gPnLKPFajN4W-JEMv-vdpfa2BJOHTuP8c7v3Misf16w==)
- [yuv.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRwso7aJWgbPKYp0qQb8sfGPsznQqb5ptBDBBNleO7P7uKyG_JIn85CxT2xKMMW2PxOmwwmGaSgUbRUSRL5Ojs_0RXrh0na39Q88PdHDiUL3skprYcFx5U)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgil73aaW4bpePFvnvfrZ-SwaH6gWSPx2lTkQSB1t987sH-i4mZzf3Yyq5rfqjxF4dHjVWrqY9pMQAf07qZpH2Ylj4T7Uh9hU6uQes1BrpgXP5YIIkh7dQ3aBNF70A9y5n6o-JPTA=)
- [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGululidzkg7vs6n8k1iYG2m6OyY5azosdNBI_0xIvNJFuevaMDTMfwQiJrNiczLcO_HeBdDudKfzKdK1kNu6IvFF1sZbwZpj6ZYEdvcZanlQ6JsDwYl3l7W5cVI7m_8fL0eAHQfi3dCoewkerSXqfj-sj891I9ymF7a0h5RdjIuBjWPSXZIeMWbY0XueQD7x9afBOAMeoBRGpajBzBmFo6xH_djks=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYeEI_lY0gwSn-3R1Zx4pm-qBwekTwwCaBkE52Vo7TFT-0QarNDLpm4gP7gmfelR6ZFHUqVvj3QQ7M4_pw_4arjCKpGeERJpFdRTPAvwBIUv_CpPmQVexXNsWMeg_IO8pMv1NREQ==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWu6tFFYqtKBaFbayN_3q7XG-cSFAEn7AxPKR7gcy5YhAWFBQUqyYCuffQFYl7bhLapPwA_09XnLmYqqem5BAwj4nW7Byn-7fVB7OnluUvW14FpU_-aNlN_42nbmiJDztuEG9qW5EhjDnI7pEhK4LhyhVJv3-8TrjcauDrOBkaPPb6qapQRY-tJCjHLgp8Ng==)


### Github Page 

https://github.com/VectifyAI/PageIndex

