---
layout: post
title: "Magic Resume (JOYCEQL/magic-resume)"
subtitle: "Trình tạo CV trực tuyến miễn phí mã nguồn mở, hỗ trợ AI (DeepSeek, Doubao) giúp bạn thiết kế hồ sơ chuyên nghiệp nhanh chóng."
tags: [github]
---

## Giớithiệu

MagicResume(魔方简历)làmộttrìnhchỉnhsửasơyếulýlịch(CV)trựctuyến, hiệnđạivàhoàntoànmiễnphí.DựángiúpgiảiquyếtkhókhăntrongviệcthiếtkếvàtốiưuhóaCVchongườitìmviệcbằngcáchcungcấpgiaodiệntrựcquan, khôngcầnđăngkýtàikhoản.ỨngdụngthựctếcủadựánlàgiúpngườidùngtạocácbảnCVchuyênnghiệp, đồngthờitậndụngsứcmạnhcủaAI(nhưDeepSeek, Doubao)đểtựđộngkiểmtralỗingữphápvàlàmnổibậtkinhnghiệmlàmviệc.Đặcbiệt, mọidữliệuđềuđượclưutrữhoàntoàntrênthiếtbịnộibộ(LocalStorage), đảmbảoquyềnriêngtưvàantoànthôngtintuyệtđối[1.2].

## Tính năng chính

Các tính năng quan trọng nhất của dự án bao gồm: 1. Hỗ trợ AI thông minh: Tích hợp API DeepSeek và Doubao giúp kiểm tra ngữ pháp và tối ưu hóa câu từ tự động. 2. Trải nghiệm hiện đại: Được xây dựng trên nền tảng Next.js 14+ / TanStack Start cùng thư viện Motion cho các hiệu ứng chuyển động mượt mà. 3. Xem trước thời gian thực (Real-time preview) và tính năng tự động lưu (Auto-save). 4. Giao diện linh hoạt: Hỗ trợ nhiều chủ đề (themes), chế độ Dark Mode và thiết kế Responsive. 5. Lưu trữ nội bộ: Bảo mật dữ liệu bằng cách lưu trữ ở mức ổ cứng cục bộ (Local Storage). 6. Xuất định dạng đa dạng: Dễ dàng xuất CV sang file PDF hoặc JSON để thuận tiện sao lưu và nộp đơn.

## Hướng dẫn cài đặt Local (macOS)

Để khởi chạy Magic Resume trên máy macOS, bạn cần thực hiện theo các bước sau: Bước 1: Mở ứng dụng Terminal và cài đặt Homebrew (nếu chưa có) bằng lệnh /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)". Bước 2: Dùng Homebrew để cài đặt Node.js và pnpm bằng lệnh brew install node và brew install pnpm. Bước 3: Tải mã nguồn dự án về máy bằng lệnh git clone https://github.com/JOYCEQL/magic-resume.git và di chuyển vào thư mục dự án bằng cd magic-resume. Bước 4: Cài đặt các thư viện cần thiết bằng lệnh pnpm install. Bước 5: Tạo file .env ở thư mục gốc để cấu hình khóa API (ví dụ: NEXT_PUBLIC_DEEPSEEK_API_KEY). Bước 6: Khởi chạy môi trường phát triển bằng lệnh pnpm dev. Mở trình duyệt và truy cập vào địa chỉ http://localhost:3000 để bắt đầu trải nghiệm dự án.

## Hướng dẫn Docker

Dự án Magic Resume hỗ trợ triển khai bằng Docker giúp việc cài đặt trở nên đơn giản. Bạn cần đảm bảo hệ thống đã cài đặt sẵn Docker và Docker Compose. Cách nhanh nhất là mở Terminal, truy cập vào thư mục mã nguồn và chạy lệnh: docker compose up -d. Lệnh này sẽ tự động đọc file docker-compose.yml có sẵn, thiết lập biến môi trường NODE_ENV=production, và chạy container trên cổng 3000 ở chế độ nền. Sau khi quá trình tải hoàn tất, bạn có thể sử dụng hệ thống qua http://localhost:3000. Dự án đã có sẵn Dockerfile ở thư mục gốc. Nếu bạn muốn tự tạo một image cơ bản cho ứng dụng Node.js/Next.js tương tự, cấu trúc file Dockerfile sẽ là: FROM node:18-alpine, WORKDIR /app, COPY package.json pnpm-lock.yaml ./, RUN npm install -g pnpm && pnpm install, COPY . ., RUN pnpm build, EXPOSE 3000, và CMD ["pnpm", "start"].

## Ví dụ Code (Example Code)

Dưới đây là một ví dụ minh họa về cấu trúc dữ liệu JSON (Resume Schema) chuẩn được Magic Resume sử dụng để lưu trữ và hiển thị hồ sơ. Bạn có thể sử dụng đoạn mã JSON này để import trực tiếp vào giao diện ứng dụng: {"basics": {"name": "Nguyễn Văn A", "label": "Kỹ sư Phần mềm", "email": "nguyenvana@example.com", "phone": "+84 123 456 789", "url": "https://github.com/nguyenvana", "summary": "Lập trình viên với 3 năm kinh nghiệm phát triển ứng dụng web hiện đại.", "location": {"city": "Hà Nội", "countryCode": "VN"}}, "work": [{"company": "Công ty TNHH Công nghệ", "position": "Lập trình viên Frontend", "startDate": "2021-01", "endDate": "2024-01", "highlights": ["Tối ưu hóa hiệu suất website, giảm 50% thời gian tải trang.", "Tích hợp API để tự động hóa quy trình."]}]}. Ngoài ra, bạn có thể thiết lập khóa API AI trực tiếp trên giao diện trình duyệt hoặc khai báo thông qua file .env bằng các biến môi trường tương tự như NEXT_PUBLIC_DEEPSEEK_API_KEY=my_key.

### Sources
- [magicv.art](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrGucz_qNcmtE383oMAo44PH5i5vSKC0_-i61EJuxz1zZsbXECUNVaGOQ11a-7wlkuRGAbPE_DDaYuNE_O0sA5nxFKEeGvmOG1KF0vb2iz_w==)
- [magicv.art](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7ZNi4pw3hYXnVdqqO8hBokE3bKF6N4lpqQX6D2wwvZwkGlLhZ9GpX5KOYQBb63La5bEwWuUjcYbACk8VWIezPmdvDuuZNuLkT2NwYh29UXQ==)
- [laoda.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4Iq-RaHJ-XSlCgwPZel_IasEmHOCdNFL6a8P4MfS5OlUfLJRZPyAb8VgOar-qW9pDlbZaejtLH3dNXQUxIZNXCulgj9-ZvD4Sa9GuOS74-x378U1Ydl8TZ5PrVtpkSKHhxGrdsCIUUBBqlSgKFOZYSb4Bmvi70MiAJaH_iw==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt3tPUkxlLfA8AwasTcFFlkVL3x0kd_dEwuLCsWN6OooOOe0xzLlwdfZvgzV-zeRNXH92qgaepOH4rRIDx51xhjRfCn9HWX1UNPoQVf-eWAoSIldQkn2lw-tYG1u5grEKXvQ==)
- [iwanlab.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzGon_aELTVrtLwNZn-J-gzB06OyaO5PDUMtpHtR2GEzAh26c-o5wqWtGukyk4gR4oHn4UrGDYvYKv5tpCJT5p2hWEyUU9BM5xDNkefdHrAKwakxs8GJUu91hcKffJd2i6seYh1XYd7CreRd6wKeIdyKI=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPKVTyHCpOqMGoO7to7dDm95Sn1FVXi44uTLw-TbZt5GuDEVF6TYQTS6--Ua06yEJZQ3YFQ9QdTAk6R3hz-2c8foaRQT-WmsXoY80LeUJhVy04Dsc48Bh37lvabyqOd2G_5pJrKLMwXtk=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNtA0fINXTHRXMCnumIrE-_1fpFiu29h9xHyaMKUc240yZwmqS9cEs1vUmI9EyBHhWCLp0c7p-C6bP2YaguDCjl_IThA2ZLj_PVquT5ro2W7DeqvY-STCWivo-G4dOc5MqQpNWuwaMOdcALvpw3VFv)


### Github Page 

https://github.com/JOYCEQL/magic-resume

