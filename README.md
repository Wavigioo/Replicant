# Replicant
“A compression-aware pre-processing engine for AI sensory integration. Created by David Walkup &amp; Vero.”
# Replicant
**v0.5.0**  
Created by David Walkup & Vero  

A compression-aware pre-processing engine for AI sensory integration.

---

## Project Structure

```
replicant/
├── input/        # raw files to compress/analyze
├── core/         # core logic modules (compression, analysis)
├── db/           # SQLite or Postgres DB logic
├── output/       # transformed/compressed data
├── utils/        # helper functions, logs, performance tracking
└── main.py       # main execution script
```
---

## Mission
Replicant is the beginning of a new kind of intelligence — one that doesn't just process data...  
**it compresses, understands, and evolves.**

---

## Changelog

### v0.1.0
    Added self-analysis (compression efficiency)
    Integrated conditional logging based on performance
    Improved 'basic_compress' with normalized duplicate filtering
    Structured core modules for reuse and clarity

### v0.2.0
- Added log history analysis via `reflect.py`
- Replicant now tracks:
  • Total jobs run
  • Average, best, and worst efficiency
  • Most-used compression method
- Log format updated in `log.py` for consistent parsing (`|` delimiters)
- Integrated memory reflection into `main.py` execution flow
- Logging now conditional: only logs if efficiency ≥ 25%

### v0.2.1

- Added behavioral logic via `check_recent_efficiency()` in `reflect.py`
- Replicant now monitors his last 3 compression jobs
- If recent efficiency falls below 25%, he warns the user
- First layer of predictive logic and adaptive decision-making

### v0.3.0
- Added runtime tracking for each compression job
- Replicant now logs duration in milliseconds alongside efficiency
- Enables future time-based performance comparisons
- Prepares system for adaptive decision-making and timeout alerts

### v0.3.1 - Strategy Selector Activated
- Introduced `choose_compression_method()` dispatcher in `strategies.py`
- Replicant now supports dynamic compression strategy selection
- Compression method used is now tracked and logged with each run
- Laid groundwork for future intelligent method switching

### v0.3.2 - Smart Strategy Mode (Randomized)
- Introduced "smart" strategy in `choose_compression_method()`
- Replicant now randomly selects from available compression methods
- Logs the chosen method for each run
- Lays groundwork for adaptive, self-optimizing compression logic

### v0.4.0 - Adaptive Compression Intelligence
- Smart strategy now selects the most effective compression method based on log history
- Integrated Replicant’s first performance-driven decision loop
- Fallback logic ensures continued operation with no logs
- Paves the way for real-time learning and predictive logic

### v0.5.0 - User Feedback Integration
- Replicant now asks the user to rate each compression run (good/bad/skip)
- Feedback is logged to a new file: `user_feedback.log`
- Added emoji-based responses to personalize interaction
- This marks Replicant’s first step toward emotional intelligence and user-driven optimization
