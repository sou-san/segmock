import time
from pathlib import Path

from textual.app import ComposeResult
from textual.reactive import reactive
from textual.screen import Screen
from textual.timer import Timer
from textual.widgets import Footer
from textual_pyfiglet import FigletWidget

import segmock.cache


class ClockWidget(FigletWidget):
    current_time: reactive[str] = reactive(time.strftime("%H:%M:%S"))

    def on_mount(self) -> None:
        self.update_timer: Timer = self.set_interval(1 / 24, self.update_time)

    def update_time(self) -> None:
        self.current_time = time.strftime("%H:%M:%S")

    def watch_current_time(self, time: str) -> None:
        self.update(time)


class ClockScreen(Screen[None]):
    def compose(self) -> ComposeResult:
        # uv build をすると src/segmock 内のディレクトリやファイルがビルドされて whl にまとめられるみたい。
        # font を src/segmock に移動して、 pathlib で動的に相対パスを指定すると正常に動作するようになった。
        font = Path(__file__).parent / "font" / "7segment"
        yield ClockWidget(font=str(font))
        yield Footer()

    def on_screen_resume(self) -> None:
        self.query_one(Footer).visible = segmock.cache.footer_visible

        self.query_one(ClockWidget).update_timer.resume()

    def on_screen_suspend(self) -> None:
        self.query_one(ClockWidget).update_timer.pause()
