---
name: portfolio-builder
description: 나만의 포트폴리오 홈페이지를 만드는 전체 과정(콘텐츠 → 디자인 → 구현 → 검수)을 에이전트 팀으로 조율하는 오케스트레이터. "포트폴리오 사이트 만들어줘", "내 소개 홈페이지", "개인 웹사이트", "이력서를 웹사이트로" 요청 시 반드시 사용. 후속 작업도 이 스킬로 처리한다 — "포트폴리오 다시 실행", "재실행", "업데이트", "수정", "보완", "프로젝트 추가", "디자인만 다시", "문구만 다시", "검수만 다시", "이전 결과 기반으로 개선". 포트폴리오와 무관한 일반 웹 개발 질문이나 단순 질문에는 쓰지 않는다.
---

# Portfolio Builder — 오케스트레이터

## 팀 구성
| 에이전트 | 파일 | 스킬 | 산출물 |
|---------|------|------|-------|
| portfolio-strategist | `.claude/agents/portfolio-strategist.md` | portfolio-content | `_workspace/01_strategist_content.md` |
| portfolio-designer | `.claude/agents/portfolio-designer.md` | portfolio-visual-design | `_workspace/02_designer_design.md`, `02_designer_tokens.css` |
| portfolio-developer | `.claude/agents/portfolio-developer.md` | portfolio-implementation | `site/`, `_workspace/03_developer_notes.md` |
| portfolio-qa | `.claude/agents/portfolio-qa.md` | portfolio-qa | `_workspace/04_qa_report.md` |

**패턴:** 파이프라인(콘텐츠 → 디자인 → 구현) + 생성-검증 루프(구현 ↔ QA)
**실행 모드:** 서브 에이전트. 각 단계가 앞 단계의 파일 산출물에 순차적으로 의존하고, 팀원 간 실시간 토론이 필요 없어서다. 모든 호출은 `Agent` 도구로 하며 `subagent_type: "general-purpose"`, `model: "opus"`를 지정한다. 프롬프트에는 "`.claude/agents/{name}.md`를 먼저 읽고 그 역할과 스킬을 따르라"를 넣는다.
**데이터 전달:** 파일 기반(`_workspace/`) + 반환값(요약·질문 목록).

## Phase 0: 컨텍스트 확인
1. `_workspace/`와 `site/` 존재 여부를 확인한다.
   - 없음 → **초기 실행** (Phase 1부터)
   - 있음 + 부분 수정 요청(예: "색만 바꿔줘", "프로젝트 하나 추가") → **부분 재실행**: 영향받는 에이전트부터만 실행
     - 문구/프로젝트 변경 → strategist → developer → qa
     - 디자인 변경 → designer → developer → qa
     - 버그/코드 수정 → developer → qa
     - 검수만 → qa
   - 있음 + 완전히 새 입력(다른 사람/새 방향) → `_workspace/`를 `_workspace_prev/`로 옮기고 초기 실행
2. 초기 실행이면 사용자에게 필요한 정보를 **한 번에** 묻는다: 이름·직무, 대상 독자, 대표 프로젝트(제목·설명·링크), 연락처, 선호 분위기/참고 사이트, 이력서·사진 파일. 사용자가 "알아서"라고 하면 `[TODO]`를 남긴 초안으로 진행한다.

## Phase 1: 콘텐츠 (strategist)
- 입력: 사용자 정보 전체(대화 내용 요약 + 첨부 파일 경로)
- 반환에 "사용자 확인 질문"이 있으면 사용자에게 전달하고, 답을 받으면 strategist를 재호출한다. 사용자가 넘어가자고 하면 그대로 진행.

## Phase 2: 디자인 (designer)
- 입력: `01_strategist_content.md` + 사용자 선호
- 추천 방향 한 문장을 사용자에게 짧게 보여준다(진행은 멈추지 않음).

## Phase 3: 구현 (developer)
- 입력: 01, 02 산출물

## Phase 4: 검수 (qa) ↔ 수정 루프
- qa 실행 → 판정이 "수정 필요"면 보고서의 "수정 필요" 항목만 developer에게 전달해 수정 → qa 재검수.
- 최대 2회 반복. 그래도 남은 항목은 최종 보고에 명시한다.

## Phase 5: 마무리
사용자에게 짧게 보고한다: 여는 방법(`site/index.html`), 남은 TODO, 알려진 문제, 다음에 할 수 있는 일(배포 등). 그리고 피드백을 묻는다 — "결과에서 바꾸고 싶은 부분이 있나요? 팀 구성이나 순서에 바꿀 점이 있나요?"

## 에러 핸들링
- 에이전트 실패 → 1회 재시도. 재실패 시 그 단계 없이 진행 가능한지 판단: 디자인 실패면 developer가 기본 토큰으로 구현, QA 실패면 `check_consistency.py`만 직접 실행해 결과 보고. 콘텐츠 실패면 중단하고 사용자에게 알린다(뒤 단계 전부의 입력이므로).
- 산출물 간 충돌 → 콘텐츠 문서 우선. 삭제하지 말고 notes에 양쪽을 기록.

## 파일 규칙
- 중간 산출물: `_workspace/{번호}_{에이전트}_{이름}.{확장자}` — 지우지 않는다(나중에 부분 재실행의 입력).
- 최종 산출물: `site/`

## 테스트 시나리오
- **정상:** "프론트엔드 개발자 포트폴리오 만들어줘, 프로젝트 3개 있어" → Phase 0 질문 → 1~4 순차 실행 → `site/index.html` 생성, QA 통과, TODO 목록 보고.
- **부분 재실행:** 기존 결과가 있을 때 "다크한 느낌으로 바꿔줘" → designer → developer → qa만 실행, 콘텐츠 문서는 변경 없음.
- **에러:** 사용자가 정보 없이 "알아서 만들어줘" → strategist가 TODO 초안 + 질문 목록 반환 → 사용자가 건너뛰기 → TODO가 표시된 사이트 완성, 보고에 TODO 목록 포함.
