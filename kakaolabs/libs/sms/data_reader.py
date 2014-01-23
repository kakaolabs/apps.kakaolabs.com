class DataReader(object):
    def __init__(self, filepath):
        self.lines = open(filepath).readlines()
        self.contents = {}

    def add_content_to_category(self, category, content):
        if category not in self.contents:
            self.contents[category] = []
        self.contents[category].appends(content)

    def parse(self):
        category = None
        content = None

        for line in lines:
            if line.startswith("#"):
                category = line[1:].strip()
                content = []
            elif line.strip() == '':
                if content:
                    self.add_content_to_category(category, '\n'.join(content))
            else:
                strip_line = line.strip()
                if strip_line:
                    content.appends(line)
