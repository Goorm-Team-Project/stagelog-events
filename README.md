# Events Service

`events`는 공연 목록, 상세, 요약 정보를 제공하는 Django 서비스입니다.

## Responsibility
- 공연 목록/상세 조회
- 다른 서비스가 참조하는 공연 내부 API 제공
- 메인 화면용 공연 카드 정보 구성

## Main Routes
- Public
  - `/api/events*`
- Internal
  - `/internal/events/{event_id}/exists`
  - `/internal/events/{event_id}/summary`
  - `/internal/events:batch-summary`

## Runtime
- Python 3.12 / Django / Gunicorn
- 컨테이너 포트: `8000`
- Kubernetes에서는 Secret key를 환경변수로 직접 주입합니다

## Deploy
- Kubernetes 매니페스트
  - [`events/deploy/k8s/events-env-externalsecret.yaml`](/home/woosupar/stagelog/events/deploy/k8s/events-env-externalsecret.yaml)
  - [`events/deploy/k8s/events-deployment.yaml`](/home/woosupar/stagelog/events/deploy/k8s/events-deployment.yaml)
- CI/CD workflow
  - [`events/.github/workflows/build-and-push.yml`](/home/woosupar/stagelog/events/.github/workflows/build-and-push.yml)

배포 흐름은 아래와 같습니다.
- GitHub Actions가 이미지를 빌드해 ECR에 push
- 같은 workflow가 `stagelog-gitops`의 이미지 태그를 갱신
- ArgoCD가 변경된 태그를 감지해 클러스터에 반영

## Configuration
주요 환경변수 예시는 [`events/.env.example`](/home/woosupar/stagelog/events/.env.example) 에 있습니다.

운영 환경에서는 SSM Parameter Store를 소스 오브 트루스로 사용하고, ExternalSecret이 필요한 키만 Kubernetes Secret으로 동기화합니다.

## Notes
- 즐겨찾기 수 집계는 `auth` 서비스의 내부 API를 통해 조회합니다.
- `events`는 단독 서비스 DB를 사용하며, 원본 monolith의 Django 공용 앱 의존은 제거된 상태입니다.
- 보호 라우트에서는 API Gateway가 전달한 `X-User-Id` 헤더를 사용자 문맥으로 사용합니다.
