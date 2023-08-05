# from flask import Flask
#
# app = Flask(__name__)
#
#
# def make_bold(function):
#     def add_bold_tags():
#         bold = "<b>" + function() + "</b>"
#         return bold
#     return add_bold_tags
#
#
# def make_italic(function):
#     def add_italic_tags():
#         italic = "<em>" + function() + "</em>"
#         return italic
#     return add_italic_tags
#
#
# def make_underline(function):
#     def add_underline_tags():
#         underline = "<u>" + function() + "</u>"
#         return underline
#     return add_underline_tags
#
#
# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#            '<p>This is a paragraph.</p>'\
#            '<img src="https://media.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif">'
#
#
# @app.route('/bye')
# @make_bold
# @make_italic
# @make_underline
# def say_bye():
#     return 'Bye'
#
#
# @app.route('/username/<path:name>/<int:number>')
# def greet(name, number):
#     return f"Hello there {name + '12'}, you are {number} years old!"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#
#
#
# # Python decorators
#
# # import time
# # current_time = time.time()
# # print(current_time)
# #
# # def speed_calc_decorator(function):
# #     def speed():
# #         function()
# #         new_time = time.time()
# #         launch_speed = new_time - current_time
# #         print (f"{function.__name__} run speed: {launch_speed}")
# #     return speed
# #
# # @speed_calc_decorator
# # def fast_function():
# #     for i in range(10000000):
# #         i * i
# #
# # @speed_calc_decorator
# # def slow_function():
# #     for i in range(100000000):
# #         i * i
# #
# # fast_function()
# # slow_function()

# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        sum = 0
        for num in args:
            sum += num
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {sum}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    return args

a_function(1,2,3)