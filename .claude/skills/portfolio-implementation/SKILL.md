---
name: portfolio-implementation
description: 포트폴리오 홈페이지를 실제 코드(HTML/CSS/JS, 또는 요청 시 React·Next.js)로 구현·수정하는 규칙. 포트폴리오 사이트 만들기, 섹션 추가, 프로젝트 카드 추가, 반응형 수정, 다크 모드 토글, QA 지적 사항 수정, 배포 준비 요청 시 사용. portfolio-developer 에이전트가 사용한다. 문구나 디자인 방향 결정에는 쓰지 않는다.
---

# 포트폴리오 구현

## 1. 기본 구조 (정적 사이트)
```
site/
├── index.html
├── css/tokens.css      ← _workspace/02_designer_tokens.css 복사
├── css/style.css
├── js/main.js          ← 내비게이션, 테마 토글, 스크롤 효과, 프로젝트 렌더링
├── data/projects.js    ← 프로젝트 데이터 (window.PROJECTS = [...])
└── assets/             ← 이미지, favicon, 이력서 PDF
```
`fetch`로 JSON을 읽으면 파일을 더블클릭해 열 때(file://) 막히므로, 데이터는 `<script src="data/projects.js">`로 불러온다.

사용자가 다른 스택을 원하면 같은 원칙(토큰 분리, 데이터 분리, 섹션 ID 유지)으로 그 스택에 맞게 구성한다.

## 2. 코드 규칙
- **섹션 ID**: 콘텐츠 문서의 ID를 `<section id="...">`에 그대로 쓴다. 내비 링크는 `#id`.
- **문구**: 콘텐츠 문서에서 그대로 복사. `[TODO]`도 그대로 두되 눈에 띄게(`<mark class="todo">`) 표시해 사용자가 찾기 쉽게 한다.
- **스타일**: `style.css`는 토큰 변수만 사용. 새 색·폰트 값이 필요하면 notes에 기록하고 tokens.css에 추가한다.
- **프로젝트 데이터**: 필드는 `id, title, summary, problem, role, result, tags, link, repo, image` — 콘텐츠 문서와 동일. 빈 필드는 해당 요소를 렌더링하지 않는다(빈 링크 버튼 금지).
- **반응형**: 모바일 우선. 375 / 768 / 1440px에서 가로 스크롤이 생기지 않아야 한다.
- **접근성**: 의미 있는 태그(`header`, `nav`, `main`, `section`, `footer`), 이미지 `alt`, 키보드 포커스 표시, 외부 링크 `rel="noopener"`.
- **메타**: `<title>`, `meta description`, Open Graph(제목·설명·이미지), favicon.
- **성능**: 이미지 `loading="lazy"`와 width/height 지정, JS는 `defer`.
- **테마**: 토글 버튼이 `document.documentElement.dataset.theme`을 바꾸고, 선택값은 `localStorage`에 저장(try/catch로 감싼다).

## 3. 마무리
- `_workspace/03_developer_notes.md`에 구현 요약, 문서와 달라진 점, 남은 TODO, 여는 방법(`site/index.html` 더블클릭), 배포 방법(GitHub Pages 한 줄 안내)을 적는다.
