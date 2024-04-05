import os
import pygame

from button import Pause, NextTrack, PrevTrack, DurationBar, VolumeBar
from player import Player
from gui import GUI
from handler import Handler

songs = []
for root, dirs, files in os.walk("music"):
    for filename in files:
        if filename.endswith('.mp3'):
            songs.append(filename)


DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = os.path.join(DIR, "music\\")

WIDTH, HEIGHT = 1000, 600
running = True

pse_but = Pause((WIDTH * 2 // 3, HEIGHT * 2.5 // 3), (WIDTH + HEIGHT) // 32)
nxt_but = NextTrack(((WIDTH * 2 // 3 + 3 * (WIDTH + HEIGHT) // 64 + WIDTH // 100), HEIGHT * 2.5 // 3), (WIDTH + HEIGHT) // 64)
prv_but = PrevTrack(((WIDTH * 2 // 3 - 3 * (WIDTH + HEIGHT) // 64 - WIDTH // 100), HEIGHT * 2.5 // 3), (WIDTH + HEIGHT) // 64)
drt_br = DurationBar((1.45 * WIDTH // 3, 2.14 * HEIGHT // 3 - 1), 1.10 * WIDTH // 3, 6, (0, 0, 255))
vlm_br = VolumeBar((WIDTH // 1.1 - 4, HEIGHT // 10), 8, HEIGHT // 1.6 - HEIGHT // 10, (0, 0, 255))

buttons = [pse_but, nxt_but, prv_but, drt_br, vlm_br]

gui = GUI(WIDTH, HEIGHT, buttons)
player = Player(MUSIC_DIR, songs)
handler = Handler(player, buttons)

if __name__ == '__main__':
    player.load_track(songs[0])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                handler.process_events(event)

        player.check_end()
        current_time, total_time = player.get_duration().values()
        gui.update_screen(current_time, total_time, player.images, player.get_volume(), *player.get_songs())