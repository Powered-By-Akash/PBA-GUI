<div align="center">

# 🖥️ PBA-GUI (PBA_GEN2025)
### Modular Python Tkinter GUI Framework & Visual Component Library

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Organization](https://img.shields.io/badge/Powered%20By-Akash-00d4ff)](https://github.com/Powered-By-Akash)
[![Founder](https://img.shields.io/badge/Founder-Akash%20Tanna-ff007f)](https://github.com/akashtanna)
[![Architecture](https://img.shields.io/badge/Engine-Tkinter%2FCanvas-10b981)](https://docs.python.org/3/library/tkinter.html)

**The high-performance, dark-theme visual UI engine powering desktop engineering suites, AutoCAD automation consoles, and production workflow tools at Powered By Akash (PBA).**

---

</div>

## 📌 Overview

**PBA-GUI** (internally designated `PBA_GEN2025`) is an agile, coordinate-driven Tkinter component framework built specifically for desktop software that requires:
- **Zero Heavy Dependencies**: Pure standard Python library (`tkinter`, `tkinter.ttk`, `scrolledtext`).
- **Precision Visual Control**: Deterministic coordinate positioning (`place`) designed for industrial consoles, telemetry dashboards, and multi-panel displays.
- **High-Contrast Dark Aesthetics**: Built-in dark container frames, neon borders (`#00d4ff`, `#ff007f`), and high-readability typography (`Fixedsys`, `Segoe UI`, `Georgia`).
- **Seamless Backwards Compatibility**: Compatible with legacy PBA desktop modules importing `PBA_GEN2025` as well as modern package setups importing `pba_gui`.

---

## 🧩 Visual Component Library

| Component | Base Class | Key Features |
|---|---|---|
| `DynamicPanel` | `tkinter.Canvas` | High-contrast container panel with custom border thickness, background tone, and highlight border color. |
| `Branding_Text` | `tkinter.Label` | Retro fixedsys branding title widget for window headers and system badges. |
| `TextLabel` | `tkinter.Label` | Flexible text label supporting custom font tuples, colors, and absolute positioning. |
| `Panel_Tag` | `tkinter.Label` | High-visibility black-and-red console tag for labeling dashboard cards and telemetry sections. |
| `SButton` | `tkinter.Button` | High-visibility action button with customized active hover states, background highlights, and callback dispatch. |
| `TextEntry` | `tkinter.Entry` | Pre-styled single-line input field with `.text()` and `.delete_text()` utility methods. |
| `LongEntry` | `tkinter.Text` | Multi-line text entry box with convenient `.text()` insertion helper. |
| `ScrollEntry` | `scrolledtext.ScrolledText` | Scrolled multi-line text terminal for logs, build outputs, and event feeds. |
| `DropDown` | `ttk.Combobox` | Readonly dropdown selector with variable binding, selection events, and default text presets. |
| `ListBox` | `tkinter.Listbox` | Dual-scrollbar list container with `.add_item(index, val)` and `.get_value()` helpers. |
| `CheckButton` | `tkinter.Checkbutton` | Styled toggle checkbox with active state highlights and integer variable bindings. |
| `RadioButton` | `tkinter.Radiobutton` | Radio selector with title formatting and custom background active states. |
| `WarVer` | `tkinter.Label` | Alert label featuring randomized palette selection for warnings and verifications. |

---

## 🚀 Quickstart & Installation

### Option 1: Install via Pip from GitHub
```bash
pip install git+https://github.com/Powered-By-Akash/PBA-GUI.git
```

### Option 2: Clone and Install in Editable Mode
```bash
git clone https://github.com/Powered-By-Akash/PBA-GUI.git
cd PBA-GUI
pip install -e .
```

---

## 💻 Minimal Code Example

```python
import tkinter as tk
from pba_gui import (
    Branding_Text,
    DynamicPanel,
    Panel_Tag,
    TextLabel,
    TextEntry,
    SButton
)

# 1. Initialize root window
root = tk.Tk()
root.title("PBA Engineering Console")
root.geometry("450x320")
root.configure(bg="#0b1120")

# 2. Add Branding Header
Branding_Text(
    win=root,
    bg_color="#0b1120",
    branding_text="POWERED BY AKASH ✦ CONSOLE v2025",
    fg_color="#00f5ff",
    text_size=11,
    xy_cor=(20, 15)
)

# 3. Add Container Panel
DynamicPanel(
    win=root,
    panel_size=(410, 240, 2),
    xy_cor=(20, 50),
    panel_bgcolor="#111827",
    panel_border_color="#00d4ff"
)

# 4. Panel Tag
Panel_Tag(
    win=root,
    panel_name=" DISPATCH CONTROLS ",
    text_size=9,
    xy_cor=(35, 62)
)

# 5. Text Entry
input_box = TextEntry(
    win=root,
    entry_width=32,
    entry_text="AutoCAD Drawing Pipeline",
    entry_text_size=10,
    xy_cor=(35, 110)
)

# 6. Action Button
def on_click():
    print(f"Executing pipeline: {input_box.get()}")

SButton(
    win=root,
    button_size=(24, 2),
    button_color="#00d4ff",
    text_color="#0b1120",
    active_button_color="#38bdf8",
    active_text_color="#ffffff",
    button_name="EXECUTE ACTION",
    button_text_size=10,
    button_text="Segoe UI",
    xy_cor=(35, 170),
    button_action=on_click
)

root.mainloop()
```

---

## 🎮 Running the Interactive Showcase

An interactive demo is bundled in the repository:

```bash
python examples/demo.py
```

---

## 📁 Repository Structure

```
PBA-GUI/
├── __init__.py           # Legacy root entry point for PBA_GEN2025
├── pba_gui.py            # Primary framework module with type hints & full component suite
├── PBA_GEN2025.py        # Drop-in backward-compatibility bridge
├── setup.py              # Setuptools distribution config
├── pyproject.toml        # Modern PEP 517/518 build specification
├── LICENSE               # MIT Open Source License
├── .gitignore            # Git exclusions
├── README.md             # Documentation and usage guide
└── examples/
    └── demo.py           # Interactive component demonstration
```

---

## 🏢 Organization & Author

- **Organization:** [Powered By Akash (PBA)](https://github.com/Powered-By-Akash)
- **Founder & Lead Architect:** [Akash Tanna](https://github.com/akashtanna)
- **Location:** Gujarat, India
- **Official Website:** [poweredbyakash.com](https://poweredbyakash.com)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.
