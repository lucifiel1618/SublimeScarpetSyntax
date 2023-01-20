# SublimeScarpetSyntax: A SublimeText Package for Scarpet

## Overview
__[Scarpet]__, or __Script for Carpet__, is a script language used to design custom programs for __[Carpet Mod]__ in __[Minecraft]__.

__SublimeScarpetSyntax__ is a __[SublimeText]__ package that enables syntax highlighting and autocomplete features of __[SublimeText]__ for __[Scarpet]__ code to improve your coding/debugging experience with __[Scarpet]__ in __[SublimeText]__.

<p align="center"><img src="preview.png" alt="preview image" width="500"></p>

## Installation
### From __[Package Control]__ (recommended)
1. Install __[Package Control]__
2. Open the command palette
   - Win/Linux: `ctrl+shift+p` -> `install package`
   - Mac: `ctrl+shift+p` -> `install package`
3. Search for `ScarpetSyntax` and press `enter` to install
### Manual
* macOS
```sh
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
git clone --depth=1 https://github.com/lucifiel1618/SublimeScarpetSyntax.git

```
* Linux
```sh
cd ~/.config/sublime-text-3/Packages
git clone --depth=1 https://github.com/lucifiel1618/SublimeScarpetSyntax.git

```
* Windows
```cmd
cd "%APPDATA%\Sublime Text 3\Packages"
git clone --depth=1 https://github.com/lucifiel1618/SublimeScarpetSyntax.git

```
## Demos

### Code from Scarpet App Store
![example code](examples/block_counter.sc.svg)

### Detailed Syntax Tests
![detailed stntax tests](examples/syntax_test_scarpet.sc.svg)

[Scarpet]: gnembon/scarpet
[Carpet Mod]: /gnembon/fabric-carpet
[Minecraft]: https://www.minecraft.net
[SublimeText]: https://www.sublimetext.com/
[Package Control]: https://packagecontrol.io/installation