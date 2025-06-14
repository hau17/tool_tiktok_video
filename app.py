from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, ImageClip
from moviepy.video.fx.MultiplySpeed import MultiplySpeed
# ========== CẤU HÌNH ==========
VIDEO_INPUT = "input_video.mp4"
TEXT_INPUT = "input_text.txt"
MUSIC_INPUT = "input_music.mp3"
IMAGE_INPUT = "product_image.jpg"
OUTPUT_VIDEO = "output.mp4"
FONT_PATH = "C:/font/SVN-Freude/SVN-Freude.otf"
BG_COLOR = (255, 206, 210)  # Màu nền cho text clip
TEXT_COLOR = "black" 
TEXT_GIA_TIEN = "Giá sản phẩm: 1.000.000 VNĐ"
TEXT_CAM_ON = "Cảm ơn bạn đã xem!"
CO_CHU = 50
# ========== TĂNG TỐC VIDEO ==========
video = VideoFileClip(VIDEO_INPUT)
# Nếu video dài hơn 80s thì mới cần tăng tốc
# Ví dụ: tăng tốc video để rút còn 80 giây
if video.duration > 80:
    speed_factor = video.duration / 80
    video = video.with_effects([MultiplySpeed(speed_factor)]).with_duration(80)
else:
    video = video.with_duration(video.duration)
# ========== ĐỌC FILE TEXT ==========
with open(TEXT_INPUT, "r", encoding="utf-8") as f:
    texts = [line.strip() for line in f if line.strip()]
num_texts = len(texts)
text_duration = video.duration / num_texts

# ========== TEXT CLIPS ==========
text_clips = []
W, H = video.size
text_y_pos = int(H * 1 / 8)

for i, sentence in enumerate(texts):
    txt_clip = (
        TextClip(text = sentence,
                    font_size=CO_CHU, 
                    color=TEXT_COLOR, 
                    bg_color = BG_COLOR, 
                    font=FONT_PATH,
                    method='caption',
                    size=(W - 200, None),        
                    text_align='center',
                    horizontal_align='center',
                    margin=(25, 25))
        .with_position(("center", text_y_pos))
        .with_duration(text_duration - 1)
        .with_start(3 + i * text_duration)
    )
    text_clips.append(txt_clip)

# ========== ẢNH SẢN PHẨM ĐẦU VIDEO ==========
product_img_clip_start = (
    ImageClip(IMAGE_INPUT)
    .resized(height=H)
    .with_position("center")
    .with_start(0)
    .with_duration(3)
)
# ========== ẢNH SẢN PHẨM CUỐI VIDEO ==========
product_img_clip_end = (
    ImageClip(IMAGE_INPUT)
    .resized(height=H)
    .with_position("center")
    .with_start(video.duration + 3)
    .with_duration(10)
)

gia_tien = TextClip(
    text=TEXT_GIA_TIEN,
    font=FONT_PATH,
    font_size=CO_CHU,
    color=TEXT_COLOR,
    bg_color=BG_COLOR,
    method='caption',
    size=(W - 200, None),         # Chiều ngang video trừ 200px
    text_align='center',
    horizontal_align='center',
    margin=(25, 25)               # padding bên trong (nếu muốn thêm)
).with_position(("center", text_y_pos)).with_start(video.duration + 3).with_duration(5)


thanks_text = TextClip(
    text=TEXT_CAM_ON,
    font=FONT_PATH,
    font_size=CO_CHU,
    color=TEXT_COLOR,
    bg_color=BG_COLOR,
    method='caption',
    size=(W - 200, None),         # Chiều ngang video trừ 200px
    text_align='center',
    horizontal_align='center',
    margin=(25, 25)               # padding bên trong (nếu muốn thêm)
).with_position(("center", text_y_pos)).with_start(video.duration + 3 +5).with_duration(5)


# ========== NHẠC NỀN ==========
bg_music = AudioFileClip(MUSIC_INPUT).subclipped(0, video.duration + 13)

# ========== GHÉP VIDEO ==========
final = CompositeVideoClip(
    [product_img_clip_start, video.with_start(3)] + text_clips + [product_img_clip_end, gia_tien, thanks_text],
    size=video.size
).with_audio(bg_music)

# ========== XUẤT VIDEO ==========
final.write_videofile(OUTPUT_VIDEO, fps=30, codec='libx264', audio_codec='aac')

# ========== ĐÓNG TÀI NGUYÊN ==========
# Đóng clip tổng
final.close()
# Đóng video đầu vào
video.close()
# Đóng nhạc nền
bg_music.close()
# Đóng từng text clip
for txt_clip in text_clips:
    txt_clip.close()
# Đóng ảnh sản phẩm và đoạn text cảm ơn
product_img_clip_start.close()
product_img_clip_end.close()
thanks_text.close()