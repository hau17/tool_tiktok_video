Tạo Video Tự Động Với Text, Nhạc, Hình Ảnh Bằng MoviePy
Chương trình này giúp bạn tạo video TikTok hoặc video quảng cáo đơn giản bằng cách:

Tăng tốc video gốc nếu cần.

Thêm các dòng chữ từ file văn bản.

Thêm hình ảnh sản phẩm ở đầu và cuối video.

Chèn nhạc nền và text cảm ơn ở cuối video.

🧰 Yêu Cầu Cài Đặt
Trước khi chạy, hãy đảm bảo bạn đã cài:
pip install moviepy

Ngoài ra, cần có:
Python 3.7 trở lên
FFmpeg đã cài và nằm trong PATH hệ thống

🗂️ Cấu Trúc Thư Mục Đầu Vào
    project_folder/
    │
    ├── app.py                # File code chính
    ├── input_video.mp4       # Video gốc
    ├── input_text.txt        # File chứa text (mỗi dòng là 1 đoạn hiển thị)
    ├── input_music.mp3       # Nhạc nền
    ├── product_image.jpg     # Ảnh sản phẩm
    └── C:/font/SVN-Freude/...# Đường dẫn font chữ OTF. tải ở :https://www.svnfont.com/viet-hoa-svn-freude/
🛠️ Cách Sử Dụng
Chuẩn bị các file đầu vào:

input_video.mp4: Video chính (bất kỳ độ dài nào).

input_text.txt: Ghi các dòng văn bản bạn muốn chèn, mỗi dòng sẽ hiển thị một đoạn.

input_music.mp3: Nhạc nền dài ít nhất 90s.

product_image.jpg: Ảnh sản phẩm để chèn vào đầu và cuối video.

Đảm bảo font chữ đúng đường dẫn (có thể đổi trong biến FONT_PATH).

Chạy chương trình:
python app.py
Kết quả:
Một video mới tên là output.mp4 được tạo ra, có:

Văn bản hiển thị lần lượt trong 80 giây.

Ảnh sản phẩm xuất hiện 3 giây đầu và 10 giây cuối.

Nhạc nền ghép suốt video.

Lời cảm ơn ở cuối.

⚙️ Cấu Hình Thay Đổi Nhanh
Bạn có thể điều chỉnh trong code:
TOTAL_DURATION = 90:	Tổng thời lượng video đầu ra
TEXT_DURATION = 80:	Thời gian hiển thị văn bản
PRODUCT_IMAGE_DURATION:	Thời gian hiển thị ảnh sản phẩm cuối
FONT_PATH:	Đường dẫn đến font chữ OTF/TTF
BG_COLOR, TEXT_COLOR:	Màu nền và chữ cho text

❓ Lưu Ý
Video đầu vào sẽ được tăng tốc nếu dài hơn TEXT_DURATION.
Nếu dùng font tiếng Việt, hãy chắc chắn font đó hỗ trợ Unicode.
