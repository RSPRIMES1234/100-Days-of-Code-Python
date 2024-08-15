from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/yo wassup")
def wassup():
    return "<p style='color:blue;'>yo WASSUP</p>"

def gg():
    import time
    def speed_calc_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            print(f"total time taken to run {func.__name__} is :{end_time - start_time}")

            return result

        return wrapper

    @speed_calc_decorator
    def fast_function():
        for i in range(1000000):
            i * i

    @speed_calc_decorator
    def slow_function():
        for i in range(10000000):
            i * i

    fast_function()
    slow_function()

if __name__=="__main__":
    gg()