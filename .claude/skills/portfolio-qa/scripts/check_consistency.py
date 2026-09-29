"""포트폴리오 경계면 자동 대조: 콘텐츠 문서 ↔ HTML ↔ projects.js ↔ 토큰 CSS.

프로젝트 루트에서 실행: python .claude/skills/portfolio-qa/scripts/check_consistency.py
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # Windows 콘솔에서 한글 깨짐 방지

ROOT = Path.cwd()
CONTENT = ROOT / "_workspace" / "01_strategist_content.md"
SITE = ROOT / "site"
issues, notes = [], []


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        issues.append(f"[높음] 파일 없음: {path.relative_to(ROOT)}")
        return ""


content = read(CONTENT)
html = read(SITE / "index.html")
projects_js = read(SITE / "data" / "projects.js")
tokens = read(SITE / "css" / "tokens.css")
style = read(SITE / "css" / "style.css")

# 1. 섹션 순서/ID
m = re.search(r"^## 섹션 순서\s*\n(.+)$", content, re.M)
doc_sections = [s.strip() for s in m.group(1).split(",")] if m else []
html_sections = re.findall(r"<section[^>]*\bid=\"([^\"]+)\"", html)
if doc_sections and html_sections != doc_sections:
    issues.append(f"[중간] 섹션 불일치 — 문서: {doc_sections} / HTML: {html_sections}")

# 2. 내비 앵커 → 실제 id
all_ids = set(re.findall(r"\bid=\"([^\"]+)\"", html))
for href in sorted(set(re.findall(r"href=\"#([^\"]+)\"", html))):
    if href not in all_ids:
        issues.append(f"[높음] 깨진 앵커: #{href}")

# 3. 프로젝트 id
doc_projects = re.findall(r"^\s*-\s*id:\s*([\w-]+)", content, re.M)
js_projects = re.findall(r"\bid\s*:\s*[\"']([\w-]+)[\"']", projects_js)
if doc_projects and doc_projects != js_projects:
    issues.append(f"[중간] 프로젝트 불일치 — 문서: {doc_projects} / projects.js: {js_projects}")

# 4. 토큰 사용
defined = set(re.findall(r"(--[\w-]+)\s*:", tokens))
for var in sorted(set(re.findall(r"var\((--[\w-]+)", style)) - defined):
    issues.append(f"[중간] 정의되지 않은 토큰: {var}")
for i, line in enumerate(style.splitlines(), 1):
    if re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(", line) and "--" not in line.split(":")[0]:
        issues.append(f"[낮음] site/css/style.css:{i} 하드코딩 색 — {line.strip()}")

# 5. 기본 메타/접근성
for tag, label in [(r"<title>", "title"), (r'name="description"', "meta description"),
                   (r'property="og:title"', "og:title"), (r'rel="icon"', "favicon")]:
    if html and not re.search(tag, html):
        issues.append(f"[중간] 누락: {label}")
for img in re.findall(r"<img\b[^>]*>", html):
    if "alt=" not in img:
        issues.append(f"[중간] alt 없는 이미지: {img[:80]}")
for a in re.findall(r"<a\b[^>]*target=\"_blank\"[^>]*>", html):
    if "noopener" not in a:
        issues.append(f"[낮음] noopener 없음: {a[:80]}")

todos = len(re.findall(r"\[TODO", html + projects_js))
if todos:
    notes.append(f"남은 TODO {todos}개 (사용자 입력 필요)")

print("== 경계면 대조 결과 ==")
print("\n".join(issues) if issues else "문제 없음")
for n in notes:
    print("참고:", n)
sys.exit(1 if any(i.startswith("[높음]") for i in issues) else 0)
