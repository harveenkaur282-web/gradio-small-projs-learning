import gradio as gr
def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict" #This exposes the function as an API endpoint.
)

demo.launch()

'''When developing locally, you can run your Gradio app in hot reload mode, 
which automatically reloads the Gradio app whenever you make changes to the file. 
To do this, simply type in gradio before the name of the file instead of python. 
In the example above, you would type: gradio app.py in your terminal. 
You can also enable vibe mode by using the --vibe flag, e.g. 
gradio --vibe app.py, which provides an in-browser chat that can be 
used to write or edit your Gradio app using natural language. 
Learn more in the Hot Reloading Guide. '''