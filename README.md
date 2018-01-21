# DS cookiecutter templates


Yes, there is a [cookeicutter-data-science](http://drivendata.github.io/cookiecutter-data-science/) repo, but I feel that it is too heavy for me to use - at least now, and at least for the most of my projects.

In this repository I'll try to mix my "best practicies" and standarts, on one hand, and keep a short list of template variations, such as js_app, ML_project, etc - through branches.

Feel free to fork and raise issues

## Requirements

- cookiecutter (duh)

## Usage

`cookiecutter -c ML https://github.com/Casyfill/DataScience_cookiecutter.git`  (or any other variation in branches)


## Key differences from cookeicutter-data-science

- few standartized environment. It's not ideal, but more realistic than creating one environment per each app (I might be wrong)
- half of my projects don't need s3 buckets and won't have models
