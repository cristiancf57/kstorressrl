from blueprints import create_route

app = create_route()

if __name__ == '__main__':
    app.run(debug=True)