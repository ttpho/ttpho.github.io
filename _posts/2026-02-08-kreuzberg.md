---
layout: post
title: "kreuzberg"
subtitle: "A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 60+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server."
tags: [github]
---

## 1. Giới thiệu & Mục đích

**Kreuzberg** (trước đây có thể được biết đến dưới tên namespace `Goldziher`) là một thư viện xử lý tài liệu (document intelligence) hiệu năng cao, được viết lại hoàn toàn bằng **Rust** trong phiên bản v4.0 mới nhất. Mục đích chính của dự án này là cung cấp giải pháp trích xuất văn bản, metadata và dữ liệu có cấu trúc từ nhiều loại định dạng file khác nhau một cách nhanh chóng, chính xác và bảo mật.

**Ứng dụng thực tế:**
*   **RAG (Retrieval-Augmented Generation):** Trích xuất nội dung từ PDF, file Word để làm dữ liệu đầu vào cho các mô hình ngôn ngữ lớn (LLM).
*   **Tự động hóa quy trình:** Xử lý hóa đơn, hợp đồng, tài liệu scan để lấy thông tin tự động.
*   **Search Engine:** Đánh chỉ mục nội dung (indexing) từ các file nhị phân mà không cần phụ thuộc vào API của bên thứ ba.
*   **Chuyển đổi định dạng:** Chuyển đổi PDF, Office sang Markdown hoặc JSON để dễ dàng xử lý bằng code.

## 2. Tính năng chính

*   **Đa ngôn ngữ (Polyglot):** Core được viết bằng Rust cho hiệu năng cực cao, nhưng cung cấp binding (thư viện) cho nhiều ngôn ngữ: **Python, TypeScript (Node.js), Go, Java, C#, Ruby, PHP, Elixir**.
*   **Hỗ trợ đa định dạng:** Xử lý hơn **56 định dạng file** bao gồm PDF (cả dạng text và scan), Microsoft Office (Word, Excel, PowerPoint), Hình ảnh, HTML, Email, v.v.
*   **Tích hợp OCR:** Hỗ trợ sẵn OCR (Nhận dạng ký tự quang học) sử dụng **Tesseract**, EasyOCR hoặc PaddleOCR để xử lý các tài liệu dạng ảnh hoặc PDF scan.
*   **Xử lý cục bộ (Local Processing):** Chạy hoàn toàn offline, không gửi dữ liệu ra ngoài, đảm bảo quyền riêng tư và bảo mật dữ liệu.
*   **Hỗ trợ Async:** (Đặc biệt với Python) Hỗ trợ cả cơ chế đồng bộ (sync) và bất đồng bộ (async), tối ưu cho các ứng dụng web server hoặc xử lý song song.
*   **Smart PDF Handling:** Tự động phát hiện và fallback sang OCR nếu PDF bị lỗi font hoặc không thể trích xuất text trực tiếp.

## 3. Hướng dẫn cài đặt Local (macOS)

Để sử dụng Kreuzberg trên macOS (ví dụ với Python binding), bạn thực hiện các bước sau:

**Bước 1: Cài đặt System Dependencies (qua Homebrew)**
Nếu bạn cần tính năng OCR hoặc Embeddings, hãy cài đặt các thư viện hệ thống cần thiết:
```bash
# Cài đặt Tesseract cho tính năng OCR
brew install tesseract

# Cài đặt ngôn ngữ cho Tesseract (ví dụ tiếng Việt và tiếng Anh)
brew install tesseract-lang

# (Tùy chọn) Cài đặt ONNX Runtime nếu dùng tính năng embeddings
brew install onnxruntime
```

**Bước 2: Cài đặt thư viện Python**
Sử dụng `pip` để cài đặt thư viện chính:
```bash
# Cài đặt bản cơ bản
pip install kreuzberg

# Hoặc cài đặt bản hỗ trợ đầy đủ async và các tính năng mở rộng
pip install "kreuzberg[async,ocr]"
```

**Lưu ý:** Nếu bạn chỉ muốn dùng công cụ dòng lệnh (CLI) mà không cần code Python:
```bash
brew install kreuzberg-dev/tap/kreuzberg
```

## 4. Hướng dẫn Docker

Kreuzberg cung cấp sẵn Docker image chính thức, có thể chạy như một REST API server hoặc một công cụ xử lý độc lập.

**Cách 1: Chạy Kreuzberg Server (REST API)**
Pull và chạy image chính thức từ GitHub Container Registry:
```bash
docker run -p 3000:3000 ghcr.io/kreuzberg-dev/kreuzberg:server
```
Sau khi chạy, bạn có thể gửi request POST tới `http://localhost:3000/extract` để trích xuất dữ liệu.

**Cách 2: Dockerfile cơ bản (cho Python App)**
Nếu bạn muốn build một ứng dụng Python sử dụng thư viện `kreuzberg`, hãy dùng Dockerfile sau để đảm bảo đầy đủ dependencies:
```dockerfile
FROM python:3.11-slim

# Cài đặt dependencies hệ thống cho Tesseract OCR
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-vie \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Cài đặt thư viện Kreuzberg
RUN pip install "kreuzberg[async]"

COPY . .

CMD ["python", "main.py"]
```

## 5. Ví dụ Code (Example Code)

Dưới đây là ví dụ sử dụng Python (Async) để trích xuất văn bản từ một file PDF:

```python
import asyncio
from kreuzberg import extract_file, ExtractionConfig

async def main():
    # Đường dẫn tới file cần xử lý
    file_path = "./tai_lieu_mau.pdf"
    
    # Cấu hình trích xuất (có thể tùy chỉnh OCR, ngôn ngữ...)
    config = ExtractionConfig(
        enable_ocr=True,          # Bật OCR nếu cần
        language="vie+eng"        # Ngôn ngữ ưu tiên (nếu dùng OCR)
    )

    try:
        # Thực hiện trích xuất bất đồng bộ
        result = await extract_file(file_path, config=config)
        
        print(f"--- Kết quả trích xuất từ: {file_path} ---")
        print(f"MIME Type: {result.mime_type}")
        print(f"Metadata: {result.metadata}")
        print("\nNội dung văn bản:")
        print(result.content[:500]) # In 500 ký tự đầu tiên
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Nguồn tham khảo

- [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqdPHW3GLDJpHk0OKFVs4Nwo61oN0yIBS4sw0YZhgUo3Vdh4c5zqUtH-nF0f4EApD6yvunJOnLaMmVo4JzttWOSAUyFfmckYxx37h--OWfly192TdzTUYQkINunQLrFq3Pym_cb5Q8ln5QwQuzy1_4)
- [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8FB5p_f0PD3iewRESN0LoyBZs78yHVC260tlNPLBeyXOofjyIvxnLxpshHYrkKmLrLWf0yNr84kK8wESaReDzslF74TmFn21US4Iin6n3M5P1Z-k4Mp596fe4l9mCYT7vxzYIdzTalPwX2WPDOmLb1RbVlEewfRn39Lr3FtgliEmVypsDarid5rjFkDn9LnzRjzSTKF_fuw==)
- [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGs0yu7AmVCaesHLaHSqwXG3dmNEqR5urpvPZS6jjkxW_Y3sFok9ZlllEsjeE2NdOKjZHKVfrW5BCHv4OkzGndi1n3zBSAEyuTewomLVJT2b_aFm_sOMeyQgGaiu4nI7W8K4ML4U9m6po2woYtlQNz-TPkfy-ahDpkUrB1X5T3g3AaDECTIXZAu6kAJJXzdrzdFVmmgXDC1i3LI5tL2oaiIzsGv6Tizg==)
- [crates.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsiSUrBt7-Y67pgRe8ucN4oYfaoxojg3NM45cxPLr5Tnfyw2AQP8l9ClA9LzjKNXeTQctS6TRxEG5AMx9OS7X-EjfN0QanU6Tg-YlL8MVunSMpKxlXeSpClA6dQIY=)
- [pypi.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy0IgE6b_40DFgPfdRH5J5kUrRpPjOcKPGfMhDH2Ipm_X5o4bgTGfDJ7p8t2RUVVVTltzEBrTUXRN4c9ZzGx1iIHDzfTRl4zAQNawUINpPTW63B679TSoL5cdksDE5)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQFSOXQ8_oTRV1VoJ8eMJ1zXhrBTZ8dlKreROGnij8UUg0bunUFD8a_L-DY_QHLih-sqOqAzttM_1um1N19N4uP3zhP36yJF-H8hd7ApNco3kW7WRt8lQGRb5am5LoetIXsq9MO_oHJW2djRobtk2KKek5xId0-EdTVZ8kCjGcFckvEZaFccUg1Vw8aFIh4lytPHjjQmbe1HsulrNJV1NvBOaa8YTD9Hv3wzi7vv163RJlZSn-fiEvQA==)
- [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVm6dur-HaFr7eLAszgmcHyJaxt_PtGoHP6YEcpnevzvCDLDFbTxZw1po477MeBDKXZKfiBgLHoDa8IWoaD99oYPkQgXWnavaEkFhTZRaMJPi09cWPwfrCK7Sq-UOZfA6c_4bsJOpaTrSYIzWdqWO8WpIk9RVY-JqzrTrXRea4uESMYVd8mq9P7LP7BxDHZD-67e4Xjg4AGmau6AhBAg==)
- [kreuzberg.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6RGhxqP5TjKP5FErcZltZgvFhOgf4m9JWGZf-NOQkGFHUekqc9VVd-HfNUDl9Q5HO8KPGPd-duD9jbpDeMtqNks4g04UdDX56IEcXmbADMhhUVeTMlw==)
- [ycombinator.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUWdA8kjaY3MHzNaOcmVOChhl6TeLJvpmK0FkSRHgNiTYa_hwvo-Etbp0xyd-JsP0LZ-UtEAyOFzD264-PDS6fVshocx2I_Ub3iblIVrzCJz-FO-ywmuDhUDCPDxs2d3ZEjNIKjw_64w==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhDjUDatW_kBep4fcNMrKZwewr-qpluEPUhhAdjrdXOJNRPtylTZk_YCQXznaTB_7xklqas3YIsIm4Kgb7XzV0g882PchbMpY0kaC9OVhUl9GLM3hKXX-J7Da4)
- [kreuzberg.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGKWyiwYCwszPguThpga6SJqxLuoIv_Av42jWioooggsUvp7j7jLnUwJFrDFEtKP31TiZQVxuh1Uy0MJuzoksE8pzAT6G-EAJe68oxDhpvEQY=)
- [docs.rs](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCQLqd6HVHaQzZL6BEu02LhAh9025JBl2vHiYgYP0eVTgV9Ly2-6Fkh8jC9-d3f6SX7qzsLcbWrH6dScF2bD8yzZwrjhDpT9m8_ktKkkRHnR1x7Gg=)


### Github Page 

https://github.com/kreuzberg-dev/kreuzberg

