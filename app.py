import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, font
import os
from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, ImageClip
from moviepy.video.fx.MultiplySpeed import MultiplySpeed
from wraptext import soft_wrap_text

# Default configuration
DEFAULT_CONFIG = {
    "VIDEO_INPUT": "input_video.mp4",
    "TEXT_INPUT": "input_text.txt",
    "MUSIC_INPUT": "input_music.mp3",
    "IMAGE_INPUT": "product_image.jpg",
    "OUTPUT_VIDEO": "output.mp4",
    "FONT_PATH": "C:/font/SVN-Freude/SVN-Freude.otf",
    "BG_COLOR": (255, 206, 210),
    "TEXT_COLOR": "black",
    "TEXT_GIA_TIEN": "Giá sản phẩm: 1.000.000 VNĐ",
    "TEXT_CAM_ON": "Cảm ơn bạn đã xem!",
    "CO_CHU": 40
}

class VideoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Editor")
        self.root.geometry("600x700")

        # Initialize variables with defaults
        self.video_path = tk.StringVar(value=DEFAULT_CONFIG["VIDEO_INPUT"])
        self.text_path = tk.StringVar(value=DEFAULT_CONFIG["TEXT_INPUT"])
        self.music_path = tk.StringVar(value=DEFAULT_CONFIG["MUSIC_INPUT"])
        self.image_path = tk.StringVar(value=DEFAULT_CONFIG["IMAGE_INPUT"])
        self.output_path = tk.StringVar(value=DEFAULT_CONFIG["OUTPUT_VIDEO"])
        self.font_path = tk.StringVar(value=DEFAULT_CONFIG["FONT_PATH"])
        self.bg_color = DEFAULT_CONFIG["BG_COLOR"]
        self.text_color = tk.StringVar(value=DEFAULT_CONFIG["TEXT_COLOR"])
        self.text_gia_tien = tk.StringVar(value=DEFAULT_CONFIG["TEXT_GIA_TIEN"])
        self.text_cam_on = tk.StringVar(value=DEFAULT_CONFIG["TEXT_CAM_ON"])
        self.co_chu = tk.IntVar(value=DEFAULT_CONFIG["CO_CHU"])

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Video Input
        tk.Label(self.root, text="Video File:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.video_path, width=50).pack()
        tk.Button(self.root, text="Browse", command=self.browse_video).pack()

        # Text Input
        tk.Label(self.root, text="Text File:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.text_path, width=50).pack()
        tk.Button(self.root, text="Browse", command=self.browse_text).pack()

        # Music Input
        tk.Label(self.root, text="Music File:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.music_path, width=50).pack()
        tk.Button(self.root, text="Browse", command=self.browse_music).pack()

        # Image Input
        tk.Label(self.root, text="Image File:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.image_path, width=50).pack()
        tk.Button(self.root, text="Browse", command=self.browse_image).pack()

        # Output Video
        tk.Label(self.root, text="Output Video:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.output_path, width=50).pack()
        tk.Button(self.root, text="Browse", command=self.browse_output).pack()

        # Font Path
        tk.Label(self.root, text="Font File (optional):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.font_path, width=50).pack()
        tk.Button(self.root, text="Browse", command=self.browse_font).pack()

        # Text Color
        tk.Label(self.root, text="Text Color (optional):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.text_color, width=50).pack()
        tk.Button(self.root, text="Choose Color", command=self.choose_text_color).pack()

        # Background Color
        tk.Label(self.root, text="Background Color (optional):").pack(pady=5)
        tk.Button(self.root, text="Choose Color", command=self.choose_bg_color).pack()

        # Font Size
        tk.Label(self.root, text="Font Size (optional):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.co_chu, width=10).pack()

        # Price Text
        tk.Label(self.root, text="Price Text:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.text_gia_tien, width=50).pack()

        # Thank You Text
        tk.Label(self.root, text="Thank You Text:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.text_cam_on, width=50).pack()

        # Generate Button
        tk.Button(self.root, text="Generate Video", command=self.generate_video).pack(pady=20)

    def browse_video(self):
        path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        if path:
            self.video_path.set(path)

    def browse_text(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if path:
            self.text_path.set(path)

    def browse_music(self):
        path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if path:
            self.music_path.set(path)

    def browse_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
        if path:
            self.image_path.set(path)

    def browse_output(self):
        path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video Files", "*.mp4")])
        if path:
            self.output_path.set(path)

    def browse_font(self):
        path = filedialog.askopenfilename(filetypes=[("Font Files", "*.otf *.ttf")])
        if path:
            self.font_path.set(path)

    def choose_text_color(self):
        color = colorchooser.askcolor(title="Choose Text Color")[1]
        if color:
            self.text_color.set(color)

    def choose_bg_color(self):
        color = colorchooser.askcolor(title="Choose Background Color")[1]
        if color:
            r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
            self.bg_color = (r, g, b)

    def validate_inputs(self):
        required_fields = [
            (self.video_path.get(), "Video file"),
            (self.text_path.get(), "Text file"),
            (self.music_path.get(), "Music file"),
            (self.image_path.get(), "Image file"),
            (self.output_path.get(), "Output file"),
            (self.text_gia_tien.get(), "Price text"),
            (self.text_cam_on.get(), "Thank you text")
        ]
        for value, field_name in required_fields:
            if not value or value.strip() == "":
                messagebox.showerror("Error", f"{field_name} is required!")
                return False
        # Validate file existence
        for path, field_name in [
            (self.video_path.get(), "Video file"),
            (self.text_path.get(), "Text file"),
            (self.music_path.get(), "Music file"),
            (self.image_path.get(), "Image file")
        ]:
            if not os.path.exists(path):
                messagebox.showerror("Error", f"{field_name} does not exist!")
                return False
        return True

    def generate_video(self):
        if not self.validate_inputs():
            return

        try:
            # Assign variables for MoviePy
            VIDEO_INPUT = self.video_path.get()
            TEXT_INPUT = self.text_path.get()
            MUSIC_INPUT = self.music_path.get()
            IMAGE_INPUT = self.image_path.get()
            OUTPUT_VIDEO = self.output_path.get()
            FONT_PATH = self.font_path.get() or DEFAULT_CONFIG["FONT_PATH"]
            BG_COLOR = self.bg_color
            TEXT_COLOR = self.text_color.get()
            TEXT_GIA_TIEN = self.text_gia_tien.get()
            TEXT_CAM_ON = self.text_cam_on.get()
            CO_CHU = self.co_chu.get()

            # ========== TĂNG TỐC VIDEO ==========
            video = VideoFileClip(VIDEO_INPUT)
            if video.duration > 77:
                speed_factor = video.duration / 77
                video = video.with_effects([MultiplySpeed(speed_factor)]).with_duration(77)
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
                wrapped_text = soft_wrap_text(
                    text=sentence,
                    fontsize=CO_CHU,
                    letter_spacing=0,
                    font_family=FONT_PATH,
                    max_width=W - 150
                )

                txt_clip = (
                    TextClip(
                        text=wrapped_text,
                        font_size=CO_CHU,
                        color=TEXT_COLOR,
                        bg_color=BG_COLOR,
                        font=FONT_PATH,
                        method='caption',
                        size=(W - 150, None),
                        text_align='center',
                        horizontal_align='center',
                        margin=(25, 25)
                    )
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

            wrapped_gia_tien = soft_wrap_text(
                text=TEXT_GIA_TIEN,
                fontsize=CO_CHU,
                letter_spacing=0,
                font_family=FONT_PATH,
                max_width=W - 150
            )

            gia_tien = TextClip(
                text=wrapped_gia_tien,
                font=FONT_PATH,
                font_size=CO_CHU,
                color=TEXT_COLOR,
                bg_color=BG_COLOR,
                method='caption',
                size=(W - 150, None),
                text_align='center',
                horizontal_align='center',
                margin=(25, 25)
            ).with_position(("center", text_y_pos)).with_start(video.duration + 3).with_duration(5)

            wrapped_thanks_text = soft_wrap_text(
                text=TEXT_CAM_ON,
                fontsize=CO_CHU,
                letter_spacing=0,
                font_family=FONT_PATH,
                max_width=W - 150
            )

            thanks_text = TextClip(
                text=wrapped_thanks_text,
                font=FONT_PATH,
                font_size=CO_CHU,
                color=TEXT_COLOR,
                bg_color=BG_COLOR,
                method='caption',
                size=(W - 150, None),
                text_align='center',
                horizontal_align='center',
                margin=(25, 25)
            ).with_position(("center", text_y_pos)).with_start(video.duration + 3 + 5).with_duration(5)

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
            final.close()
            video.close()
            bg_music.close()
            for txt_clip in text_clips:
                txt_clip.close()
            product_img_clip_start.close()
            product_img_clip_end.close()
            thanks_text.close()

            messagebox.showinfo("Success", "Video generated successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()