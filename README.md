# Orange Pi 3 LTS Lab

A hands-on embedded Linux lab focused on the Orange Pi 3 LTS (Allwinner H6). This repository documents the progression from basic userspace GPIO experiments to deeper platform bring-up work, kernel and device tree understanding, and a Yocto-based board support package.

## Overview

The goal of this project is to build practical experience with embedded Linux development on a real SBC. The work starts with simple hardware access and gradually expands into low-level system integration topics such as:

- GPIO and peripheral control from userspace
- Device tree and kernel configuration
- Boot process and board bring-up fundamentals
- Driver development and debugging
- Yocto Project BSP creation and customization

## Why this repository exists

This lab is designed as a learning journal and technical reference for embedded Linux development. It combines notes, experiments, build scripts, and configuration examples so that each step is easy to revisit, refine, and expand over time.

## Target platform

- Board: Orange Pi 3 LTS
- SoC: Allwinner H6
- Focus: embedded Linux development, board support, and systems-level experimentation

## Learning path

The repository is intentionally structured around a practical progression:

1. Userspace access to hardware
   - GPIO control
   - Serial/UART debugging
   - Basic I/O experiments

2. Linux kernel and board bring-up
   - Device tree overlays
   - Kernel modules
   - Driver interaction and debugging

3. System integration
   - Bootloader and initramfs considerations
   - Buildroot and root filesystem setup
   - Hardware validation

4. Yocto BSP development
   - Layer creation
   - Board configuration
   - Image customization for the Orange Pi 3 LTS

## Repository structure

This repo is expected to evolve as experiments are added. A typical structure may include:

- `docs/` — notes, references, and architecture summaries
- `src/` — software examples and test programs
- `kernel/` — kernel-related patches and configuration snippets
- `yocto/` — Yocto layer and BSP work
- `scripts/` — helper scripts for build, flashing, and testing

## Prerequisites

Before working with the board, you should be comfortable with:

- Linux command-line tools
- C and shell scripting
- Cross-compilation basics
- Embedded systems concepts such as bootloaders, kernels, and root filesystems

## Getting started

Clone the repository and begin with the simplest experiments first:

```bash
git clone https://github.com/SahanPrime/orange_pi3_lts_Lab.git
cd orange_pi3_lts_Lab
```

Then explore the documentation and code in order as the lab progresses.

## Notes

This project is a living lab and will continue to expand as new experiments, patches, and BSP work are added. The emphasis is on learning by doing, documenting findings, and building a complete understanding of the platform from the ground up.

## License

This project is intended for educational and personal development purposes unless a separate license is added later.

## Contact

For questions or collaboration ideas related to the lab, use the repository's issue tracker or contact the project maintainer through GitHub.
