import pygame
import os
from button import RectButton, CircleButton

class GUI:
    def __init__(self, width, height, buttons):
        self.width = width
        self.height = height
        self.buttons = buttons

        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, (self.width + self.height) // 50)

        pygame.display.set_caption("Music Player")
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_playlist(self, tracks, current_track_index):
        playlist_part = 3
        vertical_playlist_part = 6

        line_color = "#4E0707"
        song_color_current = "#354A21"
        song_color_default = "#001302"

        # Рисуем вертикальную линию для отделения плейлиста
        pygame.draw.line(self.screen, line_color,
                         [self.width // playlist_part, 0],
                         [self.width // playlist_part, self.height], 4)

        # Горизонтальные разделители
        for i in range(1, self.height // vertical_playlist_part):
            pygame.draw.line(self.screen, line_color,
                             [0, i * self.height // vertical_playlist_part],
                             [self.width // playlist_part, i * self.height // vertical_playlist_part], 2)

        # Отображение названий треков
        for index, track in enumerate(tracks[current_track_index:], start=current_track_index):
            song_name = self.font.render(track.split('.mp3')[0], False,
                                         song_color_current if index == current_track_index else song_color_default)
            self.screen.blit(song_name,
                             (0.1 * self.width / playlist_part,
                              (index - current_track_index) * self.height // vertical_playlist_part +
                              self.height // vertical_playlist_part // 2 - 8))

    def convert_to_time(self, time):
        "Конвертация времени из мс в минуты и секунды."
        if time < 0:
            time = 0
        minutes = str(int(time // 60)).zfill(2)
        seconds = str(int(time % 60)).zfill(2)
        return minutes, seconds

    def draw_current_and_total_time(self, time, total_time):
        current_minutes, current_seconds = self.convert_to_time(time // 1000)
        total_minutes, total_seconds = self.convert_to_time(total_time)

        time_str = f"{current_minutes}:{current_seconds}"
        total_time_str = f"{total_minutes}:{total_seconds}"

        time_render = self.font.render(time_str, False, "#001302")
        total_time_render = self.font.render(total_time_str, False, "#001302")

        self.screen.blit(time_render, (1.25 * self.width // 3, 2.1 * self.height // 3))
        self.screen.blit(total_time_render, (2.6 * self.width // 3, 2.1 * self.height // 3))
    def draw_progress_bar_outline(self):
        pygame.draw.circle(self.screen, ("#4E0707"),
        (1.45 * self.width // 3, 2.15 * self.height // 3), 4)

        pygame.draw.line(self.screen, ("#4E0707"),
        [1.45 * self.width // 3, 2.15 * self.height // 3 - 1],
        [2.55 * self.width // 3, 2.15 * self.height // 3 - 1], 8)

        pygame.draw.circle(self.screen, ("#4E0707"),
        (2.55 * self.width // 3, 2.15 * self.height // 3), 4)

    def draw_progress_bar(self, time, total_time):
        percentage = time / total_time / 1000
        coordinate = percentage * (1.1 * self.width // 3) + 1.45 * self.width // 3

        pygame.draw.circle(self.screen, ("#420D09"),
        (1.45 * self.width // 3, 2.15 * self.height // 3), 3)

        # active part
        pygame.draw.line(self.screen,("#420D09"),
        [1.45 * self.width // 3, 2.15 * self.height // 3 - 1],
        [coordinate, 2.15 * self.height // 3 - 1], 6)

        pygame.draw.circle(self.screen, ("#420D09"),
        (coordinate, 2.15 * self.height // 3), 5)

    def draw_volume_control_outline(self):
        pygame.draw.circle(self.screen, ("#4E0707"),
        (self.width // 1.1, self.height // 10), 4)

        pygame.draw.line(self.screen, ("#4E0707"),
        [self.width // 1.1 - 1, self.height // 10],
        [self.width // 1.1 - 1, self.height // 1.6], 8)

        pygame.draw.circle(self.screen, ("#4E0707"),
        (self.width // 1.1, self.height // 1.6), 4)
        
    def draw_volume_control(self, volume, is_muted=False):
        volume_position = self.height // 1.6 - \
        volume * (self.height // 1.6 - self.height // 10)

        color = (volume * 255, 0, 0)
        if is_muted:
            color = (128, 128, 128)

        pygame.draw.circle(self.screen, color,
        (self.width // 1.1, volume_position), 5)

        pygame.draw.line(self.screen, color,
        [self.width // 1.1 - 1, volume_position],
        [self.width // 1.1 - 1, self.height // 1.6], 6)

        pygame.draw.circle(self.screen, color,
        (self.width // 1.1, self.height // 1.6), 3)
    
    def draw_buttons(self):
        for button in self.buttons:
            coordinates = button.get_coordinates()
            color = button.get_color()

            if isinstance(button, RectButton):
                rectangle_button = pygame.Rect(
                coordinates['x'], coordinates['y'],
                coordinates['width'], coordinates['height'])

                pygame.draw.rect(self.screen, color, rectangle_button)

            if isinstance(button, CircleButton):
                pygame.draw.circle(self.screen, color,
                (coordinates['x'], coordinates['y']), coordinates['radius'])   
    def draw_track_cover(self, image_name, x, y):
        "Отображение обложки трека."
        path = os.path.join('images', image_name)  
        surface = pygame.image.load(path).convert_alpha()
        surface = pygame.transform.scale(surface, (self.width // 3, self.width // 3))
        self.screen.blit(surface, (x, y))

    def update_screen(self, time, total_time, image_name, volume_stat, tracks, index):
        self.screen.fill("#020403")
        self.draw_track_cover(image_name[index], self.width // 2, self.height // 12)
        self.draw_current_and_total_time(time, total_time)
        self.draw_buttons()
        self.draw_progress_bar_outline()
        self.draw_progress_bar(time, total_time)
        self.draw_volume_control_outline()
        self.draw_volume_control(volume_stat[0], volume_stat[1])
        self.draw_playlist(tracks, index)
        pygame.display.update()
        self.clock.tick(15)
