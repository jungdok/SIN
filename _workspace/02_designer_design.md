# 포트폴리오 디자인 명세

## 1. 미적 방향
**"여백 넓은 흰 종이 위에 왼쪽엔 항목명, 오른쪽엔 내용을 적어 내려간 한 장짜리 이력 카드."**

- 이유: 대상 독자는 여러 지원자를 빠르게 훑어보는 채용 담당자다. 모든 섹션이 같은 2열 틀(왼쪽 항목명, 오른쪽 내용)을 따르면 어디에 무엇이 있는지 바로 보이고, 이력서와 같은 읽기 방식이라 낯설지 않다.
- 사용자 선호(흰 배경, 넓은 여백, 차분한 톤)를 그대로 따른다. 장식은 헤어라인 한 줄과 잉크 블루 한 색뿐이다.
- 눈에 남는 요소는 한 곳에만 쓴다. **hero의 큰 이름(얇은 300 굵기, 최대 88px, 왼쪽 정렬)**. 나머지는 모두 조용하게 둔다.
- 피한 기본값: 중앙 정렬 히어로, 3열 카드 그리드, 카드마다 같은 그림자, 그라데이션, 제목 위 대문자 라벨, 01/02/03 번호, 버튼 뒤 '→'.

### 검토한 다른 방향 (채택하지 않음)
- 세리프 제목 + 크림색 배경의 편집 디자인: 차분하지만 "흰 배경" 선호와 어긋나고 흔한 생성형 결과와 닮았다.

## 2. 토큰 요약 (`02_designer_tokens.css`)
| 역할 | 라이트 | 다크 |
|---|---|---|
| 배경 `--color-bg` | #FFFFFF | #17191C |
| 면 `--color-surface` | #F6F7F8 | #202328 |
| 본문 `--color-text` | #1D1F23 (16:1) | #E6E7E9 (14:1) |
| 보조 `--color-text-muted` | #5F6368 (6.3:1) | #9CA1A8 (6.6:1) |
| 액센트 `--color-accent` | #2A4B8D 잉크 블루 (8.6:1) | #93B1EA (8.4:1) |
| 구분선 `--color-border` | #E4E6EA | #2C3036 |

- 폰트: **IBM Plex Sans KR** 한 종(300/400/600)으로 제목·본문 모두 처리. 한글 획이 곧고 담백해 "정돈된 기록" 느낌을 낸다. 제목과 본문의 차이는 굵기와 크기로만 준다.
- `--font-mono`는 시스템 고정폭 폰트이며 웹폰트를 불러오지 않는다. 코드 조각에만 쓰고, 태그·날짜에는 쓰지 않는다.
- 날짜·기간 숫자에는 `font-variant-numeric: tabular-nums`를 줘서 세로로 정렬되게 한다.
- 액센트 색은 링크, 주 버튼, 포커스 링, 프로젝트명 호버 밑줄에만 쓴다. 제목 일부 단어에 색을 넣지 않는다.

## 3. 공통 레이아웃 규칙
- 컨테이너: `max-width: var(--max-width)`, 좌우 여백 모바일 `--space-4`(16px), 768px 이상 `--space-6`(40px).
- **섹션 틀 (hero 제외 모든 섹션 공통)**
  - 모바일(375px~): 한 열. 섹션 제목 → 내용 순서로 쌓는다.
  - 데스크톱(≥ 960px): `grid-template-columns: var(--label-col) 1fr; gap: var(--space-6)`. 왼쪽 열에 섹션 제목(`h2`, `--text-lg`, 600, `--color-text`), 오른쪽 열에 내용. 모바일에서도 같은 크기로 쓴다.
  - 섹션 제목은 데스크톱에서 `position: sticky; top: calc(var(--header-height) + var(--space-5))`로 스크롤하는 동안 왼쪽에 머문다.
  - 각 섹션 위쪽에 `1px solid var(--color-border)` 헤어라인, 섹션 간 간격 `--space-7`(모바일) / `--space-8`(데스크톱).
- 본문 단락은 `max-width: var(--measure)`, `line-height: var(--leading-body)`, 왼쪽 정렬. 양쪽 정렬 금지.
- 섹션 제목은 한국어 명사 그대로: 소개, 프로젝트, 경험, 기술, 연락처. 영어 대문자 라벨을 위에 따로 달지 않는다.

```
데스크톱 (≥960px)
┌──────────────────────────────────────────────┐
│ 이름                     소개 프로젝트 … [◐] │  ← header (sticky)
├──────────────────────────────────────────────┤
│                                              │
│ 홍길동                                        │  ← hero (큰 이름, 왼쪽)
│ 사용자 문제를 코드로 푸는 컴퓨터공학도          │
│ [연락하기] 이력서 보기                         │
│                                              │
├──────────────────────────────────────────────┤
│ 소개        │ 본문 3~4문장 …                   │
├──────────────────────────────────────────────┤
│ 프로젝트    │ [이미지 16:10] 제목/요약/문제…    │
│  (sticky)   │ [이미지 16:10] …                 │
├──────────────────────────────────────────────┤
│ 경험        │ 2022.03–2027.02  학교 · 전공     │
└──────────────────────────────────────────────┘
```

## 4. 섹션별 레이아웃 (콘텐츠 문서 순서)

### header / 내비게이션
- 상단 고정(`position: sticky; top: 0`), 높이 `--header-height`, 배경 `--color-bg`, 스크롤 시작 후에만 아래 헤어라인 표시.
- 왼쪽: 이름(텍스트, `--text-base` 600, `#hero` 링크). 오른쪽: 섹션 링크(소개·프로젝트·경험·기술·연락처) + 다크 모드 토글 버튼(해·달 아이콘, `aria-label="다크 모드 전환"`).
- 모바일(<768px): 섹션 링크를 숨기고 "메뉴" 텍스트 버튼 하나. 누르면 헤더 아래로 링크 목록이 펼쳐진다(`aria-expanded` 사용, 높이 전환 `--duration-fast`). 링크를 누르면 닫힌다.
- 현재 보고 있는 섹션 링크는 `--color-text`, 나머지는 `--color-text-muted` (IntersectionObserver). 밑줄·배경 강조는 하지 않는다.
- `scroll-margin-top: calc(var(--header-height) + var(--space-5))`를 모든 섹션에 준다.

### hero (`#hero`)
- 왼쪽 정렬. 모바일에서 위 여백 `--space-7`, 데스크톱에서 `min-height: 70vh` 안에서 세로 중앙보다 약간 아래(하단 정렬 + 아래 여백 `--space-8`).
- 이름: `--text-display`, 굵기 300, `letter-spacing: var(--tracking-display)`, `line-height: var(--leading-tight)`. 이것이 페이지에서 유일하게 큰 요소다.
- subtitle: `--text-lg`, `--color-text-muted`, 이름 아래 `--space-4`.
- 버튼 두 개, subtitle 아래 `--space-6`, 서로 `--space-3` 간격:
  - 주 버튼 "연락하기": 배경 `--color-accent`, 글자 `--color-accent-contrast`, `--radius-sm`, 패딩 `--space-3 --space-5`, 최소 높이 44px.
  - 보조 "이력서 보기": 테두리 없는 텍스트 링크 스타일(액센트색 + 밑줄 오프셋 4px). 이력서 링크가 비어 있으면 숨긴다.
- 프로필 사진 없음(콘텐츠 문서가 미니멀 톤에서 생략 가능하다고 함). 추후 넣는다면 about 섹션 오른쪽 열 상단, 정사각 1:1, 160px, `--radius-md`.

### about (`#about`)
- 섹션 틀 그대로. 오른쪽 열에 본문 3~4문장, 첫 문장만 `--text-lg`(리드), 나머지 `--text-base`.
- 줄 길이 `--measure` 제한.

### projects (`#projects`)
- **카드 그리드가 아니라 세로 목록.** 프로젝트끼리 `--space-7` 간격, 사이에 헤어라인 없음(여백으로 구분).
- 한 항목 구조:
  1. 대표 이미지 — 비율 16:10, `--radius-md`, 배경 `--color-surface`, `object-fit: cover`.
  2. 제목 `h3` — `--text-lg` 600.
  3. summary — `--text-base`, `--color-text-muted`.
  4. 문제 / 역할 / 결과 — 작은 정의 목록(`dl`). 항목명(`dt`: 문제, 역할, 결과)은 `--text-sm` `--color-text-muted`, 값(`dd`)은 `--text-base`. 모바일은 위아래로, 데스크톱은 `dt` 4rem + `dd` 나머지 2열.
  5. tags — 텍스트를 쉼표 대신 작은 칩으로: `--text-sm`, 배경 `--color-surface`, `--radius-sm`, 패딩 `--space-1 --space-2`. 테두리 없음.
  6. 링크 — "사이트 보기", "코드 보기" 텍스트 링크(액센트색). 값이 비면 해당 링크를 렌더링하지 않는다.
- 모바일: 이미지 → 텍스트 한 열.
- 데스크톱(≥960px, 오른쪽 열 안): 이미지 5 : 텍스트 7 비율 2열 (`grid-template-columns: 5fr 7fr; gap: var(--space-5)`). 이미지는 항상 왼쪽(지그재그 금지 — 훑어보기 쉽게).
- 호버(포인터 기기만, `@media (hover: hover)`): 항목 전체가 아니라 제목 링크에만 반응. 제목에 액센트색 밑줄이 나타남(`text-decoration-color` 투명 → 액센트, `--duration-fast`). 이미지 확대·그림자·카드 들림 효과는 쓰지 않는다.
- 제목과 이미지는 `link`가 있으면 그 링크로, 없으면 `repo`로, 둘 다 없으면 링크 없음.

### experience (`#experience`)
- 오른쪽 열 안에 하위 그룹 3개: 학력, 대외활동, 수상·자격. 그룹 제목 `h3` `--text-base` 600, 그룹 간 `--space-6`.
- 항목은 기간이 있는 시간순 목록이라 날짜 열을 둔다:
  - 데스크톱: `grid-template-columns: 9rem 1fr`. 왼쪽 기간(`--text-sm`, `--color-text-muted`, tabular-nums), 오른쪽 "활동명 · 역할"(600) + 아래 설명 1줄(`--color-text-muted`).
  - 모바일: 기간을 활동명 위에 작은 글씨로.
- 항목 간 `--space-5`. 수상·자격 그룹은 비어 있으면 그룹 전체를 렌더링하지 않는다.
- 세로 타임라인 선·점은 쓰지 않는다(날짜 열만으로 충분).

### skills (`#skills`)
- 그룹별 한 줄: 데스크톱은 `grid-template-columns: 9rem 1fr`(experience와 같은 열 폭으로 맞춤), 왼쪽 그룹명(`--color-text-muted`), 오른쪽 항목을 쉼표로 나열한 일반 텍스트.
- 칩·아이콘·숙련도 막대 없음. 모바일은 그룹명 위, 항목 아래.

### contact (`#contact`)
- 오른쪽 열에 안내 문구(`--text-lg`), 아래 이메일 주소를 큰 텍스트 링크로(`--text-xl`, 400, 액센트색, `mailto:`). 이 섹션의 주인공은 이메일 주소다.
- 그 아래 GitHub · LinkedIn · 블로그 · 이력서 링크를 가로 목록으로(`gap: var(--space-5)`, 모바일에서 줄바꿈 허용). 빈 값은 렌더링하지 않는다.
- 이메일 복사 버튼(선택): 이메일 옆 "복사" 텍스트 버튼, 누르면 2초간 "복사됨"으로 바뀜(`aria-live="polite"`).

### footer
- 헤어라인 위 `--space-6` 여백, `--text-sm`, `--color-text-muted`, 왼쪽 정렬 "© 연도 이름". 한 줄.

## 5. 인터랙션
- **페이지 로드 한 번만**: hero의 이름 → subtitle → 버튼이 순서대로 불투명도 0→1, 위로 8px 이동하며 나타난다. 각 `--duration-slow`, 80ms 간격, `--ease`. 이것이 페이지의 유일한 자동 모션.
- 섹션별 스크롤 등장 효과는 **쓰지 않는다**(차분한 톤 유지, 콘텐츠를 늦게 보여주지 않기 위해).
- 링크·버튼 호버: 색·밑줄 변화만, `--duration-fast`. 주 버튼 호버는 배경을 약간 어둡게(`filter: brightness(0.92)`; 다크 모드는 `brightness(1.08)`).
- 포커스: 모든 대화형 요소에 `outline: 2px solid var(--color-focus); outline-offset: 3px`. `:focus-visible` 기준.
- 부드러운 스크롤: `html { scroll-behavior: smooth }`를 `prefers-reduced-motion: no-preference`일 때만.
- `prefers-reduced-motion: reduce`: 토큰에서 duration이 0이 되며, hero 등장 효과도 처음부터 보이는 상태로 둔다.
- 다크 모드 토글: `html[data-theme]`에 light/dark를 설정하고 localStorage에 저장(try/catch). 저장값이 없으면 시스템 설정을 따른다.

## 6. 이미지 비율과 플레이스홀더
- 프로젝트 이미지: 16:10 고정(`aspect-ratio: 16 / 10`), 권장 원본 1600×1000, WebP/PNG, `loading="lazy"`, 의미 있는 `alt`(예: "캠퍼스 스터디 매칭 서비스 검색 화면").
- 이미지가 없을 때: 같은 비율의 `--color-surface` 상자 안에 프로젝트 제목을 `--text-sm` `--color-text-muted`로 왼쪽 아래에 표시. 아이콘·패턴·그라데이션을 넣지 않는다. 이 상자는 `aria-hidden="true"`.
- 프로필 사진은 기본 생략(위 hero 참고).

## 7. 반응형 기준점
- 기본: 375px 한 열.
- 768px: 좌우 여백 확대, 헤더 섹션 링크 노출.
- 960px: 섹션 2열 틀(항목명 | 내용), 프로젝트 이미지·텍스트 2열.
- 가로 스크롤이 생기지 않아야 한다(긴 URL·이메일은 `overflow-wrap: anywhere`).

## 8. 개발자 참고
- 토큰 파일의 값 외에 색·크기·간격을 새로 만들지 않는다. 부족하면 디자이너에게 요청.
- 웹폰트 링크: `https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@300;400;600&display=swap` (preconnect 포함).
- 한글 줄바꿈: 본문에 `word-break: keep-all`.
