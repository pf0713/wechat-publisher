# -*- coding: utf-8 -*-
import json, requests, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

APP_ID = os.getenv("WX_APP_ID", "")
APP_SECRET = os.getenv("WX_APP_SECRET", "")
IMG_DIR = r"C:\Users\86151\Desktop\CC实验\推文配图"
OUT_DIR = r"C:\Users\86151\Desktop\CC实验"
BASE = "https://api.weixin.qq.com/cgi-bin"

print("[1/5] 获取 access_token...")
r = requests.get(f"{BASE}/token",
    params={"grant_type":"client_credential","appid":APP_ID,"secret":APP_SECRET})
data = r.json()
if "access_token" not in data: print(f"[X] {data}"); sys.exit(1)
token = data["access_token"]
print(f"[OK]")

print("\n[2/5] 上传图片...")
img_urls = {}
for f in ["cover.png","section1.png","section2.png","section3.png","section4.png"]:
    with open(f"{IMG_DIR}\\{f}", "rb") as fp:
        r = requests.post(f"{BASE}/media/uploadimg?access_token={token}",
                          files={"media":(f, fp, "image/png")})
    resp = r.json()
    if "url" in resp: img_urls[f]=resp["url"]; print(f"  [OK] {f}")
    else: print(f"  [X] {f}"); sys.exit(1)

print("\n[3/5] 生成HTML...")

html_parts = []

html_parts.append(f'''<section style="margin:0;padding:0;">
  <p style="text-align:center;"><img src="{img_urls['cover.png']}" style="width:100%;display:block;"></p>
</section>''')

html_parts.append('''<section style="padding:10px 16px;">
  <p style="color:#333;font-size:15px;line-height:1.8;">"让孩子得一次病，产生天然抗体，比打疫苗的抵抗力更持久。"</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">这句话在家长群里流传已久。听起来似乎还有点道理——大自然嘛，天然的肯定比人工的好？</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">2026年4月22日，国家疾控局在"全民携手 共筑免疫屏障"主题新闻发布会上，专门回应了这条说法。5月29日，2026年5月"科学"流言榜再次把它列入榜单。中国疾控中心主任医师<strong>余文周</strong>的用词很直接：</p>
  <p style="text-align:center;color:#c0392b;font-size:17px;margin:10px 0;"><strong>"不可取、不科学。"</strong></p>
  <p style="color:#333;font-size:15px;line-height:1.8;">这条流言之所以危险，不是因为听上去荒谬——恰恰相反，是因为它<strong>听上去太合理了</strong>。</p>
</section>''')

html_parts.append(f'''<section style="padding:0 16px;margin-top:15px;">
  <p style="text-align:center;"><img src="{img_urls['section1.png']}" style="width:100%;display:block;"></p>
  <h2 style="color:#1a0d2e;font-size:18px;margin:10px 0;">"天然抗体更持久"——这话哪里有问题</h2>
  <p style="color:#333;font-size:15px;line-height:1.8;">它最大的迷惑性在于：<strong>前提部分是正确的。</strong></p>
  <p style="color:#333;font-size:15px;line-height:1.8;">确实，部分传染病感染后可以产生免疫力。水痘得一次，绝大多数人终身免疫——这是真的。麻疹也是，得过后通常不会得第二次。</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">但问题在于<strong>"代价"两个字</strong>。</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">我们来算一笔账：<br>· 水痘——大多数孩子能扛过去，但少数会并发肺炎、脑炎、皮肤继发感染留下永久疤痕。你愿意赌你的孩子是"大多数"还是"少数"？<br>· 麻疹——在疫苗普及前，几乎每个孩子都会得。它不是"发几天烧出点疹子就好了"。麻疹病毒会攻击免疫系统，导致<strong>一种叫免疫健忘的状态</strong>——得过麻疹后，免疫系统会遗忘之前建立的对其他病原体的防御能力，这种效应可持续2-3年。换句话说：<strong>得一次麻疹，不等于获得了一种免疫力，反而可能失去多种免疫力。</strong><br>· 流感——每年全球导致29万-65万人死亡。流感本身不可怕，可怕的是继发的肺炎、心肌炎、脑炎。流感疫苗的核心价值不是防感染，是<strong>防重症和防死亡</strong>。</p>
</section>''')

html_parts.append(f'''<section style="padding:0 16px;margin-top:20px;">
  <p style="text-align:center;"><img src="{img_urls['section2.png']}" style="width:100%;display:block;"></p>
  <h2 style="color:#1a0d2e;font-size:18px;margin:10px 0;">疫苗和感染——一个有安全网，一个没有</h2>
  <p style="color:#333;font-size:15px;line-height:1.8;">中国疾控中心2026年4月发布的科普材料中，用一个比喻讲得很清楚：</p>
  <p style="color:#333;font-size:15px;line-height:1.8;"><strong>疫苗是一次安全的实战演练。</strong>它给你免疫系统的不是真正的敌人（活性病原体），而是一张"通缉令"（灭活病毒、蛋白亚单位、mRNA指令等）。免疫系统对着这张通缉令做训练：记住敌人的长相、准备好武器、部署好防御。等有一天真敌人来了——秒杀。</p>
  <p style="color:#333;font-size:15px;line-height:1.8;"><strong>真感染是一次没有安全网的实战。</strong>病原体进入身体，第一时间就开始繁殖和攻击。你的免疫系统需要在战斗中现学现打。赢了，产生抗体；输了，轻则住院，重则致命。中间没有裁判叫停。</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">4月25日全国儿童预防接种日，央广网专访上海市疾控中心庞红主任医师的报道中特意强调了一点：<strong>"疫苗的'保护力'和'持久性'并不差于自然感染，对于很多疫苗来说，接种诱导的免疫应答甚至优于自然感染。"</strong>原因很简单——疫苗经过科学设计，目标是激发"最佳免疫反应"而不是"随机免疫反应"。自然感染产生的抗体水平因人而异、不可预测；而疫苗接种后，绝大多数人能达到保护性抗体水平。</p>
</section>''')

html_parts.append(f'''<section style="padding:0 16px;margin-top:20px;">
  <p style="text-align:center;"><img src="{img_urls['section3.png']}" style="width:100%;display:block;"></p>
  <h2 style="color:#1a0d2e;font-size:18px;margin:10px 0;">如果没有疫苗——翻一页老病历就知道</h2>
  <p style="color:#333;font-size:15px;line-height:1.8;">有些事，距离太近了反而看不清。我们来拉远镜头：</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">· 在麻疹疫苗普及前，中国每年报告麻疹病例数百万。2024年，我国麻疹报告发病率已降至<strong>百万分之一左右</strong>。这背后是两剂次含麻疫苗的全面覆盖。<br>· 脊髓灰质炎（小儿麻痹症）——上世纪50-60年代，中国每年新增数万例。孩子早上还好好的，下午腿就瘫了。2000年，中国宣布消灭脊髓灰质炎。不是病毒消失了——是<strong>疫苗把它从中国大地上清除了</strong>。<br>· 白喉——在上世纪初是儿科病房最常见的死因之一。中国已连续多年无白喉病例报告。百白破疫苗是最大的功臣。</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">这些成就太"日常"了，日常到我们觉得理所当然。但每一个"没得病"的孩子背后，<strong>都是疫苗在替他挨了一刀</strong>。</p>
</section>''')

html_parts.append(f'''<section style="padding:0 16px;margin-top:20px;">
  <p style="text-align:center;"><img src="{img_urls['section4.png']}" style="width:100%;display:block;"></p>
  <h2 style="color:#1a0d2e;font-size:18px;margin:10px 0;">中国的免疫规划，比你想象的靠谱</h2>
  <p style="color:#333;font-size:15px;line-height:1.8;">有些家长担心的不是疫苗本身，而是"中国疫苗的质量"。说一组事实：</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">· 中国的疫苗监管体系已经<strong>连续三次通过世界卫生组织（WHO）的评估</strong>（2011年、2014年、2022年），意味着中国生产的疫苗达到了国际质量标准。<br>· 国家免疫规划里的每一支疫苗，从研发到上市，要经过<strong>临床前研究→I/II/III期临床试验→上市审批→上市后监测</strong>四个阶段，平均耗时8-15年。<br>· 中国建立的疑似预防接种异常反应（AEFI）监测系统，能实时追踪任何可能与疫苗相关的不良反应。严重不良反应发生率以<strong>百万分之一</strong>为单位计算。</p>
  <p style="color:#333;font-size:15px;line-height:1.8;">5月科学流言榜发布时引用的一句话，适合做今天的结语：</p>
  <blockquote style="border-left:3px solid #8e44ad;padding-left:12px;color:#555;margin:10px 0;"><p style="margin:0;font-size:15px;">"我们不能因为害怕百万分之一的疫苗风险，去赌十分之一的感染风险。这道算术题，答案很清楚。"</p></blockquote>
  <p style="text-align:center;color:#8e44ad;font-size:17px;margin:15px 0;"><strong>打疫苗不是冒险，不打才是。</strong></p>
</section>''')

html_parts.append('''<section style="margin-top:25px;padding:15px 16px;background:#f5f0e8;">
  <p style="color:#999;font-size:13px;text-align:center;">引用信源：2026年5月科学流言榜、国家疾控局2026年4月22日新闻发布会、中国疾控中心主任医师余文周、央广网/上海市疾控中心庞红主任医师(2026.4.25)、全国儿童预防接种日科普资料。</p>
</section>''')

html_content = "\n".join(html_parts)
html_path = f"{OUT_DIR}\\推文_得病比打疫苗持久辟谣_公众号排版.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(f"<!DOCTYPE html><html><head><meta charset=\"utf-8\"></head><body>{html_content}</body></html>")

print("\n[4/5] 上传封面...")
r = requests.post(f"{BASE}/material/add_material?access_token={token}&type=image",
    files={"media":("cover.png",open(f"{IMG_DIR}\\cover.png","rb"),"image/png")})
resp = r.json()
thumb_id = resp.get("media_id","")
if not thumb_id: print(f"[X] {resp}"); sys.exit(1)

print("\n[5/5] 创建草稿...")
article = {
    "title": "得病比打疫苗抵抗力更持久？国家疾控局：不可取，这是在拿命赌",
    "author": "杨",
    "digest": "5月科学流言榜辟谣：疫苗是安全演练，真感染没有安全网。麻疹会让人失去免疫力，脊灰曾让数万孩子瘫痪",
    "content": html_content,
    "content_source_url": "",
    "thumb_media_id": thumb_id,
    "need_open_comment": 1,
    "only_fans_can_comment": 0,
}

body = json.dumps({"articles":[article]}, ensure_ascii=False).encode("utf-8")
r = requests.post(f"{BASE}/draft/add?access_token={token}", data=body,
                  headers={"Content-Type":"application/json; charset=utf-8"})
resp = r.json()
if "media_id" in resp:
    print(f"\n  [OK] 草稿创建成功! media_id: {resp['media_id']}")
    print(f"\n  请前往微信公众平台 -> 草稿箱 查看并发布")
else:
    print(f"\n  [X] {resp}")
