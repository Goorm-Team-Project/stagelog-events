# events-service

## Responsibility
- Event catalog/list/detail read domain ownership.
- Provides event internal APIs for other services.

## Owned Domain
- Events data and event summary projection.

## API Scope
- Public: `/api/events*`
- Internal: `/internal/events/{event_id}/exists`, `/internal/events/{event_id}/summary`, `/internal/events:batch-summary`

## Data Ownership
- Primary schema: `stagelog_events`
- Events tables are read/written only by events-service.

## Dependencies
- Can call auth/core internal APIs only through defined internal contracts.

## Runtime
- API Deployment in EKS
- Shared contracts package for internal DTO compatibility
