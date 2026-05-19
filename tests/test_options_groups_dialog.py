import pytest
from pytestqt import qt_compat
from pytestqt.qt_compat import qt_api

from PyQt6.QtWidgets import QDialogButtonBox, QPushButton

from ZapMeNotQt.OptionsGroupsDialog import OptionsGroupsDialog
from ZapMeNotQt.dataStructures import Model, Energy_Grouping_Type


def test_groups_dialog(qtbot):
    assert qt_api.QtWidgets.QApplication.instance() is not None
    model = Model()
    widget = OptionsGroupsDialog(model)
    qtbot.addWidget(widget)

    # the default
    assert widget.StandardButton.isChecked() is True

    widget.ThirtyButton.click()
    assert widget.ThirtyButton.isChecked() is True
    assert widget.StandardButton.isChecked() is False
    assert widget.DiscreteButton.isChecked() is False

    widget.DiscreteButton.click()
    assert widget.DiscreteButton.isChecked() is True
    assert widget.ThirtyButton.isChecked() is False
    assert widget.StandardButton.isChecked() is False

    widget.buttonBox.button(QDialogButtonBox.StandardButton.Ok).click()

    # verify that the Model instance has been updated
    assert model.groups == Energy_Grouping_Type.Discrete
