---
layout: post
title: "MarkItDown"
subtitle: "Công cụ Python mạnh mẽ từ Microsoft giúp chuyển đổi mọi định dạng tài liệu sang Markdown để phục vụ phân tích dữ liệu và AI."
tags: [github]
---

# GitExpert Analysis Result

## Giới thiệu & Mục đích

MarkItDown là một tiện ích Python mã nguồn mở được phát triển bởi Microsoft. Mục đích chính của nó là chuyển đổi các tệp tin ở nhiều định dạng khác nhau (như PDF, Word, Excel, PowerPoint, hình ảnh, âm thanh...) sang định dạng Markdown chuẩn. Điều này đặc biệt hữu ích trong kỷ nguyên AI hiện nay, khi Markdown là định dạng đầu vào lý tưởng cho các Mô hình Ngôn ngữ Lớn (LLM) và các hệ thống RAG (Retrieval-Augmented Generation), giúp máy tính 'đọc' và hiểu cấu trúc tài liệu tốt hơn so với văn bản thô.

## Tính năng chính

- **Hỗ trợ đa định dạng văn phòng:** Chuyển đổi mượt mà các file Microsoft Office (Word .docx, PowerPoint .pptx, Excel .xlsx) giữ nguyên tiêu đề, bảng biểu và danh sách.
- **Xử lý PDF:** Trích xuất nội dung từ file PDF sang Markdown.
- **Hỗ trợ đa phương tiện (Multimodal):** Tích hợp OCR để đọc chữ từ ảnh và tính năng Transcription để chuyển đổi file âm thanh sang văn bản.
- **Tích hợp LLM:** Có khả năng kết nối với các mô hình như GPT-4 để tạo mô tả chi tiết cho hình ảnh (image captioning) thay vì chỉ lấy metadata.
- **Hỗ trợ định dạng dữ liệu & Web:** Xử lý tốt HTML, CSV, JSON, XML và thậm chí duyệt qua nội dung file nén ZIP.

## Hướng dẫn cài đặt Local (macOS)

Để chạy MarkItDown trên macOS, bạn cần cài đặt Python 3.10 trở lên.

1. **Cài đặt Python (nếu chưa có):**
   Sử dụng Homebrew:
   ```bash
   brew install python
   ```

2. **Cài đặt thư viện MarkItDown:**
   Khuyến nghị cài đặt phiên bản đầy đủ dependencies để hỗ trợ mọi định dạng:
   ```bash
   pip install "markitdown[all]"
   ```

3. **Cài đặt công cụ hỗ trợ (Optional):**
   Nếu bạn định chuyển đổi file âm thanh hoặc một số định dạng đặc thù, hãy cài thêm `ffmpeg`:
   ```bash
   brew install ffmpeg
   ```

4. **Kiểm tra cài đặt:**
   Chạy lệnh sau để xem hướng dẫn sử dụng CLI:
   ```bash
   markitdown --help
   ```

## Hướng dẫn Docker

Nếu bạn muốn chạy trong môi trường container cô lập hoặc không muốn cài nhiều dependencies lên máy, bạn có thể tự tạo một Dockerfile đơn giản như sau:

**1. Tạo file `Dockerfile`:**
```dockerfile
FROM python:3.11-slim

# Cài đặt các gói hệ thống cần thiết (ffmpeg cho audio, pandoc nếu cần)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Cài đặt markitdown với đầy đủ tính năng
RUN pip install "markitdown[all]"

WORKDIR /app
ENTRYPOINT ["markitdown"]
```

**2. Build Docker Image:**
```bash
docker build -t markitdown .
```

**3. Run Container:**
Ví dụ chuyển đổi file `document.docx` trong thư mục hiện tại:
```bash
docker run --rm -v $(pwd):/app markitdown document.docx > document.md
```

## Ví dụ Code (Example Code)

Dưới đây là đoạn code Python minh họa cách sử dụng MarkItDown để chuyển đổi một file Excel sang Markdown:

```python
from markitdown import MarkItDown

# Khởi tạo instance
md = MarkItDown()

# Chuyển đổi file (hỗ trợ xlsx, docx, pptx, pdf, v.v.)
result = md.convert("bang_tinh_tai_chinh.xlsx")

# In kết quả Markdown ra màn hình
print(result.text_content)

# Nếu muốn dùng LLM để mô tả ảnh (cần OpenAI API Key):
# from openai import OpenAI
# client = OpenAI(api_key="sk-...")
# md_ai = MarkItDown(llm_client=client, llm_model="gpt-4o")
# result_ai = md_ai.convert("bieu_do.jpg")
# print(result_ai.text_content)
```

## Nguồn tham khảo

- [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7qXB_8eZS45DugztLjsGYniyKuk3a4WzqhUFvYhdU05_Hp55aLlWNabFmLvaoEZOiiwuRgmkSBGY-cJwh_3PbScqfuz7PW6frFMscAgLyH1KCc9Hq43U15ju59ovZ_wDJeC1_fcNxEY3h1eGFjSzBkXTs9OrsBW_7AVY=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj9k7mq1TE3Ov5bbohpMs9J_4uJDvP2CecKr69Xn_JjMz9MEIQnczdYdUmgNzgWRyxxWS8Z5AGvGle-Z6-mVnIJqcGcFoNDJwDKz_dfR9_aiUqo4fKXKxa42ufdR5CdYyQMFreWupg8hrg_4o1wEAUgpQ0avlN0ENpjpE3eeqE9Cya26rC53R2eMw3U59uqxdDi3W5GINSW-cmwOVeZc8tdpP-WR8yBSOmm0-pmCzdDPLTTFQh-RYWYgpWQaPpAIk=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgY5wyCeeShkzXZet5gdOOFQdMBGen0NQkH2EkznwShhE98Px8KnssI_pTGWC1_hI_4-gUmuEAPgE1cXSvFxVNxxEgHQPpow3rgR5nrWMD_TPPe0S2-6tzABWRkUke7s_USuv25EHoAVEcy5qV9vl37tbLsIDP)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP9pQfZuWSHBjkyK6MV0wNFBRJU_FLMU6CTZRxYOjKXdimQuILRxvLbgTmyFizvNcvvYeyk9gPWfku03nspkIUOHXl66RDgUE_f_M-yk8xlu-fDgm6lntaRYvATgeib4ZTmQ==)
- [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOYyv4mZs-n1r6sZ5QSclFbir_nCzC6MxHWP6BX3Yk8uN8OirbadbmCbQ5378L0SkzcHMziLjGJ_KJRp_RNG5baYdVcJfBtqBp8QRWhPY5eR8-UD2wuc8MiODRsgTpS_s2koijELHXQc5GYgMswuBhGx7uAH5CHrvkUHfFt7tUnX2m5dx_2-UWMfTo-9IFsh7YK42ZTFZxR7BC)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrWPkGygo6N2n4J4HrDv8kB05YgHZDf-O6NYNt-UURGN7VasdXcYvZpE5_xhf7PG98SilIkAw-pH2FraUk1y_luKpAHB_qzw5HDsZi6LpPKeDMSwZwf1f3KWOdCBqST6x2gfSD8iHUROqsWWmGmp1cKnKjb8ItMO4A52emRTVauJwQRk3-5H86p2nh3T3LjlpHyQ5If9fZyySJxYnMvA==)
- [realpython.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTIxofkxrFjFmz8otKohNvLrrUhkxZKEqJ_bMoloGCtEe03GeLeH1qboWyeFlH59CnzFxEu4Z-TlkM7kubr3F2OQjUrQ1RAHLSwt2fvrt6z1-LCvzMmGJuyDCj7u3pYh4ZDGAJ)
- [avonture.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB5Qx702YA7ch9jnSHUsFKoE8MQ6YSAZPxvgc7EApkryKaziKlv7Mylxl1VEPkrLsr2iPXtl5rGxbmc7OB4BClwAyfXU3NWcsIVp8jkBSyEVhxjjA4L3pP_DVC7JWOPEBFU0Q=)
- [mcpmarket.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4qCwreOQ5-2tljQKI_b6vxecQ503RAzeU0Bb7wLn1aZEtbZ1rwadTC8kdxz4yc75bYxq4hGUlsZFO8qTzBMUFX2J5qhvGxmLY5AYfqr9gZTJn5eEIheqnwlgqeVXgWfz2-ed3)
- [skywork.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESQfSpAE1HVk9VOqV175XarT8RCModgPfuIvxvXYnGwpmPp4mr-nkRzag24SFnShHD1_1BSUJpQfjKlA8f4SLYKlXGBWQ3ZxSUc2qe_ilW0Gd9pPltb-PTp7iETnVQ1Bnte3Dy8TcW_hmlu9z_st3Oaw2WnDCwxv1VbSYLFjfF0tJdG5Ilcz1nCA==)
- [x-cmd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcj7FJdfH3PAlGsliOEdtvqCuA10axhaJKGFQXayNZyNAkmteSqJQj8J8c-ywVf0ZDTl6eopAN8BfdG2s9bmuSnr4XlUzYw_1rl5tndcR_KEp3k7b05pVEei7SO2u9AikiivLW)
- [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1E0PtBDASoqJ-fT7Z3plvVcEAjzvsM8iB4mlOBMkuOpcFJipxb6QR2rwnTu6f9WAnUrVcuYYiO_9A_xh9-EYdRK2zUBUG7oy9fNCCnt1BELvTR37b3uaYWhO4J0d7yZZD6EYawIRkpxaSHHX3bL0ux3KSAkYbUkRcn4VKHIw-ddbV2IrlrhhruuZzBM8I7z8pN1IJPpaNRldfTw==)


### Github Page 

https://github.com/microsoft/markitdown

