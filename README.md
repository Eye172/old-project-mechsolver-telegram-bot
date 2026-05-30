# MechSolver — Engineering Telegram Bot

A Telegram bot for engineering calculations, built in Python in 2022 as a personal learning project. The bot handles 18 formulas across three engineering domains and includes a unit prefix converter and a reference dictionary of mechanical terms.

## Features

### Strength of Materials (`/f1` – `/f5`)
| Command | Formula |
|---------|---------|
| `/f1 M y I` | Bending normal stress σ = M·y / I |
| `/f2 T r J` | Torsional shear stress τ = T·r / J |
| `/f3 T L J G` | Shaft twist angle φ = T·L / (J·G) |
| `/f4 P L I E` | Max beam deflection δ = P·L³ / (48·E·I) |
| `/f5 σx σy τxy` | Von Mises equivalent stress σᵥ |

### Theory of Mechanisms (`/f6` – `/f9`)
| Command | Formula |
|---------|---------|
| `/f6 z2 z1` | Gear ratio i = z₂ / z₁ |
| `/f7 vAx vAy Δx Δy ω` | Velocity of point B in a planar mechanism |
| `/f8 aAx aAy Δx Δy ω α` | Acceleration of point B in a planar mechanism |
| `/f9 J1 J2 N` | Grübler mobility criterion M = 3(N−1) − 2J₁ − J₂ |

### Cross-Section Geometry & Mass (`/f10` – `/f18`)
| Command | Formula |
|---------|---------|
| `/f10 b h` | Rectangle cross-section area A = b·h |
| `/f11 d` | Circle cross-section area A = π·d²/4 |
| `/f12 d0 di` | Hollow tube cross-section area |
| `/f13 b h` | Rectangle second moment of area I = b·h³/12 |
| `/f14 d` | Circle second moment of area I = π·d⁴/64 |
| `/f15 d0 di` | Hollow tube second moment of area |
| `/f16 d` | Circle polar moment J = π·d⁴/32 |
| `/f17 d0 di` | Hollow tube polar moment |
| `/f18 ρ A L` | Mass of prismatic part m = ρ·A·L |

### Utilities
- `/c <value> <prefix_from> <unit> <power> = <n/a> <prefix_to> <unit> <power>` — convert between SI prefixes (e.g. `M` mega → `н` nano)
- `/i <term>` — reference definition for a mechanical engineering term (e.g. `/i Нормальное_напряжение`)
- `/help` — show all available formulas as images

## Stack

- Python 3.10
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v13.x
- Pillow

## Setup

1. Clone the repo and install dependencies:
   ```bash
   pip install python-telegram-bot==13.15 Pillow
   ```

2. Create `EngineerBotsToken.py` (excluded from git) with your bot token:
   ```python
   botToken = "YOUR_TOKEN_HERE"
   ```

3. Run:
   ```bash
   python EngineerBotMain.py
   ```

## Notes

This is an archived project from 2022. The code is intentionally left as-is to preserve the original state.
