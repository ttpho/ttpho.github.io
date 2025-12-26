---
layout: post
title: Agentic AI
subtitle: Agentic AI - 101
cover-img: https://plus.unsplash.com/premium_photo-1726079246917-46f2b37f7e9e
tags: [AI]
---

# Agentic AI 

### Online course

#### Hugging Face

[https://huggingface.co/learn](https://huggingface.co/learn/agents-course/unit0/introduction)


#### Microsoft

https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/


#### Google Skill 

https://www.skills.google/paths/1951/course_templates/1267

#### Deep Learning AI 

https://www.deeplearning.ai/courses/agentic-ai/


### Overview

**Agentic AI** (Trí tuệ nhân tạo có tính tác nhân) là bước tiến tiếp theo của AI, nơi máy móc không chỉ "biết nói" hay "biết viết" mà còn **"biết làm"**.

Nếu Generative AI (như ChatGPT) là một người trợ lý giỏi trả lời câu hỏi, thì Agentic AI là một **cộng sự tự chủ** có khả năng nhận một mục tiêu lớn, tự lập kế hoạch và thực hiện các bước nhỏ để hoàn thành mục tiêu đó mà không cần bạn cầm tay chỉ việc.

Dưới đây là những điểm cốt lõi để bạn hiểu về Agentic AI:

### 1. Sự khác biệt giữa các thế hệ AI

| Đặc điểm | Generative AI (AI Tạo sinh) | Agentic AI (AI Tác nhân) |
| --- | --- | --- |
| **Vai trò** | Trợ lý nội dung | Cộng sự thực thi |
| **Cách hoạt động** | Phản hồi theo câu lệnh (Prompt) | Tự chủ thực hiện mục tiêu (Goal-oriented) |
| **Mức độ phụ thuộc** | Cần con người hướng dẫn từng bước | Tự lập kế hoạch, tự chọn công cụ |
| **Ví dụ** | "Viết cho tôi một email gửi khách hàng" | "Hãy chăm sóc khách hàng này cho đến khi họ chốt đơn" |

### 2. Bốn năng lực cốt lõi của Agentic AI

Để một hệ thống được coi là "Agentic", nó thường sở hữu vòng lặp **Perceive – Reason – Act – Learn** (Cảm nhận – Suy luận – Hành động – Học hỏi):

* **Tính tự chủ (Autonomy):** Có thể hoạt động độc lập trong thời gian dài mà không cần con người giám sát liên tục.
* **Khả năng lập kế hoạch (Planning):** Biết chia nhỏ một yêu cầu phức tạp thành một chuỗi các tác vụ khả thi (ví dụ: để đặt một chuyến du lịch, nó biết phải check giá vé, đặt phòng, rồi mới sắp xếp lịch trình).
* **Sử dụng công cụ (Tool Use):** Biết tự tìm và sử dụng các công cụ bên ngoài như truy cập web, gọi API, sử dụng phần mềm kế toán hoặc gửi email.
* **Tự phản tư (Self-Reflection):** Biết tự kiểm tra kết quả mình vừa làm, nếu thấy sai sót sẽ tự sửa đổi kế hoạch để đạt mục tiêu tốt hơn.

### 3. Ví dụ thực tế

* **Trong công việc:** Thay vì bạn phải tự trích xuất dữ liệu từ file PDF, rồi dán vào Excel, rồi gửi email báo cáo; bạn chỉ cần ra lệnh: *"Hàng tuần, hãy tổng hợp doanh số từ các hóa đơn gửi về và gửi báo cáo phân tích cho sếp"*. Agentic AI sẽ tự động canh giờ, mở file, xử lý số liệu và gửi thư.
* **Trong nghiên cứu:** AI có thể tự tìm kiếm tài liệu, tóm tắt các nguồn uy tín, đối chiếu các số liệu mâu thuẫn và viết thành một báo cáo hoàn chỉnh.

### 4. Tại sao nó quan trọng?

Agentic AI đang biến AI từ một công cụ "hỏi-đáp" thành một "lực lượng lao động kỹ thuật số". Điều này giúp doanh nghiệp tối ưu hóa những quy trình phức tạp mà trước đây bắt buộc phải có con người điều phối ở giữa các bước.


# Agentic Design Patterns

### Overview 

Agentic Design Patterns (Mẫu thiết kế tác nhân) là tập hợp các phương pháp và cấu trúc tư duy giúp xây dựng các hệ thống AI có khả năng hoạt động tự chủ, thông minh và hiệu quả hơn.

Thay vì chỉ gửi một câu lệnh (prompt) và nhận một câu trả lời duy nhất (Zero-shot), các mẫu thiết kế này tạo ra một quy trình làm việc (workflow) giúp AI biết tự đánh giá, lập kế hoạch và sửa lỗi. Khái niệm này được phổ biến rộng rãi bởi Andrew Nguyen (chuyên gia hàng đầu về AI).

Tại sao cần Agentic Design Patterns?

* **Độ chính xác cao hơn:** Giảm thiểu tình trạng AI "ảo tưởng" (hallucination) nhờ cơ chế kiểm tra chéo và phản tư.
* **Giải quyết việc khó:** Có thể xử lý các dự án kéo dài và cần nhiều bước logic phức tạp.
* **Tính linh hoạt:** AI có thể tự điều chỉnh hướng đi nếu gặp lỗi trong quá trình thực hiện thay vì dừng lại hoàn toàn.

Dưới đây là 4 mẫu thiết kế Agentic cốt lõi:


**Agentic Design Patterns** (Mẫu thiết kế tác nhân) là tập hợp các phương pháp và cấu trúc tư duy giúp xây dựng các hệ thống AI có khả năng hoạt động tự chủ, thông minh và hiệu quả hơn.

Thay vì chỉ gửi một câu lệnh (prompt) và nhận một câu trả lời duy nhất (Zero-shot), các mẫu thiết kế này tạo ra một **quy trình làm việc (workflow)** giúp AI biết tự đánh giá, lập kế hoạch và sửa lỗi. Khái niệm này được phổ biến rộng rãi bởi Andrew Ng (chuyên gia hàng đầu về AI).

Dưới đây là 4 mẫu thiết kế Agentic cốt lõi:

### 1. Reflection (Phản tư/Tự đánh giá)

Đây là mẫu thiết kế đơn giản nhưng cực kỳ mạnh mẽ. Thay vì chấp nhận kết quả đầu tiên, AI được yêu cầu tự kiểm tra và cải thiện kết quả của chính mình.

* **Cách hoạt động:** AI tạo ra bản thảo -> AI tự đóng vai "người kiểm duyệt" để tìm lỗi hoặc điểm yếu -> AI tự sửa đổi dựa trên những góp ý đó.
* **Ví dụ:** Bạn bảo AI viết code. Thay vì chạy ngay, AI sẽ tự đọc lại code để tìm lỗi bảo mật hoặc tối ưu hóa hiệu suất trước khi đưa cho bạn.

### 2. Tool Use (Sử dụng công cụ)

AI được cấp quyền truy cập vào các công cụ bên ngoài (Search engine, máy tính, trình chạy code, API ngân hàng...) để thực hiện các công việc mà mô hình ngôn ngữ không tự làm được.

* **Cách hoạt động:** AI phân tích yêu cầu -> Nhận ra mình cần dữ liệu thực tế hoặc tính toán -> Chọn công cụ phù hợp -> Đọc kết quả từ công cụ để hoàn thành tác vụ.
* **Ví dụ:** "Hãy phân tích giá cổ phiếu Apple hôm nay". AI sẽ tự dùng công cụ tìm kiếm hoặc API tài chính thay vì trả lời dựa trên dữ liệu cũ.

### 3. Planning (Lập kế hoạch)

Mẫu này dành cho các nhiệm vụ phức tạp, không thể giải quyết trong một bước. AI sẽ chia nhỏ mục tiêu lớn thành các bước nhỏ hơn.

* **Cách hoạt động:** AI xây dựng một "lộ trình" (roadmap) -> Thực hiện từng bước -> Sau mỗi bước, nó đánh giá lại xem có cần thay đổi kế hoạch ban đầu hay không.
* **Ví dụ:** "Hãy lên kế hoạch và đặt một chuyến du lịch 3 ngày tại Đà Lạt". AI sẽ tự chia nhỏ: 1. Tìm vé máy bay, 2. Tìm khách sạn, 3. Lên lịch trình ăn uống, 4. Kiểm tra thời tiết để điều chỉnh.

### 4. Multi-agent Collaboration (Hợp tác đa tác nhân)

Đây là cấp độ cao nhất, nơi nhiều "đặc vụ" AI khác nhau phối hợp với nhau, mỗi đặc vụ đảm nhận một vai trò chuyên biệt.

* **Cách hoạt động:** Giống như một công ty thu nhỏ. Có Agent đóng vai Quản lý (Manager), Agent là Lập trình viên (Coder), Agent là Kiểm thử (Tester). Chúng thảo luận và làm việc cùng nhau.
* **Ví dụ:** Trong việc phát triển phần mềm, một Agent viết code, một Agent khác viết kịch bản kiểm thử, và một Agent thứ ba kiểm tra xem code có đáp ứng yêu cầu của khách hàng không.



