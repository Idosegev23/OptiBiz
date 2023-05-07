import optibiz_app
import optibiz_backend
import optibiz_database_implementation

# Initialize the OptiBiz application
app = optibiz_app.create_app()

# Set up the database
optibiz_database_implementation.setup_database(app)

# Register the backend routes
optibiz_backend.register_routes(app)

if __name__ == '__main__':
    app.run()