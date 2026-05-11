"""Generate all README images for CPU Performance Prediction project."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets", exist_ok=True)

# ────────────────────────────────────────────────────────────
# 1. HERO IMAGE
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 5)
ax.axis('off')
fig.patch.set_facecolor('#1a1f36')

# Background gradient simulation
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack([gradient] * 10)
ax.imshow(gradient, aspect='auto', extent=[0, 14, 0, 5],
          cmap='Blues', alpha=0.15, zorder=0)

# Decorative circles
for x, y, r, alpha in [(11.5, 4.2, 2.2, 0.07), (12.5, 0.8, 1.8, 0.05), (0.5, 0.5, 1.5, 0.06)]:
    circle = plt.Circle((x, y), r, color='#818cf8', alpha=alpha, zorder=1)
    ax.add_patch(circle)

# Tag line
ax.text(0.5, 4.3, '●  MLOPS · MACHINE LEARNING · FLASK DEPLOYMENT',
        fontsize=9, color='#818cf8', fontfamily='monospace', va='top', zorder=5)

# Main title
ax.text(0.5, 3.6, 'CPU Performance', fontsize=46, fontweight='bold',
        color='white', va='top', zorder=5)
ax.text(0.5, 2.0, 'Prediction System', fontsize=46, fontweight='bold',
        color='#818cf8', va='top', zorder=5)

# Subtitle
ax.text(0.5, 1.05, 'End-to-end MLOps pipeline · ElasticNet Regression · MLflow Tracking · Flask Web App',
        fontsize=12, color='#94a3b8', va='top', zorder=5)

# Metric pills
pills = [('R²  0.908', '#4ade80'), ('RMSE  46.3', '#60a5fa'), ('MAE  33.3', '#f472b6'), ('6 Features', '#fbbf24')]
for i, (label, color) in enumerate(pills):
    x = 0.5 + i * 2.5
    rect = FancyBboxPatch((x, 0.08), 2.1, 0.55,
                          boxstyle="round,pad=0.05", linewidth=1.5,
                          edgecolor=color, facecolor='#0f172a', zorder=5)
    ax.add_patch(rect)
    ax.text(x + 1.05, 0.35, label, fontsize=11, fontweight='bold',
            color=color, ha='center', va='center', fontfamily='monospace', zorder=6)

# Tech stack on the right
techs = ['Python 3', 'scikit-learn', 'MLflow', 'Flask', 'DagsHub', 'pandas']
ax.text(11.5, 4.3, 'TECH STACK', fontsize=9, color='#475569',
        ha='center', va='top', fontfamily='monospace', zorder=5)
for i, tech in enumerate(techs):
    row, col = divmod(i, 3)
    tx = 10.2 + col * 1.3
    ty = 3.7 - row * 0.7
    rect = FancyBboxPatch((tx - 0.55, ty - 0.22), 1.1, 0.44,
                          boxstyle="round,pad=0.05", linewidth=1,
                          edgecolor='#334155', facecolor='#1e293b', zorder=5)
    ax.add_patch(rect)
    ax.text(tx, ty, tech, fontsize=9, color='#94a3b8',
            ha='center', va='center', zorder=6)

plt.tight_layout(pad=0)
plt.savefig('assets/hero.png', dpi=160, bbox_inches='tight',
            facecolor='#1a1f36', edgecolor='none')
plt.close()
print("✅ hero.png saved")

# ────────────────────────────────────────────────────────────
# 2. ARCHITECTURE DIAGRAM
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(16, 7))
ax.set_xlim(0, 16)
ax.set_ylim(0, 7)
ax.axis('off')
fig.patch.set_facecolor('#f8fafc')

ax.text(8, 6.65, 'End-to-End MLOps Architecture', fontsize=20, fontweight='bold',
        color='#0f172a', ha='center', va='top')
ax.text(8, 6.28, 'CPU Performance Prediction · 5-Stage Pipeline · Flask Serving',
        fontsize=11, color='#64748b', ha='center', va='top')

stages = [
    ('Data\nIngestion', '#3B82F6', '#EFF6FF', [
        'urllib.request', 'machine.data', 'from GitHub URL', '→ artifacts/\ndata_ingestion/']),
    ('Data\nValidation', '#8B5CF6', '#F5F3FF', [
        'schema.yaml check', '7 columns verified', 'Passed / Failed', '→ status.txt']),
    ('Data\nTransformation', '#F97316', '#FFF7ED', [
        'Drop vendor, model,ERP', 'train_test_split', '75% train · 25% test', '→ train.csv / test.csv']),
    ('Model\nTraining', '#22C55E', '#F0FDF4', [
        'ElasticNet(sklearn)', 'α=0.05 l1_ratio=0.3', 'random_state=42', '→ model.joblib']),
    ('Model\nEvaluation', '#EF4444', '#FFF1F2', [
        'R² = 0.908', 'RMSE = 46.3', 'MAE  = 33.3', '→ MLflow + DagsHub']),
]

BOX_W, BOX_H = 2.4, 3.2
GAP = 0.65
start_x = 0.4

for i, (name, color, bg, details) in enumerate(stages):
    x = start_x + i * (BOX_W + GAP)
    y = 2.5

    # Shadow
    shadow = FancyBboxPatch((x + 0.06, y - 0.06), BOX_W, BOX_H,
                            boxstyle="round,pad=0.1", linewidth=0,
                            facecolor='#cbd5e1', zorder=1)
    ax.add_patch(shadow)

    # Card
    card = FancyBboxPatch((x, y), BOX_W, BOX_H,
                          boxstyle="round,pad=0.1", linewidth=2,
                          edgecolor=color, facecolor=bg, zorder=2)
    ax.add_patch(card)

    # Header strip
    header = FancyBboxPatch((x, y + BOX_H - 0.72), BOX_W, 0.72,
                            boxstyle="round,pad=0.05", linewidth=0,
                            facecolor=color, zorder=3)
    ax.add_patch(header)

    # Stage number
    ax.text(x + 0.28, y + BOX_H - 0.36, f'0{i+1}',
            fontsize=10, fontweight='bold', color='white', va='center',
            fontfamily='monospace', zorder=4)

    # Stage name
    ax.text(x + BOX_W / 2 + 0.1, y + BOX_H - 0.36, name,
            fontsize=11, fontweight='bold', color='white',
            ha='center', va='center', zorder=4)

    # Details
    for j, detail in enumerate(details):
        ax.text(x + BOX_W / 2, y + BOX_H - 1.05 - j * 0.55, detail,
                fontsize=9, color='#374151', ha='center', va='center',
                fontfamily='monospace', zorder=4)

    # Arrow between stages
    if i < len(stages) - 1:
        ax.annotate('', xy=(x + BOX_W + GAP, y + BOX_H / 2),
                    xytext=(x + BOX_W, y + BOX_H / 2),
                    arrowprops=dict(arrowstyle='->', color='#94a3b8', lw=2),
                    zorder=5)

# Flask box at bottom
flask_x, flask_y = 3.8, 0.3
rect = FancyBboxPatch((flask_x, flask_y), 8.4, 1.6,
                      boxstyle="round,pad=0.12", linewidth=2,
                      edgecolor='#4338ca', facecolor='#eef2ff',
                      linestyle='dashed', zorder=2)
ax.add_patch(rect)

ax.text(8, flask_y + 1.22, '🌐  Flask Web Application  (port 8081)', fontsize=13,
        fontweight='bold', color='#4338ca', ha='center', va='center', zorder=4)
ax.text(8, flask_y + 0.75, 'GET  /  →  index.html  |  POST /predict  →  PredictionPipeline  →  results.html',
        fontsize=10, color='#4338ca', ha='center', va='center', fontfamily='monospace', zorder=4)
ax.text(8, flask_y + 0.32, 'GET /train  triggers  python main.py  →  reruns the full 5-stage pipeline on demand',
        fontsize=9, color='#6366f1', ha='center', va='center', zorder=4)

# Connector from Model Trainer down
model_cx = start_x + 3 * (BOX_W + GAP) + BOX_W / 2
ax.annotate('', xy=(8, flask_y + 1.6), xytext=(model_cx, 2.5),
            arrowprops=dict(arrowstyle='->', color='#4338ca', lw=1.5, linestyle='dashed'),
            zorder=3)

plt.tight_layout(pad=0.4)
plt.savefig('assets/architecture.png', dpi=160, bbox_inches='tight',
            facecolor='#f8fafc', edgecolor='none')
plt.close()
print("✅ architecture.png saved")

# ────────────────────────────────────────────────────────────
# 3. WEB INDEX MOCKUP
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis('off')
fig.patch.set_facecolor('#e2e8f0')

# Browser chrome
chrome = FancyBboxPatch((0.3, 0.3), 12.4, 7.4,
                        boxstyle="round,pad=0.1", linewidth=0, facecolor='white', zorder=1)
ax.add_patch(chrome)

# Address bar
bar = FancyBboxPatch((0.5, 7.3), 12, 0.38,
                     boxstyle="round,pad=0.05", linewidth=0, facecolor='#f1f5f9', zorder=2)
ax.add_patch(bar)
ax.add_patch(plt.Circle((0.85, 7.49), 0.08, color='#ef4444', zorder=3))
ax.add_patch(plt.Circle((1.08, 7.49), 0.08, color='#fbbf24', zorder=3))
ax.add_patch(plt.Circle((1.31, 7.49), 0.08, color='#4ade80', zorder=3))
url_bg = FancyBboxPatch((2.5, 7.35), 8, 0.28,
                        boxstyle="round,pad=0.03", linewidth=0, facecolor='white', zorder=3)
ax.add_patch(url_bg)
ax.text(6.5, 7.49, 'localhost:8081', fontsize=10, color='#374151',
        ha='center', va='center', fontfamily='monospace', zorder=4)

# Left panel (indigo)
left = FancyBboxPatch((0.5, 0.4), 5.5, 6.85, boxstyle="square,pad=0", linewidth=0,
                      facecolor='#4338ca', zorder=2)
ax.add_patch(left)

# Overlay circles
ax.add_patch(plt.Circle((1.0, 6.8), 1.8, color='#3730a3', alpha=0.5, zorder=3))
ax.add_patch(plt.Circle((5.5, 1.0), 1.5, color='#312e81', alpha=0.5, zorder=3))

ax.text(3.25, 5.9, 'Hardware', fontsize=24, fontweight='bold', color='white',
        ha='center', va='center', zorder=5)
ax.text(3.25, 5.2, 'Performance', fontsize=24, fontweight='bold', color='white',
        ha='center', va='center', zorder=5)
ax.text(3.25, 4.5, 'Modeling', fontsize=24, fontweight='bold', color='white',
        ha='center', va='center', zorder=5)
ax.text(3.25, 3.7, 'Configure your CPU specs to predict\nperformance using our ElasticNet\nregression model.',
        fontsize=9.5, color='#c7d2fe', ha='center', va='center', zorder=5)

# Right panel (form)
right = FancyBboxPatch((6.1, 0.4), 6.6, 6.85, boxstyle="square,pad=0", linewidth=0,
                       facecolor='#f8fafc', zorder=2)
ax.add_patch(right)

# Form card
card = FancyBboxPatch((6.4, 0.7), 6.0, 6.25, boxstyle="round,pad=0.1", linewidth=1,
                      edgecolor='#e2e8f0', facecolor='white', zorder=3)
ax.add_patch(card)

ax.text(9.4, 6.6, 'Run Prediction', fontsize=15, fontweight='bold',
        color='#0f172a', ha='center', va='center', zorder=4)
ax.text(9.4, 6.22, 'Please enter the physical parameters below.',
        fontsize=9, color='#64748b', ha='center', va='center', zorder=4)

# Input fields (2-column grid)
fields = [('MYCT', 'ns', 'e.g. 29'), ('MMIN', 'KB', 'e.g. 8000'),
          ('MMAX', 'KB', 'e.g. 32000'), ('CACH', 'KB', 'e.g. 64'),
          ('CHMIN', 'Ch', 'e.g. 8'), ('CHMAX', 'Ch', 'e.g. 32')]
for idx, (name, unit, hint) in enumerate(fields):
    row, col = divmod(idx, 2)
    fx = 6.65 + col * 2.9
    fy = 5.5 - row * 1.1
    ax.text(fx, fy + 0.18, f'{name}', fontsize=8.5, fontweight='600',
            color='#374151', va='center', zorder=4)
    ax.text(fx + 1.8, fy + 0.18, unit, fontsize=7.5, color='#94a3b8', va='center', zorder=4)
    inp = FancyBboxPatch((fx, fy - 0.22), 2.5, 0.36,
                         boxstyle="round,pad=0.04", linewidth=1,
                         edgecolor='#d1d5db', facecolor='white', zorder=4)
    ax.add_patch(inp)
    ax.text(fx + 0.12, fy - 0.04, hint, fontsize=8, color='#9ca3af', va='center',
            fontfamily='monospace', zorder=5)

# Submit button
btn = FancyBboxPatch((6.65, 1.05), 5.5, 0.52, boxstyle="round,pad=0.06", linewidth=0,
                     facecolor='#4338ca', zorder=4)
ax.add_patch(btn)
ax.text(9.4, 1.31, 'Calculate Performance  →', fontsize=11, fontweight='bold',
        color='white', ha='center', va='center', zorder=5)

plt.tight_layout(pad=0)
plt.savefig('assets/web_index.png', dpi=150, bbox_inches='tight',
            facecolor='#e2e8f0', edgecolor='none')
plt.close()
print("✅ web_index.png saved")

# ────────────────────────────────────────────────────────────
# 4. WEB RESULTS MOCKUP
# ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis('off')
fig.patch.set_facecolor('#e2e8f0')

# Browser chrome (same)
chrome = FancyBboxPatch((0.3, 0.3), 12.4, 7.4,
                        boxstyle="round,pad=0.1", linewidth=0, facecolor='white', zorder=1)
ax.add_patch(chrome)
bar = FancyBboxPatch((0.5, 7.3), 12, 0.38,
                     boxstyle="round,pad=0.05", linewidth=0, facecolor='#f1f5f9', zorder=2)
ax.add_patch(bar)
ax.add_patch(plt.Circle((0.85, 7.49), 0.08, color='#ef4444', zorder=3))
ax.add_patch(plt.Circle((1.08, 7.49), 0.08, color='#fbbf24', zorder=3))
ax.add_patch(plt.Circle((1.31, 7.49), 0.08, color='#4ade80', zorder=3))
url_bg = FancyBboxPatch((2.5, 7.35), 8, 0.28,
                        boxstyle="round,pad=0.03", linewidth=0, facecolor='white', zorder=3)
ax.add_patch(url_bg)
ax.text(6.5, 7.49, 'localhost:8081/predict', fontsize=10, color='#374151',
        ha='center', va='center', fontfamily='monospace', zorder=4)

# Left panel (same indigo)
left = FancyBboxPatch((0.5, 0.4), 5.5, 6.85, boxstyle="square,pad=0", linewidth=0,
                      facecolor='#4338ca', zorder=2)
ax.add_patch(left)
ax.add_patch(plt.Circle((1.0, 6.8), 1.8, color='#3730a3', alpha=0.5, zorder=3))
ax.add_patch(plt.Circle((5.5, 1.0), 1.5, color='#312e81', alpha=0.5, zorder=3))
ax.text(3.25, 5.9, 'Hardware', fontsize=24, fontweight='bold', color='white',
        ha='center', va='center', zorder=5)
ax.text(3.25, 5.2, 'Performance', fontsize=24, fontweight='bold', color='white',
        ha='center', va='center', zorder=5)
ax.text(3.25, 4.5, 'Modeling', fontsize=24, fontweight='bold', color='white',
        ha='center', va='center', zorder=5)
ax.text(3.25, 3.7, 'Configure your CPU specs to predict\nperformance using our ElasticNet\nregression model.',
        fontsize=9.5, color='#c7d2fe', ha='center', va='center', zorder=5)

# Right panel
right = FancyBboxPatch((6.1, 0.4), 6.6, 6.85, boxstyle="square,pad=0", linewidth=0,
                       facecolor='#f8fafc', zorder=2)
ax.add_patch(right)
card = FancyBboxPatch((6.4, 0.7), 6.0, 6.25, boxstyle="round,pad=0.1", linewidth=1,
                      edgecolor='#e2e8f0', facecolor='white', zorder=3)
ax.add_patch(card)

# Success badge
badge = FancyBboxPatch((8.1, 6.5), 2.6, 0.38, boxstyle="round,pad=0.08", linewidth=1,
                       edgecolor='#86efac', facecolor='#dcfce7', zorder=4)
ax.add_patch(badge)
ax.text(9.4, 6.69, '✓  Analysis Successful', fontsize=9.5, fontweight='600',
        color='#166534', ha='center', va='center', zorder=5)

# Big prediction number
ax.text(9.4, 5.75, '253.4', fontsize=52, fontweight='bold',
        color='#4338ca', ha='center', va='center', zorder=4)
ax.text(9.4, 5.0, 'Estimated Relative Performance', fontsize=10.5,
        color='#64748b', ha='center', va='center', zorder=4)

# Divider
ax.plot([6.7, 12.1], [4.72, 4.72], color='#e2e8f0', lw=1.5, zorder=4)

# Input detail grid (3 cols x 2 rows)
params = [('MYCT', '29 ns'), ('MMIN', '8000 KB'), ('MMAX', '32000 KB'),
          ('CACH', '32 KB'), ('CHMIN', '8'), ('CHMAX', '32')]
for idx, (lbl, val) in enumerate(params):
    row, col = divmod(idx, 3)
    px = 7.0 + col * 1.8
    py = 4.4 - row * 0.85
    ax.text(px, py, lbl, fontsize=8, color='#94a3b8', va='center',
            fontfamily='monospace')
    ax.text(px, py - 0.32, val, fontsize=11, fontweight='600',
            color='#0f172a', va='center')

# Back button
btn = FancyBboxPatch((6.65, 0.88), 5.5, 0.52, boxstyle="round,pad=0.06", linewidth=1,
                     edgecolor='#e2e8f0', facecolor='#f1f5f9', zorder=4)
ax.add_patch(btn)
ax.text(9.4, 1.14, '←  Calculate Another Profile', fontsize=11,
        color='#374151', ha='center', va='center', zorder=5)

plt.tight_layout(pad=0)
plt.savefig('assets/web_result.png', dpi=150, bbox_inches='tight',
            facecolor='#e2e8f0', edgecolor='none')
plt.close()
print("✅ web_result.png saved")
print("\nAll 4 images generated successfully.")
