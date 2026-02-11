---
layout: post
title: "Kokoro-FastAPI"
subtitle: "Giải pháp chạy mô hình chuyển đổi văn bản thành giọng nói (TTS) Kokoro chất lượng cao dưới dạng API tương thích với OpenAI."
tags: [github]
---

## Giới thiệu

Kokoro-FastAPI là một wrapper (lớp bao bọc) sử dụng framework FastAPI để triển khai mô hình Text-to-Speech (TTS) Kokoro-82M. Đây là một mô hình TTS mã nguồn mở nhẹ nhưng cho chất lượng giọng đọc rất tự nhiên, hỗ trợ nhiều ngôn ngữ (bao gồm tiếng Anh, tiếng Nhật, tiếng Trung, và đang phát triển tiếng Việt). Dự án này giải quyết vấn đề triển khai TTS offline/self-hosted bằng cách cung cấp một API server chuẩn, giúp bạn dễ dàng tích hợp giọng đọc AI vào các ứng dụng như trợ lý ảo (SillyTavern, OpenWebUI), đọc sách tự động, hoặc các hệ thống nhà thông minh mà không cần phụ thuộc vào dịch vụ đám mây đắt đỏ.

## Tính năng chính

- **Tương thích OpenAI API:** Cung cấp endpoint `/v1/audio/speech` giống hệt OpenAI, cho phép thay thế trực tiếp (drop-in replacement) trong các ứng dụng có sẵn.
- **Hiệu năng cao:** Hỗ trợ tăng tốc bằng GPU (NVIDIA) và chạy tốt trên CPU nhờ tối ưu hóa ONNX.
- **Giao diện Web (Web UI):** Tích hợp sẵn giao diện web để nghe thử, trộn giọng (voice mixing) và kiểm tra API trực quan.
- **Xử lý văn bản dài:** Tự động ghép nối (stitching) âm thanh cho các đoạn văn bản dài mà không bị ngắt quãng.
- **Hỗ trợ Docker:** Cung cấp sẵn các Docker image cho cả CPU và GPU, giúp việc cài đặt trở nên đơn giản chỉ với một câu lệnh.

## Hướng dẫn cài đặt Local (macOS)

Để chạy trực tiếp trên macOS (sử dụng CPU/MPS), bạn cần cài đặt các thư viện phụ thuộc:

1. **Cài đặt espeak-ng (Bắt buộc):**
   Mở Terminal và chạy lệnh Homebrew:
   `brew install espeak-ng`

2. **Clone repository:**
   ```bash
   git clone https://github.com/remsky/Kokoro-FastAPI.git
   cd Kokoro-FastAPI
   ```

3. **Cài đặt Python dependencies:**
   Khuyến khích sử dụng `uv` hoặc `venv`:
   ```bash
   # Tạo môi trường ảo
   python3 -m venv venv
   source venv/bin/activate
   
   # Cài đặt thư viện
   pip install -r requirements.txt
   ```

4. **Chạy ứng dụng:**
   ```bash
   python main.py
   ```
   Server sẽ khởi động tại `http://localhost:8880` (hoặc port 8000 tùy cấu hình mặc định).

## Hướng dẫn Docker

Cách nhanh nhất để sử dụng là qua Docker. Dự án cung cấp sẵn image trên GitHub Container Registry.

**Chạy phiên bản CPU (Phù hợp cho mọi máy):**
```bash
docker run -d -p 8880:8880 --name kokoro-tts ghcr.io/remsky/kokoro-fastapi-cpu:latest
```

**Chạy phiên bản GPU (Yêu cầu NVIDIA GPU & Drivers):**
```bash
docker run -d --gpus all -p 8880:8880 --name kokoro-tts ghcr.io/remsky/kokoro-fastapi-gpu:latest
```

Sau khi chạy, truy cập:
- **Web UI:** `http://localhost:8880/web`
- **API Docs:** `http://localhost:8880/docs`

## Ví dụ Code (Python)

Dưới đây là ví dụ sử dụng thư viện `openai` của Python để gọi API Kokoro (vì nó tương thích chuẩn OpenAI):

```python
from openai import OpenAI

# Kết nối đến server Kokoro-FastAPI local
client = OpenAI(
    base_url="http://localhost:8880/v1",
    api_key="not-needed"  # Không cần key cho local
)

response = client.audio.speech.create(
    model="kokoro",
    voice="af_bella",  # Tên giọng đọc (ví dụ: af_bella, am_adam)
    input="Xin chào, đây là giọng đọc được tạo từ Kokoro TTS!"
)

# Lưu file âm thanh
response.stream_to_file("output.mp3")
print("Đã tạo file output.mp3 thành công!")
```

### Sources
- [railway.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0_JBLjmtRC7dumJCftKjPcOD1NsPLJB7OpD7Xtdm4ooW5BJGEwj93Is6LF7EdngsnG2F_DDw6brAehlFvC_kmoBnA8GUhJzoRuwS50ECky5hSbbqBJ1MWdcZt3awR4skxdifB)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9RvBUMBpYcMGccfX5xDh9_YWQEl-RXSsHfg1_0eT77zOHnX_D4BSQn2IWQVbISxqM7GDq4zC3ZOZS0RWm10FBV8PtzWXkj_HqTrFQ56BJxTiiAJB4ZRqiPEej8U_JoM4uCXMCrCZzTaWkIa-t3nYxYCTu8tRsnTqcz5fNOat_dvQfqqal3RHHzcCbofI=)
- [aisharenet.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERj_wngoC85XLyy6U1uyxbumPGbaBHbjCaFT2C1LLn7awRnOuM7UgDqHhL4SEuKYDc6E6SihZL3VnLxdc8hB_v-4tXf_GePiv9hwcJzGqWLfrNgh94stv0J_-XjfsBCZ26GQpa)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_EbacjfPGNFKjJYS2eKPHTulbz0WyEwqEV2nuWG3Y3hhrhFcrbe8KZ8GcYTHJ1G5sdg9r5tdeEkwO4P6GTHcAWhj9LPhQsAXMCfAaW-IZAczi8Pr3JrlUpfEqh-0MXiMnnqums5oYkUvUi05WSTR2eYSySnslV0sx0b2U)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVgkB4ydVL7R3OxjCoj3kZfEAROl6a6FZQOF7udbQdAGPuq4X7oFq1psqs7WEN_TrjUkVeX6x8iGD39Q06zCRCC-hX-06C3dnp5nNHY-JeWP8Vq7s4FIgjQMvtzOnBeyBKZOAfATKy3GZIivo32dk4Omm8iQ==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3uDetHTU1zuO71zmSBmwJH_oKxzW0Muh53AQhFoqTrpI57Y1HtvXCpfrk7N1w4WgUfuYBrMXUcwjdUCD0e6FS8c_hzmUnMujxetRZATXZK4GsPXPCNIIC90fZ1ishYARaueqsYt0WB5Eda7YJ0tmSMz64cPs=)
- [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYM8sAu0tudr7doCByMbnDUFlRw2SU-CQ35Q-9F84gx1jQOIG0N3nWPE-7gQ48eAIVXxrYYjan-czSIIXCeZBg86DK82sO2WDMsX-bjPMRlsua3zYoCTRo4FxHAbuoWJpTJRYievdxxlL3QSQpvG468WAk6IHLaewQYjZDMbs8O7dBsM-_hZs8Hf5DCZOjdTnUf38PgOvjGYwzG9iNoFFx0g==)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtY5QXMZ7cd5zS0ngpLbwWvWaiCTc8huX32q1vki8ivLcffFNJsP5YCebnR-gF7lRzvqNO-Ao202-8GT80vyxKcaYVnmq7gHgZkyz0XtET4J0uKonSpT1QzTWWX0v8LapRNu2Ep2c=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfA7ITrB0jZZ_BLL0hchClvUVx1Wqw2XJkRC6cRtRByI43wmJMJw-8FkTsYFUmjWv1YbzrcQuG8dBTCkR4PwM6bjKWRG0wuzChV8OohMEwiU8VN_6FBBZubeMjr4zyTpm_170=)


### Github Page 

https://github.com/remsky/Kokoro-FastAPI

