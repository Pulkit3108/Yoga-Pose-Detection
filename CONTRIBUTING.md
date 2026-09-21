# Contributing

Contributions should improve clarity, reproducibility, or safe local use of the project.

## Scope

- Keep Flask application changes separate from notebook retraining or data-collection work.
- Do not replace `detect_pose.pkl` without documenting the training data, feature schema, dependency versions, evaluation procedure, and measured result.
- Do not commit camera captures, user uploads, credentials, local environments, or notebook checkpoints.
- Preserve the original report, presentation, scraped text, and model artifacts unless a change explicitly updates their provenance or replaces them.

## Documentation Changes

- Distinguish observed notebook output from independently reproduced results.
- State the safety boundary: pose labels are informational and do not assess exercise form or health.
- Keep setup instructions aligned with the dependency files and app entry point.

## Validation

Before opening a pull request, run the narrowest relevant validation. Documentation-only changes should pass `git diff --check` and have working local Markdown links. Application changes should include a reproducible test or manual validation plan that does not require a camera or user-uploaded image by default.
