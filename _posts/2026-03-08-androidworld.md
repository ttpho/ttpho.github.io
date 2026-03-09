---
layout: post
title: "AndroidWorld"
subtitle: "Môi trường và hệ thống đánh giá (benchmark) động dành cho các tác nhân AI tự hành tương tác trên thiết bị Android."
tags: [github]
---

## Giới thiệu

AndroidWorld là một môi trường và hệ thống benchmark mã nguồn mở do Google Research phát triển [1.1], dành cho các tác nhân AI (autonomous agents) trên nền tảng di động. Dự án này giải quyết vấn đề thiếu hụt các môi trường tương tác thực tế và công cụ đo lường độ chính xác khi AI thực hiện các tác vụ điều khiển điện thoại (như vuốt, chạm, nhập text). Thay vì đánh giá dựa trên các bộ dữ liệu tĩnh, AndroidWorld tạo ra một môi trường giả lập sống động với khả năng chấm điểm (reward) dựa trên trạng thái thực tế của hệ thống hệ điều hành (thông qua ADB). Ứng dụng thực tế của dự án là phục vụ nghiên cứu, đào tạo và kiểm thử các trợ lý ảo, giúp chúng có khả năng tự động hóa các quy trình công việc phức tạp trên smartphone của con người.

## Tính năng chính

- Cung cấp 116 tác vụ đa dạng trải dài trên 20 ứng dụng Android thực tế trong một môi trường mở.
- Khởi tạo tác vụ động (Dynamic task instantiation): Tự động tạo ra hàng triệu biến thể tác vụ với các tham số ngẫu nhiên để tránh việc AI học vẹt.
- Hệ thống phần thưởng đáng tin cậy (Durable reward signals): Đánh giá thành công của tác vụ qua việc kiểm tra trực tiếp trạng thái hệ thống (database, file system) thay vì chỉ phân tích giao diện UI.
- Dung lượng nhẹ: Chỉ yêu cầu khoảng 2 GB RAM và 8 GB bộ nhớ đĩa cho môi trường.
- Tính mở rộng cao: Cho phép các nhà nghiên cứu dễ dàng bổ sung các ứng dụng và tác vụ đánh giá mới.
- Tích hợp sẵn bộ benchmark web nổi tiếng MiniWoB++.

## Hướng dẫn cài đặt Local (macOS)

Để chạy AndroidWorld trên macOS, bạn cần cài đặt Android Emulator và môi trường Python. Thực hiện các bước sau:

1. Cài đặt Android Studio & Emulator:
- Tải và cài đặt Android Studio.
- Mở Virtual Device Manager (AVD), tạo một máy ảo mới với cấu hình: Hardware là Pixel 6, System Image là Tiramisu (API Level 33), và đặt tên AVD là `AndroidWorldAvd`.

2. Khởi chạy Emulator qua Command Line:
- Không chạy qua UI mà hãy chạy lệnh sau để bật cổng GRPC (giúp giao tiếp với app Accessibility):
```bash
export EMULATOR_NAME="AndroidWorldAvd"
~/Library/Android/sdk/emulator/emulator -avd $EMULATOR_NAME -no-snapshot -grpc 8554
```

3. Cài đặt môi trường Python (Khuyến nghị dùng Conda):
- Tạo và kích hoạt môi trường Python 3.11.8:
```bash
conda create -n android_world python=3.11.8
conda activate android_world
```

4. Clone source code và cài đặt:
```bash
git clone https://github.com/google-research/android_world.git
cd android_world
pip install -r requirements.txt
python setup.py install
```

## Hướng dẫn Docker (Experimental)

AndroidWorld cung cấp tính năng hỗ trợ Docker thử nghiệm (Experimental Docker Support), giúp gói gọn Android Emulator và một FastAPI server vào chung một container để đảm bảo môi trường đồng nhất. Bạn có thể xem các script có sẵn như `scripts/run_suite_on_docker.py` để tương tác với server này.

Nếu bạn chỉ muốn tạo một Dockerfile cơ bản đóng vai trò làm Client (kết nối đến Emulator đang chạy trên máy Host), bạn có thể dùng đoạn code sau:

```dockerfile
# Sử dụng image Python 3.11
FROM python:3.11.8-slim

# Cài đặt git và các thư viện cần thiết
RUN apt-get update && apt-get install -y git

# Thiết lập thư mục làm việc
WORKDIR /app

# Clone repository
RUN git clone https://github.com/google-research/android_world.git .

# Cài đặt dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py install

# Cấu hình biến môi trường
ENV PYTHONUNBUFFERED=1

# Chạy script mặc định
CMD ["python", "minimal_task_runner.py"]
```

## Ví dụ Code (Example Code)

Dự án đi kèm một tệp `minimal_task_runner.py` để minh họa cơ chế hoạt động. Dưới đây là đoạn code mẫu mô phỏng lại cách khởi tạo môi trường, thiết lập tác vụ và chạy một Agent (như M3A) trên AndroidWorld:

```python
import android_world
from android_world.agents import m3a
from android_world.env import interface

# Khởi tạo môi trường giao tiếp với thiết bị Android (Emulator đang chạy qua cổng grpc 8554)
env = interface.AsyncEnv()

# Lấy danh sách tác vụ và chọn một tác vụ cụ thể
task_registry = android_world.registry.TaskRegistry()
# Ví dụ: Tạo sự kiện trên app Lịch. Nếu không truyền, một task ngẫu nhiên sẽ được chọn.
task = task_registry.get_task("create_calendar_event")

# Khởi tạo agent mặc định M3A
# Lưu ý: Cần export biến môi trường OPENAI_API_KEY nếu dùng mô hình GPT-4
agent = m3a.M3A(model_name="gpt-4-turbo-2024-04-09")

print(f"Đang thực thi tác vụ: {task.name}")

# Chạy agent trên environment
success = agent.run(env, task)

if success:
    print("Tác vụ đã được hoàn thành thành công!")
else:
    print("Agent chưa thể hoàn thành tác vụ này.")
```

### Sources
- [alphaxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcjyGej-qUSh9TcAgomylKhd7fHJ_nYVhIVCU84eaTM2twwaECdFsi-ogXfYmic1CPcaJKzXoCrqBrRSwxXEXk82ZrPgO9O7eg-usw1Dk9s3olPoF0b2JlEhXVzO_C7ZEyBMc5Hwh9cqOON5yp2E6nIe4u8xDyselA6Q==)
- [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUZP4485IkMaJZy22Hi5hGbG6AVUCt2cnCQt32riU9eHNLnv1CbBY31vqcLGHL5Fc68W1AK-kvdWhIVUvs_Mqdw1ZuaUaEplarPePqIMAjrPHbDYmuu8vvJO4G)
- [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgdw_kQPl1GmA0w4mAQ4rlg9kikahv59W8g5dtK4i1q2r_pp5OQJpdB1aoLL8bM98fWCHPPzHeojBmTqT0s4B0i3JzMkiX41thQAhGf1EmcOsYkKw8uAhGiNKV7fZoGMXzer8t)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfvgEPvLUe6O0Q3E--FN_D_fyvqW4umK4USN2kikU3UecRNFDTjDzQIHffVWWxlhvCNGfTB6gxDYilocadcZrjvq3ebtuqFXik4bSZkUmsP_D9OyQvxmvfQFM_k-Ucj61dNyxbJhImWn0s)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwZ-dSq-P8LA4B733Kk5_-TwhCP0-qq41RbJMZPNETln1PtIQfQbceNPzYy6gVtRLFafNbplbAj5giWwQwMu0pdOMnA891SAswart9259NRSSjfMyLwovUFUP4F--a5r3EqXPnJXnewIER)


### Github Page 

https://github.com/google-research/android_world

