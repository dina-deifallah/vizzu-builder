# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from dataclasses import dataclass, field
import json
from pathlib import Path
import black
import streamlit_vizzu
import streamlit as st
from streamlit_extras.row import row

from .data.generator import DataCodeGenerator
from .data.parser import DataFrameParser
from .story import StoryBuilder


@dataclass
class ChartConfig:
    # pylint: disable=too-many-instance-attributes

    categories = None
    values = None
    cat1 = None
    selected_cat1 = None
    cat2 = None
    selected_cat2 = None
    value1 = None
    selected_value1 = None
    value2 = None
    selected_value2 = None
    label = None
    tooltips = True
    key = None
    keys: list = field(
        default_factory=lambda: [
            "Cat1, Value1",
            "Cat1, Value1, Value2",
            "Cat1, Cat2, Value1",
            "Cat1, Cat2, Value1, Value2",
        ]
    )


class ChartBuilder:
    # pylint: disable=too-few-public-methods

    def __init__(self, file_name, df):
        self._file_name = file_name
        self._df = df
        if self._df is not None:
            self._filters = st.session_state["filters"]
            self._presets = self._parse_presets_file()
            self._config = ChartConfig()
            self._config.categories, self._config.values = self._get_columns()
            self._story_builder = StoryBuilder(self._file_name, self._df)
            self._add_title()
            with st.form("Chart builder form"):
                self.select_rows = row(2)
                self._add_select_buttons()
                st.form_submit_button("Update charts")
            self._set_key()
            self._add_charts()
            self._add_story()

    def _add_title(self):
        st.subheader("Create Chart")

    def _get_columns(self):
        categories = []
        values = []
        for column_name in self._df.columns:
            if self._df[column_name].dtype == object:
                categories.append(column_name)
            else:
                values.append(column_name)
        return categories, values

    def _add_select_buttons(self):
        self._add_tooltip_button()
        (
            self._config.cat1,
            self._config.selected_cat1,
            self._config.cat2,
            self._config.selected_cat2,
        ) = self._add_select_buttons_by_type(DataFrameParser.DIMENSION)
        (
            self._config.value1,
            self._config.selected_value1,
            self._config.value2,
            self._config.selected_value2,
        ) = self._add_select_buttons_by_type(DataFrameParser.MEASURE)
        self._add_label_button()

    def _add_select_buttons_by_type(self, column_type):
        items1 = self._config.categories
        if column_type == DataFrameParser.MEASURE:
            items1 = self._config.values
        button1 = self.select_rows.selectbox(
            f"Select {column_type} 1 (mandatory)", items1
        )
        items2 = [c for c in items1 if c != button1]
        items2.insert(0, None)
        button2 = self.select_rows.selectbox(
            f"Select {column_type} 2 (optional)", items2
        )
        return items1, button1, items2, button2

    def _add_label_button(self):
        labels = [None]
        for item in [
            self._config.selected_cat1,
            self._config.selected_cat2,
            self._config.selected_value1,
            self._config.selected_value2,
        ]:
            if item is not None:
                labels.append(item)
        self._config.label = self.select_rows.selectbox(
            "Select Label (optional)", labels
        )

    def _add_tooltip_button(self):
        self._config.tooltips = st.toggle("Show tooltips", value=True)
        self._story_builder.set_tooltip(self._config.tooltips)

    def _set_key(self):
        contains = {"Cat1": False, "Cat2": False, "Value1": False, "Value2": False}
        if self._config.selected_cat1 is not None:
            contains["Cat1"] = True
        if self._config.selected_cat2 is not None:
            contains["Cat2"] = True
        if self._config.selected_value1 is not None:
            contains["Value1"] = True
        if self._config.selected_value2 is not None:
            contains["Value2"] = True
        self._config.key = ", ".join(key for key, value in contains.items() if value)
        if self._config.key not in self._config.keys:
            st.warning("Please select at least one category and one value!")

    def _parse_presets_file(self):
        presets = Path(__file__).parent / "config/presets.json"
        with open(presets, "r", encoding="utf8") as json_file:
            return json.load(json_file)

    def _add_charts(self):
        if self._presets and self._config.key:
            if self._config.key in self._presets:
                data = streamlit_vizzu.Data()
                data.add_df(self._df)
                data.set_filter(self._filters)

                for index in range(0, len(self._presets[self._config.key]), 2):
                    col1, col2 = st.columns(2)
                    self._add_chart(data, index, col1)
                    next_index = index + 1
                    if next_index < len(self._presets[self._config.key]):
                        self._add_chart(data, next_index, col2)

    def _add_chart(self, data, index, col):
        raw_config = self._presets[self._config.key][index]
        config = self._process_raw_config(raw_config)
        with col:
            self._add_chart_title(raw_config)
            self._add_chart_animation(index, data, config)
            self._add_chart_code(config)
            self._add_save_button(config)

    def _add_chart_title(self, raw_config):
        st.subheader(raw_config["chart"])

    def _add_chart_animation(self, index, data, config):
        chart = streamlit_vizzu.VizzuChart(
            height=300,
            key=f"vizzu_{self._config.key}_{index}",
            use_container_width=True,
        )
        chart.animate(data, streamlit_vizzu.Config(config))
        chart.feature("tooltip", self._config.tooltips)
        chart.show()

    def _add_chart_code(self, config):
        show_code = st.expander("Show code")
        with show_code:
            code = []
            code.append("from streamlit_vizzu import VizzuChart, Data, Config")
            code.append("import pandas as pd")
            code += DataCodeGenerator.get_data_code(self._file_name, self._df)
            code.append("chart = VizzuChart()")
            if self._config.tooltips:
                code.append('chart.feature("tooltip", True)')
            code.append("chart.animate(data)\n")
            filters = f'Data.filter("{self._filters}"), ' if self._filters else ""
            code.append(f"chart.animate({filters}Config({config}))\n")
            code.append("chart.show()")
            unformatted_code = "\n".join(code)
            formatted_code = black.format_str(unformatted_code, mode=black.FileMode())
            st.code(
                formatted_code,
                language="python",
            )

    def _add_save_button(self, config):
        button = st.button("Add Chart to Story", key=config, use_container_width=True)
        if button:
            self._story_builder.add_slide(self._filters, config)

    def _process_raw_config(self, raw_config):
        config = {}
        for key, value in raw_config.items():
            if key not in ["chart", "y_range_min", "y_range_max"] and value is not None:
                if isinstance(value, list):
                    value = [self._replace_config(v) for v in value]
                else:
                    value = self._replace_config(value)
                config[key] = value
        if "y" in config:
            config["y"] = {"set": config["y"]}
        if "y_range_min" in raw_config and raw_config["y_range_min"] is not None:
            config["y"] = config.get("y", {})
            config["y"]["range"] = config["y"].get("range", {})
            config["y"]["range"]["min"] = raw_config["y_range_min"]
        if "y_range_max" in raw_config and raw_config["y_range_max"] is not None:
            config["y"] = config.get("y", {})
            config["y"]["range"] = config["y"].get("range", {})
            config["y"]["range"]["max"] = raw_config["y_range_max"]
        if self._config.label is not None:
            config["label"] = self._config.label
        return config

    def _replace_config(self, value):
        if isinstance(value, str):
            value = value.replace("Cat1", self._config.selected_cat1 or "")
            value = value.replace("Cat2", self._config.selected_cat2 or "")
            value = value.replace("Value1", self._config.selected_value1 or "")
            value = value.replace("Value2", self._config.selected_value2 or "")
        return value

    def _add_story(self):
        self._story_builder.play()