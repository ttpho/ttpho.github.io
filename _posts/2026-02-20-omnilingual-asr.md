---
layout: post
title: "Omnilingual ASR"
subtitle: "Hệ thống nhận dạng giọng nói mã nguồn mở hỗ trợ hơn 1.600 ngôn ngữ với khả năng học zero-shot tiên tiến."
tags: [github]
---

## Giới thiệu

Omnilingual ASR là dự án nghiên cứu đột phá từ Meta AI (FAIR) nhằm giải quyết vấn đề rào cản ngôn ngữ trong công nghệ nhận dạng giọng nói (ASR). Trong khi các hệ thống hiện tại chỉ hỗ trợ khoảng 100 ngôn ngữ phổ biến, Omnilingual ASR mở rộng khả năng hỗ trợ lên tới hơn 1.600 ngôn ngữ, bao gồm hàng trăm ngôn ngữ chưa từng được công nghệ ASR tiếp cận. Dự án này ứng dụng thực tế trong việc bảo tồn ngôn ngữ hiếm, phát triển trợ lý ảo đa ngữ, và cung cấp công cụ chuyển đổi giọng nói thành văn bản cho các cộng đồng yếu thế (low-resource languages).

## Tính năng chính

- **Hỗ trợ hơn 1.600 ngôn ngữ:** Bao phủ rộng khắp các hệ ngôn ngữ trên thế giới, vượt trội so với các mô hình trước đây (như Whisper hay MMS).
- **Zero-Shot Learning:** Khả năng nhận dạng ngôn ngữ mới chưa từng được huấn luyện chỉ bằng cách cung cấp một vài ví dụ mẫu (audio-text pairs) trong ngữ cảnh (in-context learning).
- **Đa dạng kiến trúc mô hình:** Cung cấp nhiều biến thể từ mô hình CTC truyền thống đến các mô hình LLM-ASR (dựa trên Large Language Models) với kích thước từ 300M đến 7B tham số.
- **Mã nguồn mở hoàn toàn:** Phát hành theo giấy phép Apache 2.0, cho phép cộng đồng tự do sử dụng, nghiên cứu và thương mại hóa.
- **Tích hợp Hugging Face:** Dễ dàng truy cập dataset và mô hình thông qua hệ sinh thái Hugging Face.

## Hướng dẫn cài đặt Local (macOS)

Để chạy dự án trên macOS, bạn cần cài đặt Python và các thư viện xử lý âm thanh.

1. **Cài đặt System Dependencies (qua Homebrew):**
   Mở Terminal và chạy lệnh sau để cài đặt `ffmpeg` và `libsndfile` (cần thiết cho xử lý audio):
   ```bash
   brew install ffmpeg libsndfile git
   ```

2. **Thiết lập môi trường Python:**
   Khuyến khích sử dụng Anaconda hoặc Virtualenv (Python 3.9+):
   ```bash
   conda create -n omniasr python=3.10
   conda activate omniasr
   ```

3. **Cài đặt PyTorch:**
   Cài đặt PyTorch tương thích với chip M1/M2/M3 (MPS acceleration):
   ```bash
   pip install torch torchaudio
   ```

4. **Clone và cài đặt Repository:**
   ```bash
   git clone https://github.com/facebookresearch/omnilingual-asr.git
   cd omnilingual-asr
   pip install -e .
   # Cài đặt thêm các thư viện hỗ trợ data nếu cần
   pip install "omnilingual-asr[data]"
   ```

## Hướng dẫn Docker

Sử dụng Docker giúp tránh xung đột thư viện. Dưới đây là `Dockerfile` cơ bản để chạy dự án:

1. **Tạo file `Dockerfile`:**
   ```dockerfile
   FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

   # Cài đặt system dependencies
   RUN apt-get update && apt-get install -y \
       git \
       ffmpeg \
       libsndfile1 \
       && rm -rf /var/lib/apt/lists/*

   # Thiết lập workdir
   WORKDIR /app

   # Clone repo và cài đặt dependencies
   RUN git clone https://github.com/facebookresearch/omnilingual-asr.git .
   RUN pip install --no-cache-dir -e .
   RUN pip install --no-cache-dir "omnilingual-asr[data]"

   # Lệnh mặc định (ví dụ mở python shell)
   CMD ["python3"]
   ```

2. **Build và Run:**
   ```bash
   # Build image
   docker build -t omni-asr .

   # Run container (mount thư mục hiện tại để truy cập file audio)
   docker run -it --rm -v $(pwd):/app/data omni-asr
   ```

## Ví dụ Code (Example Code)

Dưới đây là đoạn code Python minh họa cách tải một mô hình LLM-ASR và thực hiện nhận dạng giọng nói từ file âm thanh:

```python
import torch
from omnilingual_asr.models.inference.pipeline import ASRInferencePipeline
import soundfile as sf

# 1. Khởi tạo Pipeline với mô hình 7B (hoặc chọn 'omniASR_CTC_300M' cho nhẹ hơn)
# Model sẽ tự động tải về từ Hugging Face
print("Đang tải model...")
pipeline = ASRInferencePipeline(model_card="omniASR_LLM_7B", device="cuda" if torch.cuda.is_available() else "cpu")

# 2. Chuẩn bị dữ liệu audio (giả sử bạn có file 'test_audio.wav')
# Lưu ý: Model hỗ trợ input dạng path hoặc mảng numpy
audio_path = "test_audio.wav"

# Nếu chưa có file, tạo file dummy hoặc tải từ dataset mẫu
# import numpy as np
# audio_data = [{"waveform": np.random.randn(16000), "sample_rate": 16000}] # Dummy data

# 3. Thực hiện nhận dạng (Transcribe)
# Bạn có thể chỉ định ngôn ngữ đích (ví dụ: 'vie_Latn' cho tiếng Việt)
print("Đang nhận dạng...")
transcriptions = pipeline.transcribe(
    [audio_path], 
    lang="vie_Latn",  # Mã ngôn ngữ cho Tiếng Việt
    batch_size=1
)

# 4. In kết quả
for i, text in enumerate(transcriptions):
    print(f"Kết quả: {text}")
```

### Sources
- [aibars.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw9ICnwrYiJRK69Pfktg2SeYdYFyEQ-QZHQJQ9-LBVnTq0zcmZKjPCdu3XVpydcb8R42Jy1RqH035mkGnMOPnk1sYBznyk1aSyOuju63LxzAU4Nd-GPTkrDbXqhtc0zc9iNnuL1ywUr2BWlF-lwJqaVycmyDcGZF9PIrmIHrc5h9NWt0T-bw==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFStp4PtGe8qg2-ZsuGWK1YpM9sTjEejziLz66xUlOOrgQiXbf6of24Lb73NnSH_egI0s61UTceoFF5sdrKDTdvucTY88QVLTmr9DcvG4rPkB60MXnxr3NlG-90qAY1tilxCXbbB4GovKA_ZDA58w==)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnGZo7H6oViAzaFO9wP3RFZiAOk8ycVOhNZTJl2Oun7n6gLWnMAB1dpwBKohquAi0P9h3au_MLKMg1cZd3W1WJ8KoObE_AlbYY9P5KzP1y_tBXERGodkbYZoBkcjdq5OI7mvY8W9rOQQP6U1uC37w_A6A3cYzTCVLll7NP9naJ6QPy2K2_CRG_fh1JkeBgGx4OnG-9WKMuzZTUoAVeVxquZwfi5Rs6nNSgPtgqpUbTvkvw7VZL1_LSSfY=)
- [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6XLVM3xszTzV0fa-7FIouvXgb7Im3y4_pHNVldZYS5siKV-jKSKVI-yd5v1NyLp_ns1PwTL8MB7pyx53ah9qJRv37gf6lZIWkk9tvPv42RCwvfHaVmG6r9kUquljZ)
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM4buvYw_2eEVsrat84Y0S-rC0f1UKaptrwGNHaVhkI2yU0Tq-T2EeyThgFKPB_XUewgzcXz0gcRAu_S00dg5QO35nxMClcFbn_gESgs_dikx6-V1vPGJMpGqYcpDTGQCB0L4=)
- [listendata.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1Lea0NjDsVF6BN48SPMu3GIYH_-Vow7KJQJ01C0HIF4S-yOnrSntg6NKViruLSsk4CfmZJGycd9GEhrCs04LTQBECExkQGh029s7AYd516nDW6yZEjBdY90G9cBf3a1lcMPFJPyWxUkb7avtOw9R7ci3LnuLzHHJuYXC7wCLILA==)


### Github Page 

https://github.com/facebookresearch/omnilingual-asr

