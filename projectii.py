The children property is special. By convention, it's always the first attribute which means that you can omit it: html.H1(children='Hello Dash') is the same as html.H1('Hello Dash'). Also, it can contain a string, a number, a single component, or a list of components.
# Lab Question

Extract average monthly arrival delay time and see how it changes over the year.

## Dash Application Creation

### Todo for the lab question

1.  Import required libraries, read the airline data, and create an application layout
2.  Add title to the dashboard using HTML H1 component
3.  Add a HTML division and core text input component inside the division. Provide an input component id and a default value to the component.
4.  Add a HTML dividion and core graph component. Provide a graph component id.
5.  Add callback decorator and provide input and output parameters.
6.  Define callback function, perform computation to extract required information, create the graph, and update the layout.
7.  Run the app


For step 1 (only review), this is very specific to running app from Jupyerlab.

    *   For Jupyterlab,we will be using `jupyter-dash` library. Adding `from jupyter_dash import JupyterDash` import statement.
    *   Instead of creating dash application using `app = dash.Dash()`, we will be using `app = JupyterDash(__name__)`.
    *   Use pandas to read the airline data.
    For step 2,

    *   [Plotly H1 HTML Component](https://dash.plotly.com/dash-html-components/h1?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)

    *   Title as `Airline Performance Dashboard`

    *   Use `style` parameter and make the title center aligned, with color code `#503D36`, and font-size as 40. Check `More about HTML` section [here](https://dash.plotly.com/layout?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01).
*   For step 3,


Add [dcc input](https://dash.plotly.com/dash-core-components/input?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) component and provide id as `input-year`. Use `style` parameter and assign height of the inout box to be `50px` and font-size to be `35`.

    *   HTML [Div](https://dash.plotly.com/dash-html-components/div?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) component and provide id as `line-plot`. Use `style` parameter and assign font-size as `40`.
*   For step 4,

    *   Core [graph](https://dash.plotly.com/dash-core-components/graph?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) component and assign id as `line-plot`.
*   For 5 and 6,

    *   Basic [callback](https://dash.plotly.com/basic-callbacks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
