from flask import Flask, request, render_template_string

app = Flask(__name__)

# List to store book details
library = []

@app.route("/", methods=["GET", "POST"])
def manage_library():
    if request.method == "POST":
        book_title = request.form["book_title"]
        author = request.form["author"]
        description = request.form["description"]
        
        # Add the book to the library list
        library.append({"title": book_title, "author": author, "description": description})
    
    # Render the page with the library data
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Library Management System</title>
    </head>
    <body>
        <h1>Library Management System</h1>
        
        <form method="POST" action="/">
            <label for="book_title">Book Title:</label>
            <input type="text" id="book_title" name="book_title" required>
            <br><br>
            
            <label for="author">Author:</label>
            <input type="text" id="author" name="author" required>
            <br><br>
            
            <label for="description">Description:</label>
            <textarea id="description" name="description" rows="4" required></textarea>
            <br><br>
            
            <input type="submit" value="Add Book">
        </form>
        
        <h2>Books in Library</h2>
        {% for book in library %}
            <div>
                <h3>Title: {{ book.title }}</h3>
                <p><strong>Author:</strong> {{ book.author }}</p>
                <p><strong>Description:</strong> {{ book.description }}</p>
                <hr>
            </div>
        {% endfor %}
    </body>
    </html>
    ''', library=library)

if __name__ == "__main__":
    app.run(debug=True)