# Page State Machine - GraphViz Implementation

Howdy, I hope you enjoyed the blog post. Let's see if we can automate your navigation development experience.

## Get your data into format

So, in the script, we assume the same format within the blog post.
As long as your "PageState" table contains an Id and Title,
and your "PageTransition" table contains an EventId, StateId, and NextStateId,
and you can export both into a format which is column: comma delimited and row: semi-colon delimited,
you can use the script as is.
Otherwise, you will need to make alterations to the python script.

## Dependencies

- json library (standard to python)
- graphviz library (link below will help you to install it for your solution)

## Use GraphViz with Python

https://www.devtoolsdaily.com/graphviz/python/

## Graph with Example Data

[graph-example.pdf](./graph-example.pdf)
