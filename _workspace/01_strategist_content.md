# 포트폴리오 콘텐츠

> 초안 상태: 사용자가 구체 정보 없이 "알아서 초안으로"를 선택함. 아래 `[TODO: ...]`는 모두 실제 정보로 바꿔야 하며, 자리표시 문구는 레이아웃 확인용 예시일 뿐 사실이 아니다.
> 표기 규칙: `[TODO: 설명]` = 반드시 채울 정보. 괄호 안 "예:"는 형식 예시다. 개발자는 TODO 문자열을 화면에 그대로 노출하지 말고, 자리표시 텍스트(예시 값)를 넣고 주석으로 TODO를 남긴다.

## 기본 정보
- 이름: [TODO: 이름 — 예: 홍길동]
- 직무/분야: 학생·취업 준비생 — [TODO: 전공과 희망 직무 — 예: 컴퓨터공학 전공, 프론트엔드 개발자 지망]
- 대상 독자: 채용 담당자·인턴십 담당자 (가정)
- 원하는 행동: 이메일로 연락 (보조 행동: 이력서 PDF 보기) (가정)
- 톤: 깔끔·미니멀, 차분하고 담백함. 꾸밈말 없이 한 일과 배운 것을 짧게 쓴다.
- 언어: 한국어 단일 (영어 병기 없음)

## 섹션 순서
hero, about, projects, experience, skills, contact

- 가정: 채용 대상이므로 `projects` → `experience` 순. 학생은 경력보다 프로젝트가 가장 강한 근거이므로 프로젝트를 앞에 둔다.
- `experience`는 학력·대외활동·수상을 하위 그룹으로 묶는다(학생 특성상 회사 경력보다 이쪽이 중심).

## hero
- title: [TODO: 이름] — 예: 홍길동
- subtitle: [TODO: 한 줄 정체성, 20자 안팎] — 예: "사용자 문제를 코드로 푸는 컴퓨터공학도"
- cta_label: 연락하기
- cta_link: #contact
- secondary_label: 이력서 보기 (선택)
- secondary_link: [TODO: 이력서 PDF 경로 — 예: /resume.pdf]

## about
(본문 — 3~4문장. 아래는 형식 예시이며 전부 교체 필요)

[TODO: 소속 — 예: ○○대학교 ○○학과 4학년]에 재학 중인 [TODO: 이름]입니다.
[TODO: 관심 분야 — 예: 웹 서비스의 사용성]에 관심을 두고, 수업과 동아리에서 [TODO: 해 온 일 — 예: 팀 프로젝트로 실제 사용자가 쓰는 서비스를 만들어 왔습니다].
프로젝트마다 문제를 정의하고, 직접 만들고, 결과를 돌아보는 과정을 기록합니다.
[TODO: 목표 — 예: 졸업 후 ○○ 분야의 주니어 개발자로 일하고 싶습니다.]

- 사진: [TODO: 프로필 사진 사용 여부 — 미니멀 톤에서는 생략 가능]

## projects
대표작 3개(자리표시). 가장 강한 프로젝트를 맨 앞에 둔다. 문구는 문제 → 내가 한 일 → 결과 순서.

- id: project-one
  title: [TODO: 프로젝트명 — 예: 캠퍼스 스터디 매칭 서비스]
  summary: [TODO: 한 줄 요약 — 예: 같은 수업 수강생끼리 스터디를 찾는 웹 서비스]
  problem: [TODO: 어떤 문제를 풀었나 — 예: 스터디원을 구하는 공지가 단톡방에 흩어져 찾기 어려웠다]
  role: [TODO: 내 역할·기여 — 예: 4인 팀에서 프론트엔드 전담, 검색·필터 화면 구현]
  result: [TODO: 결과 — 사용자 수, 수상, 배운 점 등 실제 있는 것만. 수치가 없으면 "배운 점" 1문장]
  tags: [TODO: 사용 기술·도구 — 예: React, Firebase]
  link: [TODO: 배포 URL, 없으면 비움]
  repo: [TODO: GitHub 저장소 URL, 없으면 비움]
  image: [TODO: 대표 이미지 경로 — 예: images/project-one.png]

- id: project-two
  title: [TODO: 프로젝트명 — 예: 수업 과제/졸업 작품]
  summary: [TODO: 한 줄 요약]
  problem: [TODO: 풀려고 한 문제]
  role: [TODO: 내 역할·기여]
  result: [TODO: 결과 또는 배운 점]
  tags: [TODO: 사용 기술·도구]
  link: [TODO: 배포 URL, 없으면 비움]
  repo: [TODO: 저장소 URL, 없으면 비움]
  image: [TODO: images/project-two.png]

- id: project-three
  title: [TODO: 프로젝트명 — 예: 공모전·해커톤 출품작]
  summary: [TODO: 한 줄 요약]
  problem: [TODO: 풀려고 한 문제]
  role: [TODO: 내 역할·기여]
  result: [TODO: 결과 — 수상 이력이 있다면 여기에 명시]
  tags: [TODO: 사용 기술·도구]
  link: [TODO: 배포 URL, 없으면 비움]
  repo: [TODO: 저장소 URL, 없으면 비움]
  image: [TODO: images/project-three.png]

- 참고: 링크·저장소가 비어 있으면 해당 버튼을 숨긴다. 프로젝트가 3개 미만이면 카드 수를 줄이고, 6개를 넘기지 않는다.

## experience
최신순. 항목당 1~2줄(한 일·성과). 하위 그룹 3개.

### 학력 (education)
- [TODO: 학교명 · 전공] — [TODO: 기간, 예: 2022.03 – 2027.02(졸업 예정)]
  - [TODO: 관련 수업·학점 등 강조할 점 1줄 (선택)]

### 대외활동 (activities)
- [TODO: 활동명 · 역할 — 예: ○○ 개발 동아리 · 운영진] — [TODO: 기간]
  - [TODO: 한 일 1줄 — 예: 신입 부원 대상 스터디 운영]
- [TODO: 활동명 · 역할 — 예: ○○ 서포터즈 / 교내 학생회] — [TODO: 기간]
  - [TODO: 한 일 1줄]

### 수상·자격 (awards)
- [TODO: 수상명 또는 자격증명 — 발급 기관, 연도. 없으면 이 그룹 전체 생략]

## skills
그룹별 나열. 숙련도 막대·퍼센트는 쓰지 않는다.

- 언어: [TODO: 예: JavaScript, Python]
- 프레임워크·라이브러리: [TODO: 예: React]
- 도구: [TODO: 예: Git, Figma, Notion]
- 기타: [TODO: 외국어 등 — 예: 영어(TOEIC 점수가 있다면 기재), 없으면 생략]

## contact
- 안내 문구: "인턴십·채용 관련 제안은 이메일로 연락 주세요. 빠르게 답장드리겠습니다."
- email: [TODO: 이메일 주소 — 예: name@example.com]
- links:
  - GitHub: [TODO: URL, 없으면 생략]
  - LinkedIn: [TODO: URL, 없으면 생략]
  - 블로그/벨로그/노션: [TODO: URL, 없으면 생략]
- 이력서: [TODO: 이력서 PDF 경로 — hero의 secondary_link와 동일]
- footer: © [TODO: 연도] [TODO: 이름]

## TODO 및 사용자 확인 질문

### 사용자에게 확인할 질문 (우선순위 순)
1. 이름(사이트에 표시할 이름)과 연락용 이메일은 무엇인가요?
2. 전공과 희망 직무는 무엇인가요? (개발·디자인·기획·마케팅 등 — hero 한 줄 정체성과 skills 그룹이 여기에 따라 달라집니다)
3. 대표 프로젝트 1~3개의 이름, 한 일, 결과(또는 배운 점)를 알려주세요. 배포 링크·GitHub 저장소가 있나요?
4. 대외활동·수상·자격증 중 넣고 싶은 항목이 있나요?
5. 이력서 PDF를 사이트에 올릴 건가요? 프로필 사진을 넣을 건가요?

### TODO 목록
- [기본 정보] 이름, 전공, 희망 직무
- [hero] title(이름), subtitle(한 줄 정체성), 이력서 링크
- [about] 소속·학년, 관심 분야, 해 온 일, 목표 / 프로필 사진 여부
- [projects] 프로젝트 3개의 title·summary·problem·role·result·tags·link·repo·image
- [experience] 학력(학교·전공·기간), 대외활동 2개, 수상·자격(없으면 생략)
- [skills] 언어·프레임워크·도구·기타
- [contact] 이메일, GitHub·LinkedIn·블로그 URL, 이력서 PDF, footer 연도

### 가정 사항
- 대상 독자는 채용·인턴십 담당자, 최종 행동은 이메일 연락으로 가정했다.
- 희망 직무를 모르므로 예시는 개발 직군 기준으로 썼다. 다른 직군이면 skills 그룹명과 프로젝트 필드 예시를 바꾼다(섹션 ID·필드명은 유지).
