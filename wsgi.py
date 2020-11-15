from app import generate_app

app = generate_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')