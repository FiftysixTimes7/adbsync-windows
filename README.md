adbsync-windows
===============

adbsync-windows is a tool to synchronize files between a Windows PC and an Android
device using the ADB (Android Debug Bridge).

This is a modified version of Google's adb-sync(https://github.com/google/adb-sync)
to make it run on Windows.

Licensed under GPL-3.0 or later.

WARNING
-------
This project is still WIP. It may cause file corruption.

Related Projects
================

Before getting used to this, please review this list of projects that are
somehow related to adbsync-windows and may fulfill your needs better:

* [adb-sync](https://github.com/google/adb-sync) is the original project.
* [rsync](http://rsync.samba.org/) is a file synchronization tool for local
  (including FUSE) file systems or SSH connections. This can be used even with
  Android devices if rooted or using an app like
  [SSHelper](https://play.google.com/store/apps/details?id=com.arachnoid.sshelper).
* [adbfs](http://collectskin.com/adbfs/) is a FUSE file system that uses adb to
  communicate to the device. Requires a rooted device, though.
* [adbfs-rootless](https://github.com/spion/adbfs-rootless) is a fork of adbfs
  that requires no root on the device. Does not play very well with rsync.
* [go-mtpfs](https://github.com/hanwen/go-mtpfs) is a FUSE file system to
  connect to Android devices via MTP. Due to MTP's restrictions, only a certain
  set of file extensions is supported. To store unsupported files, just add
  .txt! Requires no USB debugging mode.

Setup
=====

Android Side
------------

First you need to enable USB debugging mode. This allows authorized computers
(on Android before 4.4.3 all computers) to perform possibly dangerous
operations on your device. If you do not accept this risk, do not proceed and
try using [go-mtpfs](https://github.com/hanwen/go-mtpfs) instead!

On your Android device:

* Go to the Settings app.
* If there is no "Developer Options" menu:
  * Select "About".
  * Tap "Build Number" seven times.
  * Go back.
* Go to "Developer Options".
* Enable "USB Debugging".

PC Side
-------

* Install the [Android SDK](http://developer.android.com/sdk/index.html) (the
  stand-alone Android SDK "for an existing IDE" is sufficient). Alternatively,
  some Linux distributions come with a package named like "android-tools-adb"
  that contains the required tool.
* Make sure "adb" is in your PATH. If you use a package from your Linux
  distribution, this should already be the case; if you used the SDK, you
  probably will have to add an entry to PATH in your ~/.profile file, log out
  and log back in.
* `git clone https://github.com/fiftysixtimes7/adbsync-windows`

Usage
=====

To get a full help, type:

```
adbsync-windows --help
```

To synchronize your music files from ~/Music to your device, type one of:

```
adbsync-windows ~/Music /sdcard
adbsync-windows ~/Music/ /sdcard/Music
```

To synchronize your music files from ~/Music to your device, deleting files you
removed from your PC, type one of:

```
adbsync-windows --delete ~/Music /sdcard
adbsync-windows --delete ~/Music/ /sdcard/Music
```

To copy all downloads from your device to your PC, type:

```
adbsync-windows --reverse /sdcard/Download/ ~/Downloads
```

Contributing
============

Patches to this project are very welcome.
