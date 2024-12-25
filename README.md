# HTLM2TXT
Tkinter gui to convert HTLM to sort of readable TXT file
This code defines a Python-based GUI application for converting HTML content into plain text using the tkinter library for the user interface and BeautifulSoup from the bs4 library for HTML parsing.

Overview of Key Components:
Class Definition:

HTMLToTextConverter: Encapsulates all functionalities for the GUI and HTML-to-text conversion.
Initialization (__init__):

Sets up the root window and initializes widgets by calling create_widgets.
Widgets Setup (create_widgets):

File Selection:
Provides a label, entry, and "Browse" button to select an HTML file.
Conversion Buttons:
"Convert" button to convert HTML content to text.
"Save Text" button to save the converted text.
Text Display Areas:
Two separate tk.Text widgets:
One for showing the original HTML content.
Another for displaying the converted plain text.
Both include vertical and horizontal scrollbars for navigation.
Functionality:

Browse File (browse_file):
Allows users to select an HTML file, reads its content, and displays it in the "HTML Content" text area.
Convert to Text (convert_to_text):
Parses the HTML content from the "HTML Content" area using BeautifulSoup.
Extracts readable text and displays it in the "Readable Text" area.
Save Text (save_text):
Saves the text from the "Readable Text" area to a .txt file selected by the user.
Error Handling:

Provides warnings or error messages for invalid inputs or failed operations (e.g., file read errors, empty content).
Styling:

Customizes background colors, borders, and text entry areas for a more visually appealing UI.
Main Execution:

If the script is executed directly, it creates a tk.Tk instance, initializes the application, and starts the Tkinter event loop.
Summary:
The application simplifies the process of converting HTML files into plain text by providing a user-friendly interface to load files, view their HTML content, convert it into text, and save the result. It is practical for users needing a straightforward way to extract readable text from HTML documents.
