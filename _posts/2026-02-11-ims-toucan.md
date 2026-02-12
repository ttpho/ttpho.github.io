---
layout: post
title: "IMS Toucan"
subtitle: "Bộ công cụ mạnh mẽ hỗ trợ huấn luyện, giảng dạy và sử dụng các mô hình Text-to-Speech hiện đại cho hơn 7000 ngôn ngữ."
tags: [github]
---

## Giới thiệu

IMS Toucan là một bộ công cụ mã nguồn mở được phát triển bởi Viện Xử lý Ngôn ngữ Tự nhiên (IMS) thuộc Đại học Stuttgart. Repository này giải quyết vấn đề tổng hợp tiếng nói (Text-to-Speech - TTS) với chất lượng cao, tốc độ nhanh và khả năng kiểm soát tốt. Điểm đặc biệt của IMS Toucan là khả năng hỗ trợ đa ngôn ngữ khổng lồ (lên tới hơn 7000 ngôn ngữ) và tính năng nhân bản giọng nói (voice cloning) chỉ với lượng dữ liệu nhỏ. Dự án này được ứng dụng thực tế trong việc tạo trợ lý ảo, đọc sách nói tự động, nghiên cứu ngôn ngữ học, và hỗ trợ người khiếm thị.

## Tính năng chính

- **Hỗ trợ đa ngôn ngữ (Massively Multilingual):** Khả năng tổng hợp tiếng nói cho hơn 7000 ngôn ngữ khác nhau nhờ sử dụng embedding ngôn ngữ.
- **Voice Cloning & Prosody Control:** Cho phép nhân bản giọng nói của người nói cụ thể và điều chỉnh ngữ điệu, cảm xúc, độ cao độ (pitch), và tốc độ nói.
- **Kiến trúc hiện đại:** Sử dụng FastSpeech 2 kết hợp với HiFi-GAN và Normalizing Flows để tạo ra âm thanh tự nhiên nhất.
- **Thuần Python & PyTorch:** Mã nguồn được viết hoàn toàn bằng Python và PyTorch, không phụ thuộc vào các thư viện C++ phức tạp (như Kaldi), giúp dễ dàng cài đặt và tùy chỉnh.
- **Giao diện trực quan:** Cung cấp GUI để người dùng có thể tinh chỉnh các tham số phát âm một cách trực quan.

## Hướng dẫn cài đặt Local (macOS)

Để chạy IMS Toucan trên macOS (Apple Silicon hoặc Intel), hãy làm theo các bước sau:

1. **Cài đặt dependencies hệ thống:**
   Bạn cần cài đặt `espeak-ng` (công cụ tổng hợp tiếng nói nền tảng) thông qua Homebrew:
   ```bash
   brew install espeak-ng
   brew install libsndfile
   ```

2. **Clone repository:**
   ```bash
   git clone https://github.com/DigitalPhonetics/IMS-Toucan.git
   cd IMS-Toucan
   ```

3. **Thiết lập môi trường Python:**
   Khuyến nghị sử dụng Python 3.10. Tạo môi trường ảo:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Cài đặt thư viện Python:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Xử lý lỗi espeak (nếu có):**
   Trên macOS, đôi khi thư viện `phonemizer` không tìm thấy `espeak-ng`. Bạn có thể cần thiết lập biến môi trường:
   ```bash
   export PHONEMIZER_ESPEAK_LIBRARY=$(brew --prefix espeak-ng)/lib/libespeak-ng.dylib
   ```
   Thêm dòng trên vào `.zshrc` nếu cần thiết.

## Hướng dẫn Docker

Dự án không cung cấp sẵn Dockerfile ở thư mục gốc, nhưng bạn có thể tạo một file `Dockerfile` đơn giản để chạy môi trường này:

1. **Tạo file `Dockerfile`:**
   ```dockerfile
   FROM python:3.10-slim

   # Cài đặt espeak-ng và các thư viện cần thiết
   RUN apt-get update && apt-get install -y \
       espeak-ng \
       libsndfile1 \
       git \
       && rm -rf /var/lib/apt/lists/*

   WORKDIR /app

   # Copy source code
   COPY . .

   # Cài đặt python dependencies
   RUN pip install --no-cache-dir -r requirements.txt

   # Command mặc định
   CMD ["python", "run_text_to_file_reader.py"]
   ```

2. **Build và Run:**
   ```bash
   # Build image
   docker build -t ims-toucan .

   # Run container (ví dụ chạy script demo)
   docker run -it --rm -v $(pwd)/output:/app/output ims-toucan
   ```

## Ví dụ Code (Example Code)

Dưới đây là đoạn code Python mẫu để tải một mô hình pre-trained và chuyển văn bản thành file âm thanh `.wav`:

```python
import os
from InferenceInterfaces.ToucanTTSInterface import ToucanTTSInterface

# Tạo thư mục output nếu chưa có
os.makedirs("output", exist_ok=True)

# Khởi tạo interface (sẽ tự động tải model mặc định nếu chưa có)
# Bạn có thể chọn ngôn ngữ (VD: 'English', 'Vietnamese', 'German')
tts = ToucanTTSInterface(device="cpu", tts_model_path=None)

text = "Hello, this is a test of the IMS Toucan speech synthesis toolkit."

# Thực hiện tổng hợp tiếng nói
print("Đang tổng hợp tiếng nói...")
tts.read_to_file(
    text_list=[text],
    file_location="output/test_audio.wav",
    language="English"
)

print("Hoàn tất! Kiểm tra file tại output/test_audio.wav")
```

### Sources
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPHJ2GulK-JBJnEOJOcByw0yY5bpHjm57BZnOw5ZE2G3mlOfZDvk98y9_eBQqpgHAh3-jpW38i7EY5fSE4k3U2OGoE8hagX3S_ymxZFVFpvuM6Hz6EMlOyDhfc8-o=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8FROUS0cJwNiVKzbC2qB_9X6-KOyJeQvZkP7s1XuAI45tXoxvb8YDVrqL2jvwNNwlyxM1lB3OELECdLXpMyc16hFeMkWheE9XqLV7suIsCUl5jL30lZAZEPkDyiH0IXIvnHvD2YDkNw==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8leQSMY3KhjEczKSunudxnfYufjhdjszJQAHTZN4bBIIrmCqW46bUIEqMUT27Shww2D7ayhnrrtG_mytJk7EF6IhQTe3Bimimv-KgrpVPXkuADVYcNxzUFK-YSiY__1qdLUP01Kz0rw==)
- [redhat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtvGLaiLEfaw-TG9KoHl9tAALUU_JwzNg8D2yzHbpVvxLma8o-OPQcdbRIzjY7BYC0_nsooHS7eO1XAp0nGd5PixgA38Uv47iUEIWebSSXXGlrEDOiYUFAnXbpnaVYtWeKBIyhfOCJWi71jhkwH2nn1uD4h1KrLCpCnTmlWdQYPFTvU0obd4pZDIPUmZK0DeoPJNj2b8CW0NTt0NpLFtpPtA==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSCGSS4gPEK4X01eVYVEvkERLAJ6A0m297icDYxQhqHXKTjzvrrQE5D5CKyg5TgSCWpGyITNfKOjgy_B5r04yAnGRyWK3LrSKwe-4z6tteJGooSDMOuEEsi5gHwgfrZNTJBEKqPTd1wlSxbT_R7Whljf4yJMG8UwGVmM-xGC1Hf9ddt6mpUr7c1phZuviW2bxphVj5DhQB)
- [merlio.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbimgDQL2li2h85amwxi5YHl65nAzMD6sl-qDkBwheZ0D0QUCbWPyO8YrOcERdtXhXzx0aRhimkJTdJatQlYvqqkG7wx57qHsq-CAVt6c769xmTOXFL35snhfH1hqWvK6-n-vFcRictSPvQj21zQBd5tt65o4wcNnVgqlM)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGep5N8_O4b92P7lkFRpPmqlpnQE8eNrf4H241fuN9wSTk4n6GMXfyHF02nEWK9CU0Q9_RYmF10KNCkMLSNSRPeB5LI3zhVEVFgYtTmm3OnTxMp_wJ57UYo5QTRj2Q6UhMUCZ2NKHWpSsp3d-qcnecrFg==)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEte28pWgDPvZLAPeNVypr8nVjRWUiKBReWLJYfLyG1YSGxE0Zl4DRJdJ3yTVsBAryXEEdwlgytGxzlU3Nn11tVIrmogxDhdEWluIq4cVZrSDUZREckoVj750mjsoD-sWas7JY=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoWDLZYZcaUQ5NfqFONK7sjybUM9WX3HSjlGhQ-STlLapBh5w4VVwHwIYRmbjCl0mW_Kjsjpg2i9439aw9R28MoZYOlY1CdUaZSwwqVWWg0aYy_2lPcZggEE7c-O5da2EVG1l1im8Xwa10oPiM3qJr)
- [toucansites.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiRiO1skzxcSFmywLfWf-lSIeWZbMf691OwyNHatBuzP_N0fSYRsc7wTWDeItBHk61fmMGlTZVcOwWZ2NdBwJt6RX0e_ud2P7IIFyEpOiXvA2wud-11al_li_yLzeW6X2YqyfDBqqvDbD5)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI5Pfz1ZrIQ5G0623rc2aOM6ZGEvR2Pe4Oc6AgHdNBwcAgWC8PQfIZwAIrrT0H6zRcQ_m-QaRFlWTK6eZzkolzSpGsW6lBSzgu_ELAebwQn7PcN1oJzn5l1kqWRkPfDZM0Erp8Ug==)


### Github Page 

https://github.com/DigitalPhonetics/IMS-Toucan

