# -*- coding: utf-8 -*-
# Copyright 2026 Yize He
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Merge extra words from 1.txt into the original HTML without changing UI/JS."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
src = (ROOT / "1.txt").read_text(encoding="utf-8")
start = src.find("<!DOCTYPE html>")
end = src.find("</html>")
if start < 0 or end < 0:
    raise SystemExit("1.txt does not contain a complete HTML document")
html = src[start : end + len("</html>")]

m = re.search(r"const wordData = (\[[\s\S]*?\n\]);", html)
if not m:
    raise SystemExit("wordData array not found")
existing = json.loads(m.group(1))
seen = {item["en"].lower() for item in existing}

# Extra words parsed from the three 加词 blocks in 1.txt
extras = [
    # 2026.08.12
    {"en": "venue", "cn": "n. 会场；场地"},
    {"en": "deaf", "cn": "adj. 聋的"},
    {"en": "individual", "cn": "n. 个人；个体 adj. 个别的；独特的"},
    {"en": "fibre", "cn": "n. 纤维；纤维素"},
    {"en": "react", "cn": "v. 反应；回应"},
    {"en": "merry", "cn": "adj. 快乐的；愉快的"},
    {"en": "hence", "cn": "adv. 因此；所以"},
    {"en": "tailor", "cn": "n. 裁缝 v. 定制；修改"},
    {"en": "steak", "cn": "n. 牛排；肉排"},
    {"en": "liberty", "cn": "n. 自由；自主权"},
    {"en": "prospect", "cn": "n. 前景；可能性"},
    {"en": "facilitate", "cn": "v. 促进；使容易"},
    {"en": "organ", "cn": "n. 器官；风琴"},
    {"en": "remarkable", "cn": "adj. 非凡的；显著的"},
    {"en": "frontier", "cn": "n. 边境；边疆"},
    {"en": "genius", "cn": "n. 天才；天赋"},
    {"en": "definitely", "cn": "adv. 肯定地；确实地"},
    {"en": "nowhere", "cn": "adv. 无处；任何地方都不"},
    {"en": "variation", "cn": "n. 变化；变异"},
    {"en": "percentage", "cn": "n. 百分比；百分率"},
    {"en": "quantity", "cn": "n. 数量；量"},
    {"en": "dormitory", "cn": "n. 宿舍；学生宿舍"},
    {"en": "interaction", "cn": "n. 互动；相互作用"},
    {"en": "primitive", "cn": "adj. 原始的；远古的"},
    {"en": "fluent", "cn": "adj. 流利的；流畅的"},
    {"en": "extent", "cn": "n. 程度；范围"},
    {"en": "typhoon", "cn": "n. 台风"},
    {"en": "frost", "cn": "n. 霜；霜冻 v. 结霜"},
    {"en": "upper", "cn": "adj. 上部的；较高的 n. 鞋帮"},
    {"en": "anticipate", "cn": "v. 预料；预期"},
    {"en": "butcher", "cn": "n. 屠夫；肉贩 v. 屠宰；弄糟"},
    {"en": "being", "cn": "n. 存在；生物 v. 是（be 的现在分词）"},
    {"en": "extinction", "cn": "n. 灭绝；消失"},
    {"en": "resident", "cn": "n. 居民；住户 adj. 居住的；常驻的"},
    {"en": "dozen", "cn": "n. 一打；十二个"},
    # 2026.08.14
    {"en": "rigid", "cn": "adj. 僵硬的；严格的"},
    {"en": "clue", "cn": "n. 线索；提示"},
    {"en": "dining", "cn": "n. 进餐；用餐"},
    {"en": "handkerchief", "cn": "n. 手帕；手绢"},
    {"en": "integrity", "cn": "n. 正直；诚实"},
    {"en": "discrimination", "cn": "n. 歧视；辨别"},
    {"en": "institute", "cn": "n. 学院；研究所 v. 建立；制定"},
    {"en": "calorie", "cn": "n. 卡路里（热量单位）"},
    {"en": "export", "cn": "v. 出口；输出 n. 出口商品"},
    {"en": "geometry", "cn": "n. 几何学"},
    {"en": "presentation", "cn": "n. 展示；陈述"},
    {"en": "infer", "cn": "v. 推断；推论"},
    {"en": "gramme", "cn": "n. 克（重量单位）"},
    {"en": "refrigerator", "cn": "n. 冰箱；冷藏库"},
    {"en": "suspend", "cn": "v. 暂停；中止"},
    {"en": "scholarship", "cn": "n. 奖学金"},
    {"en": "sustain", "cn": "v. 维持；支撑"},
    {"en": "cottage", "cn": "n. 小屋；村舍"},
    {"en": "consistent", "cn": "adj. 一致的；始终如一的"},
    {"en": "consultation", "cn": "n. 咨询；商议"},
    {"en": "bridegroom", "cn": "n. 新郎"},
    {"en": "worthy", "cn": "adj. 值得的；有价值的"},
    {"en": "county", "cn": "n. 县；郡"},
    {"en": "marathon", "cn": "n. 马拉松赛跑 adj. 马拉松式的；持久的"},
    {"en": "strengthen", "cn": "v. 加强；巩固"},
    {"en": "genuine", "cn": "adj. 真诚的；真实的"},
    {"en": "minority", "cn": "n. 少数；少数民族"},
    {"en": "tension", "cn": "n. 紧张；张力"},
    {"en": "chorus", "cn": "n. 合唱；合唱团 v. 齐声说；合唱"},
    {"en": "directory", "cn": "n. 名录；目录"},
    {"en": "assign", "cn": "v. 分配；指派"},
    {"en": "entirely", "cn": "adv. 完全地；彻底地"},
    {"en": "pan", "cn": "n. 平底锅"},
    {"en": "intervention", "cn": "n. 干预；介入"},
    {"en": "receipt", "cn": "n. 收据；收到"},
    # 2026.08.17
    {"en": "pub", "cn": "n. 酒吧；酒馆"},
    {"en": "wedding", "cn": "n. 婚礼；结婚典礼"},
    {"en": "herb", "cn": "n. 药草；香草"},
    {"en": "pudding", "cn": "n. 布丁"},
    {"en": "comparison", "cn": "n. 比较；对比"},
    {"en": "hydrogen", "cn": "n. 氢"},
    {"en": "enhance", "cn": "v. 提高；增强"},
    {"en": "enormous", "cn": "adj. 巨大的；庞大的"},
    {"en": "dare", "cn": "v. 敢；敢于 n. 挑战；胆量"},
    {"en": "rely", "cn": "v. 依靠；依赖"},
    {"en": "intense", "cn": "adj. 强烈的；剧烈的"},
    {"en": "shave", "cn": "v. 刮脸；剃须 n. 刮脸；剃须"},
    {"en": "protein", "cn": "n. 蛋白质"},
    {"en": "departure", "cn": "n. 离开；出发"},
    {"en": "means", "cn": "n. 方法；手段"},
    {"en": "massive", "cn": "adj. 大量的；巨大的"},
    {"en": "contradictory", "cn": "adj. 矛盾的；对立的"},
    {"en": "fabric", "cn": "n. 织物；布料"},
    {"en": "creature", "cn": "n. 生物；动物"},
    {"en": "threat", "cn": "n. 威胁；恐吓"},
    {"en": "librarian", "cn": "n. 图书管理员"},
    {"en": "contrast", "cn": "n. 对比；对照 v. 对比；形成对照"},
    {"en": "statistic", "cn": "n. 统计数据"},
    {"en": "circus", "cn": "n. 马戏团"},
    {"en": "conclusion", "cn": "n. 结论；结尾"},
    {"en": "stretch", "cn": "v. 伸展；延伸 n. 伸展；一段"},
    {"en": "external", "cn": "adj. 外部的；外来的"},
    {"en": "chef", "cn": "n. 厨师"},
    {"en": "relay", "cn": "n. 转播；接力 v. 转播；传递"},
    {"en": "tablet", "cn": "n. 药片；片剂"},
    {"en": "imply", "cn": "v. 暗示；意味着"},
    {"en": "bride", "cn": "n. 新娘"},
    {"en": "clerk", "cn": "n. 职员；办事员"},
    {"en": "mineral", "cn": "n. 矿物"},
    {"en": "theft", "cn": "n. 盗窃；偷窃"},
    # 2026.08.19
    {"en": "surrounding", "cn": "adj. 周围的；附近的"},
    {"en": "horrible", "cn": "adj. 可怕的；糟糕的"},
    {"en": "bar", "cn": "n. 酒吧；吧台 v. 阻挡；禁止"},
    {"en": "bet", "cn": "v. 打赌 n. 赌注"},
    {"en": "visual", "cn": "adj. 视觉的；视力的 n. 视觉资料；图像"},
    {"en": "leisure", "cn": "n. 闲暇；空闲"},
    {"en": "domain", "cn": "n. 领域；范围；领土；领地"},
    {"en": "criticise", "cn": "v. 批评；指责"},
    {"en": "beard", "cn": "n. 胡须；络腮胡子"},
    {"en": "moreover", "cn": "adv. 而且；此外"},
    {"en": "prior", "cn": "adj. 先前的；在前的"},
    {"en": "ideal", "cn": "adj. 理想的；完美的 n. 理想；典范"},
    {"en": "throughout", "cn": "prep. 遍及；在整个期间"},
    {"en": "exposure", "cn": "n. 暴露；接触；曝光；揭露"},
    {"en": "bunch", "cn": "n. 一束；一串 v. 聚集成束"},
    {"en": "tale", "cn": "n. 故事；传说"},
    {"en": "estate", "cn": "n. 地产；房地产"},
    {"en": "suburb", "cn": "n. 郊区；近郊"},
    {"en": "mist", "cn": "n. 薄雾；雾霭"},
    {"en": "investment", "cn": "n. 投资；投入"},
    {"en": "addict", "cn": "n. 上瘾的人；瘾君子 v. 使沉溺；使上瘾"},
    {"en": "wire", "cn": "n. 电线；金属丝"},
    {"en": "botanical", "cn": "adj. 植物学的；植物的"},
    {"en": "golf", "cn": "n. 高尔夫球运动 v. 打高尔夫球"},
    {"en": "memorial", "cn": "n. 纪念馆；纪念碑 adj. 纪念的；追悼的"},
    {"en": "gymnastics", "cn": "n. 体操；体育"},
    {"en": "native", "cn": "adj. 本国的；本土的 n. 本地人；土著"},
    {"en": "factor", "cn": "n. 因素；要素"},
    {"en": "disc", "cn": "n. 磁盘；圆盘"},
    {"en": "comprehensive", "cn": "adj. 全面的；综合的"},
    {"en": "lap", "cn": "n. 大腿部；一圈；膝上"},
    {"en": "representative", "cn": "n. 代表；代理人 adj. 代表性的；典型的"},
    {"en": "assumption", "cn": "n. 假定；假设"},
    # 2026.08.21
    {"en": "premier", "cn": "n. 首相；总理 adj. 首要的；第一的"},
    {"en": "civilian", "cn": "n. 平民；百姓"},
    {"en": "bacon", "cn": "n. 咸肉；熏肉"},
    {"en": "adorable", "cn": "adj. 可爱的；讨人喜欢的"},
    {"en": "carbon", "cn": "n. 碳"},
    {"en": "coverage", "cn": "n. 覆盖范围；新闻报道"},
    {"en": "astronomer", "cn": "n. 天文学家"},
    {"en": "respective", "cn": "adj. 各自的；分别的"},
    {"en": "comfort", "cn": "n. 安慰；舒适 v. 安慰；使舒适"},
    {"en": "virtue", "cn": "n. 美德；优点"},
    {"en": "shelf", "cn": "n. 架子；搁板"},
    {"en": "subsequent", "cn": "adj. 随后的；后来的"},
    {"en": "digest", "cn": "v. 消化 n. 文摘；摘要"},
    {"en": "phenomenon", "cn": "n. 现象"},
    {"en": "buffet", "cn": "n. 自助餐 v. 连续猛击"},
    {"en": "needle", "cn": "n. 针；指针"},
    {"en": "illustrate", "cn": "v. 说明；阐明"},
    {"en": "jaw", "cn": "n. 下巴；颌"},
    {"en": "resign", "cn": "v. 辞职；放弃"},
    {"en": "council", "cn": "n. 委员会；理事会"},
    {"en": "substance", "cn": "n. 物质；实质"},
    {"en": "joint", "cn": "n. 关节 adj. 连接的；共同的"},
    {"en": "proposal", "cn": "n. 提议；建议；求婚"},
    {"en": "arch", "cn": "n. 拱门；拱形结构 v. 拱起；成弓形"},
    {"en": "military", "cn": "adj. 军事的；军用的 n. 军队；军方"},
    {"en": "idiom", "cn": "n. 习语；成语"},
    {"en": "slightly", "cn": "adv. 稍微；轻微地"},
    {"en": "smog", "cn": "n. 烟雾；雾霾"},
    {"en": "saucer", "cn": "n. 茶碟；小碟子"},
    {"en": "radium", "cn": "n. 镭（化学元素）"},
    # 2026.08.24
    {"en": "passive", "cn": "adj. 被动的；消极的"},
    {"en": "pear", "cn": "n. 梨"},
    {"en": "saving", "cn": "n. 节省；节约 adj. 节省的；挽救的"},
    {"en": "grain", "cn": "n. 谷物；粮食；颗粒；纹理"},
    {"en": "superb", "cn": "adj. 极佳的；卓越的"},
    {"en": "gifted", "cn": "adj. 有天赋的；有才华的"},
    {"en": "crucial", "cn": "adj. 至关重要的；决定性的"},
    {"en": "obviously", "cn": "adv. 显然；明显地"},
    {"en": "intend", "cn": "v. 打算；计划"},
    {"en": "mass", "cn": "n. 大量；群众 adj. 大量的；大众的"},
    {"en": "garlic", "cn": "n. 大蒜"},
    {"en": "arrow", "cn": "n. 箭；箭头"},
    {"en": "division", "cn": "n. 除法；部门；分部"},
    {"en": "stimulate", "cn": "v. 刺激；促进"},
    {"en": "innovation", "cn": "n. 创新；革新"},
    {"en": "poetry", "cn": "n. 诗歌；诗集"},
    {"en": "motive", "cn": "n. 动机；目的"},
    {"en": "physician", "cn": "n. 内科医生；医师"},
    {"en": "lung", "cn": "n. 肺；肺部"},
    {"en": "housing", "cn": "n. 住房；住宅"},
    {"en": "march", "cn": "v. 行进；前进 n. 三月"},
]

added = []
skipped = []
for item in extras:
    key = item["en"].lower()
    if key in seen:
        skipped.append(item["en"])
        continue
    existing.append(item)
    seen.add(key)
    added.append(item["en"])

lines = ["const wordData = ["]
for i, item in enumerate(existing):
    comma = "," if i < len(existing) - 1 else ""
    lines.append(
        '{"en":%s,"cn":%s}%s'
        % (
            json.dumps(item["en"], ensure_ascii=False),
            json.dumps(item["cn"], ensure_ascii=False),
            comma,
        )
    )
lines.append("];")
new_arr = "\n".join(lines)
html = html[: m.start()] + new_arr + html[m.end() :]
if html.startswith("<!DOCTYPE html>"):
    html = (
        "<!DOCTYPE html>\n"
        "<!--\n"
        "Copyright 2026 Yize He\n"
        "Licensed under the Apache License, Version 2.0\n"
        "http://www.apache.org/licenses/LICENSE-2.0\n"
        "-->\n"
        + html[len("<!DOCTYPE html>") :].lstrip("\n")
    )

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
print(f"original={len(existing) - len(added)} added={len(added)} skipped={skipped} total={len(existing)}")
print(f"wrote {out}")
