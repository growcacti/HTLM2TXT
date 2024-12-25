from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, messagebox


class HTMLToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML to Text Converter")
        self.create_widgets()

    def create_widgets(self):
        # File selection
        tk.Label(self.root, text="Select HTML File:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.file_entry = tk.Entry(self.root,bd=11,bg="cyan", width=50)
        self.file_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root,bd=6,bg="pale green", text="Browse", command=self.browse_file).grid(row=0, column=2, padx=10, pady=5)

        # Conversion buttons
        tk.Button(self.root,bd=6,bg="aquamarine", text="Convert", command=self.convert_to_text).grid(row=1, column=1, pady=10)
        tk.Button(self.root,bd=6,bg="peach puff", text="Save Text", command=self.save_text).grid(row=1, column=2, pady=10)

        # HTML Content Text widget with scrollbar
        tk.Label(self.root, text="HTML Content:").grid(row=2, column=0, padx=10, pady=5, sticky="nw")
        html_frame = tk.Frame(self.root)
        html_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.html_text = tk.Text(html_frame,bd=11,bg="wheat", width=60, height=15, wrap="none")
        html_scroll_y = tk.Scrollbar(html_frame, bd=5,bg="light yellow",orient="vertical", command=self.html_text.yview)
        html_scroll_x = tk.Scrollbar(html_frame, bd=5,bg="light yellow",orient="horizontal", command=self.html_text.xview)
        self.html_text.configure(yscrollcommand=html_scroll_y.set, xscrollcommand=html_scroll_x.set)
        html_scroll_y.pack(side="right", fill="y")
        html_scroll_x.pack(side="bottom", fill="x")
        self.html_text.pack(side="left", fill="both", expand=True)

        # Readable Text Text widget with scrollbar
        tk.Label(self.root,bg="misty rose", text="Readable Text:").grid(row=3, column=0, padx=10, pady=5, sticky="nw")
        readable_frame = tk.Frame(self.root)
        readable_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.readable_text = tk.Text(readable_frame,bd=14,bg="light cyan", width=60, height=15, wrap="none")
        readable_scroll_y = tk.Scrollbar(readable_frame,bd=6,bg="aquamarine", orient="vertical", command=self.readable_text.yview)
        readable_scroll_x = tk.Scrollbar(readable_frame,bd=6,bg="aquamarine", orient="horizontal", command=self.readable_text.xview)
        self.readable_text.configure(yscrollcommand=readable_scroll_y.set, xscrollcommand=readable_scroll_x.set)
        readable_scroll_y.pack(side="right", fill="y")
        readable_scroll_x.pack(side="bottom", fill="x")
        self.readable_text.pack(side="left", fill="both", expand=True)

    def browse_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html"), ("All Files", "*.*")])
        if filepath:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filepath)
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()
                self.html_text.delete(1.0, tk.END)
                self.html_text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file: {e}")

    def convert_to_text(self):
        html_content = self.html_text.get(1.0, tk.END).strip()
        if not html_content:
            messagebox.showwarning("Warning", "No HTML content to convert!")
            return

        try:
            soup = BeautifulSoup(html_content, "html.parser")
            readable_text = soup.get_text(separator="\n")  # Ensure newlines are preserved
            self.readable_text.delete(1.0, tk.END)
            self.readable_text.insert(tk.END, readable_text)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert HTML: {e}")

    def save_text(self):
        text_content = self.readable_text.get(1.0, tk.END).strip()
        if not text_content:
            messagebox.showwarning("Warning", "No text content to save!")
            return

        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filepath:
            try:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(text_content)
                messagebox.showinfo("Success", "Text saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save text: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = HTMLToTextConverter(root)
    root.mainloop()
