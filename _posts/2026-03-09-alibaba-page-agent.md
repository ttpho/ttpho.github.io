---
layout: post
title: "alibaba/page-agent"
subtitle: "A JavaScript in-page GUI agent that transforms any website into an AI-native app controllable via natural language."
tags: [github]
---

## Giới thiệu

Repository alibaba/page-agent là một giải pháp tự động hóa giao diện web (GUI Agent) thuần Front-end, hoạt động trực tiếp trên trình duyệt bằng JavaScript [1.1]. Thư viện này giải quyết bài toán biến các trang web thông thường thành các ứng dụng tích hợp AI (AI-native apps) mà không cần can thiệp vào backend hay cài đặt thêm phần mềm như Python, Headless Browser hay Extension phức tạp. Ứng dụng thực tế: SaaS AI Copilot (Tích hợp trực tiếp trợ lý AI vào sản phẩm, giúp người dùng thao tác phần mềm bằng ngôn ngữ tự nhiên), Tự động điền form / Smart Form Filling (Rút ngắn các quy trình nghiệp vụ ERP, CRM, Admin system phức tạp), Khả năng truy cập / Accessibility (Giúp người dùng khiếm khuyết dễ dàng điều khiển website qua giọng nói hoặc văn bản thay vì sử dụng thao tác click chuột).

## Tính năng chính

Các tính năng quan trọng nhất bao gồm: Tích hợp cực kỳ đơn giản (Chỉ cần thêm một thẻ script hoặc cài đặt qua npm, mọi quá trình đều diễn ra ngay trên web page của bạn). Thao tác DOM dựa trên văn bản (Hoạt động không cần chụp ảnh màn hình, không cần OCR hay các mô hình LLM đa phương thức nặng nề). Hỗ trợ đa dạng LLM / Bring your own LLM (Tương thích với các model phổ biến như OpenAI, Claude, Qwen, DeepSeek, Gemini hoặc chạy offline với Ollama). Giao diện Human-in-the-loop (Agent có giao diện để hỏi ý kiến hoặc xin xác nhận trước khi thực hiện hành động, loại bỏ rủi ro tự động hóa mù quáng). Quyền riêng tư mặc định (Mọi xử lý đều chạy trên trình duyệt client, dữ liệu không bị gửi đi một cách bí mật). Hỗ trợ Chrome Extension (Tuỳ chọn bổ sung dành riêng cho các tác vụ nâng cao cần điều khiển đa trang hoặc nhiều tab).

## Hướng dẫn cài đặt Local (macOS)

Do PageAgent là một thư viện Front-end JavaScript, bạn cần môi trường Node.js để quản lý project. Thực hiện các bước sau trên Terminal macOS: Bước 1: Cài đặt Node.js qua Homebrew bằng lệnh `brew install node`. Bước 2: Khởi tạo dự án bằng lệnh `mkdir page-agent-demo && cd page-agent-demo` sau đó chạy `npm init -y`. Bước 3: Cài đặt thư viện bằng lệnh `npm install page-agent`. Bước 4: Cấu hình biến môi trường bằng cách tạo file `.env` ở thư mục gốc dự án để lưu trữ API Key của mô hình LLM, ví dụ: `OPENAI_API_KEY=sk-your-api-key-here`. Bước 5: Sử dụng các bundler như Vite hoặc Webpack để build code ES6. (Ngoài ra, bạn cũng có thể sử dụng file script cdn mà không cần cài đặt Node.js bằng cách chèn trực tiếp thẻ script vào file HTML).

## Hướng dẫn Docker (nếu có)

Bản chất PageAgent chạy hoàn toàn ở phía client (trình duyệt) nên repository không yêu cầu sử dụng Dockerfile cho hạ tầng backend hay worker. Tuy nhiên, nếu bạn muốn dùng Docker để host một trang HTML tĩnh có chứa thư viện PageAgent, bạn có thể tạo một file có tên `Dockerfile` trong thư mục gốc với nội dung như sau: `FROM nginx:alpine` ; `RUN rm -rf /usr/share/nginx/html/*` ; `COPY ./index.html /usr/share/nginx/html/index.html` ; `EXPOSE 80` ; `CMD ["nginx", "-g", "daemon off;"]`. Sau đó, build và run Docker trên Terminal bằng các lệnh: `docker build -t page-agent-app .` và `docker run -d -p 8080:80 page-agent-app`. Cuối cùng, mở trình duyệt web và truy cập http://localhost:8080 để trải nghiệm ứng dụng.

## Ví dụ Code (Example Code)

Dưới đây là một đoạn mã JavaScript mẫu minh họa cách tích hợp và gọi hàm của PageAgent để tự động hóa một tác vụ trên giao diện. Đoạn code: `import { PageAgent } from 'page-agent'; const copilot = new PageAgent({ model: 'gpt-4o', apiKey: process.env.OPENAI_API_KEY }); async function runAutomation() { try { console.log('Đang thực thi lệnh...'); await copilot.execute('Điền tên là John Smith vào báo cáo và nhấn nút Submit'); console.log('Tác vụ hoàn tất thành công!'); } catch (error) { console.error('Lỗi trong quá trình chạy:', error); } } document.getElementById('start-btn').addEventListener('click', runAutomation);` (Lưu ý: Nếu không sử dụng NPM modules, bạn có thể thử nghiệm nhanh chóng bằng cách nhúng thẻ `<script src="page-agent.js"></script>` vào trực tiếp bên trong file HTML).

### Sources
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGw_sF2cUKF7H0yPAfPgH_s3WCH6q9jFqh8V18iTktJLoH3R0Dak34V1BybvsMwr2tYGx13yz4njzrkY5FG3BDaUbpGGgISmxCDnIh9ryNeZIH-HKar_iDbBwPGyxJ8rI=)
- [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzKD2d7nm5neoXPFhHXs8Ibm21xX5pHh7ApLwA8_Y54qHJJmN-GWqU_TTZ5pu88LSiHTEQ4BldStvulJuCJW4oUv6o3BCpbLd3L6NP3pQM4GmY5wWLQNRv1xgpGGG5QZU=)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVctTacglVEYQs4sUELK911zEBP6qxTJ-85jf8kbmzTejVMGhJ3865KJ21u3wiuoOeuRpirX2TjcsQLIcIujNgM8nM2aza80U_OhsfvC0BZLyc403aCbrQ4IGEYwnViHBzuulTYQ==)


### Github Page 

https://github.com/alibaba/page-agent

