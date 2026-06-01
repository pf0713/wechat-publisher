"""
生成公众号推文配图
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = r"C:\Users\86151\Desktop\CC实验\推文配图"
os.makedirs(OUT, exist_ok=True)

FONT_PATHS = [
    "C:/Windows/Fonts/msyh.ttc","C:/Windows/Fonts/msyhbd.ttc",
    "C:/Windows/Fonts/simhei.ttf","C:/Windows/Fonts/simsun.ttc",
]

def load_font(size):
    for fp in FONT_PATHS:
        try: return ImageFont.truetype(fp, size)
        except: continue
    return ImageFont.load_default()

def make_cover():
    w, h = 900, 500
    img = Image.new("RGB", (w, h), "#1a0d2e")
    draw = ImageDraw.Draw(img)
    font_big = load_font(42)
    title = "得病比打疫苗抵抗力更持久？"
    tw = draw.textbbox((0,0), title, font=font_big)[2]
    draw.text(((w-tw)//2, 130), title, fill="#ffffff", font=font_big)
    font_mid = load_font(28)
    sub = "5月科学流言榜：一场病可能让你付出生命的代价"
    sw = draw.textbbox((0,0), sub, font=font_mid)[2]
    draw.text(((w-sw)//2, 220), sub, fill="#e74c3c", font=font_mid)
    font_sm = load_font(20)
    tag = "国家疾控局：疫苗是安全的实战演练，不是用健康去赌博"
    tw2 = draw.textbbox((0,0), tag, font=font_sm)[2]
    draw.text(((w-tw2)//2, 350), tag, fill="#9b59b6", font=font_sm)
    path = os.path.join(OUT, "cover.png")
    img.save(path)
    print(f"封面: {path}")

def make_section_img(title, subtitle, filename, bg="#f5f0e8"):
    w, h = 800, 400
    img = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 8, h], fill="#8e44ad")
    font_big = load_font(34)
    draw.text((60, 130), title, fill="#1a0d2e", font=font_big)
    font_sm = load_font(22)
    draw.text((60, 200), subtitle, fill="#666", font=font_sm)
    path = os.path.join(OUT, filename)
    img.save(path)
    print(f"配图: {path}")

if __name__ == "__main__":
    make_cover()
    make_section_img("这句话为什么听起来有道理",
                     "天然抗体确实存在——但用一场病换来抗体，代价可能大到无法承受", "section1.png")
    make_section_img("疫苗和得病，根本不是一回事",
                     "疫苗是预处理过的安全信号，得病是真刀真枪的感染——一个可控，一个不可控", "section2.png")
    make_section_img("那些得了病才后悔的案例",
                     "麻疹脑炎、流脑败血症、小儿麻痹后遗症——疫苗普及前，这些是儿科日常", "section3.png")
    make_section_img("接种疫苗，是给孩子最划算的健康投资",
                     "麻疹疫苗普及后发病率降至百万分之一；流感疫苗大幅降低老年重症死亡率", "section4.png",
                     bg="#1a0d2e")
    print("\n全部配图生成完毕")
