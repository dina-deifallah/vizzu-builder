# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,R0801

from __future__ import annotations

from .style import Style


class D1M1:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get(dimension1: str, measure1: str) -> list:
        return [
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": "110%"}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Column Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": measure1,
                    "y": {"set": dimension1, "range": {"min": None, "max": None}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Bar Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": "110%"}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Area Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "line",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": "110%"}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Line Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": "110%"}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style_lollipop(),
                "chart": "Lollipop",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": None}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Polar Column Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": measure1,
                    "y": {"set": dimension1, "range": {"min": "-50%", "max": None}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Radial Bar Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": "130%"}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Polar Area Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "line",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": "130%"}},
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Polar Line Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": [dimension1, measure1],
                    "y": {"set": None, "range": {"min": None, "max": None}},
                    "color": dimension1,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Pie Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": [dimension1, measure1],
                    "y": {"set": None, "range": {"min": "-200%", "max": "100%"}},
                    "color": dimension1,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Donut Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": None,
                    "y": {"set": None, "range": {"min": None, "max": None}},
                    "color": dimension1,
                    "lightness": None,
                    "size": [dimension1, measure1],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Treemap",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": None,
                    "y": {"set": None, "range": {"min": None, "max": None}},
                    "color": dimension1,
                    "lightness": None,
                    "size": measure1,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Bubble Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {
                        "set": [dimension1, measure1],
                        "range": {"min": None, "max": "110%"},
                    },
                    "color": None,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Waterfall",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {
                        "set": [dimension1, measure1],
                        "range": {"min": None, "max": "110%"},
                    },
                    "color": measure1,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Waterfall V2",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": dimension1,
                    "y": {"set": dimension1, "range": {"min": None, "max": "110%"}},
                    "color": measure1,
                    "lightness": None,
                    "size": measure1,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Correlogram",
            },
        ]