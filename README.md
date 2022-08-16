# Project Astraeus
A WIP Star Citizen flight deck.

### About
The goal of this project is to create an immersive Star Citizen simulator, with a cockpit and 3 MFD interfaces to control ships, instruments, and social interations in the game. Feel free to follow along with this project, or contribute wherever necessary.

This project is following along with [this guide](http://www.bogdanberg.com/2020/02/08/diy-motion-simulator-part-1-intro-photos-shopping-list/).

### Status
Software and logistics is being developed for the simulator's MFD's.

  +----------------+----------+-----------+-----------+
  |                |          |           |           |
+-+-+              |     +----+---+  +----+---+  +----+---+         +---+         +---+
|+5v|              |     |        |  |        |  |        |         |GnD+---------+ / |
+---+              |     |  Rasp  |  |  Rasp  |  |  Rasp  |         +---+         +-+-+
                   |     |        |  |        |  |        |                         |
                   |     +----+---+  +----+---+  +----+---+                         |
                   |          |           |           |                             |
                   |          +-----------+-----------+-----------------------------+
                   |                                                                |
                   +-------------+------------------+-----------------+             |
                                 |                  |                 |             |
                                 |                  |                 |             |
                         +-------+-------+ +--------+------+ +--------+------+    +-+-+
                         |               | |               | |               |    | / |
                         |               | |               | |               |    +-+-+
                         |               | |               | |               |      |
                         |   GameGlass   | |   GameGlass   | |   GameGlass   |      |
                         |      MFD      | |      MFD      | |      MFD      |      |
                         |               | |               | |               |      |
                         |               | |               | |               |      |
                         +-------+-------+ +-------+-------+ +--------+------+      |
                                 |                 |                  |             |
                                 +-----------------+------------------+-------------+

### Updates
- 8/15/2022:
  - Created an embedded GameGlass webapp inside a python webview (see "/bin/gameglass_mfd.py")
  - Added a configuration file for quickly opening a pre-specified shard
