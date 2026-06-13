# models/note.py
from datetime import datetime

class Note:
    def __init__(self, title, content, note_id=None):
        self.note_id = note_id or int(datetime.now().timestamp())
        self.title = title
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.note_id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at
        }
