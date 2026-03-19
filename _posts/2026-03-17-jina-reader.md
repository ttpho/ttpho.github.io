---
layout: post
title: "Jina Reader"
subtitle: "Chuyển đổi bất kỳ URL nào thành định dạng Markdown chất lượng cao, tối ưu cho LLM và RAG."
tags: [github]
---

## Giới thiệu

Jina Reader là một công cụ mã nguồn mở mạnh mẽ giúp chuyển đổi các trang web từ HTML phức tạp sang định dạng Markdown tinh gọn. Vấn đề lớn nhất mà nó giải quyết là loại bỏ các thành phần 'rác' như quảng cáo, thanh điều hướng và mã script để chỉ giữ lại nội dung chính yếu. Điều này cực kỳ hữu ích cho việc xây dựng các ứng dụng Retrieval-Augmented Generation (RAG), cung cấp dữ liệu sạch cho các mô hình ngôn ngữ lớn (LLM) và tự động hóa quy trình thu thập thông tin web.

## Tính năng chính

- Chuyển đổi Markdown: Trích xuất nội dung cốt lõi và định dạng lại thành Markdown chuẩn.
- Loại bỏ nội dung thừa: Tự động lọc bỏ headers, footers và quảng cáo dựa trên thuật toán thông minh.
- Hỗ trợ Multimedia: Có khả năng đọc hình ảnh và trích xuất thông tin từ chúng.
- Tương thích cao: Tích hợp dễ dàng với các framework AI như LangChain hoặc LlamaIndex.
- Tốc độ tối ưu: Xử lý nhanh chóng ngay cả với các trang web nặng.

## Hướng dẫn cài đặt Local (macOS)

1. Cài đặt Node.js: Đảm bảo bạn đã cài Homebrew, sau đó chạy `brew install node`.

2. Clone repository: Chạy lệnh `git clone https://github.com/jina-ai/reader.git && cd reader`.

3. Cài đặt dependencies: Sử dụng lệnh `npm install` hoặc `pnpm install` nếu bạn có pnpm.

4. Thiết lập biến môi trường: Tạo file `.env` từ `.env.example` và điều chỉnh các cổng (mặc định là 3000).

5. Khởi chạy: Chạy lệnh `npm run dev` để bắt đầu server tại địa chỉ http://localhost:3000.

## Hướng dẫn Docker

Để chạy Jina Reader bằng Docker, bạn có thể sử dụng image chính thức từ Docker Hub hoặc build thủ công:

- Build thủ công: `docker build -t jina-reader .`

- Khởi chạy container: `docker run -p 3000:3000 jina-reader`

- Sử dụng bản build sẵn: `docker run -p 3000:3000 jinaai/reader:latest`. Sau khi chạy, bạn có thể truy cập bằng cách thêm URL vào sau địa chỉ server, ví dụ: http://localhost:3000/https://google.com.

## Ví dụ Code (Example Code)

Dưới đây là cách sử dụng đơn giản bằng JavaScript (Fetch API) để lấy nội dung Markdown từ một trang web qua instance local:


```javascript

const targetUrl = 'https://example.com';
const readerUrl = `http://localhost:3000/${targetUrl}`;


fetch(readerUrl)
.then(res => res.text())
.then(markdown => {
console.log('Nội dung đã chuyển đổi:');
console.log(markdown);\n  })
.catch(err => console.error('Lỗi khi đọc trang:', err));

```


### Github Page 

https://github.com/jina-ai/reader

