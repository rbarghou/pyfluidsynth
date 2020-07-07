from jinja2 import Template

import pandas as pd

from ast import literal_eval

import re


df = pd.read_csv("./synth_functions.csv")
df["c_argument_list"] = df["c_argument_list_str"].apply(literal_eval).apply(lambda x: x[1:])
all_arguments = set.union(*df.c_argument_list.apply(set))




def parse(c_arg_str):
    return re.sub(r"\*\b", "* ", c_arg_str).rsplit(" ", 1)


def generate_method_without_pointer(
        method_name,
        arguments,
        c_method_name,
        c_arguments
):
    return Template(
        """
            @fluid_check
            def {{ method_name }}(self{% for argument in arguments %}, {{ argument }}{% endfor %}):
                return Lib.{{ c_method_name }}(
                    self.synth,{% for c_argument in c_arguments %}
                    c_argument,{% endfor %}
                )
        """
    ).render(
        method_name=method_name,
        arguments=arguments,
        c_method_name=c_method_name,
        c_arguments=c_arguments
    )

