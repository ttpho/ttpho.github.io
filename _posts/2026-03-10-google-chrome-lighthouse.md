---
layout: post
title: "Google Chrome Lighthouse"
subtitle: "Công cụ tự động mã nguồn mở giúp phân tích, đánh giá và cải thiện chất lượng toàn diện của các trang web."
tags: [github]
---

## Giới thiệu

Lighthouse là một công cụ mã nguồn mở tự động do Google phát triển nhằm giúp các nhà phát triển nâng cao chất lượng trang web. Dự án này giải quyết các khó khăn trong việc đánh giá hiệu suất (performance), khả năng truy cập (accessibility), tối ưu hóa công cụ tìm kiếm (SEO) và tiêu chuẩn Progressive Web Apps (PWA) bằng cách cung cấp hệ thống kiểm tra (audits) toàn diện. Trong thực tế, Lighthouse có thể được sử dụng trực tiếp qua Chrome DevTools, công cụ dòng lệnh (CLI), hoặc được tích hợp như một Node module để tự động hóa quy trình kiểm định chất lượng website trong các hệ thống CI/CD.

## Tính năng chính

- Đánh giá hiệu suất (Performance): Đo lường các chỉ số cốt lõi của trang web như First Contentful Paint (FCP), Largest Contentful Paint (LCP) và Cumulative Layout Shift (CLS).\n- Đánh giá khả năng truy cập (Accessibility): Đảm bảo trang web tuân thủ các tiêu chuẩn để thân thiện với người khuyết tật.\n- Phân tích SEO: Kiểm tra các yếu tố tối ưu hóa công cụ tìm kiếm cơ bản.\n- Đánh giá PWA: Kiểm tra xem trang web có đáp ứng các tiêu chuẩn của một Progressive Web App hay không.\n- Tích hợp linh hoạt: Cung cấp khả năng chạy qua Chrome DevTools, CLI hoặc tích hợp vào code bằng thư viện Node.js.

## Hướng dẫn cài đặt Local (macOS)

Để chạy Lighthouse CLI trên macOS, bạn cần cài đặt Node.js và Google Chrome. Các bước thực hiện như sau:\n\n1. Cài đặt Homebrew (nếu máy bạn chưa có):\n`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`\n\n2. Cài đặt Node.js thông qua Homebrew:\n`brew install node`\n\n3. Đảm bảo bạn đã cài đặt trình duyệt Google Chrome trên máy (có thể tải từ trang chủ hoặc dùng lệnh `brew install --cask google-chrome`).\n\n4. Cài đặt thư viện Lighthouse dưới dạng package toàn cục (global) qua npm:\n`npm install -g lighthouse`\n\n5. Kiểm tra cài đặt xem đã thành công hay chưa:\n`lighthouse --version`

## Hướng dẫn Docker (nếu có)

Repository gốc của Lighthouse không cung cấp sẵn Dockerfile chính thức cho CLI thuần túy. Tuy nhiên, bạn hoàn toàn có thể tự viết một Dockerfile cơ bản kết hợp Node.js và Headless Chromium để chạy công cụ này trong container như sau:\n\n```dockerfile\nFROM node:18-alpine\n\n# Cài đặt Chromium\nRUN apk add --no-cache chromium\n\n# Cấu hình biến môi trường cho Lighthouse sử dụng Chromium vừa cài\nENV CHROME_PATH=/usr/bin/chromium-browser\nENV LIGHTHOUSE_CHROMIUM_PATH=/usr/bin/chromium-browser\n\n# Cài đặt Lighthouse CLI\nRUN npm install -g lighthouse\n\nWORKDIR /app\n\n# Lệnh mặc định khi chạy container\nENTRYPOINT ["lighthouse", "--port=9222", "--chrome-flags='--headless --no-sandbox'"]\n```\n\nCách Build và Run bằng Docker:\n1. Build image:\n`docker build -t my-lighthouse .`\n2. Run container:\n`docker run --rm my-lighthouse https://example.com --view=false --output=html --output-path=/stdout > report.html`

## Ví dụ Code (Example Code)

Dưới đây là một ví dụ minh họa cách sử dụng Lighthouse như một Node.js module (Programmatic Usage) để tự động hóa việc đánh giá trang web:\n\n```javascript\nconst fs = require('fs');\nconst lighthouse = require('lighthouse');\nconst chromeLauncher = require('chrome-launcher');\n\n(async () => {\n  // 1. Khởi chạy Chrome ở chế độ headless\n  const chrome = await chromeLauncher.launch({chromeFlags: ['--headless']});\n  const options = {\n    logLevel: 'info',\n    output: 'html',\n    onlyCategories: ['performance'],\n    port: chrome.port\n  };\n  \n  // 2. Chạy Lighthouse cho URL được chỉ định\n  const runnerResult = await lighthouse('https://example.com', options);\n\n  // 3. Ghi báo cáo ra file HTML\n  const reportHtml = runnerResult.report;\n  fs.writeFileSync('lhreport.html', reportHtml);\n\n  // 4. In ra điểm hiệu suất (Performance score)\n  console.log('Điểm hiệu suất:', runnerResult.lhr.categories.performance.score * 100);\n\n  // 5. Đóng Chrome\n  await chrome.kill();\n})();\n```\n\n*Lưu ý: Bạn cần chạy lệnh `npm install lighthouse chrome-launcher` để cài đặt các dependency trước khi thực thi đoạn code trên.*


### Github Page 

https://github.com/GoogleChrome/lighthouse

