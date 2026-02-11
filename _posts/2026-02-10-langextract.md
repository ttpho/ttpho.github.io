---
layout: post
title: "LangExtract"
subtitle: "Thư viện Python mã nguồn mở của Google giúp trích xuất dữ liệu có cấu trúc từ văn bản thô bằng LLM với khả năng truy xuất nguồn gốc chính xác."
tags: [github]
---

## Giới thiệu

LangExtract (google/langextract) là một thư viện Python được thiết kế để giải quyết vấn đề khó khăn nhất trong xử lý văn bản bằng AI: chuyển đổi dữ liệu phi cấu trúc (như hồ sơ y tế, hợp đồng pháp lý, báo cáo tài chính) thành dữ liệu có cấu trúc (JSON) tin cậy. Điểm đặc biệt của LangExtract so với các công cụ khác là tính năng 'Source Grounding' (Truy xuất nguồn gốc) – mọi thông tin được trích xuất đều được liên kết chính xác đến vị trí (character offset) trong văn bản gốc, giúp người dùng dễ dàng kiểm chứng (audit) độ chính xác và giảm thiểu ảo giác (hallucination) của LLM.

## Tính năng chính

- **Precise Source Grounding**: Liên kết mọi dữ liệu trích xuất với vị trí chính xác trong văn bản gốc để dễ dàng xác minh.
- **Structured Outputs**: Đảm bảo đầu ra tuân thủ schema nghiêm ngặt (thường là JSON), phù hợp để nạp vào cơ sở dữ liệu.
- **Xử lý văn bản dài (Long Documents)**: Sử dụng chiến lược chia nhỏ (chunking), xử lý song song và quét nhiều lần (multi-pass) để không bỏ sót thông tin trong các tài liệu lớn.
- **Trực quan hóa tương tác**: Tự động tạo file HTML để hiển thị dữ liệu trích xuất ngay trên văn bản gốc (highlight visual).
- **Hỗ trợ đa mô hình**: Tối ưu hóa cho Google Gemini (Vertex AI) nhưng cũng hỗ trợ các mô hình cục bộ qua Ollama.

## Hướng dẫn cài đặt Local (macOS)

Để chạy LangExtract trên macOS, bạn cần Python 3.9 trở lên.

1. **Cài đặt thư viện qua pip**:
   Mở Terminal và chạy lệnh:
   ```bash
   pip install langextract
   ```

2. **Cấu hình API Key**:
   LangExtract sử dụng Google Gemini mặc định. Bạn cần có API Key từ Google AI Studio.
   ```bash
   export GOOGLE_API_KEY="your_google_api_key_here"
   ```
   (Hoặc cấu hình Vertex AI nếu dùng Google Cloud).

3. **Cài đặt môi trường ảo (Khuyên dùng)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install langextract
   ```

## Hướng dẫn Docker

Dự án này là một thư viện Python, không phải một ứng dụng standalone, nhưng bạn có thể đóng gói nó vào Docker để chạy các script trích xuất.

**Dockerfile cơ bản:**
```dockerfile
# Sử dụng Python slim image
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt git và các dependencies cần thiết (nếu có)
RUN apt-get update && apt-get install -y git

# Cài đặt langextract
RUN pip install langextract

# Copy source code của bạn vào container
COPY . /app

# Thiết lập biến môi trường cho API Key (nên truyền qua docker run -e)
ENV GOOGLE_API_KEY="your_key_placeholder"

# Lệnh chạy mặc định
CMD ["python", "main.py"]
```

**Cách build và run:**
```bash
docker build -t langextract-app .
docker run -e GOOGLE_API_KEY="xxx" langextract-app
```

## Ví dụ Code (Example Code)

Đoạn code dưới đây minh họa cách trích xuất các thực thể (nhân vật, cảm xúc) từ một đoạn văn bản mẫu:

```python
import langextract as lx
from langextract.data import ExampleData, Extraction

# 1. Định nghĩa yêu cầu (Prompt)
prompt = "Extract characters and their emotions from the text."

# 2. Cung cấp ví dụ (Few-shot examples) để hướng dẫn LLM
examples = [
    ExampleData(
        text="ROMEO. But soft! What light through yonder window breaks?",
        extractions=[
            Extraction(
                extraction_class="character",
                extraction_text="ROMEO",
                attributes={"emotion": "wonder"}
            )
        ]
    )
]

# 3. Văn bản cần xử lý
text_content = "JULIET. O Romeo, Romeo! wherefore art thou Romeo? Deny thy father and refuse thy name."

# 4. Thực thi trích xuất
print("Đang trích xuất...")
result = lx.extract(
    text_content,
    prompt_description=prompt,
    examples=examples,
    model_id="gemini-1.5-flash" # Hoặc model khác được hỗ trợ
)

# 5. Hiển thị kết quả
for item in result.extractions:
    print(f"Class: {item.extraction_class} | Text: '{item.extraction_text}' | Attr: {item.attributes}")

# (Tùy chọn) Tạo file HTML trực quan hóa
# lx.visualize(result, "output.html")
```

### Sources
- [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgzRe3SyWqK9IQEBSK3Cz3psEgSGFnVpvHOqsnjCWSIYH6R9W4QjkHvlX6-rUf6QFzbx0eKRjz1RgJW9mWF8WaGwOgXbtpc6y6H4QPGi7YsSfhpIB27FjGBbSLQSmYS27yIdXwa3I3FM0c3H6NainDwD5Ui2hKzc-I9xe28FI8fNEau7R0XgluUjqtuETjbEquIGc=)
- [brightcoding.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfYG_2rupAC4NPZy86pk9dNlXICB0lay1byEheB4tWx8jrqrn598MRNoJwnHTJpUg-CJqTUO0mF0Zy6fMmHE7-zbMtaaFQyqzDL64DHwaBrmYGihhu6NtkiioxRJ6FuXhZHLEkceDGGHjAbQzdbC_N83rEyCg_m4J8MOEvW4qe4_8RZqqu0rk_EmXlWJ9y_-FYKzu8WvtH4g696HW1Ga61nTb8Cgit39lnCliimQ==)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuQy8kNdn4yw_QIaUcSoHLx1fucNsK7DqBK0B_gqrz4PXY_Jd6qmeAr8bTMwCy_lxOjjlQVs9JTlNScumSgjmOGShqBNBj_Xc6IG-E5rVej2685lHgVMQOmF_R8xncDYG5d8gZOMAQzGjByVvsu6cRjAA5prW3hd0VcufLr4-Eh2jtXjV9ihb7OWHqdpUCqmtyw8oSywR3ETsEDJKxllwy98msi_4=)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG13KS3-UazVQVmfrbEWpVtoSaMturzhqawzylIgy3KaFzPQBgayN1UohgaO8gxqGEoz9XU3hOyVITHjN9ZJcJTpUBBdM6aIklZKFZ9l3iOInfWRtP3A-ZRNiymcjlHhbWW4iBkYKA=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk4PfK43A9EEVWP2BzhnNgWZJpJXPtisUknwdAv5no02YUHSnFqrj45te2QfpmO5NAGLLECrlnPjFKj1XhCgZTw9e85gv900bpFRg0P9x9YfZVY-SDJQ-_a0IC0LXfFxCUuCkTiBdpkIPGxeMhHhE2boaS0oPlXEHXq2_sgwr3aLHmmk12vREMu47ZCH47d7GlvziSuBJZCkHwrOLzF2FqbIJuX5neVXlBizPdotAoAU1G3G0PmxGl)
- [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2n33HRcp17yGOEOc5M8o2dDFSEFDxYPNz6S5OTdF4_tDbidV3qSk9x0nJxu4YmgMzDGhR_UduFi36DDtfMQhVNXgovfbEaCAdnj-HGZ_cdMFLNfCJr2zU8CbjSKw_Bd4hm4XUUdZewSWm-bB-Ez7rrCwZeAtTMj_T7mMuMv4VwLvkIVoVA8KgBTXCLfCbKyqk-_AcW4aWe13rTaCS)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdGvQO-NthaXT_AeyFeq9pb24jJITBEvpycgfyzqjE78w5tasGA8FNbplPIy0StOlMvfWtSgFDGvek9MG_gKstm9wiVkZ3Mgfv5OJO8mFJT14YMqMibYwmMbn8O4sysDU=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnAC3EIvgz56_lfj7y9OgYXrEKvp-X-4yRFg4JN7y1bRxTjDh06zI1p563U_60tKvi140M3Q7sSHYTU2Ev7wp7Pzm-cuIDIJGTRM749uw85dJEDJanL4BfdZbZ6mfSAua9dp0uOPi1V0wR)


### Github Page 

https://github.com/google/langextract

