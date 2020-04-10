# Survey to rate tweets

<iframe src="https://giphy.com/embed/S8xctlEGFHwI4loppT" width="360" height="300" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

## Getting Started

Install the environment with conda and

```bash
$ conda env create
```

or follow the instructions on https://otree.readthedocs.io/en/latest/install.html to
install oTree.

## General Structure

This repo consists of several apps, the furthest developed is scale_after_scale. It displays one scale after another for one tweet and repeats that process 40 times.


To run the surveys one has to navigate to the parent folder of the project. Then, run:

```bash
$ otree devserver
```

Follow the further instructions to get to the sessions.

### bots

The apps have bots configured who randomly choose their answers.
Run them from the command line with:

```bash
$ otree test appname
```

When you are interested in the produced data use:

```bash
$ otree test appname --export=out_data
```

## Resources

The documentation on https://otree.readthedocs.io/en/latest/ proved to be very useful in
programming the survey.
