class CodeEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def insert(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack.clear()
        print(f"Inserted: {new_text}")

    def delete(self, count):
        if count > len(self.text):
            count = len(self.text)
        self.undo_stack.append(self.text)
        deleted_text = self.text[-count:]
        self.text = self.text[:-count]
        self.redo_stack.clear()
        print(f"Deleted: {deleted_text}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        print("Undo performed.")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        print("Redo performed.")

    def show(self):
        print(f"Current text: '{self.text}'")


# Example usage
editor = CodeEditor()
editor.insert("Hello")
editor.show()
editor.insert(" World")
editor.show()
editor.delete(6)
editor.show()
editor.undo()
editor.show()
editor.redo()
editor.show()
