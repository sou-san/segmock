import time

from textual.app import ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Footer
from textual_pyfiglet import FigletWidget


class ClockDisplay(FigletWidget):
    current_time: reactive[str] = reactive(time.strftime("%H:%M:%S"))

    def on_mount(self) -> None:
        self.set_interval(1 / 24, self.update_time)

    def update_time(self) -> None:
        self.current_time = time.strftime("%H:%M:%S")

    def watch_current_time(self, time: str) -> None:
        self.update(time)


class ClockScreen(Screen[None]):
    def compose(self) -> ComposeResult:
        yield ClockDisplay(font="font/7segment")
        yield Footer()
