---
name: portfolio-qa
description: 포트폴리오 홈페이지 검수 체크리스트. 콘텐츠 문서·디자인 토큰·코드 간 불일치, 반응형 깨짐, 접근성, 깨진 링크, 콘솔 오류를 찾는다. 포트폴리오 사이트 검수·점검·테스트·"잘 되는지 확인", 배포 전 확인 요청 시 사용. portfolio-qa 에이전트가 사용한다.
---

# 포트폴리오 QA

## 1. 경계면 대조 (가장 중요)
파일이 있는지가 아니라, 양쪽을 **동시에 읽고 비교**한다.

| 경계 | 비교 방법 |
|------|----------|
| 콘텐츠 → HTML | 콘텐츠 문서의 섹션 순서·ID 목록과 `index.html`의 `section[id]` 목록이 같은가. 문구가 바뀌거나 빠지지 않았는가 |
| 콘텐츠 → projects.js | 프로젝트 수, 필드명, 값이 문서와 같은가 |
| 토큰 → CSS | `style.css`의 `var(--x)`가 모두 tokens.css에 정의돼 있는가. 하드코딩된 색(`#`, `rgb(`)이 있는가 |
| 데이터 → 렌더링 | 빈 필드(link 없음 등)일 때 빈 버튼이나 `undefined`가 보이지 않는가 |
| 내비 → 섹션 | 모든 `href="#..."`가 실제 id를 가리키는가 |

`scripts/check_consistency.py`를 먼저 실행하면 위 항목 대부분을 자동으로 확인한다:
```
python .claude/skills/portfolio-qa/scripts/check_consistency.py
```

## 2. 실행 검증
`example-skills:webapp-testing` 스킬(Playwright)을 쓸 수 있으면:
- `site/index.html`을 375 / 768 / 1440px로 열어 `_workspace/qa_screens/`에 전체 스크린샷 저장
- 콘솔 오류 0개인지
- 가로 스크롤 여부 (`document.documentElement.scrollWidth > innerWidth`)
- 다크 모드 토글 후 글자가 보이는지
- Tab 키로 모든 링크·버튼에 포커스가 보이는지

쓸 수 없으면 정적 검사로 대체하고 보고서에 명시한다.

## 3. 기본 점검
- 이미지 `alt`, `<title>`, meta description, OG 태그, favicon
- 외부 링크 `target="_blank"`에 `rel="noopener"`
- 남은 `[TODO]` 목록 (결함이 아니라 사용자에게 알릴 항목)
- `prefers-reduced-motion`에서 애니메이션이 꺼지는지

## 4. 보고서 — `_workspace/04_qa_report.md`
```markdown
# QA 보고서
판정: 통과 | 수정 필요
## 이전 지적 사항 해결 여부   ← 재검수 시
## 수정 필요 (심각도 순)
- [높음] site/css/style.css:42 — 증상 — 수정 방법
## 참고 제안 (취향, 선택)
## 남은 TODO (사용자 입력 필요)
## 스크린샷
```
심각도: 높음(깨짐·안 보임·오류) / 중간(불일치·접근성) / 낮음(사소함).
