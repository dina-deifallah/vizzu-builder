# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from __future__ import annotations

import streamlit_vizzu  # type: ignore

from .d1m1 import D1M1
from .d1m2 import D1M2
from .d2m1 import D2M1
from .d2m2 import D2M2
from ..unset import UNSET
from ...chart.configurator import SelectedChartConfig


class Preset:
    # pylint: disable=too-few-public-methods

    def __init__(self, data: streamlit_vizzu.Data, presets: list, index: int) -> None:
        self.index: int = index
        self.data: streamlit_vizzu.Data = data
        preset = presets[index]
        self.config: dict = preset["config"]
        self.style: dict = preset["style"]
        self.chart: str = preset["chart"]


class Presets:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get(
        config: SelectedChartConfig,
    ) -> list:
        presets = []
        if len(config.dimensions) == 1 and len(config.measures) == 1:
            dimension1 = config.dimensions[0]
            measure1 = Presets._set_aggregator(
                config.measures[0], config.aggregators[0]
            )
            presets = D1M1.get(dimension1, measure1)
        elif len(config.dimensions) == 1 and len(config.measures) == 2:
            dimension1 = config.dimensions[0]
            measure1 = Presets._set_aggregator(
                config.measures[0], config.aggregators[0]
            )
            measure2 = Presets._set_aggregator(
                config.measures[1], config.aggregators[1]
            )
            presets = D1M2.get(dimension1, measure1, measure2)
        elif len(config.dimensions) == 2 and len(config.measures) == 1:
            dimension1 = config.dimensions[0]
            dimension2 = config.dimensions[1]
            measure1 = Presets._set_aggregator(
                config.measures[0], config.aggregators[0]
            )
            presets = D2M1.get(dimension1, dimension2, measure1)
        elif len(config.dimensions) == 2 and len(config.measures) == 2:
            dimension1 = config.dimensions[0]
            dimension2 = config.dimensions[1]
            measure1 = Presets._set_aggregator(
                config.measures[0], config.aggregators[0]
            )
            measure2 = Presets._set_aggregator(
                config.measures[1], config.aggregators[1]
            )
            presets = D2M2.get(dimension1, dimension2, measure1, measure2)
        label = Presets._get_label(config)
        presets = Presets._set_labels(presets, label)
        return presets

    @staticmethod
    def _get_label(config: SelectedChartConfig) -> str | None:
        new_label: str | None = config.label
        if new_label == UNSET:
            new_label = None
        elif new_label == config.measures[0]:
            new_label = Presets._set_aggregator(new_label, config.aggregators[0])
        elif new_label == config.measures[1]:
            new_label = Presets._set_aggregator(new_label, config.aggregators[1])
        return new_label

    @staticmethod
    def _set_labels(presets: list, label: str | None) -> list:
        for index, _ in enumerate(presets):
            presets[index]["config"]["label"] = label
        return presets

    @staticmethod
    def _set_aggregator(measure: str, aggregator: str) -> str:
        new_measure: str = measure
        if aggregator not in [UNSET, "Sum"]:
            new_measure = f"{aggregator.lower()}({measure})"
        if measure == "Count":
            new_measure = f"{measure.lower()}()"
        return new_measure