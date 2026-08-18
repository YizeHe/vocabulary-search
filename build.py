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

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
print(f"original={len(existing) - len(added)} added={len(added)} skipped={skipped} total={len(existing)}")
print(f"wrote {out}")
