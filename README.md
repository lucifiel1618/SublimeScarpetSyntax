# SublimeScarpetSyntax: A SublimeText Package for Scarpet
![GitHub release (latest by date)](https://img.shields.io/github/v/release/lucifiel1618/SublimeScarpetSyntax)
![Test](https://github.com/lucifiel1618/SublimeScarpetSyntax/actions/workflows/main.yml/badge.svg)
## Overview
__[Scarpet]__, or __Script for Carpet__, is a script language used to design custom programs for __[Carpet Mod]__ in __[Minecraft]__.

__SublimeScarpetSyntax__ is a __[SublimeText]__ package that enables syntax highlighting and autocomplete features of __[SublimeText]__ for __[Scarpet]__ code to improve your coding/debugging experience with __[Scarpet]__ in __[SublimeText]__.

<p align="center"><img src="https://media.githubusercontent.com/media/lucifiel1618/SublimeScarpetSyntax/main/preview.png" alt="preview image" width="500"></p>

## Installation
### A. From __[Package Control]__ (recommended)
1. [Install Package Control]
2. Open the command palette
   - Win/Linux: <kbd>control ⌃</kbd><kbd>shift ⇧</kbd>+<kbd>p</kbd> -> `install package`
   - Mac: <kbd>command ⌘</kbd><kbd>shift ⇧</kbd>+<kbd>p</kbd> -> `install package`
3. Search for `Scarpet` and press <kbd>enter ⏎</kbd> to install

### B. Manual
* Mac
```sh
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
git clone --depth=1 https://github.com/lucifiel1618/SublimeScarpetSyntax.git Scarpet

```
* Linux
```sh
cd ~/.config/sublime-text-3/Packages
git clone --depth=1 https://github.com/lucifiel1618/SublimeScarpetSyntax.git Scarpet

```
* Win
```sh
cd "%APPDATA%\Sublime Text 3\Packages"
git clone --depth=1 https://github.com/lucifiel1618/SublimeScarpetSyntax.git Scarpet

```

## Demos
### Code from Scarpet App Store
![example code](https://media.githubusercontent.com/media/lucifiel1618/SublimeScarpetSyntax/main/examples/block_counter.sc.svg)

### Detailed Syntax Tests
![detailed stntax tests](https://media.githubusercontent.com/media/lucifiel1618/SublimeScarpetSyntax/main/examples/syntax_test_scarpet.sc.svg)

[Scarpet]: https://github.com/gnembon/scarpet
[Carpet Mod]: https://github.com/gnembon/fabric-carpet
[Minecraft]: https://www.minecraft.net
[SublimeText]: https://www.sublimetext.com/
[Package Control]: https://packagecontrol.io/packages/Scarpet
[Install Package Control]: https://packagecontrol.io/installation
