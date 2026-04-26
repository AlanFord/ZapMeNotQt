import pytest
# from pytestqt.qt_compat import qt_api
import MainWindow1


@pytest.fixture
def widget(qtbot):
    widget = MainWindow1.MainWindow()
    qtbot.addWidget(widget)
    return widget


def test_application_start(qtbot, widget):
    pass
