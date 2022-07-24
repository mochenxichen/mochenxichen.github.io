from flask import Flask,render_template
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__)



from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker





def pie_base() :

    pie = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    return pie

@app.route("/")
def show_diagrams():
    pyecharts_pie = pie_base()
    return render_template("index.html",pie_opitions=pyecharts_pie.dump_options())


if __name__ == "__main__":
    app.run(debug=True)