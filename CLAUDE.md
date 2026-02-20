# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A static e-learning platform for Taiwan CDC (疾病管制署) — "AI 應用基礎班" (AI Application Fundamentals). Pure HTML/CSS/JavaScript with zero dependencies, no build tools, and no backend. All content is in Traditional Chinese (zh-TW).

## Running Locally

Serve with any static HTTP server:
```bash
python -m http.server 8000
# then visit http://localhost:8000
```
Or just open `index.html` directly in a browser. There is no build step, no package manager, no install command.

## Architecture

**Single JS file (`js/main.js`)** controls all interactive behavior. It exposes a global `window.CDC_Learning` API object that module HTML pages call directly (e.g., `onclick="CDC_Learning.checkQuizAnswer(...)"`).

**Global state** lives in `APP_STATE` with progress, current module, and current unit. Persistence uses three `localStorage` keys:
- `cdc_learning_progress` — module/unit completion status
- `cdc_quiz_results` — quiz answer records
- `cdc_checklist` — checklist item states

**Initialization chain** in `DOMContentLoaded`: `loadProgress → initMobileMenu → initTabs → initAccordions → initQuizzes → initDragDrop → initFillBlanks → initChecklists → initCopyButtons → initModuleNavigation → updateProgressDisplay → initLearningMap`.

**Single CSS file (`css/style.css`)** uses CSS custom properties defined on `:root` for theming (primary: `#1a5f7a`, secondary: `#57c5b6`, accent: `#159895`). Responsive breakpoints at 1024px, 860px, 768px, and 480px.

## Content Structure

- `index.html` — Landing page with learning map and module grid
- `modules/module0-5.html` — 6 course modules, each with sidebar unit navigation and a main content area containing units
- `certificate.html` — Graduation certificate page (unlocked when all modules complete and final quiz ≥ 80%)
- `recipes/prompt-recipes.html` — 20+ reusable prompt templates across 4 categories, each with copy-to-clipboard
- `resources/links.html` — Curated external learning resources
- `docs/影片腳本.md` — Video scripts for all modules (production reference)
- `slides/` — Python slide generation scripts (python-pptx, managed via `uv`)
  - `shared.py` — Brand constants and 15 reusable slide builder functions
  - `generate_module0-5.py` — One script per module
  - `generate_all.py` — Batch runner (`cd slides && uv run python generate_all.py`)
  - `output/` — 6 generated `.pptx` files (115 slides total, 56–64 KB each)
  - `output/pdf/` — PDF versions of slides (exported by user after generation)

## Interactive Components

Each module page may contain these component types, all driven by `main.js`:

| Component | HTML Pattern | JS Handler |
|-----------|-------------|------------|
| Single/multi-select quiz | `.quiz-container` with radio/checkbox | `checkQuizAnswer()` |
| Drag-and-drop ordering | `.drag-drop-container` with `.drag-item` | `checkDragDropAnswer()` / `resetDragDrop()` |
| Fill-in-the-blank | `.fill-blank-container` with inputs/selects | `checkFillBlankAnswer()` / `showFillBlankAnswers()` |
| Scenario questions | `.scenario-container` | `checkScenarioAnswer()` |
| Checklists | `.checklist` with checkboxes | `initChecklists()` (auto-persisted) |
| Copy buttons | `.btn-copy` with `data-copy-target` | `initCopyButtons()` |
| Tabs / Accordions | `.tab-btn` / `.accordion-header` | `initTabs()` / `initAccordions()` |

## Key Conventions

- Module pages follow a consistent structure: sidebar nav listing units + main area with `#unit-N` containers
- Quiz answers are encoded in HTML `data-correct` attributes
- Fill-in-the-blank accepts multiple answers separated by `|` (pipe), matching is case-insensitive
- Unit navigation uses `showUnit(moduleId, unitIndex)` — called from sidebar links
- Completion is tracked per-unit; module auto-completes when all units are done
- Video sections embed YouTube iframes via `.video-container` (16:9 padding-bottom aspect-ratio wrapper); a PDF slide deck download link (`../slides/output/pdf/`) appears below each video
