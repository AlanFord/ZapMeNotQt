import pytest
from pytestqt import qt_compat
from pytestqt.qt_compat import qt_api

from ZapMeNotQt.OptionsGroupsDialog import OptionsGroupsDialog

def test_groups_dialog(qtbot):
    assert qt_api.QtWidgets.QApplication.instance() is not None
    widget = OptionsGroupsDialog()
    qtbot.addWidget(widget)
    widget.setWindowTitle("W1")
    # widget.show()

    # assert widget.isVisible()
    assert widget.windowTitle() == "W1"

    widget.StandardButton.click()
    assert widget.ThirtyButton.isChecked() is False

