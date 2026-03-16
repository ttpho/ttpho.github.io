---
layout: post
title: "DroidClaw"
subtitle: "Khung làm việc (framework) tự động hóa Android mạnh mẽ kết hợp AI để điều khiển và kiểm thử ứng dụng thông qua ngôn ngữ tự nhiên."
tags: [github]
---

## Giới thiệu

DroidClaw là một công cụ mã nguồn mở được thiết kế để giải quyết sự phức tạp và tính dễ gãy của các kịch bản tự động hóa Android truyền thống. Thay vì phụ thuộc vào các ID phần tử cố định hoặc tọa độ màn hình, DroidClaw sử dụng trí tuệ nhân tạo (AI) để hiểu giao diện người dùng. Ứng dụng thực tế của dự án bao gồm: kiểm thử phần mềm tự động (Automation Testing), xây dựng các tác nhân AI (AI Agents) có khả năng thao tác trên điện thoại như người thật, và thu thập dữ liệu ứng dụng di động một cách thông minh.

## Tính năng chính

1. Khả năng điều khiển thiết bị bằng ngôn ngữ tự nhiên thông qua tích hợp LLM. 2. Nhận diện phần tử giao diện (UI) dựa trên thị giác máy tính và phân tích cấu trúc phân cấp. 3. Hỗ trợ đa nền tảng backend bao gồm Appium và uiautomator2. 4. API tinh gọn, lấy cảm hứng từ Playwright giúp lập trình viên dễ dàng tiếp cận. 5. Cơ chế tự phục hồi (Self-healing) khi giao diện ứng dụng thay đổi nhẹ. 6. Tích hợp sẵn công cụ chụp ảnh màn hình và quay video thao tác để phục vụ phân tích AI.

## Hướng dẫn cài đặt Local (macOS)

Để cài đặt trên macOS, thực hiện các bước sau: 1. Cài đặt Homebrew nếu chưa có. 2. Cài đặt ADB (Android Debug Bridge): 'brew install --cask android-platform-tools'. 3. Cài đặt Python 3.9+: 'brew install python'. 4. Clone repository: 'git clone https://github.com/unitedbyai/droidclaw.git && cd droidclaw'. 5. Tạo và kích hoạt môi trường ảo: 'python3 -m venv venv && source venv/bin/activate'. 6. Cài đặt các thư viện phụ thuộc: 'pip install -r requirements.txt'. 7. Đảm bảo thiết bị Android đã bật 'Tùy chọn nhà phát triển' và 'Gỡ lỗi USB' (USB Debugging) trước khi kết nối.

## Hướng dẫn Docker

Mặc dù dự án ưu tiên chạy local để kết nối USB, bạn có thể sử dụng Docker để đóng gói môi trường logic. Nếu chưa có Dockerfile, bạn có thể tạo một file cơ bản như sau: 'FROM python:3.10-slim \n RUN apt-get update && apt-get install -y android-tools-adb \n WORKDIR /app \n COPY . . \n RUN pip install -r requirements.txt \n CMD ["python", "main.py"]'. Khi chạy container, hãy sử dụng chế độ '--privileged' và map thiết bị USB hoặc kết nối với ADB Server chạy trên Host thông qua IP mạng.

## Ví dụ Code (Example Code)

Dưới đây là ví dụ cơ bản để khởi tạo và tương tác: 'from droidclaw.client import DroidClaw \n \n # Kết nối với thiết bị \n claw = DroidClaw(device_id="emulator-5554") \n \n # Thực hiện các hành động thông minh \n claw.click(text="Cài đặt") \n claw.type(text="Wifi", target_label="Tìm kiếm") \n \n # Sử dụng AI để phân tích màn hình hiện tại \n view_summary = claw.analyze_screen() \n print(f"Màn hình hiện tại chứa: {view_summary}")'


### Github Page 

https://github.com/unitedbyai/droidclaw

