# Project Artifacts

This repository includes the original course-project material alongside the Flask application. These files are retained as project evidence, not as a claim that every artifact is needed at runtime.

| Location | Purpose | Handling |
| --- | --- | --- |
| `app.py`, `templates/`, `static/` | Flask user interface and inference routes | Runtime application source. |
| `detect_pose.pkl` | Gradient Boosting classifier loaded by the Flask app | Treat as a binary compatibility artifact; use scikit-learn 0.24.2 unless it is retrained and revalidated. |
| `Machine Learning Code/` | Landmark-feature classifier training/evaluation notebook and CSV | Historical experiment source. The notebook writes the bundled pickle from its Gradient Boosting pipeline. |
| `Deep Learning Code/` | Separate TensorFlow pose-classification experiment and saved model | Not used by `app.py`; keep its dependencies separate from the Flask app. |
| `Web Scraper/` | Source-collection notebook and scraped pose text | Historical data-collection material; review source and license terms before reuse. |
| `Docs/` | Original report, presentation, artifact notes, and demo media | Project documentation, not runtime dependencies. `media/demo-screenshot.png` links to `media/demo.mp4` from the README. |
| `upload/` | Files saved by the local upload route | Runtime data. New uploads are ignored by Git and should not be published. |

## Artifact Boundaries

- Do not unpickle an artifact from an untrusted source. Python pickle can execute code during deserialization.
- The bundled classifier recognizes only the five labels documented in the README. Other poses are out of scope.
- The repository does not include a dataset manifest, a repeatable training environment, or an independent evaluation dataset. Any retraining effort should add those pieces before replacing the model.
