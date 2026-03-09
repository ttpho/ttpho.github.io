---
layout: post
title: "Google Cloud Platform - Generative AI"
subtitle: "Kho lưu trữ mã nguồn mẫu và hướng dẫn chính thức từ Google Cloud để xây dựng các ứng dụng Trí tuệ Nhân tạo Tạo sinh (Generative AI)."
tags: [github]
---

## Giới thiệu

Repository GoogleCloudPlatform/generative-ai là một kho lưu trữ chính thức từ Google Cloud. Nó cung cấp hàng trăm notebook (Jupyter), mã nguồn mẫu và hướng dẫn chi tiết giúp lập trình viên tìm hiểu và tích hợp các mô hình Generative AI (như Gemini, PaLM 2, Imagen, Codey) thông qua nền tảng Vertex AI. Ứng dụng thực tế của dự án bao gồm việc xây dựng chatbot thông minh, hệ thống hỏi đáp dựa trên dữ liệu doanh nghiệp (RAG - Retrieval-Augmented Generation), phân tích văn bản, sinh hình ảnh, lập trình tự động và tối ưu hóa các quy trình liên quan đến ngôn ngữ tự nhiên.

## Tính năng chính

- Cung cấp Jupyter Notebooks phong phú, bao phủ từ mức cơ bản đến nâng cao.
- Hướng dẫn chi tiết cách gọi và tương tác với Vertex AI, Gemini API, và PaLM API.
- Các ví dụ thực tế về kỹ thuật RAG (Retrieval-Augmented Generation) kết hợp với các framework phổ biến như LangChain và LlamaIndex.
- Hướng dẫn tinh chỉnh mô hình (Model Fine-tuning / Parameter-Efficient Fine-Tuning).
- Xử lý đa phương tiện (Multimodal): bao gồm thao tác với Văn bản, Hình ảnh, Giọng nói và Video.
- Tích hợp các công cụ MLOps và Vector Search phục vụ phát triển ứng dụng AI thực tế.

## Hướng dẫn cài đặt Local (macOS)

Do đây chủ yếu là tập hợp các Jupyter Notebooks và Python scripts, việc cài đặt chủ yếu xoay quanh việc thiết lập môi trường Python và Google Cloud CLI trên macOS.

1. Cài đặt Homebrew (nếu chưa có): Mở Terminal và chạy `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Cài đặt Python và Git: `brew install python git`
3. Cài đặt Google Cloud SDK: `brew install --cask google-cloud-sdk`
4. Tải repository về máy: `git clone https://github.com/GoogleCloudPlatform/generative-ai.git && cd generative-ai`
5. Tạo và kích hoạt môi trường ảo Python: `python3 -m venv venv && source venv/bin/activate`
6. Cài đặt các thư viện lõi cần thiết (phụ thuộc vào từng notebook cụ thể): `pip install jupyter google-cloud-aiplatform langchain`
7. Đăng nhập và xác thực với Google Cloud: `gcloud auth application-default login`
8. Khởi chạy Jupyter Notebook để bắt đầu học: `jupyter notebook`

## Hướng dẫn Docker (nếu có)

Dự án này chủ yếu chứa các tài liệu Notebook thay vì một ứng dụng web, do đó không có sẵn một Dockerfile chung cho toàn bộ dự án. Tuy nhiên, bạn có thể dễ dàng thiết lập một Docker container để có môi trường Jupyter cô lập.

Dưới đây là gợi ý `Dockerfile` cơ bản để chạy các notebook:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
# Tạo file requirements.txt với các thư viện: jupyter, google-cloud-aiplatform, langchain...
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

Cách build và chạy Docker:
1. Build Docker image: `docker build -t gcp-genai-env .`
2. Run container: `docker run -p 8888:8888 -v $(pwd):/app -e GOOGLE_APPLICATION_CREDENTIALS=/app/key.json gcp-genai-env`
*(Lưu ý: Bạn cần cấp quyền cho container bằng cách mount file service account key của Google Cloud (key.json) vào trong container).*

## Ví dụ Code (Example Code)

Dưới đây là một đoạn code mẫu (Python) minh họa cách gọi mô hình Gemini từ Vertex AI để tạo văn bản:

```python
import vertexai
from vertexai.generative_models import GenerativeModel

# 1. Khởi tạo Vertex AI với Project ID và Location của bạn
PROJECT_ID = "your-google-cloud-project-id"
LOCATION = "us-central1"
vertexai.init(project=PROJECT_ID, location=LOCATION)

# 2. Tải mô hình Gemini (Ví dụ: Gemini 1.5 Pro)
model = GenerativeModel("gemini-1.5-pro-preview-0409")

# 3. Đặt câu hỏi / yêu cầu cho mô hình
prompt = "Hãy giải thích ngắn gọn về RAG (Retrieval-Augmented Generation) là gì?"
response = model.generate_content(prompt)

# 4. In kết quả phản hồi
print(response.text)
```


### Github Page 

https://github.com/GoogleCloudPlatform/generative-ai

