"""generate_all.py — Generate all 6 module PPTX files.

Usage:
    cd slides && uv run python generate_all.py
"""
import time

print("╔══════════════════════════════════════════════════════════╗")
print("║  疾管署 AI 應用基礎班 — PPTX 批次產生器                    ║")
print("╚══════════════════════════════════════════════════════════╝\n")

t0 = time.time()

import generate_module0; generate_module0.build()
import generate_module1; generate_module1.build()
import generate_module2; generate_module2.build()
import generate_module3; generate_module3.build()
import generate_module4; generate_module4.build()
import generate_module5; generate_module5.build()

elapsed = time.time() - t0
print(f"\n✨  全部完成！共 6 份 PPTX，耗時 {elapsed:.1f} 秒。")
print("📁  輸出目錄：slides/output/")
