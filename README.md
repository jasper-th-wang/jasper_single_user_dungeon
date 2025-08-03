# Underworld Single User Dungeon

## 📍 Overview

A terminal-based dungeon adventure featuring a **custom text-to-dialogue parser** that transforms structured text files into interactive narrative experiences. The game combines ASCII-rendered maps, character progression mechanics, and branching dialogue trees to create an immersive story-driven experience.

### Core Technical Features

- **Custom Dialogue Parser**: Transforms text files with special syntax (`->` for options, `@` for NPCs, `$` for players) into interactive dialogue trees with branching narratives
- **Terminal Rendering Engine**: Real-time typewriter effects, color-coded text output, and ASCII map visualization
- **Dynamic Character System**: Stats (Wisdom, Fury, Essence) that evolve based on player choices throughout the narrative
- **JSON Configurable Game Worlds**: JSON-based level configuration with procedural monster encounters and goal validation
- **Elimination-based Dialogue System**: Dynamic option removal where dialogue choices disappear after selection, creating evolving conversation trees that adapt to player decisions
- **ASCII Map Rendering with Live Updates**: Real-time coordinate-based ASCII visualization system using symbol mapping (`@` for player, `!` for NPCs) with dynamic grid generation
- **Procedural Scenario Distribution**: Algorithmic environmental generation using dictionary comprehension to randomly distribute narrative descriptions across coordinate-mapped game boards

*The narrative follows an amnesiac soul navigating the underworld, uncovering forgotten memories through encounters with mythological figures like Thanatos, Eirene, and other inhabitants of the realm.*

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the jasper_single_user_dungeon repository:

```sh
git clone https://github.com/jasper-th-wang/jasper_single_user_dungeon
```

2. Change to the project directory:

```sh
cd jasper_single_user_dungeon
```

### 🤖 Running jasper_single_user_dungeon

```sh
python game.py
```

### 🧪 Tests

```sh
python -m unittest
```

---
