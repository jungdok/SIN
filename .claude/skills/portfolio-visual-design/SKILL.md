---
name: portfolio-visual-design
description: 포트폴리오 홈페이지의 미적 방향, 색 팔레트, 폰트 조합, 간격, 섹션 레이아웃, 다크 모드, 호버·스크롤 효과를 정하고 디자인 토큰(CSS 변수)으로 만드는 방법. 포트폴리오 디자인·스타일·색·폰트·분위기 변경, "더 세련되게", "다른 느낌으로" 요청 시 사용. portfolio-designer 에이전트가 사용한다. 문구 작성이나 실제 HTML 구현에는 쓰지 않는다.
---

# 포트폴리오 비주얼 디자인

## 1. 참고할 설치된 스킬
- **`ui-ux-pro-max:ui-ux-pro-max`** — 스타일·팔레트·폰트 조합·UX 가이드라인 데이터. 콘텐츠의 톤과 직무에 맞는 스타일과 팔레트 후보를 여기서 찾는다.
- **`example-skills:frontend-design`** — 템플릿 같지 않은, 의도가 분명한 미적 방향을 잡는 원칙.

두 스킬을 불러 읽은 뒤 이 문서의 절차로 결과를 정리한다. 스킬을 불러올 수 없으면 아래 원칙만으로 진행한다.

## 2. 방향 정하기
콘텐츠 문서의 **톤·직무·대상 독자**에서 출발한다.
- 개발자 → 정돈된 그리드, 고정폭 폰트 포인트, 절제된 색
- 디자이너/아티스트 → 작업물이 주인공. 큰 이미지, 과감한 타이포, UI는 뒤로
- 기획/마케팅 → 읽기 쉬운 본문, 성과 수치 강조

방향은 한 문장으로 적는다 (예: "신문 편집 디자인처럼 큰 세리프 제목과 넉넉한 여백"). 흔한 기본값(보라-파랑 그라데이션, 중앙 정렬 히어로 + 3열 카드, Inter 단독 사용)은 이유가 없으면 피한다.

## 3. 토큰 — `_workspace/02_designer_tokens.css`
```css
:root {
  --color-bg: ; --color-surface: ; --color-text: ; --color-text-muted: ;
  --color-accent: ; --color-accent-contrast: ; --color-border: ;
  --font-display: ; --font-body: ; --font-mono: ;
  --text-sm: ; --text-base: ; --text-lg: ; --text-xl: ; --text-display: ;   /* clamp() 권장 */
  --space-1: ; ... --space-8: ;
  --radius-sm: ; --radius-md: ;
  --shadow-card: ;
  --max-width: ;
  --ease: ;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { /* 색만 재정의 */ } }
:root[data-theme="dark"] { /* 동일 */ }
```
- 본문 대비 4.5:1, 큰 제목 3:1 이상을 확인한다.
- 웹폰트는 Google Fonts에서 2개 이하. 한글이 들어가면 한글 지원 폰트(Pretendard, Noto Sans KR 등)를 본문에 둔다.

## 4. 명세 — `_workspace/02_designer_design.md`
- 방향 한 문장 + 이유
- 섹션별 레이아웃 (콘텐츠 문서의 섹션 ID 순서대로, 모바일 → 데스크톱 변화 포함)
- 프로젝트 카드 구조와 호버 상태
- 인터랙션: 스크롤 등장 효과 등. `prefers-reduced-motion`이면 끈다
- 내비게이션 방식 (상단 고정 / 사이드 등)
- 이미지 비율과 플레이스홀더 규칙
