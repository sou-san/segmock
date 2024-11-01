from textual.app import App
from textual.binding import Binding
from textual.events import Resize

from segmock.blocking_screen import MIN_HEIGHT, MIN_WIDTH, BlockingScreen
from segmock.clock import ClockScreen
from segmock.stopwatch import StopwatchScreen


class Segmock(App[None]):
    ENABLE_COMMAND_PALETTE = False
    MODES = {
        "clock": ClockScreen,
        "stopwatch": StopwatchScreen,
    }
    DEFAULT_MODE = "clock"
    BINDINGS = [
        Binding("q", "exit_app", "Exit"),
        Binding("c", "app.switch_mode('clock')", "Clock"),
        Binding("s", "app.switch_mode('stopwatch')", "Stopwatch"),
    ]

    async def on_resize(self, event: Resize) -> None:
        if event.size.width < MIN_WIDTH or event.size.height < MIN_HEIGHT:
            self.push_screen(BlockingScreen())

    def action_exit_app(self) -> None:
        self.exit()
