# PokePi Emulator

##About
PokePi Emulator is an emulator, made to work on Linux and Windows (and maybe MacOS in the future).

It's purpose is to simplify the testing of the PokePi/Linux images for Raspberry Pi's without carrying around the boards. You only need a .pimg or .img file to run it. The image doesn't require a kernel to be embedded, however, the system needs to be compiled for aarch64, and compatible with at least a Raspberry Pi 3b.

The script also require Qemu, which can be autoinstalled, by PokePi Emulator. 

##Installation
```sh
git clone -b emulator https://github.com/bastien8060/PokePi
cd ./PokePi
```
##Usage

Cannot get simpler!
```sh
python main.py
# Wait... If asked, download dependencies. Then, open your .pimg/img file. Tada.
```
